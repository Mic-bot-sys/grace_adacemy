import json
from GraceForteAPI.Models.BookingModel import Booking

def MigrateToDatabase():
    with open('themigdata/bookings.json') as bookingsObj:
        data = json.load(bookingsObj)

    print(data)
    
    for book in data:
        obj = Booking(
            Id = book['pk'],
            bookerFirstName = book['fields']['bookerFirstName'],
            bookerLastName = book['fields']['bookerLastName'],
            phoneNumber = book['fields']['phoneNumber'],
            email = book['fields']['email'],
            accessCode = book['fields']['accessCode'],
            dateCreated = book['fields']['dateCreated'],
            isDeleted = book['fields']['isDeleted'],
        )
        obj.save()
        
        
    return "Successfully Migrated"