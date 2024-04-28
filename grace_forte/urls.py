from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-user/', include('grace_forte_app.urls.AdminUrls')),
    
    
    path('', include('grace_forte_app.urls.HomeUrls')),
    path('auth/', include('grace_forte_app.urls.AuthenticationUrls')),
    path('services/', include('grace_forte_app.urls.ServicesUrls')),
    path('trainings/', include('grace_forte_app.urls.TrainingsUrls')),
    path('trainings-payment/', include('grace_forte_app.urls.TrainingsPaymentUrls')),
    path('services-payment/', include('grace_forte_app.urls.ServicesPaymentUrls')),
    path('user-profile/', include('grace_forte_app.urls.UserProfileUrls')),    
    
    path('admin-user/training/', include('grace_forte_app.urls.AdminTrainingUrls')),
    path('admin-user/service/', include('grace_forte_app.urls.AdminServiceUrls')),
]

if settings.DEBUG:
    urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)