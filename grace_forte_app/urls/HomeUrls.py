from grace_forte_app.views import HomeViews
from django.urls import path


app_name = "main"

urlpatterns = [
    path('', HomeViews.home, name="home"),
    path('about/', HomeViews.about, name="about"),
    path('pending-trainings/', HomeViews.pending_trainings_transaction, name="pending-trainings"),
    path('approved-trainings/', HomeViews.approved_trainings_transaction, name="approved-trainings"),
    path('approved-bookings/', HomeViews.approved_bookings_transaction, name="approved-bookings"),
    path('pending-bookings/', HomeViews.pending_bookings_transaction, name="pending-bookings"),
    
    path('contact/', HomeViews.contact, name="contact"),
]