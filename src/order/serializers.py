

from marshmallow import Schema, fields


class OrderSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class OrderSchemaPutAndPatch(Schema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


order_schema = OrderSchema()
order_schemas = OrderSchema(many=True)
order_schema_put_and_patch = OrderSchemaPutAndPatch()
