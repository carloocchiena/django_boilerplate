from django.contrib import admin
from django.contrib.auth.models import User,Group

from .models import Profile

# Register your models here.

# create our custom user admin interface
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

# remove the default admin and  group since we'll not use it
# and add our UserAdmin class
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
