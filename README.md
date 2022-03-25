# Django boilerplate

[!]https://img.shields.io/tokei/lines/github.com/carloocchiena/django_boilerplate

Is it possible to use Django to create websites and web applications that are consistent, functional, and easy to use and modify?
<br><br>
Can a pre-configured Django environment offer an alternative to Wordpress and other low-code environments?<br>
<br>
That's the challenge I've attempted to scratch with this project, offering three ready-made templates for web projects.<br>

1. A landing page with a lead collection form.
2. An example of a social network with user logins and interactions between them.
3. A traditional website with Blog, Products and About pages.

The project will be work in progress for a while, and I'd also like it to become an open source project, with contributions and comments from other users.<br>
So feel free to reach out to me if you have any questions or suggestions.<br>

Let's see where I could land :)<br>

## Environment setup and quick-start
1. Clone the project: `git clone https://github.com/carloocchiena/django_boilerplate.git` 
2. Create a virtual environment (conda `conda create -n my_env pip python=3.8`) (python `python3 -m venv my_env`)
3. Activate your virtual environment: (conda`conda activate my_env`) (Linux/MacOS `source my_env/bin/activate`) (Windows `source my_env/Scripts/activate`)
4. Install requirements.txt: `pip install -r requirements.txt` 
5. Navigate to the folder you want (`landing_page`, or `portfolio` or `social`) 
6. Make migrations with: `python manage.py makemigrations` and apply them with  `python manage.py migrate`
7. Let's start the engine with `python manage.py runserver`
8. Have fun! :) 

## How to proceed:

Here's a draft walkthrough of the steps required to modify the django boilerplate to your needs.

1. modify the html look and feel in the `templates` folder
2. modify the images in the `static` folder (if you change the name, update the `url` in the `templates` accordingly)
3. to change the url of website section update the views in `urls.py` and in `views.py`
4. modify the `settings.py` file to your needs, don't forgetting to update the `SECRET_KEY`
5. update the models in `models.py` in the case you need other kind of data saved to the database
6. update the forms in `forms.py` in the case you need other kind of userdata
7. follow a consistency pattern in the `urls.py` and `views.py`, as well as other dependecies
8. usual dependencies in a django project are: `urls.py`, `views.py`, `models.py`, `forms.py`, `settings.py`, `admin.py` 
9. django requires a strict go-live checklist to be followed, [here's a list of the things you should do](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/). 

**Important:** in none of these projects have additional security features been implemented beyond the standard Django features.<br>
The project is a continuous work in progress and this version was created for educational and demonstration purposes, not for production use.<br> In any case, use it with caution and awareness of possible risks.<br>
For further information about warranty and compliance, please refer to the MIT License, under which this project is released.

---

### Landing Page

CSS: Bootstrap 5.0.0

This is a template for a static landing page teasing a launch of a new product\service\brand.<br>
To modify the look and feel of the landing page, modify the html in the `templates` folder.<br>
While to update images, background and logo, just update them in the `static\landing_page\img` folder.<br>
There are no issues as soon as you keep the same names. If you'd like to update them, you should also update the templates accordingly, using the static convention (`src="{% static 'landing_page/img/image_name.jpg' %}"`).<br>
The landing page has an admin section (url_name/admin) where you can check and interact with the saved data. To create a superuser, check the `CLI_commands` file. Currently there's just a superuser called `admin` with the password `admin`.<br>

#### Interesting features
- Plain vanilla full-stack Django project, perfect to start with.
- Responsive Bootstrap 5 design.
- Custom admin section with user management and the ability to get all the users emails.
- Easy to customize and expand following the boilerplate logic.

---

### Social Media Clone

##### CSS: Bulma v0.9.3 and Font Awesome 6.0.0

##### Database Diagram:

Check the in-folder image for zoom and better quality.

![twtr_db_diagram](https://user-images.githubusercontent.com/57464184/159914308-407a4016-2259-4bd5-86a6-1e48cea70e71.png)

A true Django classic: the Twitter clone. 
Modify this is a little bit harder than the landing page since the items are heavily interconnected one each other.<br>
Anyway, you'll find:<br>
1. the standard navbar, that conveniently redirect to the home page.
2. the first page, that is the login page for non-registered user.
3. `Login` and `Register` page.
4. `Dashboard` page, that is the landing for registered user, where you can see all the tweets for the users you follow (yourself included). From this page you can also add more tweets and visit the `All Profiles` page and `My Profile` page. Here there is also a `Logout` button.
Each tweet has a link to its creator, and daytime details. 
5. all profiles page where you have all the profiles with default avatars and links to their respective pages.
6. my profile page where you can see all the tweets you've created, and the users you are following and that are following you. A `Logout` button is also here, interesting, this is dinamically rendered depending on the user.
7. Admin page allows you to manage all the users, and the tweets.

Bulma is an interesting framework. The documentation is not as good as Bootstrap, but the classes are somehow simpler than Bootstrap. I don't mind using it. It has been a good experiment.<br>
Starting from this social media template it's not hard to replicate to other kind of similar or even more complex social media interactions.

#### Interesting features
- A good base for a more complex usage of Django.
- User lifecycle management: signup, signin, signout.
- Social Media interactions: follow, unfollow, see users list, see contents based on the people the user is following.
- Interactive dashboard: multiple access point to user profile clicking on redirect links.

---

### Personal blog and portfolio showcase 

CSS: Bootstrap 5.0.0

A website aiming to provide a canvas for a portfolio (or products) showcase, a blog and an about page.<br>
At this point won't be harder to you to mix other features from social media (such as login) or landing page (such as lead gen form).<br>
The admin section here is the core for data entry and content creation. <br>
You can easily uploads media files, edit texts, create new product cards. <br>
Blog is pretty straight forward, no images at the moment, but a category tag and comment section. <br>
About page shows just a little image, contact data and text. But being plain html here should not be hard to extend.<br>

#### Interesting features
- Clean project, great opportunity to be cannibalized and used elsewhere.
- Easily create project objects via admin panel.
- Image management via `media` folder.
- Pre-made templates for project details page.
- Custom `next` button to navigate thru the project details page.
- Pretty good example of Django project with multiple app (`blog`, `projects`) with templates and models.
- Ready-made blog template with categories, index and detail views.

---

### Please readme
I created also some additional walktrought that should help you configuring your Django project:<br>
[The django walkthrough](django_walktrought.md)<br>
[A list of useful commands](CLI_commands.md)<br>

---

### Contribute
Every feedback and contribution is welcome.
Please just:
1. open an issue and discuss the changes you'd like to make or  the bug\issue you'd like to report<br>
2. once ready to submit a pull request, provide proof of the testing you've done<br>
