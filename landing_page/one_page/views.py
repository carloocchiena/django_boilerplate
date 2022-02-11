from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            #return redirect(reverse('home_page'))
    else:
        form = ContactForm() 
    return render(request, 'landing_page/home_page.html', context={'form':form})
