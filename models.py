from peewee import *

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class Subject(BaseModel):
    id_str = CharField(index=True, unique=True)
    screen_name = CharField(index=True, unique=True)


class Follower(BaseModel):
    id_str = CharField(index=True, unique=True)
    botometer = FloatField(index=True, null=True)


class Relationship(BaseModel):
    subject = ForeignKeyField(Subject)
    follower = ForeignKeyField(Follower)

    class Meta:
        indexes = ((('subject', 'follower'), True), )


db.create_tables([Subject, Follower, Relationship])
