from cian_app import create_app

from cian_app.loader import read_csv, save_flats

app = create_app()
with app.app_context():
    cian_data = read_csv('cian_parsing_full.csv')
    save_flats(cian_data)
