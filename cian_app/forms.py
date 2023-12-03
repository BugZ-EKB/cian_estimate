from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class FlatForm(FlaskForm):
    rooms_count = IntegerField('Количество комнат',
                               validators=[DataRequired()], render_kw={'class': 'form-control'})
    total_meters = IntegerField('Общая площадь',
                                validators=[DataRequired()], render_kw={'class': 'form-control'})
    price = IntegerField('Цена квартиры',
                         validators=[DataRequired()], render_kw={'class': 'form-control'})
    living_meters = IntegerField('Жилая площадь',
                                 validators=[DataRequired()], render_kw={'class': 'form-control'})
    kitchen_meters = IntegerField('Площадь кухни',
                                  validators=[DataRequired()], render_kw={'class': 'form-control'})
    floor = IntegerField('Этаж',
                         validators=[DataRequired()], render_kw={'class': 'form-control'})
    floors_count = IntegerField('Всего этажей в здании',
                                validators=[DataRequired()], render_kw={'class': 'form-control'})
    year_of_construction = IntegerField('Год постройки',
                                        validators=[DataRequired()], render_kw={'class': 'form-control'})
    district = SelectField('Район',
                           choices=[("Автовокзал", "Автовокзал"),
                                    ("Верх-Исетский", "Верх-Исетский"),
                                    ("Дзержинский", "Дзержинский"),
                                    ("Железнодорожный", "Железнодорожный"),
                                    ("Кировский", "Кировский"),
                                    ("Ленинский", "Ленинский"),
                                    ("Октябрьский", "Октябрьский"),
                                    ("Орджоникидзевский", "Орджоникидзевский"),
                                    ("Тагилстроевский", "Тагилстроевский"),
                                    ("Центр", "Центр"),
                                    ("Чкаловский", "Чкаловский"),
                                    ],
                           validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-success'})


class EstimateForm(FlatForm):
    submit = SubmitField('Рассчитать цену', render_kw={'class': 'btn btn-success'})
