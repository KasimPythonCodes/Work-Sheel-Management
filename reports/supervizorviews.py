from django.shortcuts import render , HttpResponse ,redirect ,HttpResponseRedirect
from reports.models import*
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from studentapp.models import Course,Session_Year,CustomUser,Student,Staff
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def Manager_Add(request):
    if request.method == 'POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        position=request.POST.get('position')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already exist")
            return redirect('/manager-views/')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"Username is already exist")
            return redirect('/manager-views/')
        
        
        else:
            user=CustomUser(
                first_name = first_name,
                last_name =last_name,
                email = email,
                username=username,
                profile_pic = profile_pic,
                user_type = 2
                
            )   
            user.set_password(password)
            user.save()
            manageruser=AdminManager(
                    profile_m_img = profile_pic,
                    manager = user,
                    position = position,
            )
            manageruser.save()
            messages.success(request, user.first_name + "  "+ user.last_name + ' Are Successfully Added !!' )
            return redirect('/manager-views/')
    return render(request , 'manager/manager.html')



