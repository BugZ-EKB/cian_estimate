import csv
from db import db_session
from model import Flats


def read_csv(filename):
    with open(filename, 'r', encoding='windows-1251') as f:
        fields = [
            'bargainterms_price', 'price_sqm', 'floors_max',
            'roomscount', 'totalarea',	'livingarea', 'kitchenarea',
            'repairtype',	'combinedwcscount',	'separatewcscount',
            'balconiescount',	'loggiascount'
                 ]
        reader = csv.DictReader(f, fields, delimiter=';')
        flats_data = []
        for row in reader:
            flats_data.append(row)
        return flats_data


def save_flats(data):
    db_session.bulk_insert_mappings(Flats, data)
    db_session.commit()


if __name__ == '__main__':
    flats_data = read_csv('cian_data_csv.csv')
    flats = save_flats(flats_data)