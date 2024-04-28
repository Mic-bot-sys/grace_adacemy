from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
from datetime import datetime
    
class Course(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    price= models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    accessLink = models.CharField(max_length=255, null=True, blank=True)
    imageBase = models.TextField(null=True, blank=True)


    # Foreign Fields
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy_course')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
   
    class Meta:
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        # return f"{self.title} - {self.code}"
        return self.title