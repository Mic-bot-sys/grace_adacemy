from GraceForteAPI.Models.HierarchyModel import Hierarchy
from GraceForteAPI.Serializers.HierarchySerializer import HierarchySerializer
from .BaseImportService import *



def GetHierarchies():
    # notification = BookingNotification(receiver, subject, body)
    hierarchies = Hierarchy.objects.filter(isDeleted=False).order_by('title')
    if hierarchies is not None:
        serializer = HierarchySerializer(hierarchies, many=True)
        return serializer
    return None
        
        
        
def GetHierarchyById(id):
    hierarchy = Hierarchy.objects.filter(isDeleted=False, Id=id).first()
    if hierarchy is not None:
        serializer = HierarchySerializer(hierarchy, many=False)
        return serializer
    return None
        
        
        
def CreateHierarchy(body):
    title = body.get('title')
    fullTitle = body.get('fullTitle')
    createdById = body.get('createdBy')
    
    if not Hierarchy.objects.filter(title=title).exists():
        createdBy = User.objects.get(pk = createdById)
        
        with transaction.atomic():
            hierrchy = Hierarchy(
                title = title,
                fullTitle = fullTitle,
                createdBy = createdBy,
            )
            hierrchy.save()
            
            serializer = HierarchySerializer(hierrchy, many=False)
            return serializer
    
    return None



def UpdateHierarchy(id, body):
    title = body.get('title')
    fullTitle = body.get('fullTitle')
    
    hierarchy = Hierarchy.objects.filter(Id=id).first()
    if hierarchy is not None:
        hierarchy.title = title
        hierarchy.fullTitle = fullTitle
        hierarchy.save()

        serializer = HierarchySerializer(hierarchy, many=False)
        return serializer
    
    
    
def DeleteHierarchy(id):
    hierarchy = Hierarchy.objects.filter(Id=id).first()
    hierarchy.isDeleted = True
    hierarchy.save()
    
    result = "Record Deleted Successfully"
    return result