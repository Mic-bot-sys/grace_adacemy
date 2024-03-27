from grace_forte_app.models.AccountInformationModel import AccountInformation
from grace_forte_app.models.BookingModel import Booking
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from grace_forte_app.signals.service_email_signals import serviceEmailNotifySignals
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save



class ServicePayment(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paymentStatus = models.CharField(max_length=50, default="Pending")
    proofBase = models.TextField()
    bookedDuration = models.CharField(max_length=50, default="1hr")
    expectedAmount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    isApproved = models.BooleanField(default=False)
    approvedDate = models.DateTimeField(auto_now_add=False, blank=True, null=True )
    preferedBookingDate = models.DateTimeField(auto_now_add=False, blank=True, null=True )
    isExpired = models.BooleanField(default=False)
    receiptId = models.CharField(max_length=100)

    # Foreign Fields
    service = models.ForeignKey(ServiceRendered, on_delete=models.CASCADE, related_name="service_payment")
    account = models.ForeignKey(AccountInformation, on_delete=models.CASCADE, related_name="account_service")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_service')
    approvedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_admin_approved')

    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    
    class Meta:
        verbose_name_plural = 'ServicePayment'
        
    
    def __str__(self):
        return f'{self.user.user_profile.firstName} - {self.service.title} {self.paymentStatus}'
    
    
    def getDateApprovedOnly(self):
        return self.approvedDate.strftime('%B %d %Y')
    
# Connecting to the Signals
post_save.connect(serviceEmailNotifySignals, sender=ServicePayment)