from grace_forte_app.models.BookingModel import Booking
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
    
class Appointment(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointmentDate = models.DateTimeField(auto_now_add=True)
    rescheduledDate = models.DateTimeField(auto_now_add=False, blank=True)
    
    # Foreign Fields
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_appointment')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy_appointment')
    
    # Others
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        return str(self.appointmentDate)