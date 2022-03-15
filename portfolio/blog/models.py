from django.db import models

# Create your models here.
class Category(models.Model):
    """Manage blog categories"""
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    """Manage blog entries"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    """Manage blog comments"""
    author = models.CharField(max_length=60)
    body = models.TextField(max_length="1500")
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    