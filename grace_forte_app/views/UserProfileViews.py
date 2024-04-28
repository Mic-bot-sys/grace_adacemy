from django.shortcuts import render
from grace_forte_app.models.ProfileModel import Profile
from django.contrib.auth.decorators import login_required



@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.filter(user_id=user.id).first()
    return render(request, "pages/profile.html", {"user_profile": profile})

