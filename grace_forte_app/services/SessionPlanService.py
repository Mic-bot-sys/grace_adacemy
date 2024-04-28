from GraceForteAPI.Models.PlanTypeModel import PlanType
from GraceForteAPI.Models.SessionPlanModel import SessionPlan
from GraceForteAPI.Serializers.SessionPlanSerializer import SessionPlanSerializer
from .BaseImportService import *




def GetSessionPlans():
    # notification = BookingNotification(receiver, subject, body)
    sessionPlans = SessionPlan.objects.filter(isDeleted=False).order_by('name')
    if sessionPlans is not None:
        serializer = SessionPlanSerializer(sessionPlans, many=True)
        return serializer
    return None
        
        
        
def GetSessionPlanById(id):
    sessionPlan = SessionPlan.objects.filter(isDeleted=False, Id=id).first()
    if sessionPlan is not None:
        serializer = SessionPlanSerializer(sessionPlan, many=False)
        return serializer
    return None
        
        
        
def CreateSessionPlan(body):
    name = body.get('name')
    price = body.get('price')
    duration = Decimal(body.get('duration'))
    createdById = body.get('createdBy')
    planTypeId = body.get('planTypeId')
    
    if not SessionPlan.objects.filter(name=name).exists():
        createdBy = User.objects.get(pk = createdById)
        planType = PlanType.objects.filter(Id = planTypeId).first()
        
        with transaction.atomic():
            sessionPlan = SessionPlan(
                name = name,
                price = price,
                duration = duration,
                createdBy = createdBy,
                planType = planType,
            )
            sessionPlan.save()
            
            serializer = SessionPlanSerializer(sessionPlan, many=False)
            return serializer
    return None



def UpdateSessionPlan(id, body):
    name = body.get('name')
    price = body.get('price')
    duration = Decimal(body.get('duration'))
    
    sessionPlan = SessionPlan.objects.filter(Id=id).first()
    if sessionPlan is not None:
        sessionPlan.name = name
        sessionPlan.price = price
        sessionPlan.duration = duration
        sessionPlan.save()

        serializer = SessionPlanSerializer(sessionPlan, many=False)
        return serializer
    
    
    
def DeleteSessionPlan(id):
    sessionPlan = SessionPlan.objects.filter(Id=id).first()
    sessionPlan.isDeleted = True
    sessionPlan.save()
    
    result = "Record Deleted Successfully"
    return result