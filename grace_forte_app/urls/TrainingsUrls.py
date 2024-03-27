from django.urls import path

from grace_forte_app.views import TrainingsViews

app_name = "trainings"

urlpatterns = [
    path('', TrainingsViews.trainings, name="trainings"),
    path('details/<str:id>/', TrainingsViews.training_details, name="training-details"),
    path('enroll/<str:id>/', TrainingsViews.training_enrollment, name="training-enrollment"),
    path('training-receipt/<str:id>/', TrainingsViews.approved_training_receipt, name="training-receipt"),
]