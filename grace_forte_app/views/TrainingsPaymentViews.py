from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from decimal import Decimal

from grace_forte_app.special_services.CustomBase64Converter import CustomInMemoryBase64Converter
from grace_forte_app.special_services.EmailNotifier import EmailNotification
from django.contrib.auth.decorators import login_required



@csrf_exempt
@login_required
def training_payment(request):
    try:
        if request.user.is_authenticated:
            body = dict(request.POST)
            user = request.user
            course_id = body["courseId"][0]
            initialAmount =  body["amount"][0]
            amount = Decimal(initialAmount)
            paymentProof =  request.FILES["paymentProof"]
            account_id =  body["accountId"][0]
            
            paymentProof = CustomInMemoryBase64Converter(paymentProof)
            
            trainingPayment = TrainingPayment(
                user_id = user.id,
                expectedAmount = amount,
                proofBase = paymentProof,
                account_id= account_id,
                enrolledCourse_id = course_id              
            )
            trainingPayment.save()
            
            # notification = EmailNotification(request.user.email, "Enrollment Notofication", "We text to inform you that you have made a move for enrollment and we will send you a confirmation mail as soon as we confirm your payment. Thank you for choosing us.")
            
            return JsonResponse({"title": "Request Successful", "message": "You will get a confirmation mail as soon as your Payment is confirmed", "status":"success"})
        
    except Exception as ex:
        print(ex)
        return JsonResponse({"title": "Error Occured", "message": "An Error occured during the Enrollment Process", "status": "error"})
