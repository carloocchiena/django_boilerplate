from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_details, name='project_details'),
    path('about/', views.about_page, name='about_page'),
]
