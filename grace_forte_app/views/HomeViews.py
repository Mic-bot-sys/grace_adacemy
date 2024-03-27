from django.shortcuts import render
from check_mail import EmailNotify
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required

from imgtempmail import ImgTemplateEmailNotify



# Create your views here
def home(request):    
    return render(request, "pages/index.html")



def about(request):
    return render(request, "pages/about.html")



@login_required
def pending_trainings_transaction(request):
    try:   
        transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=False, user_id=request.user.id, isExpired=False).order_by("-dateCreated")[:10]
        return render(request, "pages/pending-trainings-transaction.html", {"pending_transactions": transactions, "length": len(transactions)})
    except Exception as ex:
        print(ex)



@login_required
def approved_trainings_transaction(request):
    try:
        transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=True, user_id=request.user.id, isExpired=False).order_by("-approvedDate")[:10]
        return render(request, "pages/approved-trainings-transaction.html", {"approved_transactions": transactions, "length": len(transactions)})
    except Exception as ex:
        print(ex)



@login_required
def approved_bookings_transaction(request):
    try:
        transactions = ServicePayment.objects.filter(isDeleted=False, isApproved=True, user_id=request.user.id, isExpired=False).order_by("-approvedDate")[:10]
        return render(request, "pages/approved-bookings-transaction.html", {"approved_transactions": transactions, "length": len(transactions)})
    except Exception as ex:
        print(ex)
        


def pending_bookings_transaction(request):
    try:   
        transactions = ServicePayment.objects.filter(isDeleted=False, isApproved=False, user_id=request.user.id, isExpired=False).order_by("-dateCreated")[:10]
        return render(request, "pages/pending-bookings-transaction.html", {"pending_transactions": transactions, "length": len(transactions)})
    except Exception as ex:
        print(ex)
    



def contact(request):
    return render(request, "pages/contact.html")
