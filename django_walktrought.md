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


## About the django workspace and virtual env you are using 
I recommend you to include in the virtual environment:

1. `pip install python-dotenv` in order to manage the .env file and secrets in your project.
the process is as follows:
`from dotenv import load_dotenv, find_dotenv`

`load_dotenv(find_dotenv())`
`SECRET_KEY = os.environ['SECRET_KEY']`

2. `pip install pylint-django`

Also, include in the workspace (root):

3. a custom python file `.pylintrc` for each project.
run in terminal: `pylint --generate-rcfile > .pylintrc`
then I suggest  you to add:

>in [MASTER] section:
`load-plugins=pylint_django`
`django-settings-module=myprojectname.settings`

>in [BASIC] section:
`docstring-min-length=10`

Please also note that .2 and .3 are mostly to avoid VS CODE stressing you with non-existent warnings and errors.


