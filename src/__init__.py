#TO-LOOKUP: Route Decorator
#Resource to understand Blueprints: https://www.youtube.com/watch?v=pjVhrIJFUEs&ab_channel=PrettyPrinted

from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy
from src.auth import auth
from src.bookmarks import bookmarks_blueprint
from src.database import db
from flask_jwt_extended import JWTManager, jwt_manager

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        )
    else:
        app.config.from_mapping(test_config)
    
    db.app=app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks_blueprint)

    return app 



