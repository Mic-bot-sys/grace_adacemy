from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import  *
from django.contrib.auth.models import User


class AccountInformation(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    accountName = models.CharField(max_length=255, null=False, blank=False)
    accountNo = models.CharField(max_length=15, null=False, blank=False)
    bank = models.CharField(max_length=255, null=False, blank=False)
    selected = models.BooleanField(default=False)
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="isDeletedBy_bankInformation")
    isDeleted = models.BooleanField(default=False)
    
   
    class Meta:
        verbose_name_plural = 'AccountInformation'
    
    def __str__(self):
        return f"{self.accountName} - {self.bank}"