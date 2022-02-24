from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

# remove the default admin group since we'll not use it
admin.site.unregister(Group)
