"""
Inventory Model
Defines the Inventory model for the 'inventory' table.

This model represents the current stock quantity for each product.

Attributes:
    - id (int): The unique identifier for the inventory record.
    - product_id (int): The foreign key reference to the product.
    - stock_quantity (int): The current stock quantity of the product.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from data_access_layer.db import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock_quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="inventory")
