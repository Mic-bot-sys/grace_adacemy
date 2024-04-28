from django.urls import path

from grace_forte_app.views.BookingViews import *

urlpatterns = [
    path('get/', GetBookings, name="get_bookings"),
    path('get/<str:id>/', GetBookingById, name="get_booking"),
    path('post', CreateBooking, name="create_booking"),
]