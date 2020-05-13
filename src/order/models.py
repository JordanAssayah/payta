# -*- coding: utf-8 -*-
"""Order models."""
from src.database import Column, Model, SurrogatePK, db
from src.extensions import bcrypt


class Order(SurrogatePK, Model):
    __tablename__ = 'orders'


class Orderitem(SurrogatePK, Model):
    __tablename__ = 'orderitems'


class Product(SurrogatePK, Model):
    __tablename__ = 'products'
