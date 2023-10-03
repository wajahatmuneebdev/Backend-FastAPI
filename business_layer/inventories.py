from fastapi import HTTPException
from data_access_layer.models.inventory import Inventory
from data_access_layer.models.inventory_change import InventoryChange
from data_access_layer.models.product import Product
from data_access_layer.models.low_stock_alert import LowStockAlert


def fetch_inventory(db_session, product_id):
    product_data = (
        db_session.query(
            Product.name.label("product_name"),
            Product.price.label("product_price"),
            Inventory.stock_quantity.label("quantity_in_stock"),
        )
        .join(Inventory)
        .filter(Product.id == product_id)
        .first()
    )

    if not product_data:
        raise HTTPException(status_code=404, detail="Product not found")

    low_stock_alerts_data = (
        db_session.query(
            LowStockAlert.threshold.label("alert_threshold"),
            LowStockAlert.triggered.label("alert_triggered"),
        )
        .filter(LowStockAlert.product_id == product_id)
        .all()
    )

    return {"product_data": product_data, "low_stock_alerts": low_stock_alerts_data}


def update_inventory(db_session, product_id, quantity_change):
    product = db_session.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    inventory = (
        db_session.query(Inventory).filter(Inventory.product_id == product_id).first()
    )

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory record not found")

    inventory.stock_quantity += quantity_change

    inventory_change = InventoryChange(
        product_id=product_id,
        change_quantity=quantity_change,
    )

    db_session.add(inventory_change)

    db_session.commit()
    db_session.refresh(inventory)


def get_inventory_changes(db_session, product_id):
    changes = (
        db_session.query(InventoryChange)
        .filter(InventoryChange.product_id == product_id)
        .all()
    )

    if not changes:
        raise HTTPException(status_code=404, detail="Inventory changes not found")

    return changes
