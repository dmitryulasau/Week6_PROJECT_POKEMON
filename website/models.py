from . import db

from flask_login import UserMixin
from datetime import datetime as dt, timedelta

user_pokemon = db.Table(
    'user_pokemon',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)

    owning = db.relationship('Pokemon', secondary=user_pokemon, backref="masters")

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ability = db.Column(db.String)
    defense = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    gif = db.Column(db.String)
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))