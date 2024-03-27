from GraceForteAPI.Models.EmployeeModel import Employee
from GraceForteAPI.Serializers.EmployeeSerializer import EmployeeSerializer
from .BaseImportService import *



def GetEmployees():
    # notification = BookingNotification(receiver, subject, body)
    employees = Employee.objects.filter(isDeleted=False).order_by('-dateCreated')
    if employees is not None:
        serializer = EmployeeSerializer(employees, many=True)
        return serializer
    return None
        
        
        
def GetEmployeeById(id):
    employee = Employee.objects.filter(isDeleted=False, Id=id).first()
    if employee is not None:
        serializer = EmployeeSerializer(employee, many=False)
        return serializer
    return None
        
        
        
def CreateEmployee(body):
    firstName = body.get('firstName')
    lastName = body.get('lastName')
    middleName = body.get('middleName')
    homeAddress = body.get('homeAddress')
    createdById = body.get('createdBy')
    
    createdBy = User.objects.get(pk = createdById)
    
    with transaction.atomic():        
        if firstName and lastName is not None:  
            employee = Employee(
            firstName = firstName,
            lastName = lastName,
            createdBy = createdBy
            )
        if middleName is not None:
            employee.middleName = middleName
        if homeAddress is not None:
            employee.homeAddress = homeAddress
            
        employee.save()
        
    serializer = EmployeeSerializer(employee, many=False)
    return serializer
    return None



def UpdateEmployee(employeeId, body):
    firstName = body.get('firstName')
    lastName = body.get('lastName')
    middleName = body.get('middleName')
    homeAddress = body.get('homeAddress')
    
    employee = Employee.objects.filter(Id=employeeId).first()
        
    with transaction.atomic():
        if firstName and lastName is not None:
            employee.firstName = firstName
            employee.lastName = lastName
        if middleName is not None:
            employee.middleName = middleName
        if homeAddress is not None:
            employee.homeAddress = homeAddress
        employee.lastUpdated = datetime.now()
        employee.save()

    updated_employee = Employee.objects.filter(Id=employeeId).first()
    serializer = EmployeeSerializer(updated_employee, many=False)
    return serializer
    
    
    
def DeleteEmployee(id, body):
    deletedBy = body.get('deletedBy')
    
    employee = Employee.objects.filter(Id=id).first()
    employee.isDeleted = True
    employee.dateDeleted = datetime.now()
    
    user = User.objects.get(pk=int(deletedBy))
    employee.isDeletedBy = user
    employee.save()
    
    result = "Employee Deleted Successfully"
    return result