from django.urls import path

from .views import dashboard

app_name = 'twtr'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
