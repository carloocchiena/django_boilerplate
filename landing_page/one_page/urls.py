from django.urls import path
from . import views

app_name = 'one_page'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('about/', views.AboutPage.as_view(), name='about_page'),
]
