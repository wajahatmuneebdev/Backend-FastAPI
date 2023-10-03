"""
Product Model
Defines the Product model for the 'products' table.

This model represents products available for sale. Each product belongs to a category and can have sales records,
inventory information, and low stock alerts associated with it.

Attributes:
    - id (int): The unique identifier for the product.
    - name (str): The name of the product.
    - price (float): The price of the product.
    - category_id (int): The foreign key reference to the product's category.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import relationship
from data_access_layer.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")
    sales = relationship("Sale", back_populates="product")
    inventory = relationship("Inventory", back_populates="product")
    inventory_changes = relationship("InventoryChange", back_populates="product")
    low_stock_alerts = relationship("LowStockAlert", back_populates="product")


Index("ix_product_id", Product.id, unique=True)
Index("ix_product_category_id", Product.category_id)
