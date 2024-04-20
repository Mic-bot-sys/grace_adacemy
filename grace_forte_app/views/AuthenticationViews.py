from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from grace_forte_app.models.AccountInformationModel import AccountInformation
from grace_forte_app.models.ProfileModel import Profile
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages



# Create your Views here
def auth(request):
    return render (request, "auth/index.html")




def loginUser(request):    
    try:
        if request.method == "POST":
                email = request.POST["lEmail"]
                username = email.split('@')[0]
                password = request.POST["lPassword"]
                # userObj = User.objects.filter(username=username).select_related("user_profile").first()
                # prof = userObj.user_profile
                # profName = userObj.user_profile.firstName
                user = authenticate(username=username, password=password)
                if user.is_superuser:
                    return redirect("authentication:auth")
                login(request, user)
                
                if "debutUserEmail" in request.session:
                    del request.session['debutUserEmail']
                
                account = AccountInformation.objects.filter(isDeleted=False, selected=True).first()
                request.session["fullName"] = request.user.user_profile.get_full_name()
                request.session["accountId"] = str(account.Id)
                request.session["accountName"] = account.accountName
                request.session["accountNo"] = account.accountNo
                request.session["bank"] = account.bank
                
                return redirect("main:home")            
            
        if "debutUserEmail" in request.session:
            debutUserEmail = request.session['debutUserEmail']
            return render(request, "auth/index.html", {"debutUserEmail": debutUserEmail})
        
        return render(request, "auth/index.html")

    except Exception as ex:
                print(ex)




def register(request):
    if request.method == "POST":
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            confirmPassword = request.POST["confirmPassword"]
            firstName = request.POST["firstName"]
            lastName = request.POST["lastName"]
            phone = request.POST["phone"]
            
            username = email.split('@')[0]
            
            if password == confirmPassword:                
                try:
                    with transaction.atomic():
                        user = User.objects.create_user(username,email,password)
                        
                        profile = Profile(
                            user_id = user.id,
                            firstName=firstName,
                            lastName=lastName,
                            phone = phone
                        )
                        profile.save()
                        request.session['debutUserEmail'] = email
                    return redirect("authentication:login")        
                except IntegrityError as e:
                    print("Integrity Error: ",e)
                    messages.add_message(request, messages.ERROR, 'Email Exists. Try again!!!')
                    return redirect("authentication:login")   

              
        except Exception as ex:
            print(ex)
    



@login_required
def logoutUser(request):
        logout(request)
        return redirect("authentication:auth")