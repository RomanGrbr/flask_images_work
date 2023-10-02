import json

import click

from . import app, db
# from .models import Image, Token


# @app.cli.command('load_tokens')
# def load_tokens():
#     """Функция загрузки изображений в базу данных."""
#     with open('0tokens.jsonlines', mode='r') as f:
#         counter = 0
#         for line in f:
#             if line:
#                 img = json.loads(line)
#                 tokens = img.pop('tokens')
#                 image = Image(**img)
#                 db.session.add(image)
#                 for name in tokens:
#                     token = Token.query.filter_by(name=name).first()
#                     if not token:
#                         token = Token(name=name)
#                         db.session.add(token)
#                         image.tokens.append(token)
#                 # db.session.add(image)
#                 counter += 1
#                 db.session.commit()
#     click.echo(f'Загружено изображений: {counter}')
