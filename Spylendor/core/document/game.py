from mongoengine import *


class Gems(Document):
    Black = IntField(0)
    Blue = IntField(0)
    Green = IntField(0)
    Red = IntField(0)
    White = IntField(0)
    Yellow = IntField(0)


class Card(Document):
    points = IntField(0)
    gems = ReferenceField(Gems)
    color = StringField()


class Player(Document):
    cards = ListField(Card)


class Game(Document):
    id = StringField(primary_key=True, required=True, max_length=64)
    players = ListField(Player)
