from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
    
class Employee(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255,  blank=False, null=False)
    middleName = models.CharField(max_length=255,  blank=True, null=True)
    homeAddress = models.CharField(max_length=255, editable=True)
    
    # Foreign Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=False, blank=True, null=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.middleName}"