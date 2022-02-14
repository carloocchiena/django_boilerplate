# django boilerplate
WIP

I'd like to create a django pre-made website that could easily be customized and used for production even to non-django users.

let's see where i could land :)

### How to proceed:

Here's a draft walkthrough of the steps required to modify the django boilerplate to your needs.

1. modify the html look and feel in the `templates` folder
2. modify the images in the `static` folder (if you change the name, update the `url` in the `templates` accordingly)
3. to change the url of website section update the views in `urls.py` and in `views.py`
4. modify the `settings.py` file to your needs, don't forgetting to update the `SECRET_KEY`
5. update the models in `models.py` in the case you need other kind of data saved to the database
6. update the forms in `forms.py` in the case you need other kind of userdata
7. follow a consistency pattern in the `urls.py` and `views.py`, as well as other dependecies
8. usual dependencies in a django project are: `urls.py`, `views.py`, `models.py`, `forms.py`, `settings.py`, `admin.py` 
9. django requires a strict go-live checklist to be followed, here's a list of the things you should do: https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/ 

