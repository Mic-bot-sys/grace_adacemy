from grace_forte_app.services import ServiceRenderedService
from grace_forte_app.special_services.CustomBase64Converter import CustomBase64Converter
from .BaseImportViews import *




# Create your views here.
@api_view(['GET'])
def GetServicesRendered(request):
    try:
        servicesRendered = ServiceRenderedService.GetServicesRendered()
        data_set = servicesRendered.data
        
        for service in data_set:
            image_path = service['image']
            image_path = image_path.replace('/', "", 1)
            image_data = CustomBase64Converter(image_path)
                
            service['actual_image_file'] = image_data
        
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": data_set})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetServiceRenderedById(request, id):
    try:
        serviceRendered = ServiceRenderedService.GetServiceRenderedById(id)
        image_path = serviceRendered.data['image']
        
        image_path = image_path.replace('/', "", 1)
        image_data = CustomBase64Converter(image_path)
            
        recent_data = serviceRendered.data
        recent_data['actual_image_file'] = image_data
        
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": recent_data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateServiceRendered(request):
    try:
        received_json_data = request.data
        serviceRendered = ServiceRenderedService.CreateServiceRendered(received_json_data)
        if serviceRendered == "Record Exists":
            return Response({"Message": "Repeated Request", "Status": status.HTTP_406_NOT_ACCEPTABLE, "Payload": serviceRendered})
        else: 
            return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": serviceRendered.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['PUT'])
def UpdateServiceRendered(request, id):
    try:
        received_json_data = request.data
        serviceRendered = ServiceRenderedService.UpdateServiceRendered(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": serviceRendered.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['DELETE'])
def DeleteServiceRendered(request, id):
    try:
        received_json_data = request.data
        serviceRendered = ServiceRenderedService.DeleteServiceRendered(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": serviceRendered})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    