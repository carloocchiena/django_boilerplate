from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Use to customize admin pages"""
    pass

class CategoryAdmin(admin.ModelAdmin):
    """Use to customize admin pages"""
    pass

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
