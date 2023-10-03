"""
InventoryChange Model
Defines the InventoryChange model for the 'inventory_changes' table.

This model represents changes in inventory levels over time for products.

Attributes:
    - id (int): The unique identifier for the inventory change record.
    - product_id (int): The foreign key reference to the product.
    - change_quantity (int): The quantity by which the inventory changed.
    - change_date (datetime): The date and time when the inventory change occurred.
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from data_access_layer.db import Base


class InventoryChange(Base):
    __tablename__ = "inventory_changes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    change_quantity = Column(Integer, nullable=False)
    change_date = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("Product", back_populates="inventory_changes")
