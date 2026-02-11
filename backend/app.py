from datetime import timedelta
import os
from db import db
from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from flask_cors import CORS
import models
from resources import user_blp
from flask_jwt_extended import JWTManager

load_dotenv()


def create_app():
    app = Flask(__name__)

    # config flask smorest + openapi
    app.config["API_TITLE"] = "Task Master API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # config database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # config JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "my-super-secret-key")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_COOKIE_PATH"] = "/"
    app.config["JWT_REFRESH_COOKIE_PATH"] = "/"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False
    app.config["JWT_HTTPONLY"] = True
    jwt = JWTManager(app)

    db.init_app(app)
    CORS(
        app,
        resources={r"/*": {"origins": "http://locahost:3003"}},
        supports_credentials=True,
    )
    api = Api(app)
    api.register_blueprint(user_blp)

    with app.app_context():
        print("successfully connected to database")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
