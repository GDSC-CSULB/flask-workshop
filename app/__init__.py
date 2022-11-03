from os import path

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "courses.db"


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import Course

    create_database(app)

    from .resources import CoursesResource, CourseResource

    api.add_resource(CoursesResource, '/courses')
    api.add_resource(CourseResource, '/course/<string:department>/<int:number>')

    @app.route("/")
    def hello_world():
        return "Hello world"

    return app


def create_database(app):
    with app.app_context():
        db.create_all()
        print(f'{DB_NAME} created')
