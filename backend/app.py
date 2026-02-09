import os
from db import db
from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from flask_cors import CORS
import models

load_dotenv()
def create_app():
    app = Flask(__name__)

    # config flask smorest + openapi
    app.config['API_TITLE'] = "Task Master API"
    app.config['API_VERSION'] = "v1"
    app.config['OPENAPI_VERSION'] = "3.0.3"
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # config database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTION"] = True

    db.init_app(app)
    CORS(app, resources={r'/*':{'origins':'http//locahost:3003'}})
    api = Api(app)

    with app.app_context():
        print('successfully connected to database')

    return app


if (__name__ == "__main__"):
    app = create_app()
    app.run(debug=True, port=5000)