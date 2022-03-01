from django.shortcuts import render
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, 'twtr/dashboard.html')

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
