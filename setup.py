from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Uuid, String, Integer

db = SQLAlchemy()
app = Flask(__name__)

username = 'admin'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = 'database-1.c94axs45lkvi.eu-central-1.rds.amazonaws.com'
dbname   = ''


app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("student_id", Uuid, primary_key=True),
    Column("student_name", String(24)),
    Column("student_age", Integer)
)

metadata.create_all(db.engine)

print("sent?")