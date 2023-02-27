from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "People.db"))


class People(Model):
    name = CharField()
    PhoneNumber = CharField(unique=True)
    email = CharField(unique=True)
    county = CharField()
    gender = CharField()
    religion = CharField()
    password = CharField(unique=True)

    class Meta:
        database = db


People.create_table(fail_silently=True)
