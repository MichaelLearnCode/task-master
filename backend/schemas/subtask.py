from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import SubtaskModel
from db import db


class SubtaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubtaskModel
        load_instance = True
        include_fk = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    content = fields.Str(
        required=True,
        validate=validate.Length(min=3, error="min length of content is 3"),
        error_messages={"required": "content is required"},
    )
    is_completed = auto_field()
    task_id = fields.Str(
        required=True, error_messages={"required": "task_id is required"}
    )
    created_at = auto_field(dump_only=True)
