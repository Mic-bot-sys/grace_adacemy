from GraceForteAPI.Models.CourseModel import Course
from GraceForteAPI.Models.TrainingModel import Training
from GraceForteAPI.Serializers.TrainingSerializer import TrainingSerializer
from GraceForteAPI.Serializers.TrainingPaymentSerializer import TrainingPaymentSerializer
from GraceForteAPI.Models.TrainingPaymentModel import TrainingPayment
from .BaseImportService import *
from datetime import datetime

# Start the  details for the Notification Module
subject = "TRAINING PAYMENT NOTIFICATION!!!"
body_message = "A payment has been made to the Organization's Bank Account for Traning Purpose. \
    Kindly Login to your Dashboard for confirmation"
# End the  details for the Notification Module




def GetTrainings():
    training_list = Training.objects.filter(isDeleted=False).order_by('-dateCreated')
    if training_list is not None:
        serializer = TrainingSerializer(training_list, many=True)
        return serializer
    return None
        
        
        
def GetTrainingById(id):
    training = Training.objects.filter(isDeleted=False, id=id)
    if training is not None:
        serializer = TrainingSerializer(training, many=False)
        return serializer
    return None
        
        
        
def CreateTraining(body):
    enrolledById = body.get('enrolledById')
    courseEnrolledId = body.get('courseEnrolledId')
    paymentProof = body.get('paymentProof')
    proofBase = body.get('proofBase')
    expectedAmount = body.get('expectedAmount')
    
    enrolledBy = User.objects.filter(Id=enrolledById).first()
    courseEnrolled = Course.objects.filter(Id=courseEnrolledId).first()
    
    
    with transaction.atomic():
        training = Training(
            enrolledBy = enrolledBy,
            courseEnrolled = courseEnrolled,
        )
        
        trainingPayment = TrainingPayment(
            training = training,
            paymentProof = paymentProof,
            expectedAmount = expectedAmount,
            dateCreated = datetime.now(),
            proofBase = proofBase,
        )
        trainingPayment.save()
        
    main_user = User.objects.get(username="tolubaba")
    if main_user is not None:
        notification = BookingNotification(main_user.email, subject, body_message)
   
    trainingPaymentObj = TrainingPayment.objects.filter(isDeleted=False, Id=trainingPayment.Id, isExpired=False).first()
    if trainingPaymentObj is not None:
        serializer = TrainingPaymentSerializer(trainingPaymentObj, many=False)
        return serializer
    return None