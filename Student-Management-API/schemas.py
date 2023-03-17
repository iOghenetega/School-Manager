from marshmallow import Schema, fields

class StudentSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.Email(required=True)


class CourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    teacher = fields.String(required=True)


# class EnrollmentSchema(Schema):
#     course_id = fields.Int(required=True)
#     student_id = fields.Int(required=True)
#     grades = fields.Str(max=50)
    

