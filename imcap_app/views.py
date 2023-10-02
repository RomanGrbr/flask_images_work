import json

from flask import redirect, render_template, url_for, flash

from . import app, db
from .forms import TokenForm
from .models import Token


IMAGES = []


with open('0tokens.jsonlines', mode='r') as file:
    """Открыть файл и составить список с записями"""
    for line in file:
        if line:
            IMAGES.append(json.loads(line))
    file.close()


def get_url(uuid: str) -> str:
    """Получить путь к директории с изображением"""
    if uuid:
        return f'/static/images/{uuid[:2]}/{uuid[2:4]}/{uuid}.jpg'
    return ''


def get_tokens_alternatives(image_tokens: list) -> list:
    """Формирует строки с именами токенов и их альтернативами из базы"""
    tokens = list()
    for name in image_tokens:
        token = Token.query.filter_by(name=name.lower()).first()
        if token:
            tokens.append(
                {'name': f'{name} -> {token.alternative}', 'id': token.id})
        else:
            tokens.append({'name': name})
    return tokens


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = TokenForm()
    try:
        with open('session.txt', mode='r') as session:
            line = session.readline()
            number = int(line.strip())
    except FileNotFoundError:
        with open('session.txt', mode='w') as session:
            number = 0
            session.write(str(number))

    image: dict[str, list[str]] = {
        'uuid': IMAGES[number].get('uuid'),
        'text': IMAGES[number].get('text'),
        'tokens': get_tokens_alternatives(IMAGES[number].get('tokens'))
    }

    if form.validate_on_submit():
        name = form.name.data.lower()
        alternative = form.alternative.data.lower()
        if name not in IMAGES[number].get('tokens'):
            flash('Такого токена нет на странице!', 'not_token_in_page')
            return render_template(
                'index.html', image=image, form=form,
                file=get_url(image.get('uuid'))
                )
        token_from_db = Token.query.filter_by(name=name).first()
        if token_from_db:
            token_from_db.alternative = alternative
            db.session.add(token_from_db)
            db.session.commit()
            return redirect(url_for('index_view'))
        token = Token(
            name=name,
            alternative=alternative
        )
        db.session.add(token)
        db.session.commit()
        return redirect(url_for('index_view'))
    return render_template(
                'index.html', image=image, form=form,
                file=get_url(image.get('uuid'))
                )


def open_file_and_write(minus: bool) -> None:
    """Вычислить и записать индекс текущего изображения"""
    with open('session.txt', mode='r') as session_read:
        line = session_read.readline()
        if line:
            number = int(line.strip())
    with open('session.txt', mode='w') as session_write:
        session_write.write(str(number - 1 if minus else number + 1))


@app.route('/next')
def next_view():
    """Следующее изображение"""
    open_file_and_write(minus=False)
    return redirect(url_for('index_view'))


@app.route('/previous')
def previous_view():
    """Предыдущее изображение"""
    open_file_and_write(minus=True)
    return redirect(url_for('index_view'))


@app.route('/delete/<int:token_id>')
def delete_token_view(token_id: int):
    token = Token.query.get_or_404(token_id)
    db.session.delete(token)
    db.session.commit()
    return redirect(url_for('index_view'))
