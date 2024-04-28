import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
@csrf_exempt
def admin_login(request):
    try: 
        if request.method == "POST":
            recieved_json_data = json.loads(request.body)
            username = recieved_json_data.get('username')
            password =recieved_json_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser == True:            
                login(request, user)
                # return redirect("the_admin:dashboard")
                return JsonResponse({"message": "Admin authenticated Successfully", "status": "200"})
        
        elif request.method == "GET":
            return render(request, 'admin/authentication/admin-login.html')
        
    except Exception as ex:
        print(ex)
        
        

@csrf_exempt
def logout(request):
    logout(request)
    return redirect("the_admin:admin_auth")