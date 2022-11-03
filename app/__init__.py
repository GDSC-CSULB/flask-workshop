from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "university.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import Course

    create_database(app)

    @app.route("/")
    def hello_world():
        return "Hello world"

    return app


def create_database(app):
    if not path.exists('app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print(f'{DB_NAME} created')
