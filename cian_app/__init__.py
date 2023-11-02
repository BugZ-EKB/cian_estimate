from flask import Flask, flash, redirect, render_template, url_for

from cian_app.model import db, Flats
from cian_app.forms import FlatForm


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
            year_of_construction=flat_form.year_of_construction.data,
            living_meters=flat_form.living_meters.data,
            kitchen_meters=flat_form.kitchen_meters.data,
            district=flat_form.district.data
        )
        db.session.add(new_flat)
        db.session.commit()
        flash('Квартира добавлена')
        return redirect(url_for('add_flat'))

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
