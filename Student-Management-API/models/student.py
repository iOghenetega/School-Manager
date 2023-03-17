from db import db


class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    

class CourseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    students = db.relationship('StudentModel', secondary='course_students', backref='courses')

# Define course-student association table
class CourseStudents(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('course_model.id'), primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student_model.id'), primary_key=True)