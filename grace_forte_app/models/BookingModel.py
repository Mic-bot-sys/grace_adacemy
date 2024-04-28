from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid

from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from grace_forte_app.special_services.CustomDateTime import DateTime

# Create your models here.
class Booking(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookerFirstName = models.CharField(max_length=50, blank=True, null=True)
    bookerLastName = models.CharField(max_length=50, blank=True, null=True)
    phoneNumber = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, null=False)
    accessCode = models.CharField(max_length=6, blank=True, null=True)
    
    # Foreign Fields
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_booking')
    serviceRendered = models.ForeignKey(ServiceRendered, blank=True, null=True, on_delete=models.CASCADE, related_name='serviceRendered')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    
    class Meta:
        verbose_name_plural = 'Bookings'
    
    def __str__(self):
        return f"{self.bookerLastName} {self.bookerFirstName}"
    


