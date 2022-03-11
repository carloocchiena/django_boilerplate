# Django Walkthrough

A basic checklist for getting started with Django:

1. we assume you have already a virtual environment with django installed.
2. activate your venv: `conda activate my_env`
3. create a new django project: `django-admin startproject my_project`
4. create a new django app: `python manage.py startapp my_app`
5. register the app in setting.py `INSTALLED_APPS = [`
6. register the app in admin.py `admin.site.register(MyModel)`
7. remove secret key into .env
8. create a `urls.py` file in your app and link it to main project urls.py with `include`
9. register your app name in such `urls.py` file `app_name = 'my_app'`
10. update `settings.py` accordingly with the location of your static and templates folder if needed
11. run migrations
12. create a superuser
13. create your first model
14. make migrations and run migrations
15. add custom custom errors templates
16. align or customize admin section


## About the django workspace and virtual env you are using 
I recommend you to include in the virtual environment:

1. `pip install python-dotenv` in order to manage the .env file and secrets in your project.<br>

The usage is as follows:<br>
`from dotenv import load_dotenv, find_dotenv`<br>

`load_dotenv(find_dotenv())`<br>
`SECRET_KEY = os.environ['SECRET_KEY']`<br>

2. `pip install pylint-django`

Also, include in the workspace (root):

3. a custom python file `.pylintrc` for each project.<br>
run in terminal: `pylint --generate-rcfile > .pylintrc`<br>
then I suggest you to add:<br>

>in [MASTER] section:<br>
`load-plugins=pylint_django`<br>
`django-settings-module=myprojectname.settings`<br>

>in [BASIC] section:<br>
`docstring-min-length=10`<br>

Please also note that .2 and .3 are mostly to avoid VS CODE stressing you with non-existent warnings and errors.
