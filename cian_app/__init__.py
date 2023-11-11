from flask import Flask, flash, redirect, render_template, session, url_for
import pickle
import pandas as pd
import numpy as np


from cian_app.model import db, Flats
from cian_app.forms import EstimateForm, FlatForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Список квартир'
        flat_list = Flats.query.all()
        return render_template('index.html', page_title=title, flat_list=flat_list)

    @app.route('/add_flat')
    def add_flat():
        title = 'Добавить квартиру'
        flat_form = FlatForm()
        return render_template('add_flat.html', page_title=title, form=flat_form)

    @app.route('/process_add_flat', methods=['POST'])
    def process_add_flat():
        flat_form = FlatForm()
        new_flat = Flats(
            link='-',
            floor=flat_form.floor.data,
            floors_count=flat_form.floors_count.data,
            rooms_count=flat_form.rooms_count.data,
            total_meters=flat_form.total_meters.data,
            price=flat_form.price.data,
            year_of_construction=flat_form.year_of_construction.data,
            living_meters=flat_form.living_meters.data,
            kitchen_meters=flat_form.kitchen_meters.data,
            district=flat_form.district.data
        )
        db.session.add(new_flat)
        db.session.commit()
        flash('Квартира добавлена')
        return redirect(url_for('add_flat'))

    @app.route('/estimate_flat')
    def estimate_flat():
        title = 'Оценить квартиру'
        estimate_form = EstimateForm()
        return render_template('estimate_flat.html', page_title=title, form=estimate_form)

    @app.route('/result_estimate_flat', methods=['POST'])
    def process_estimate_flat():
        title = 'Результат оценки'
        with open('encoder.pkl', 'rb') as f:
            encoder = pickle.load(f)
        with open('finalized_model.pkl', 'rb') as f:
            regressor = pickle.load(f)
        flat_data = EstimateForm().data
        df = pd.DataFrame(flat_data, index=[0])
        df.drop('_sa_instance_state', axis=1, errors='ignore', inplace=True)
        df.drop('link', axis=1, errors='ignore', inplace=True)
        df.drop('author', axis=1, errors='ignore', inplace=True)
        df.drop('street', axis=1, errors='ignore', inplace=True)
        df.drop('city', axis=1, errors='ignore', inplace=True)
        df.drop('accommodation_type', axis=1, errors='ignore', inplace=True)
        df.drop('deal_type', axis=1, errors='ignore', inplace=True)
        df.drop('phone', axis=1, errors='ignore', inplace=True)
        df.drop('residential_complex', axis=1, errors='ignore', inplace=True)
        df.drop('underground', axis=1, errors='ignore', inplace=True)
        df.drop('submit', axis=1, errors='ignore', inplace=True)
        df.drop('csrf_token', axis=1, errors='ignore', inplace=True)
        df.replace('', np.NaN, inplace=True)
        df['district'] = encoder.transform(df['district'])
        price = round(regressor.predict(df)[0])
        price = '{:,}'.format(price).replace(',', ' ')
        return render_template('result_estimate.html', page_title=title, price=price)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
