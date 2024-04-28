
# Start Signals
from check_mail import EmailNotify
from grace_forte_app.special_services.servicemail import ConfirmedServiceTemplateEmailNotify, ServiceTemplateEmailNotify



def serviceEmailNotifySignals(sender, instance, created, **kwargs):
    if created:
        print("This Email Signal has been Triggered Successfully!!!")
        result = ServiceTemplateEmailNotify(instance.user.email, "Initiated Service Booking Transaction", "Sure this is Great!!!", instance.user.user_profile.firstName)
    elif instance.isApproved:
        print("Training Payment approved Successfully by the admin")
        result = ConfirmedServiceTemplateEmailNotify(instance.user.email, "Confirmed Service Booking Transaction", "The Service Booking Transaction you made has been confirmed by us. You can therefore proceed to the next line of action", instance.user.user_profile.firstName, instance)
