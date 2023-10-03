"""
Sale Model
Defines the Sale model for the 'sales' table.

This model represents individual sales records. Each sale is associated with a product.

Attributes:
    - id (int): The unique identifier for the sale.
    - product_id (int): The foreign key reference to the sold product.
    - quantity (int): The quantity of the product sold.
    - sale_date (datetime): The date and time when the sale occurred.
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from data_access_layer.db import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("Product", back_populates="sales")


Index("ix_sale_sale_date", Sale.sale_date)
Index("ix_sale_product_id", Sale.product_id)
