# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with

from src.database import db
from .serializers import user_schema

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/users', methods=['GET'])
def get_all():
    return {}
