# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint
from .models import User
from flask_apispec import use_kwargs, marshal_with
from .serializers import user_schemas, user_schema, user_schema_put_and_patch

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/users', methods=['POST'])
@use_kwargs(user_schema)
@marshal_with(user_schema)
def create_user(**kwargs):
    new_user = User.create(**kwargs)
    return new_user


@blueprint.route('/api/users', methods=['GET'])
@marshal_with(user_schemas)
def get_all():
    users = User.query.all()
    return users


@blueprint.route('/api/users/<id>', methods=['GET'])
@marshal_with(user_schema)
def get_one(id):
    user = User.query.get(id)
    return user


@blueprint.route('/api/users/<id>', methods=['DELETE'])
@use_kwargs(user_schema)
@marshal_with(user_schema)
def delete_one(id):
    user = User.delete(id)
    return user


@blueprint.route('/api/users/<id>', methods=['PUT'])
@use_kwargs(user_schema_put_and_patch)
@marshal_with(user_schema_put_and_patch)
def update_user(id, **kwargs):
    user = User.query.get(id)
    user.update(**kwargs)
    return user
