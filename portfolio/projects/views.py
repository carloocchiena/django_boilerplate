from django.shortcuts import render
from . import models

# Create your views here.
def project_index(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def project_details(request, pk):
    project = models.Project.objects.get(pk=pk)
    return render(request, 'projects/project_details.html', {'project': project}) 
