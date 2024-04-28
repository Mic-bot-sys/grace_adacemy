from GraceForteAPI.Serializers.UserSerializer import UserSerializer
from .BaseImportService import *



def GetUsers():
    # notification = BookingNotification(receiver, subject, body)
    users = User.objects.all().order_by('first_name')
    if users is not None:
        serializer = UserSerializer(users, many=True)
        return serializer
    return None
        
        
        
def GetUserById(id):
    user = User.objects.filter(id=id).first()
    if user is not None:
        serializer = UserSerializer(user, many=False)
        return serializer
    return None