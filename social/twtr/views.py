from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import TwtForm
from .models import Twt, Profile

# Create your views here.
@login_required
def dashboard(request):
    """Manage interactions within the dashboard"""
    form = TwtForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            twt = form.save(commit=False)
            twt.user = request.user
            twt.save()
            return redirect('twtr:dashboard')
    
    followed_twts = Twt.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-created_at')
        
    return render(request, 'twtr/dashboard.html', {'form': form, 'twts': followed_twts})

def register(request):
    """Manage user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('twtr:dashboard')
    
    else:
        form = UserCreationForm()
    return render(request, 'twtr/register.html', {'form': form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'twtr/profile_list.html', {'profiles': profiles})

def profile(request, pk):
    """Manage user profile, follows and unfollows"""
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'twtr/profile.html', {'profile': profile})

# custom error handling

# 404 page
def custom_page_not_found_view(request, exception=None):
    return render(request, "twtr/errors/404.html", status=404)

# 500 page
def custom_error_view(request, exception=None):
    return render(request, "twtr/errors/500.html", status=500)

# 403 page
def custom_permission_denied_view(request, exception=None):
    return render(request, "twtr/errors/403.html", status=403)

# 400 page
def custom_bad_request_view(request, exception=None):
    return render(request, "twtr/errors/400.html", status=400)