import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required




# Create your Views
def services(request):
    services = ServiceRendered.objects.filter(isDeleted=False)
    return render(request, "pages/services.html", {"services": services})



@csrf_exempt
def service_details(request, id):
    try:            
        service = ServiceRendered.objects.get(pk=id)
        return render(request, "pages/services-details.html", {"service": service})
    
    except Exception as ex:
        print(ex)



@csrf_exempt
def service_note(request, id, duration, totalAmount):
        if request.method == "POST":            
            request.session["duration"] = duration
            request.session["totalAmount"] = totalAmount      
            return JsonResponse({"message": "service choice noted", "status": "200"})



def service_booking(request, id):
    try:
        if request.user.is_authenticated:
            service = ServiceRendered.objects.get(pk=id)
            return render(request, "pages/services-booking.html", {"service": service})
        return redirect("authentication:auth")
    
    except Exception as ex:
        print(ex)
        
        
        
        
@login_required
def approved_service_receipt(request, id):
    if request.user.is_authenticated:
        receipt = ServicePayment.objects.filter(Id=id, isDeleted=False, isApproved=True, isExpired=False).first()
        dateApproved = receipt.getDateApprovedOnly()
        return render(request, "receipts/approved-service-transaction-receipt.html", {"receipt": receipt, "dateApproved": dateApproved})
