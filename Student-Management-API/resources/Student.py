from flask.views import MethodView
from flask_smorest import Blueprint,abort #blueprint is used to register informations in the StudentBlueprint
from db import db
from schemas import StudentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import StudentModel

StudentBlueprint =  Blueprint("student", __name__, description="Operations on students")

@StudentBlueprint.route("/students")
class StoreList(MethodView):
    @StudentBlueprint.response(200, StudentSchema(many=True))
    def get(self):
        """retrieve all students"""
        return StudentModel.query.all()

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(201, StudentSchema)
    def post(self, data):
        """create a student"""
        student = StudentModel(**data)
        db.session.add(student)
        db.session.commit()
        return student


@StudentBlueprint.route('/students/<int:id>')
class StudentDetail(MethodView):
    @StudentBlueprint.response(200, StudentSchema)
    def get(self, id):
        """retrieve a student by ID"""
        student = StudentModel.query.get_or_404(id)
        return student

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(200, StudentSchema)
    def put(self, data, id):
        """update an existing student"""
        student = StudentModel.query.get_or_404(id)
        student.name = data['name']
        student.email = data['email']
        db.session.commit()
        return student
    
    @StudentBlueprint.response(204)
    def delete(self, id):
        """delete a student"""
        student = StudentModel.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()





