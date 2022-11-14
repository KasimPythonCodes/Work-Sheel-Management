from django.shortcuts import render , HttpResponse
from reports.models import*
from django.http import HttpResponse
from django.shortcuts import redirect,render
# from studentapp.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import time
# Create your views here.

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


 


class EmailBackend(ModelBackend):
    def authenticate(self, username = None, password = None, **kwargs):
        CustomUser = get_user_model()
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

def user_login(request):
    return render(request, 'login.html')  

def Login_All_User(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username = request.POST.get('email'),password=request.POST.get('password'),)
        if user!=None:
            login(request,user)                                        
            user_type = user.user_type
            if user_type == '1':
                # return HttpResponse("Super Admin Dashboard")
                return redirect('SUPERUSER_DASHBOARD')
            
            elif user_type == '2':
                # return redirect("SUPERVIZOR_DASHBOARD")
                return HttpResponse("Manger  Dashboard")
            
            elif user_type =='3':
                # return HttpResponse("Supervizer  Dashboard")
                return redirect('SUPERVIZOR_DASHBOARD')
                
            else:
                messages.error(request, "Email or Password are Invalid!!")
                return redirect('user_login')
        else:
            messages.error(request, "Email or Password are Invalid!!")
            print("KKKKKKKK")
            return redirect('user_login')
    else:
        return redirect('user_login')
        
        
def logout_user(request):
    logout(request)
    return redirect('/login/')