from django.db import models
from django.core.validators import validate_email

# Create your models here.
class ContactDatabase(models.Model):
    objects = models.Manager() # this is needed to avoid VS Code error
    email = models.EmailField(max_length=100, validators=[validate_email])
    
    def __str__(self):
        return str(self.email)
