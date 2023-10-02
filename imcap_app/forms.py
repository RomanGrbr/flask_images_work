from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Optional


# class ImageForm(FlaskForm):
#     uuid = StringField(
#         'уникальный номер uuid',
#         validators=[DataRequired(message='Обязательное поле'),
#                     Length(1, 128)]
#     )
#     text = TextAreaField(
#         'Описание изображения, спиок строк или строка',
#         validators=[DataRequired(message='Обязательное поле')]
#     )
#     submit = SubmitField('Добавить')


class TokenForm(FlaskForm):
    name = StringField(
        'Имя токена',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    alternative = StringField(
        'Альтернативное название',
        validators=[DataRequired(message='Обязательное поле')]
    )
    # images = IntegerField('id изображения')
    submit = SubmitField('Добавить')
