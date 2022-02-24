# Django Walkthrough

A basic checklist for getting started with Django:

1. We assume you have already a virtual environment with django installed.
2. activate your venv: `conda activate my_env`
3. create a new django project: `django-admin startproject my_project`
4. create a new django app: `python manage.py startapp my_app`
5. register the app in setting.py `INSTALLED_APPS = [`
6. remove secret key into .env
7. run migrations
8. create a superuser
9. create your first model
10. make migrations and run migrations