from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import TaskModel
from db import db


class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        load_instance = True
        include_fk = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    title = fields.Str(
        required=True,
        validate=validate.Length(min=3, error="min length of title is 3"),
        error_messages={"required": "title is required"},
    )
    description = auto_field(
        required=True, error_messages={"required": "description is required"}
    )
    order_index = fields.Float(
        required=True, error_messages={"required": "order_index is required"}
    )
    list_id = fields.Str(
        required=True, error_messages={"required": "list_id is required"}
    )
    created_at = auto_field(dump_only=True)
