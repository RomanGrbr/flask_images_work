(venv) ... $ flask shell
>>> from opinions_app import db
>>> db.create_all()

Создать репозиторий с миграциями
(venv) ... $ flask db init

Создать миграции
(venv) ... $ flask db migrate -m "you comment"

Применить миграции
(venv) ... $ flask db upgrade