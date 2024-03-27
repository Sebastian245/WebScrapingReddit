from flask import Flask
from flask_cors import CORS
from routes import WebScrapperRoutes

from database.db import db

def init_app():
    app = Flask(__name__)
    CORS(app)

    app.secret_key = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/webContentParser'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(WebScrapperRoutes.main, name='user_blueprint')

    db.init_app(app)
    return app
