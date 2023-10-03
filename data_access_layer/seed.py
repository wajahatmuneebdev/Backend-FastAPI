from .db import engine
from .models.category import Category
from .models.product import Product
from .models.low_stock_alert import LowStockAlert
from .models.inventory import Inventory
from .models.sale import Sale
from .models.inventory_change import InventoryChange


def create_schema():
    conn = engine.connect()
    table_names = engine.table_names()

    with conn.connection.cursor() as cursor:
        for table_name in table_names:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")

    conn.connection.commit()
    conn.close()

    creation_order = [
        Category.__table__,
        Product.__table__,
        LowStockAlert.__table__,
        Inventory.__table__,
        Sale.__table__,
        InventoryChange.__table__,
    ]

    for table in creation_order:
        table.create(bind=engine)
