from .models.category import Category
from .models.product import Product
from .models.low_stock_alert import LowStockAlert
from .models.inventory import Inventory
from .models.sale import Sale
from .models.inventory_change import InventoryChange
from data_access_layer.db import get_db
from datetime import datetime


def load_demo_data():
    db = get_db()

    try:
        category1 = Category(name="Electronics")
        category2 = Category(name="Clothing")
        db.add(category1)
        db.add(category2)
        db.commit()

        # Create products
        product1 = Product(name="Laptop", price=800.0, category=category1)
        product2 = Product(name="Smartphone", price=400.0, category=category1)
        product3 = Product(name="T-shirt", price=20.0, category=category2)
        product4 = Product(name="Jeans", price=40.0, category=category2)
        db.add_all([product1, product2, product3, product4])
        db.commit()

        # Create sales
        sale1 = Sale(product=product1, quantity=5)
        sale2 = Sale(product=product2, quantity=10)
        sale3 = Sale(product=product3, quantity=15)
        sale4 = Sale(product=product4, quantity=20)
        sale5 = Sale(product=product4, quantity=10, sale_date=datetime(2022, 1, 1))
        sale6 = Sale(product=product1, quantity=5, sale_date=datetime(2023, 2, 1))
        sale7 = Sale(product=product2, quantity=9, sale_date=datetime(2020, 1, 1))
        sale8 = Sale(product=product3, quantity=7, sale_date=datetime(2023, 2, 24))
        sale9 = Sale(product=product1, quantity=12, sale_date=datetime(2023, 4, 6))
        sale10 = Sale(product=product2, quantity=13, sale_date=datetime(2023, 7, 10))
        db.add_all([sale1, sale2, sale3, sale4, sale5])
        db.commit()

        # Create inventory and inventory changes
        inventory1 = Inventory(product=product1, stock_quantity=50)
        inventory2 = Inventory(product=product2, stock_quantity=100)
        inventory3 = Inventory(product=product3, stock_quantity=200)
        inventory4 = Inventory(product=product4, stock_quantity=150)
        db.add_all([inventory1, inventory2, inventory3, inventory4])
        db.commit()

        # Create low stock alerts
        alert1 = LowStockAlert(product=product1, threshold=10, triggered=False)
        alert2 = LowStockAlert(product=product2, threshold=20, triggered=False)
        alert3 = LowStockAlert(product=product3, threshold=30, triggered=False)
        alert4 = LowStockAlert(product=product4, threshold=40, triggered=False)
        db.add_all([alert1, alert2, alert3, alert4])
        db.commit()

        # Create inventory changes
        change1 = InventoryChange(product=product1, change_quantity=5)
        change2 = InventoryChange(product=product2, change_quantity=10)
        change3 = InventoryChange(product=product3, change_quantity=-15)
        change4 = InventoryChange(product=product4, change_quantity=-20)
        db.add_all([change1, change2, change3, change4])
        db.commit()

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()
