from django.shortcuts import render, redirect

from .forms import TwtForm
from .models import Twt, Profile

# Create your views here.
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
