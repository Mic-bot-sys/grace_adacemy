from GraceForteAPI.Models.BookingModel import Booking
from .BaseImportService import *
from GraceForteAPI.Models.BookingPaymentModel import BookingPayment
from GraceForteAPI.Serializers.BookingPaymentSerializer import BookingPaymentSerializer




def GetBookingPayments():
    booking_payments = BookingPayment.objects.filter(isDeleted=False).order_by('paymentStatus')
    if booking_payments is not None:
        serializer = BookingPaymentSerializer(booking_payments, many=True)
        return serializer
    return None



def GetBookingPaymentsByPaymentStatus():
    booking_payments = BookingPayment.objects.filter(isDeleted=False, paymentStatus="Confirmed").order_by('-paymentStatus')
    if booking_payments is not None:
        serializer = BookingPaymentSerializer(booking_payments, many=True)
        return serializer
    return None



def GetPendingBookingPayments():
    booking_payments = BookingPayment.objects.filter(isDeleted=False, paymentStatus="Pending").order_by('-dateCreated')
    if booking_payments is not None:
        serializer = BookingPaymentSerializer(booking_payments, many=True)
        return serializer
    return None



def GetApprovedBookingPayments():
    booking_payments = BookingPayment.objects.filter(isDeleted=False, paymentStatus="Approved").order_by('-approvedDate')
    if booking_payments is not None:
        serializer = BookingPaymentSerializer(booking_payments, many=True)
        return serializer
    return None



def ApproveBookingPayment(body):
    confirmedById = body.get('confirmedBy')
    id = body.get('bookingPaymentId')
    
    
    confirmedBy = User.objects.get(pk=confirmedById)   
    bookingPayment = BookingPayment.objects.filter(Id=id).first()
    booking = Booking.objects.filter(Id=bookingPayment.booking.Id).first()
    
    
    with transaction.atomic():
        if confirmedBy and bookingPayment is not None:
            bookingPayment.approvedBy = confirmedBy
            bookingPayment.paymentStatus = "Approved"
            bookingPayment.approvedDate = datetime.now()
            
            if booking.accessCode == "" or booking.accessCode == None:
                while True:
                    code = random.randint(100000, 999999)
                    if Booking.objects.filter(isDeleted=False, accessCode=code).exists():
                        continue
                    else:
                        break
                    
                booking.accessCode = code
                booking.save()
                
                bookingPayment.save()
                
                subject = "PAYMENT APPROVED!!!"
                body_message = f"Your Payment has been confirmed. Your Access Code to claim your Booked Session is {booking.accessCode}. The Date for your Session will be communicated to you. Thanks"


                notification = BookingNotification(booking.email, subject, body_message)
                
                result = "Confirmation Successful"
                
                return result
        
        return None
  
  
  
def DeleteBookingPayment(id, body):
    deletedBy = body.get('deletedBy')
    
    bookingPayment = BookingPayment.objects.filter(Id=id).first()
    bookingPayment.isDeleted = True
    bookingPayment.dateDeleted = datetime.now()
    
    user = User.objects.get(pk=int(deletedBy))
    bookingPayment.isDeletedBy = user
    bookingPayment.save()
    
    result = "Record Deleted Successfully"
    return result