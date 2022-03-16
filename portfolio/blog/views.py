from django.shortcuts import render, redirect

from . import models
from . import forms

# Create your views here.
def blog_index(request):
    """return blog main page"""
    posts = models.Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    
    return render(request, "blog/blog_index.html", context)

def blog_category(request, category):
    """return the blog categories"""
    posts = models.Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    
    return render(request, "blog/blog_category.html", context)

def blog_detail(request, pk):
    """return the blog item with comment form"""
    post = models.Post.objects.get(pk=pk)
    form = forms.CommentForm()
    
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comments(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    
    comments = models.Comments.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    
    return render(request, "blog/blog_detail.html", context)
