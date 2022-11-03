from flask_restful import Resource, abort, fields, marshal_with, reqparse

from app import db
from .models import Course

courses_post_args = reqparse.RequestParser()
courses_post_args.add_argument("department", type=str, help="Course department required", required=True)
courses_post_args.add_argument("number", type=int, help="Course number required", required=True)
courses_post_args.add_argument("name", type=str, help="Course name required", required=True)
courses_post_args.add_argument("units", type=int, help="Number of units required", required=True)
courses_post_args.add_argument("desc", type=str, help="Course description")

course_put_args = reqparse.RequestParser()
course_put_args.add_argument("name", type=str, help="Course name")
course_put_args.add_argument("units", type=int, help="Number of units")
course_put_args.add_argument("desc", type=str, help="Course description")

resource_fields = {
    'department': fields.String,
    'number': fields.Integer,
    'name': fields.String,
    'units': fields.Integer,
    'desc': fields.String
}


class CoursesResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Course.query.all(), 200, {'Access-Control-Allow-Origin': '*'}

    @marshal_with(resource_fields)
    def post(self):
        args = courses_post_args.parse_args()
        result = Course.query.get((args['department'], args['number']))

        if result:
            abort(400, message="Course with this number in this department already exists")

        course = Course(department=args['department'], number=args['number'], name=args['name'], units=args['units'],
                        desc=args['desc'])
        db.session.add(course)
        db.session.commit()

        return course, 201


class CourseResource(Resource):
    @marshal_with(resource_fields)
    def get(self, department, number):
        result = Course.query.get((department, number))

        if not result:
            abort(404, message="Course with this number in this department does not exist")

        return result, 200

    @marshal_with(resource_fields)
    def put(self, department, number):
        args = course_put_args.parse_args()
        result = Course.query.get((department, number))

        if not result:
            abort(404, message="Course with this number in this department does not exist")

        if args['name']:
            result.name = args['name']
        if args['units']:
            result.units = args['units']
        if args['desc']:
            result.desc = args['desc']

        db.session.commit()

        return result, 200

    def delete(self, department, number):
        result = Course.query.get((department, number))

        if not result:
            abort(404, message="Course with this number in this department does not exist")

        db.session.delete(result)
        db.session.commit()

        return '', 204
