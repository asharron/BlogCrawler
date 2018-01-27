from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('fname', VARCHAR(length=30)),
    Column('interest', VARCHAR(length=30)),
    Column('lname', VARCHAR(length=30)),
    Column('password_hash', VARCHAR(length=128)),
)

mentee = Table('mentee', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=30)),
    Column('lname', String(length=30)),
    Column('email', String(length=30)),
    Column('interest', String(length=30)),
    Column('password_hash', String(length=128)),
)

mentor = Table('mentor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=30)),
    Column('lname', String(length=30)),
    Column('email', String(length=30)),
    Column('interest', String(length=30)),
    Column('mentee', Integer),
    Column('password_hash', String(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['mentee'].create()
    post_meta.tables['mentor'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['mentee'].drop()
    post_meta.tables['mentor'].drop()
