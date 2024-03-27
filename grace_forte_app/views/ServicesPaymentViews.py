from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from decimal import Decimal

from grace_forte_app.special_services.CustomBase64Converter import CustomInMemoryBase64Converter
from grace_forte_app.special_services.EmailNotifier import EmailNotification
from django.contrib.auth.decorators import login_required



@csrf_exempt
@login_required
def service_payment(request):
    try:
        body = dict(request.POST)
        initialAmount =  body["amountId"][0]
        
        amount = Decimal(initialAmount)
        account_id =  body["accountId"][0]
        service_id = body["serviceId"][0]
        duration =  body["durationId"][0]
        paymentProof =  request.FILES["paymentProofId"]
        preferredDate =  body["preferedDateId"][0]
        user = request.user
        
        paymentProof = CustomInMemoryBase64Converter(paymentProof)
        
        servicePayment = ServicePayment(
            expectedAmount = amount,
            account_id= account_id,
            service_id=service_id,
            bookedDuration=duration,
            user_id = user.id,
            proofBase = paymentProof,
            preferedBookingDate=preferredDate,
        )
        servicePayment.save()
        
       
        return JsonResponse({"title": "Service Booking Successful", "message": "You will be notified via your email as soon as your Payment is confirmed", "status":"success"})
    
    except Exception as ex:
        print(ex)
        return JsonResponse({"title": "Error Occured", "message": "An Error occured during the Booking Process", "status": "error"})
