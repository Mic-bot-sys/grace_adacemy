
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from itertools import chain
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment


#Create your Views here
@login_required
def dashboard(request):
    pending_trainings = TrainingPayment.objects.filter(isDeleted=False, isApproved=False, isExpired=False).order_by("-dateCreated")[:3]
    pending_services = ServicePayment.objects.filter(isDeleted=False, isApproved=False, isExpired=False).order_by("dateCreated")[:3]
    result_list = list(chain(pending_trainings, pending_services))
    color_list = ["success", "primary", "danger", "info", "warning", "muted"]
    content = {
        "pending_trainings": result_list,
        "pending_services": pending_services,
        "color_list": color_list
    }
    
    return render(request, 'admin/dashboard/dashboard.html', content)