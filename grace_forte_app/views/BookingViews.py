from datetime import datetime
from grace_forte_app.models.BookingModel import Booking
from grace_forte_app.services import BookingService
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetBookings(request):
    try:
        bookings = BookingService.GetBookings()
        # result = MigrateToDatabase()
        # return Response(bookings.data) #in order
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": bookings.data})
    
    except Exception as ex: 
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetBookingById(request, id):
    try:
        booking = BookingService.GetBookingById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": booking.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateBooking(request):
    try:
        received_json_data = request.data
        booking = BookingService.CreateBooking(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": booking.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    