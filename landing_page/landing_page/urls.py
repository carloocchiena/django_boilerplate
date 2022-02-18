"""landing_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('one_page.urls'), name='home_page'),
    path('admin/', admin.site.urls),
]

# custom error handling
handler404 = 'one_page.views.custom_page_not_found_view'
handler500 = 'one_page.views.custom_error_view'
handler403 = 'one_page.views.custom_permission_denied_view'
handler400 = 'one_page.views.custom_bad_request_view'

# custom admin page
admin.site.site_header = "My Landing Page Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Your Site Admin Portal"
