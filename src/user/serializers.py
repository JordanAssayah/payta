# coding: utf-8

from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    image = fields.Url()
    token = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
