from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import ListModel
from db import db


class ListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ListModel
        load_instance = True
        include_fk = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    title = fields.Str(
        required=True,
        validate=validate.Length(min=3, error="min length of title is 3"),
        error_messages={"required": "title is required"},
    )
    order_index = fields.Float(
        required=True, error_messages={"required": "order_index is required"}
    )
    board_id = fields.Str(
        required=True, error_messages={"required": "board_id is required"}
    )
    created_at = auto_field(dump_only=True)
