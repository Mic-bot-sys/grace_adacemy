from grace_forte_app.services import BookingPaymentService
from .BaseImportViews import *



@api_view(['GET'])
def GetBookingPayments(request):
    try:
        bookingPayments = BookingPaymentService.GetBookingPayments()
        # result = MigrateToDatabase()
        # return Response(bookings.data) #in order
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": bookingPayments.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetByPaymentStatus(request):
    try:
        bookingPayments = BookingPaymentService.GetBookingPaymentsByPaymentStatus()
        # result = MigrateToDatabase()
        # return Response(bookings.data) #in order
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": bookingPayments.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetPendingBookingPayments(request):
    try:
        bookingPayments = BookingPaymentService.GetPendingBookingPayments()
        # result = MigrateToDatabase()
        # return Response(bookings.data) #in order
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": bookingPayments.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetApprovedBookingPayments(request):
    try:
        bookingPayments = BookingPaymentService.GetApprovedBookingPayments()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": bookingPayments.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['POST'])
def ApproveBookingPayment(request):
    try:
        received_json_data = request.data
        confirmation = BookingPaymentService.ApproveBookingPayment(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": confirmation})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
