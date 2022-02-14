from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render

from .forms import ContactForm
from .models import ContactDatabase

def home_page(request):
    """Manage how user interact with the form in the landing page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            if ContactDatabase.objects.filter(email=form.cleaned_data['email']).count() < 1:
                print(form.cleaned_data)
                form.save()
                return render(request, 'landing_page/home_page.html', context={'form':form, 'warning': 'Thanks for your interest!'})
            else:
                return render(request, 'landing_page/home_page.html', context={'form':form, 'warning': 'Warning! Email already exists'})
        else:
                return render(request, 'landing_page/home_page.html', context={'form':form, 'warning': 'Insert a valid email!'})
    else:
        form = ContactForm()
    return render(request, 'landing_page/home_page.html', context={'form':form, 'warning': ''})
