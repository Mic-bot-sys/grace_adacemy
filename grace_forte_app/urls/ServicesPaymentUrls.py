from django.urls import path
from grace_forte_app.views.ServicesPaymentViews import service_payment


app_name = "service_payment"

urlpatterns = [
    path('post', service_payment, name="service-payment"),
]