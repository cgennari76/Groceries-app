from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# db variable initialization
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    from app.models import db
    db.init_app(app)   #db.init works in the interpreter via create_app

    migrate = Migrate(app, db)

    from app import models

    from .groceries import groceries as groceries_blueprint
    app.register_blueprint(groceries_blueprint)

    return app