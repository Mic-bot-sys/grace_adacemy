from django.urls import path
from grace_forte_app.views.BookingPaymentViews import *

urlpatterns = [
    path('get/', GetBookingPayments, name="booking_payments"),
    path('get/payment/', GetByPaymentStatus, name="confirmed_payments"),
    path('get/pending/', GetPendingBookingPayments, name="pending_payments"),
    path('get/approved/', GetApprovedBookingPayments, name="approved_payments"),
    path('post/approve/', ApproveBookingPayment, name="confirm_booking_payment"),
]