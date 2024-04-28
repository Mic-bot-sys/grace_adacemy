from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import  *
from django.contrib.auth.models import User

class Profile(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_profile')
    imageBase = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    
    # Other fields
    dateUpdated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstName
    
    
    def get_full_name(self):
        return f"{self.lastName} {self.firstName}"