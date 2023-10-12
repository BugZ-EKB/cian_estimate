import sqlite3
import sqlalchemy
from sqlalchemy import sql
from sqlalchemy import Column, Date, Integer, String, TEXT
from db import Base, engine

db = sqlalchemy.SQLAlchemy()


class Flats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bargainterms_price = db.Column(db.Integer,nullable=False)
    price_sqm = db.Column(db.Integer,nullable=False)
    floors_max = db.Column(db.Integer)
    roomscount = db.Column(db.Integer)
    totalarea = db.Column(db.Integer)
    livingarea = db.Column(db.Integer)
    kitchenarea = db.Column(db.Integer)
    repairtype = db.Column(db.String)
    combinedwcscount = db.Column(db.Integer)
    separatewcscount = db.Column(db.Integer)
    balconiescount = db.Column(db.Integer)
    loggiascount = db.Column(db.Integer)

    def __repr__(self):
        return f'Flat {self.id}, price={self.bargainterms_price}'


db.create_all()
