from django.urls import path
from . import views

app_name = 'one_page'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
]
