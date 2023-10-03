"""
Category Model
Defines the Category model for the 'categories' table.

This model represents product categories. Each category can have multiple products associated with it.

Attributes:
    - id (int): The unique identifier for the category.
    - name (str): The name of the category.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_access_layer.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="category")
