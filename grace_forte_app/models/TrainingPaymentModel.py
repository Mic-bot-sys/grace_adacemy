from grace_forte_app.models.AccountInformationModel import AccountInformation
from grace_forte_app.models.CourseModel import Course
from grace_forte_app.signals.training_email_signals import emailNotifySignals
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import  *
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class TrainingPayment(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paymentStatus = models.CharField(max_length=50, default="Pending")
    proofBase = models.TextField()
    expectedAmount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    isApproved = models.BooleanField(default=False)
    isExpired = models.BooleanField(default=False)
    receiptId = models.CharField(max_length=100)
    approvedDate = models.DateTimeField(auto_now_add=False, blank=True, null=True )
    
    # Foreign Fields
    account = models.ForeignKey(AccountInformation, on_delete=models.CASCADE, related_name="account_information")
    enrolledCourse = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_training_payment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_training_payment')
    approvedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='approvedBy_trainingPayment')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    
   
    class Meta:
        verbose_name_plural = 'TrainingPayments'
    
    def __str__(self):
        return f'{self.paymentStatus} - {self.user.username}'
    
    def getDateApprovedOnly(self):
        return self.approvedDate.strftime('%B %d %Y')
    

# Connecting to the Signals
post_save.connect(emailNotifySignals, sender=TrainingPayment)

    