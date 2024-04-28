from django.urls import path
from grace_forte_app.views.AdminTrainingViews import *

app_name = "admin_training"

urlpatterns = [
    path('create', create_training, name="create-training"),
    path('get', trainings, name="all-training"),
    path('get/<str:id>/', getTrainingDetails, name="training-details"),
    path('edit/', updateTraining, name="update-details"),
]