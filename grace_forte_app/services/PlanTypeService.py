from GraceForteAPI.Models.PlanTypeModel import PlanType
from GraceForteAPI.Serializers.PlanTypeSerializer import PlanTypeSerializer
from .BaseImportService import *



def GetPlanTypes():
    # notification = BookingNotification(receiver, subject, body)
    planTypes = PlanType.objects.filter(isDeleted=False).order_by('name')
    if planTypes is not None:
        serializer = PlanTypeSerializer(planTypes, many=True)
        return serializer
    return None
        
        
        
def GetPlanTypeById(id):
    planType = PlanType.objects.filter(isDeleted=False, Id=id).first()
    if planType is not None:
        serializer = PlanTypeSerializer(planType, many=False)
        return serializer
    return None
        
        
        
def CreatePlanType(body):
    name = body.get('name')
    createdById = body.get('createdBy')
    
    createdBy = User.objects.get(pk = createdById)
    
    with transaction.atomic():
        planType = PlanType(
            name = name,
            createdBy = createdBy
        )
        planType.save()
        
        serializer = PlanTypeSerializer(planType, many=False)
        return serializer
    return None



def UpdatePlanType(id, body):
    name = body.get('name')
    
    planType = PlanType.objects.filter(Id=id).first()
    if planType is not None:
        planType.name = name
        planType.save()

        serializer = PlanTypeSerializer(planType, many=False)
        return serializer
    
    
    
def DeletePlanType(id):
    planType = PlanType.objects.filter(Id=id).first()
    planType.isDeleted = True
    planType.save()
    
    result = "Record Deleted Successfully"
    return result