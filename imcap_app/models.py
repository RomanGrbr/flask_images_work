from datetime import datetime

from . import db


# image_token = db.Table(
#     'image_token',
#     db.Column('image_id', db.Integer, db.ForeignKey('image.id')),
#     db.Column('token_id', db.Integer, db.ForeignKey('token.id'))
# )


# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(128), nullable=False)
#     _text = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'<Image "{self.uuid}">'

#     @property
#     def text(self):
#         return self._text

#     @text.setter
#     def text(self, new_text):
#         if isinstance(new_text, list):
#             self._text = ', '.join(new_text)
#         elif isinstance(new_text, str):
#             self._text = new_text
#         else:
#             raise ValueError(
#                 'Тип поля "text" должен быть строкой или списком строк')


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    alternative = db.Column(db.String(128), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # image = db.relationship('Image', secondary=image_token, backref='tokens')

    def __repr__(self):
        return f'<Token "{self.name}">'
