from django.urls import path

from grace_forte_app.views.UserProfileViews import *


app_name = "user_profile"


urlpatterns = [
    path('', user_profile, name="user-profile"),
]