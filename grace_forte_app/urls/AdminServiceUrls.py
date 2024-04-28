from django.urls import path

from grace_forte_app.views.AdminServiceViews import *

app_name = "admin_service"

urlpatterns = [
    path('create', create_service, name="create-service"),
    path('get/', services, name="all-services"),
    path('get/<str:id>/', getServiceDetails, name="service-details"),
    path('edit/', updateService, name="update-service-details"),

]