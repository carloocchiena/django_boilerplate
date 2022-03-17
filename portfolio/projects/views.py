from django.shortcuts import render
from . import models

# Create your views here.
def project_index(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def project_details(request, pk):
    projects = models.Project.objects.all(), #delete this line if "next" link is not working
    project = models.Project.objects.get(pk=pk)
    
    #delete this line if "next" link is not working
    context = {
        'projects': projects,
        'project': project
    }
    
    return render(request, 'projects/project_details.html', context=context) #modify this line if "next" link is not working
