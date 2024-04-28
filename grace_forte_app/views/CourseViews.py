from grace_forte_app.services import CourseService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetCourses(request):
    try:
        courses = CourseService.GetCourses()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": courses.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetCourseById(request, id):
    try:
        course = CourseService.GetCourseById(id)
        if course == None:
            return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": course})
        elif course.data:
            return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": course.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateCourse(request):
    try:
        received_json_data = request.data
        course = CourseService.CreateCourse(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": course.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['PUT'])
def UpdateCourse(request, id):
    try:
        received_json_data = request.data
        course = CourseService.UpdateCourse(id,received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": course.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['DELETE'])
def DeleteCourse(request, id):
    try:
        course = CourseService.DeleteCourse(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": course})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    