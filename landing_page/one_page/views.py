from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import ContactDatabase

# home page
class HomePage(TemplateView):
    """Manage home page and forms"""
    template_name = 'landing_page/home_page.html'
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        """Manage form submission"""
        form = ContactForm(request.POST)
        if form.is_valid():
            if ContactDatabase.objects.filter(email=form.cleaned_data['email']).count() < 1:
                print(form.cleaned_data)
                form.save()
                message = 'Thanks for your interest!'
            else:
                message = 'Warning! Email already exists'
        else:
            message = 'Insert a valid email!'
        
        return render(request, self.template_name, {'form': form, 'warning': message})
        
# about page
class AboutPage(TemplateView):
    template_name = 'landing_page/about_page.html'
    
# custom error handling

# 404 page
def custom_page_not_found_view(request, exception=None):
    return render(request, "landing_page/errors/404.html", status=404)

# 500 page
def custom_error_view(request, exception=None):
    return render(request, "landing_page/errors/500.html", status=500)

# 403 page
def custom_permission_denied_view(request, exception=None):
    return render(request, "landing_page/errors/403.html", status=403)

# 400 page
def custom_bad_request_view(request, exception=None):
    return render(request, "landing_page/errors/400.html", status=400)
