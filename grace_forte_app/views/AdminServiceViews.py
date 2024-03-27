from django.utils import timezone
from decimal import Decimal
import json
import random
from django.http import JsonResponse
from django.shortcuts import render
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required 
from django.conf import settings
login_url = settings.ADMIN_LOGIN_URL


        
# Create the Views here
@login_required(login_url=login_url)
def create_service(request):
    try:
        if request.method == "GET":
            return render(request, "admin/service/create-service.html")
        
        body = json.loads(request.body)
    except Exception as ex:
        print(ex)
        
        
        
@login_required(login_url=login_url)
def services(request):
    try:
        if request.method == "GET":            
            services = ServiceRendered.objects.filter(isDeleted=False)
            return render(request, "admin/service/services.html", {"services": services})
    except Exception as ex:
        print(ex)
        
        
    
@login_required(login_url=login_url)
def getServiceDetails(request, id):
    try:
        if request.method == "GET":            
            service = ServiceRendered.objects.get(pk=id)
            return render(request, "admin/service/_service-details.html", {"service": service})
    except Exception as ex:
        print(ex)
        
        

@login_required
def updateService(request):
    try:
        body = request.POST
        Id = body["Id"]
        name = body["name"]
        summary = body["summary"]
        price = body["price"]
        description = body["description"]
        image = body["image"]
           
        service = ServiceRendered.objects.get(pk=Id)
        service.title=name
        service.summary=summary
        service.description=description
        service.price=Decimal(price)
        service.imageBase=image
        service.dateUpdated= timezone.now()
        service.save()
        
        return JsonResponse({"message": "Service updated Successfully", "status": "200"})
    except Exception as ex:
        print(ex)