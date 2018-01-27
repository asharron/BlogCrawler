from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = "85s2pm%8p)dq9y%qh6++vb1bqw(+p%c5iu#^l+5-^ian0@=0)g"


from app import views, models
