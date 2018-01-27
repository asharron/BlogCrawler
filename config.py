import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


WTF_CSRF_ENABLED = True
SECRET_KEY = '85s2pm%8p)dq9y%qh6++vb1bqw(+p%c5iu#^l+5-^ian0@=0)g'