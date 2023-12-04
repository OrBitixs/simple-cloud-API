from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy.sql import text

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)

# make sure the database username, database password and
# database name are correct
username = 'admin'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# keep this as is for a hosted website
server  = 'database-1.c94axs45lkvi.eu-central-1.rds.amazonaws.com'
# CHANGE to YOUR database name, with a slash added as shown
dbname   = ''
# there is no socket


# CHANGE NOTHING BELOW
# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection - and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)