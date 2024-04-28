from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
    
class PlanType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    # Foreign Fields
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy_planType')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
   
    class Meta:
        verbose_name_plural = 'PlanTypes'
    
    def __str__(self):
        return self.name