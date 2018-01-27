from app import db
from app.models import *

db.drop_all()
db.create_all()


#dummy data
test = Post()
test.title = "This is a test title"
test.content = "This is a test post to see if the program can handle it"
test.data = "10/12/13"

db.session.add(test)
db.session.commit()