from django.contrib import admin
from grace_forte_app.models.AccountInformationModel import AccountInformation

from grace_forte_app.models.BookingModel import Booking
from grace_forte_app.models.CourseModel import Course
from grace_forte_app.models.ProfileModel import Profile
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment

# Register your models here.
admin.site.register(Booking)
admin.site.register(ServiceRendered)
admin.site.register(AccountInformation)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(TrainingPayment)
admin.site.register(ServicePayment)