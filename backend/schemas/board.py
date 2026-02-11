from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import BoardModel
from db import db


class BoardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BoardModel
        load_instance = True
        include_fk = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    title = fields.Str(
        required=True,
        validate=validate.Length(min=4, error="min length of title is 4"),
        error_messages={"required": "title is required"},
    )
    user_id = fields.Str(
        required=True, error_messages={"required": "user_id is required"}
    )
    created_at = auto_field(dump_only=True)
