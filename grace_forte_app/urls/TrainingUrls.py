from django.urls import path

from grace_forte_app.views.TrainingViews import *

urlpatterns = [
    path('get/', GetTrainings, name="get_trainings"),
    path('get/<str:id>/', GetTrainingById, name="get_training"),
    path('post', CreateTraining, name="create_training"),
]