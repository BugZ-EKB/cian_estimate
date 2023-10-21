import csv
# from db import db_session
from cian_app.model import Flats, db


def read_csv(filename):
    with open(filename, 'r', encoding='windows-1251') as f:
        fields = [
            'link', 'floor', 'floors_count', 'rooms_count',
            'total_meters',	'price', 'year_of_construction',
            'living_meters',	'kitchen_meters',	'district'
        ]
        reader = csv.DictReader(f, fields, delimiter=';')
        flats_data = []
        for row in reader:
            flats_data.append(row)
        return flats_data


def save_flats(data):
    for flat in data:
        flat = Flats(
            link=flat['link'],
            floor=flat['floor'],
            floors_count=flat['floors_count'],
            rooms_count=flat['rooms_count'],
            total_meters=flat['total_meters'],
            price=flat['price'],
            year_of_construction=flat['year_of_construction'],
            living_meters=flat['living_meters'],
            kitchen_meters=flat['kitchen_meters'],
            district=flat['district'],
        )
        db.session.add(flat)
    db.session.commit()
    # db_session.bulk_insert_mappings(Flats, data)
    # db_session.commit()


if __name__ == '__main__':
    cian_data = read_csv('cian_parsing.csv')
    save_flats(cian_data)
