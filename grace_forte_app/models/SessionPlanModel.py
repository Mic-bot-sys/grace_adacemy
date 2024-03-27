from grace_forte_app.models.PlanTypeModel import PlanType
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User

class SessionPlan(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price= models.DecimalField(max_digits=20, decimal_places=2)
    duration= models.DecimalField(max_digits=10, decimal_places=2)
    
    # Foreign Fields
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy_sessionPlan')
    planType = models.ForeignKey(PlanType, on_delete=models.CASCADE, related_name='planType')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name_plural = 'SessionPlans'
    
    def __str__(self):
        return self.name
    