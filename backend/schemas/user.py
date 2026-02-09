from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from models import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password",)

    id = fields.Str(dump_only=True)
    username = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=50),
        error_messages={"required": "please input username"},
    )
    email = fields.Email(required=True)
    password = fields.Int(load_only=True, required=True, validate=validate.Length(min=6))
    created_at = auto_field(dump_only=True)