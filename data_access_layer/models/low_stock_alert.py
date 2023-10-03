"""
LowStockAlert Model
Defines the LowStockAlert model for the 'low_stock_alerts' table.

This model represents low stock alerts for products. It tracks whether an alert has been triggered based on a predefined threshold.

Attributes:
    - id (int): The unique identifier for the alert.
    - product_id (int): The foreign key reference to the product.
    - threshold (int): The predefined stock threshold for triggering the alert.
    - triggered (bool): Indicates whether the alert has been triggered.
"""

from sqlalchemy import Column, Integer, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship
from data_access_layer.db import Base


class LowStockAlert(Base):
    __tablename__ = "low_stock_alerts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    threshold = Column(Integer, nullable=False)
    triggered = Column(Boolean, nullable=False)

    product = relationship("Product", back_populates="low_stock_alerts")


Index("ix_low_stock_alert_product_id", LowStockAlert.product_id)
