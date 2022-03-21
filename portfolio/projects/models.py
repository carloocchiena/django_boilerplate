from django.db import models

# Create your models here.
class Project(models.Model):
    """model for the single project"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(null=True, blank=True)
    
    def get_next(self):
        """function to navigate thru the projects using a Next button"""
        next = Project.objects.filter(id__gt=self.id).order_by('id').first()
        if next:
            return next
        else:
            return Project.objects.all().order_by('id').first()
       