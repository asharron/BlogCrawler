from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Blog(db.Model):
    __tablename__ = 'blog'
    bid = db.Column(db.Integer(),primary_key=True)
    student = db.Column(db.String(250))
    url = db.Column(db.String(250))
    titletag = db.Column(db.String(100))
    titleclass = db.Column(db.String(100))
    bodytag = db.Column(db.String(100))
    bodyclass = db.Column(db.String(100))

class Post(db.Model):
    __tablename__ = 'post'
    pid = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.String(5000))
    author = db.Column(db.String(100))

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(250))
    password_hash = db.Column(db.String(256))
 
    @property
    def password(self):
        raise AttributeError('password is not a readable attribtue')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


