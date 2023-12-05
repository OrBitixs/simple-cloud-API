from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Uuid, String, Integer, create_engine


username = 'admin'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = 'database-1.c94axs45lkvi.eu-central-1.rds.amazonaws.com'
dbname   = '/simpleDB'

engine = create_engine(userpass+server+dbname)

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("student_id", Uuid, primary_key=True),
    Column("student_name", String(24)),
    Column("student_age", Integer)
)

metadata.create_all(engine)

print("sent?")

