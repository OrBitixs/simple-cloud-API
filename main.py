import uuid

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import Uuid, Integer, String, delete

db = SQLAlchemy()
app = Flask(__name__)

username = 'admin'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = 'database-1.c94axs45lkvi.eu-central-1.rds.amazonaws.com'
dbname   = '/simpleDB'


app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


class Students(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(Uuid, primary_key=True)
    student_name = db.Column(String(24))
    student_age = db.Column(Integer)


# this route will test the database connection - and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>Database is connected.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.get('/students')
def getStudent():
    try:
        students = Students.query.all()

        student_list = []
        for student in students:
            student_list.append({
                'student_id': student.student_id,
                'student_name': student.student_name,
                'student_age': student.student_age
            })

        return jsonify(student_list)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.post('/students')
def postStudents():
    try:
        body = request.get_json()
        new_student = Students(student_id=uuid.uuid1(), student_name=body["student_name"], student_age=body["student_age"])
        db.session.add(new_student)
        db.session.commit()
        return '<h1>Successfully added.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.delete('/students')
def deleteStudents():
    try:
        body = request.get_json()
        Students.query.filter(Students.student_id == uuid.UUID(body["student_id"])).delete()
        db.session.commit()
        return '<h1>Successfully deleted.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.put('/students')
def putStudents():
    try:
        body = request.get_json()
        Students.query.filter(Students.student_id == uuid.UUID(body["student_id"])).update({"student_name": body["student_name"], "student_age": body["student_age"]})
        # db.session.commit()
        return '<h1>Successfully updated.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)