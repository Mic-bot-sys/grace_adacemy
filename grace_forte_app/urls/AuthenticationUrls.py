from django.urls import path
from grace_forte_app.views.AuthenticationViews import *


app_name = "authentication"

urlpatterns = [
    path('', auth, name="auth"),
    path('login', loginUser, name="login"),
    path('register', register, name="register"),
    path('logout', logoutUser, name="logout"),
]