from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
mentee = Table('mentee', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=30)),
    Column('lname', String(length=30)),
    Column('email', String(length=30)),
    Column('interest', String(length=30)),
    Column('state', String(length=30)),
    Column('city', String(length=30)),
    Column('password_hash', String(length=128)),
)

mentor = Table('mentor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=30)),
    Column('lname', String(length=30)),
    Column('email', String(length=30)),
    Column('interest', String(length=30)),
    Column('mentee_id', Integer),
    Column('state', String(length=30)),
    Column('city', String(length=30)),
    Column('password_hash', String(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['mentee'].columns['city'].create()
    post_meta.tables['mentee'].columns['state'].create()
    post_meta.tables['mentor'].columns['city'].create()
    post_meta.tables['mentor'].columns['state'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['mentee'].columns['city'].drop()
    post_meta.tables['mentee'].columns['state'].drop()
    post_meta.tables['mentor'].columns['city'].drop()
    post_meta.tables['mentor'].columns['state'].drop()
