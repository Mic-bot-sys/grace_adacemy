from django.urls import path
from grace_forte_app.views import ServicesViews

app_name = "services"

urlpatterns = [
    path('', ServicesViews.services, name="services"),
    path('details/<str:id>/', ServicesViews.service_details, name="service-details"),
    path('onnote/<str:id>/<str:duration>/<str:totalAmount>/', ServicesViews.service_note, name="service-note"),
    path('book/<str:id>/', ServicesViews.service_booking, name="service-bookings"),
    path('service-booking-receipt/<str:id>/', ServicesViews.approved_service_receipt, name="service-receipt"),
]