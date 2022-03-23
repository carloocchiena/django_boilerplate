- start a new Python env: `conda create -n my_env pip python=3.8.8`

- activate Python Env: `conda activate my_env`

- create custom pylint file: `pylint --generate-rcfile > .pylintrc`

- install Django: `pip install django`

- update requirements.txt: `pip list --format=freeze > requirements.txt`

- start django app: `django-admin startproject my_project`

- run django server: `python manage.py runserver -port=8000`

- start new django app: `python manage.py startapp my_app`

- make the migration: `python manage.py makemigrations`

- migrate the main database: `python manage.py migrate`

- migrate the app database: `python manage.py migrate my_app`

- see SQL commands run by django: `python manage.py sqlmigrate first_app 0001`

- run django shell: `python manage.py shell`

- run django db shell: `python manage.py dbshell`

- run django tests: `python manage.py test`

- import modules in the shell: `from first_app.models import MyModel`

- examples of queries: `MyModel.objects.all()`, `MyModel.objects.filter(name='my_name')`, `MyModel.objects.filter(age__gte=20).all()`, `MyModel.objects.filter(first_name__startswith="c").all()`, `MyModel.objects.filter(first_name__startswith="c").exclude(age__gte=20).all()`, `MyModel.objects.order_by('age').all()`

- create superuser: `python manage.py createsuperuser`

- run tests `python manage.py test --verbosity=2` 

- collect all static files `python manage.py collectstatic` (run this command in the production environments)