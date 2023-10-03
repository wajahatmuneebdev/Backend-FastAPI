from data_access_layer.models.inventory import Inventory
from data_access_layer.models.product import Product
from data_access_layer.models.category import Category


def register_new_product(db_session, product_data):
    product_name = product_data.get("name")
    product_price = product_data.get("price")
    category_name = product_data.get("category")
    initial_stock_quantity = product_data.get("initial_stock_quantity")

    category = db_session.query(Category).filter(Category.name == category_name).first()
    if not category:
        category = Category(name=category_name)
        db_session.add(category)

    new_product = Product(
        name=product_name,
        price=product_price,
        category=category,
    )

    db_session.add(new_product)
    db_session.flush()

    inventory = Inventory(
        product=new_product,
        stock_quantity=initial_stock_quantity,
    )

    db_session.add(inventory)

    db_session.commit()
    db_session.refresh(new_product)
