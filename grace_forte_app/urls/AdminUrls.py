from django.urls import path
from grace_forte_app.views.AdminAuthViews import admin_login
from grace_forte_app.views.AdminDashboardViews import dashboard
from grace_forte_app.views.AdminTransactionViews import *

app_name = "the_admin"

urlpatterns = [
    path('', admin_login, name="admin_auth"),
    
    path('dashboard/', dashboard, name="dashboard"),
    path('pending/', pending_training_payments, name="pending-training-payments"),
    path('booking/pending/', pending_booking_payments, name="pending-booking-payments"),
    path('pending/<str:id>/', pending_training_payment_details, name="pending-training_payment-details"),
    path('booking/pending/<str:id>/', pending_booking_payment_details, name="pending-booking-payment-details"),
    
    path('approved/', approved_training_payments, name="approved-training-payments"),
    path('booking/approved/', approved_booking_payments, name="approved-booking-payments"),
    path('approved/<str:id>/', approve_training_payment, name="approve-training-payment"),
    path('booking/approved/<str:id>/', approve_booking_payment, name="approve-booking-payment"),
    path('approved/get/<str:id>/', approved_training_payment_details, name="approve-training-payment-details"),
    path('booking/approved/get/<str:id>/', approved_booking_payment_details, name="approve-booking-payment-details"),
    
]