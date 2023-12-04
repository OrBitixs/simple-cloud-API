from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

@app.route('/')
def forbidden():
    return "<p>Pls, do not access from here.</p>"