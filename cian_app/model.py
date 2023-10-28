from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True, nullable=False)
    floor = db.Column(db.Integer,nullable=False)
    floors_count = db.Column(db.Integer)
    rooms_count = db.Column(db.Integer)
    total_meters = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)
    year_of_construction = db.Column(db.Integer)
    living_meters = db.Column(db.Integer)
    kitchen_meters = db.Column(db.Integer)
    district = db.Column(db.String)

    def __repr__(self):
        return f'Flat {self.id}, price={self.bargainterms_price}'
