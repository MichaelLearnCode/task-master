from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import UserModel
from db import db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("password_hash",)
        sqla_session = db.session

    id = fields.Str(dump_only=True)
    username = fields.Str(
        dump_only=True,
        required=True,
        validate=validate.Length(min=3, max=50, error="min character >= 3 and <= 50"),
        error_messages={"required": "please input username"},
    )
    email = fields.Email(
        required=True,
        error_messages={
            "invalid": "Invalid format",
        },
    )
    password = fields.Str(
        load_only=True,
        required=True,
        validate=validate.Length(min=5, error="min length of password is 5"),
        error_messages={"required": "password is required"},
    )
    created_at = auto_field(dump_only=True)
