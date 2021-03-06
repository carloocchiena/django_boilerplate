from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Profile, Twt

# Register your models here.

# create our custom user admin interface
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

# add our UserAdmin class
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Twt)
