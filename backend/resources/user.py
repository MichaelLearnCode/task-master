from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import UserSchema
from models import UserModel
from db import db
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)

blp = Blueprint("Users", __name__, description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(
            (UserModel.username == user_data["username"])
            | (UserModel.email == user_data["email"])
        ).first():
            abort(409, message="An user with that username or email already exist")
        user_data["password_hash"] = pbkdf2_sha256.hash(user_data["password"])
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            abort(500, message="An error occured while registering")

        return {"success": True, "message": "Account created successfully"}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.email == user_data["email"]).first()
        if not user or not pbkdf2_sha256.verify(
            user_data["password"], user.password_hash
        ):
            abort(401, message="user name or password is incorrect")
        access_token = create_access_token(identity=str(user.id), fresh=True)
        refresh_token = create_refresh_token(identity=str(user.id))

        response = jsonify({"success": True, "message": "login successfully"})

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response, 200
