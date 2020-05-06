# coding: utf-8

from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str(load_only=True)
    image = fields.Url()
    token = fields.Str(dump_only=True)
    createdAt = fields.DateTime(attribute='created_at', dump_only=True)
    updatedAt = fields.DateTime(attribute='updated_at')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
