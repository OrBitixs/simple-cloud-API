from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy.sql import text

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
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(24))
    student_age = db.Column(db.Integer)


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

@app.route('/students')
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



if __name__ == '__main__':
    app.run(debug=True)