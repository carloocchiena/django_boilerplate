from django.contrib.auth import views as auth_views
from django.urls import path

from .views import dashboard, profile_list, profile, register

app_name = 'twtr'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='twtr/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='twtr/logout.html'), name='logout'),
    path('register/', register, name='register'),
    # path('accounts/', include('django.contrib.auth.urls')), # default django auth urls you may abilitate
]
