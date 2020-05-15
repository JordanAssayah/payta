# -*- coding: utf-8 -*-
"""Order models."""
from src.database import Column, Model, SurrogatePK, db
from src.extensions import bcrypt
from src.database import reference_col


class Order(SurrogatePK, Model):
    __tablename__ = 'orders'
    user_id = reference_col('users', nullable=False)


class Orderitem(SurrogatePK, Model):
    __tablename__ = 'orderitems'
    order_id = reference_col('orders', nullable=False)
    product_id = reference_col('products', nullable=False)
    quantity = Column(db.Integer(), nullable=False)


class Product(SurrogatePK, Model):
    __tablename__ = 'products'
    name = Column(db.String(80), unique=False, nullable=False)
    image = Column(db.String(120), nullable=False)
    price = Column(db.Integer(), nullable=False)
    description = Column(db.Text(), nullable=False)
