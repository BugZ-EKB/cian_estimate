import csv
from cian_app.model import Flats, db


def read_csv(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        fields = [
            'link', 'floor', 'floors_count', 'rooms_count',
            'total_meters',	'price', 'year_of_construction',
            'living_meters',	'kitchen_meters',	'district'
        ]
        # reader = csv.DictReader(f, fields, delimiter=';')
        reader = csv.DictReader(f, delimiter=';')

        flats_data = []

        for row in reader:
            flat_data = {field: row[field] for field in fields}
            flats_data.append(flat_data)
        return flats_data


def save_flats(data):
    for flat in data:
        flat_exist = Flats.query.filter(Flats.link == flat['link']).count()
        if not flat_exist:
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


# if __name__ == '__main__':
#     cian_data = read_csv('cian_parsing.csv')
#     save_flats(cian_data)
