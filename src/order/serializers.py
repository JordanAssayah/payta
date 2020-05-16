

from marshmallow import Schema, fields


class OrderSchema(Schema):
    user_id = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class OrderSchemaPutAndPatch(Schema):
    user_id = fields.Integer()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class OrderItemSchema(Schema):
    order_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class OrderItemSchemaPutAndPatch(Schema):
    order_id = fields.Integer()
    product_id = fields.Integer()
    quantity = fields.Integer()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    image = fields.url(required=True)
    price = fields.Integer(required=True)
    description = fields.Text(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


class ProductSchemaPutAndPatch(Schema):
    id = fields.Integer()
    name = fields.Str()
    image = fields.url()
    price = fields.Integer()
    description = fields.Text()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()

    class Meta:
        strict = True


order_schema = OrderSchema()
order_schema_put_and_patch = OrderSchemaPutAndPatch()
orderItem_schema = OrderSchema()
order_Item_schema_put_and_patch = OrderItemSchemaPutAndPatch()
product_schema = OrderSchema()
product_schema_put_and_patch = ProductSchemaPutAndPatch()
order_schemas = OrderSchema(many=True)
