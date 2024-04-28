from grace_forte_app.models.EmployeeModel import Employee
from grace_forte_app.models.HierarchyModel import Hierarchy
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
    
class EmployeeHierarchy(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='employee')
    hierarchy = models.ForeignKey(Hierarchy, on_delete = models.CASCADE, related_name='hierarchy')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'EmployeeHierarchies'
    
    def __str__(self):
        return f"{self.employee.user.username} - {self.hierarchy.title}"