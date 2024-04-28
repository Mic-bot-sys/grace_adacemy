from GraceForteAPI.Models.ServiceRenderedModel import ServiceRendered
from GraceForteAPI.Serializers.BookingPaymentSerializer import BookingPaymentSerializer
from GraceForteAPI.Serializers.BookingSerializer import BookingSerializer
from .BaseImportService import *
from GraceForteAPI.Models.BookingPaymentModel import BookingPayment
from GraceForteAPI.Models.BookingModel import Booking
from datetime import datetime

# Start the  details for the Notification Module
subject = "BOOKING PAYMENT NOTIFICATION!!!"
body_message = "A payment has been made to the Organization's Bank Account for Booking Purpose. \
    Kindly Login to your Dashboard for confirmation"
# End the  details for the Notification Module



def GetBookings():
    # notification = BookingNotification(receiver, subject, body)
    booking_list = Booking.objects.filter(isDeleted=False).order_by('bookerFirstName')
    if booking_list is not None:
        serializer = BookingSerializer(booking_list, many=True)
        return serializer
    return None
        
        
        
def GetBookingById(id):
    booking = Booking.objects.filter(isDeleted=False, id=id)
    if booking is not None:
        return booking
    return None
        
        
        
def CreateBooking(body):
    bookerFirstName = body.get('bookerFirstName')
    bookerLastName = body.get('bookerLastName')
    phoneNumber = body.get('phoneNumber')
    email = body.get('email')
    serviceRenderedId = body.get('serviceRenderedId')
    paymentProof = body.get('paymentProof')
    sessionAmount = body.get('sessionAmount')
    totalExpectedAmount = body.get('totalExpectedAmount')
    imageBase = body.get('imageBase')
    
    serviceRendered = ServiceRendered.objects.filter(Id=serviceRenderedId).first()
    
    with transaction.atomic():
        booking = Booking(
            bookerFirstName = bookerFirstName,
            bookerLastName = bookerLastName,
            phoneNumber = phoneNumber,
            email = email,
            dateCreated = datetime.now(),
        )
        if serviceRendered is not None:
            booking.serviceRendered = serviceRendered
        booking.save()
        
        bookingPayment = BookingPayment(
            booking = booking,
            paymentProof = paymentProof,
            sessionAmount = sessionAmount,
            totalExpectedAmount = totalExpectedAmount,
            dateCreated = datetime.now(),
            proofBase = imageBase,
        )
        bookingPayment.save()
        
    main_user = User.objects.get(username="tolubaba")
    if main_user is not None:
        notification = BookingNotification(main_user.email, subject, body_message)
    bookingPaymentObj = BookingPayment.objects.filter(isDeleted=False, Id=bookingPayment.Id).first()
    if bookingPaymentObj is not None:
        # serializer = serializers.BookingSerializer(bookingObj, many=False)

        serializer = BookingPaymentSerializer(bookingPaymentObj, many=False)
        return serializer
    return None