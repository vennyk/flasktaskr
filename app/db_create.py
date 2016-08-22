# project/db_create.py


from views import db
from models import Task
from datetime import date

db.create_all()

db.session.add(Task("finish tutorial", date(2014,3,13),10,1))
db.session.add(Task("finish real python", date(2014,3,13),10,1))

db.session.commit()