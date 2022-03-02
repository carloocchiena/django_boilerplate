from django import forms
from .models import Twt

class TwtForm(forms.ModelForm):
    """Manage input with a form field in dashboard"""
    body = forms.CharField(required=True, 
                           widget=forms.widgets.Textarea(
                               attrs={'placeholder': 'What\'s happening?',
                                      'class':'textarea is-info is-medium'}),
                           label='',
                           )
    
    class Meta:
        model = Twt
        exclude = ('user',)
        