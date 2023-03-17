from flask import  Flask
from flask_smorest import Api
from resources.Student import StudentBlueprint
from resources.Course import CourseBlueprint
from db import db



app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "School Manager "
app.config["API_VERSION"] = "v1.01"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
api = Api(app)

api.register_blueprint(StudentBlueprint) 
api.register_blueprint(CourseBlueprint)




# Create the tables
with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)