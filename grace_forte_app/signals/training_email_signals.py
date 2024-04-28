
# Start Signals
from check_mail import EmailNotify
from grace_forte_app.special_services.trainingmail import ConfirmedTrainingTemplateEmailNotify, TrainingTemplateEmailNotify
from grace_forte_app.utils import send_confirmed_training_mail, send_pending_training_mail



def emailNotifySignals(sender, instance, created, **kwargs):
    if created:
        print("This Pending Notification mail Signal has been Triggered Successfully!!!")
        result = send_pending_training_mail(instance.user.email, "Initiated Transaction", "", instance.user.user_profile.firstName)
        print(result)
    elif instance.isApproved:
        print("Training Payment approved Successfully by the admin and mail has been triggered")
        result = send_confirmed_training_mail(instance.user.email, "Confirmed Transaction", "The Transaction you made has been confirmed by us. You can therefore proceed to the next line of action", instance.user.user_profile.firstName, instance)
        print(result)


# THE FORMER CODE
# def emailNotifySignals(sender, instance, created, **kwargs):
#     if created:
#         print("This Email Signal has been Triggered Successfully!!!")
#         result = TrainingTemplateEmailNotify(instance.user.email, "Initiated Transaction", "", instance.user.user_profile.firstName)
#     elif instance.isApproved:
#         print("Training Payment approved Successfully by the admin")
#         result = ConfirmedTrainingTemplateEmailNotify(instance.user.email, "Confirmed Transaction", "The Transaction you made has been confirmed by us. You can therefore proceed to the next line of action", instance.user.user_profile.firstName, instance)
