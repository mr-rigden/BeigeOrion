import os

from peewee import *
import utils

db_path = os.path.join(utils.get_code_dir(), "data.db")
db = SqliteDatabase(db_path)


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
    subject = ForeignKeyField(Subject, index=True)
    follower = ForeignKeyField(Follower, index=True)

    class Meta:
        indexes = ((('subject', 'follower'), True), )


class Quality_Report(BaseModel):
    subject = ForeignKeyField(Subject, index=True)
    epoch_time = IntegerField(index=True)
    total = IntegerField()
    very_good = IntegerField()
    good = IntegerField()
    neutral = IntegerField()
    poor = IntegerField()
    very_poor = IntegerField()


db.create_tables([Subject, Follower, Relationship, Quality_Report])
