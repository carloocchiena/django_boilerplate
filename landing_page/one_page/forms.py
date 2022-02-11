from django import forms
from django.forms import ModelForm
from .models import ContactDatabase

class ContactForm(ModelForm):
    class Meta:
        model = ContactDatabase
        fields = "__all__"
        
        # add here your custom labels for the forms
        labels = {
            'email': 'Please insert your email'
        }
        
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'})
        }
        