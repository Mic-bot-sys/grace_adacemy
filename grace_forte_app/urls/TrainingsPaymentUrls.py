from django.urls import path

from grace_forte_app.views import TrainingsPaymentViews

app_name = "training_payment"

urlpatterns = [
    path('post', TrainingsPaymentViews.training_payment, name="training-payment"),
]