from GraceForteAPI.Models.ServiceRenderedModel import ServiceRendered
from GraceForteAPI.Serializers.ServiceRenderedSerializer import ServiceRenderedSerializer
from .BaseImportService import *



def GetServicesRendered():
    servicesRendered = ServiceRendered.objects.filter(isDeleted=False, isAvailable = True).order_by('title')
    if servicesRendered is not None:
        serializer = ServiceRenderedSerializer(servicesRendered, many=True)
        return serializer
    return None



def GetRemovedServicesRendered():
    servicesRendered = ServiceRendered.objects.filter(isDeleted=False, isAvailable = False).order_by('title')
    if servicesRendered is not None:
        serializer = ServiceRenderedSerializer(servicesRendered, many=True)
        return serializer
    return None
        
        
        
def GetServiceRenderedById(id):
    serviceRendered = ServiceRendered.objects.filter(isDeleted=False, Id=id).first()
    if serviceRendered is not None:
        serializer = ServiceRenderedSerializer(serviceRendered, many=False)
        return serializer
    return None
        
        
        
def CreateServiceRendered(body):
    title = body.get('title')
    summary = body.get('summary')
    description = body.get('description')
    price = body.get('price')
    priceType = body.get('priceType')
    image = body.get('image')
    createdById = body.get('createdBy')
    
    createdBy = User.objects.get(pk = createdById)
    
    isExist = ServiceRendered.objects.filter(title=title).first()
    if not isExist:
        with transaction.atomic():
            serviceRendered = ServiceRendered(
                title = title,
                summary = summary,
                description = description,
                price = Decimal(price),
                priceType = priceType,
                image = image,
                createdBy = createdBy
            )
            serviceRendered.save()
            
            serializer = ServiceRenderedSerializer(serviceRendered, many=False)
            return serializer
        return None
    return "Record Exists"


def UpdateServiceRendered(id, body):
    title = body.get('title')
    summary = body.get('summary')
    description = body.get('description')
    price = Decimal(body.get('price'))
    priceType = body.get('priceType')
    image = body.get('image')
    updatedById = body.get('updatedBy')
    updatedDate =datetime.now()
    
    updatedBy = User.objects.get(pk = updatedById)
    
    serviceRendered = ServiceRendered.objects.filter(Id=id).first()
    if serviceRendered is not None:
        serviceRendered.title = title
        serviceRendered.summary = summary
        serviceRendered.description = description
        serviceRendered.price = price
        serviceRendered.priceType = priceType
        serviceRendered.image = image
        serviceRendered.updatedBy = updatedBy
        serviceRendered.dateUpdated = updatedDate
        serviceRendered.save()

        checkServiceRendered = ServiceRendered.objects.filter(Id=id, isDeleted = False, isAvailable=True).first()
        serializer = ServiceRenderedSerializer(checkServiceRendered, many=False)
        return serializer
    
    

def RemoveServiceRendered(id):
    serviceRendered = ServiceRendered.objects.filter(Id=id).first()
    serviceRendered.isAvailable = False
    serviceRendered.save()
    
    result = "Record Removed Successfully"
    return result    



def DeleteServiceRendered(id, body):
    deletedBy = body.get('deletedBy')
    
    serviceRendered = ServiceRendered.objects.filter(Id=id).first()
    serviceRendered.isDeleted = True
    serviceRendered.dateDeleted = datetime.now()
    
    user = User.objects.get(pk=int(deletedBy))
    serviceRendered.isDeletedBy = user
    serviceRendered.save()
    
    result = "Record Deleted Successfully"
    return result