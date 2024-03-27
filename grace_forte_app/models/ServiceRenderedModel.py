from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import  *
from django.contrib.auth.models import User

class ServiceRendered(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    imageBase = models.TextField(null=True, blank=True)
    price= models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    priceType = models.CharField(max_length=255, null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    
    # Other fields
    dateUpdated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updatedBy')
    dateCreated = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='serviceCreatedBy')
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='isDeletedBy')
    isDeleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    