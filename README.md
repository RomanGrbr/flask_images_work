sshfs mniti@10.102.100.110:/opt/vit_data/shd_lvm/images ~/dev/flask_mniti/imcap_app/static/images

(venv) ... $ flask shell
>>> from imcap_app import db
>>> db.create_all()

Создать репозиторий с миграциями
(venv) ... $ flask db init

Создать миграции
(venv) ... $ flask db migrate -m "you comment"

Применить миграции
(venv) ... $ flask db upgrade