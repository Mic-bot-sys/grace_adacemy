from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
import uuid

class Discount(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    percentage = models.IntegerField()
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)   
    
    def __str__(self):
        return self.percentage