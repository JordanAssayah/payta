"""Order views."""
from flask import Blueprint
from .models import Order
from flask_apispec import use_kwargs, marshal_with
from .serializers import order_schemas, order_schema, order_schema_put_and_patch

blueprint = Blueprint('order', __name__)


@blueprint.route('/api/orders', methods=['POST'])
@use_kwargs(order_schema)
@marshal_with(order_schema)
def create_order(**kwargs):
    new_order = Order.create(**kwargs)
    return new_order


@blueprint.route('/api/orders/<id>', methods=['GET'])
@marshal_with(order_schemas)
def get_orders():
    orders = Order.query.get(id)
    return orders


@blueprint.route('/api/orders/<id>', methods=['DELETE'])
@use_kwargs(order_schema)
@marshal_with(order_schema)
def delete_one(id):
    order = Order.delete(id)
    return order


@blueprint.route('/api/orders/<id>', methods=['PUT'])
@use_kwargs(order_schema_put_and_patch)
@marshal_with(order_schema_put_and_patch)
def update_user(id, **kwargs):
    order = Order.query.get(id)
    order.update(**kwargs)
    return order
