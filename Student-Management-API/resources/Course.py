from flask.views import MethodView
from flask_smorest import Blueprint, abort 
from db import db
from schemas import CourseSchema, StudentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import CourseModel, StudentModel


CourseBlueprint =  Blueprint("Courses", __name__, description="Operations on courses")
@CourseBlueprint.route('/courses')
class CourseList(MethodView):
    @CourseBlueprint.response(200, CourseSchema(many=True))
    def get(self):
        """retrieve all courses"""
        courses = CourseModel.query.all()
        return courses

    @CourseBlueprint.arguments(CourseSchema)
    @CourseBlueprint.response(201, CourseSchema)
    def post(self, data):
        """Create a new course"""
        course = CourseModel(**data)
        db.session.add(course)
        db.session.commit()
        return course



@CourseBlueprint.route("/courses/<int:id>")
class Course(MethodView):
    @CourseBlueprint.response( 200, CourseSchema)
    def get(self, id):
        """retrieve a single course by ID"""
        course = CourseModel.query.get_or_404(id)
        return course
    
    @CourseBlueprint.arguments(CourseSchema)
    @CourseBlueprint.response(200, CourseSchema)
    def put(self, course, id):
        """update an existing course"""
        course_to_update = CourseModel.query.get_or_404(id)
        course_to_update.name = course['name']
        course_to_update.teacher = course['teacher']
        db.session.commit()
        return course_to_update

    @CourseBlueprint.response(200)
    def delete(self, id):
        """delete a course"""
        course_to_delete = CourseModel.query.get_or_404(id)
        db.session.delete(course_to_delete)
        db.session.commit()


# @CourseBlueprint.route("/course/<int:id>/register")
# class CourseRegistration(MethodView):
#     @CourseBlueprint.arguments(StudentSchema)
#     def post(self, student, id):
#         #Register a student for a course
#         course = CourseModel.query.get_or_404(id)
#         student = StudentModel.query.get_or_404(student.id)
#         course.students.append(student)
#         db.session.commit()
#         return {"message": "Student successfully registered for course."}

    

