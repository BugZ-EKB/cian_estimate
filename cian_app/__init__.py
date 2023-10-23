from flask import Flask, render_template

from cian_app.model import db, Flats


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Список квартир'
        flat_list = Flats.query.all()
        return render_template('index.html', page_title=title, flat_list=flat_list)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
