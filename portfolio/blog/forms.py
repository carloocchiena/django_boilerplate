from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        label='Name', 
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        })
    )
    body = forms.CharField(
        label='Comment',
        max_length=1500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write your comment'
            })
    )
 