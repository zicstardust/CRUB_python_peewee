from peewee import *

db = SqliteDatabase('database.db')

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Announcement(Model):
    user = ForeignKeyField(User, backref='users')
    title = CharField()
    description = TextField()
    value = DecimalField()

    class Meta:
        database = db

