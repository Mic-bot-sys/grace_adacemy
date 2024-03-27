from GraceForteAPI.Models.CourseModel import Course
from .BaseImportService import *
from datetime import datetime
from GraceForteAPI.Serializers.CourseSerializer import CourseSerializer

# from django.core.serializers import serialize
# import json



def GetCourses():
    course_list = Course.objects.filter(isDeleted=False).order_by('title')
    if course_list is not None:
        # serialized_data = serialize("json", course_list)
        # serialized_data = json.loads(serialized_data)
        serializer = CourseSerializer(course_list, many=True)
        return serializer
    return None
        
        
        
def GetCourseById(id):
    course = Course.objects.filter(isDeleted=False, Id=id).first()
    if course is not None:
        serializer = CourseSerializer(course, many=False)
        return serializer
    return None
        
        
        
def CreateCourse(body):
    title = body.get('title')
    code = body.get('code')
    summary = body.get('summary')
    price = body.get('price')
    description = body.get('description')
    accessLink = body.get('accessLink')
    image = body.get('image')
    baseImage = body.get('baseImage')
    createdById = body.get('createdById')
    
    createdBy = User.objects.filter(id=int(createdById)).first()
    
    
    with transaction.atomic():
        course = Course(
            title = title,
            code = code,
            summary = summary,
            price = price,
            description = description,
            accessLink = accessLink,
            baseImage = baseImage,
            image = image,
            createdBy = createdBy,
            dateCreated = datetime.now(),
        )
        course.save()
        
    courseObj = Course.objects.filter(isDeleted=False, Id=course.Id).first()
    if courseObj is not None:
        serializer = CourseSerializer(courseObj, many=False)
        return serializer
    return None



def UpdateCourse(id, body):
    title = body.get('title')
    code = body.get('code')
    summary = body.get('summary')
    price = body.get('price')
    description = body.get('description')
    accessLink = body.get('accessLink')
    baseImage = body.get('baseImage')
    
    
    course = Course.objects.filter(Id=id).first()
    
    with transaction.atomic():
        if course is not None:
            course.title = title
            course.code = code
            course.summary = summary
            course.price = price
            course.description = description
            course.accessLink = accessLink
            course.baseImage = baseImage
            course.updatedDate = datetime.now()
            course.save()

    serializer = CourseSerializer(course, many=False)
    return serializer

    
    
def DeleteCourse(id):
    course = Course.objects.filter(Id=id).first()
    with transaction.atomic():
        course.isDeleted = True
        course.save()
    
    result = "Record Deleted Successfully"
    return result