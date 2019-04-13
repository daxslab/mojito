from peewee import CharField

from ron.models.basemodel import BaseModel


class Person(BaseModel):
    name = CharField()
