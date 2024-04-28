from datetime import datetime, timezone
from decimal import Decimal
import json
import random
from django.http import JsonResponse
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from grace_forte_app.models.CourseModel import Course
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.utils import timezone

from grace_forte_app.special_services.CustomBase64Converter import CustomInMemoryBase64Converter
login_url = settings.ADMIN_LOGIN_URL


        
# Create the Views here
@login_required(login_url=login_url)
def create_training(request):
    try:
        if request.method == "GET":            
            return render(request, "admin/training/create-training.html")
        body = request.POST
        name = body["name"]
        summary = body["summary"]
        price = body["price"]
        accessLink = body["accessLink"]
        description = body["description"]
        image = request.FILES["image"]
        
        imageBase = CustomInMemoryBase64Converter(image)
        
        course = Course(
            title=name,
            summary=summary,
            description=description,
            accessLink=accessLink,
            price=price,
            imageBase=imageBase,
            createdBy_id=request.user.id
        )
        course.save()
        return JsonResponse({"message": "Training created Successfully", "status": "200"})
    except Exception as ex:
        print(ex)
        


@login_required(login_url=login_url)
def trainings(request):
    try:
        if request.method == "GET":            
            trainings = Course.objects.filter(isDeleted=False).order_by('-dateCreated')
            return render(request, "admin/training/trainings.html", {"trainings": trainings})
    except Exception as ex:
        print(ex)



@login_required(login_url=login_url)
def getTrainingDetails(request, id):
    try:
        if request.method == "GET":            
            training = Course.objects.get(pk=id)
            return render(request, "admin/training/_training-details.html", {"training": training})
    except Exception as ex:
        print(ex)
        
        
    
@login_required
def updateTraining(request):
    try:
        body = request.POST
        Id = body["Id"]
        name = body["name"]
        summary = body["summary"]
        price = body["price"]
        accessLink = body["accessLink"]
        description = body["description"]
        image = body["image"]
           
        course = Course.objects.get(pk=Id)
        course.title=name
        course.summary=summary
        course.description=description
        course.accessLink=accessLink
        course.price=Decimal(price)
        course.imageBase=image
        course.updatedDate=timezone.now()
        course.save()
        
        return JsonResponse({"message": "Training updated Successfully", "status": "200"})
    except Exception as ex:
        print(ex)