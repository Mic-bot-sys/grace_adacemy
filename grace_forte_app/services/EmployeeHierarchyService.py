from GraceForteAPI.Models.EmployeeHierarchyModel import EmployeeHierarchy
from GraceForteAPI.Serializers.EmployeeHierarchySerializer import EmployeeHierarchySerializer
from .BaseImportService import *




def GetEmployeeHierarchies():
    # notification = BookingNotification(receiver, subject, body)
    employeeHierarchies = EmployeeHierarchy.objects.filter(isDeleted=False).order_by('dateCreated')      
    if employeeHierarchies is not None:
        serializer = EmployeeHierarchySerializer(employeeHierarchies, many=True)
        return serializer
    return None
        
        
        
def GetEmployeeHierarchyById(id):
    employeeHierarchy = EmployeeHierarchy.objects.filter(isDeleted=False, Id=id).first()
    if employeeHierarchy is not None:
        serializer = EmployeeHierarchySerializer(employeeHierarchy, many=False)
        return serializer
    return None