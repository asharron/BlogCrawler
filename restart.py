from app import db, models
db.drop_all()
db.create_all()
import pop
import update
user = models.User()
user.username='test'
user.password = 'password'
db.session.add(user)
db.session.commit()
