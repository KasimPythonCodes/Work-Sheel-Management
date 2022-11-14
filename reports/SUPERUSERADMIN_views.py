from django.shortcuts import render , HttpResponse ,redirect ,HttpResponseRedirect
from reports.models import*
from django.contrib import messages
from reports.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from studentapp.models import Course,Session_Year,CustomUser,Student,Staff
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator


"""
def SUPERADMIN_EDIT(request, id ):
    user = CustomUser.objects.filter(id = id)
    edit = Supervizor.objects.all()
    context={
        'edit':edit,
        'user':user,
    }
    return render(request, 'superuser/superadmin_profile.html',context)
def SUPERADMIN_UPDATE(request):
    if request.method =='POST':
        try:
            cust_id = request.POST['cust_id']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            profile_pic = request.POST['profile_pic']
            print(cust_id  , first_name  , last_name , profile_pic)
            user = CustomUser.objects.get(pk= cust_id)
            user.first_name = first_name
            user.last_name = last_name
            if profile_pic != None and profile_pic !="":
                user.profile_pic = profile_pic
            user.save()
            messages.success(request , "Recoard Successfully Update!!")
            return redirect('/super-admin-update/')
        except:
            pass
            # messages.warning(request , "Recoard Failed!!")
    return render(request, 'superuser/superadmin_profile.html')
"""



 

@login_required(login_url='/dologin/')
def SUPERUSER_DASHBOARD(request):
    supcount = Supervizor.objects.all().count()
    staffcount = Staff_TL.objects.all().count()
    # supcount = Supervizor.objects.all().count()
    # supcount = Supervizor.objects.all().count()
    context = {
        'supcount':supcount,
        'staffcount':staffcount,
    }
    return render(request , 'SUPERUSER/superuser-dashboard.html',context)

@login_required(login_url='/dologin/')
def SUPERVIZOR_DASHBOARD(request):
    user=request.user
    demo = Supervizor.objects.get(admin = user)
    demoid = Staff_TL.objects.all().count()
    
    context ={
        'demoid':demoid
    }
    return render(request , 'SUPERVIZOR/supervizor-dashboard.html')


def hod_profile(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # print(first_name)
        
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, "Your Profile Updated Successfully !!")
            return HttpResponseRedirect(reverse("hodprofile"))
            # redirect('/')
        except :
            messages.error(request, "Failed to Update Your Profile")
    # user=request.user.id
    # print(user)
    # user=CustomUser.objects.all().filter(id=user)
    return render(request, 'SUPERUSER/hod_profile.html')


#my code
"""
import datetime
import csv

def fund_export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    # response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename= User Details'+ str(datetime.datetime.now())+'.csv'
    member_list = CustomUser.objects.all()
    writer = csv.writer(response)
    writer.writerow(['User Id', 'Ref ID', 'User Name', 'Amount'])
    
    for approve in member_list:
        print(approve)
    
        writer.writerow(
                [
                approve.id, 
				approve.user_type, 
				approve.username,
				approve.username, 
				approve.first_name, 
				approve.last_name, 
				approve.email, 
     
				# approve.amount, 
				# approve.Payable_amout, 
				# approve.payment_amount, 
				# approve.remaining_amount, 
				# approve.payment_mode, 
				# approve.remarks,
                # approve.joinig_date, 
                ])
           

    return response

"""

#HOD UPDATE


def HOD_UPDATE(request):
    user=request.user.id
    # print(user)
    if request.method=='POST':
            instructor_id = request.POST.get('instructor_id')
            # print(instructor_id)
            profile_pic=request.FILES.get('profile_pic')
            username=request.POST.get('username')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            # print(profile_pic ,username , first_name ,last_name ,email)
            user = CustomUser.objects.get(id=instructor_id)
            user.username=username ,
            user.first_name=first_name , 
            user.last_name=last_name , 
            user.email=email,
            user.save()
            messages.success(request , "Recoard Successfully Update!!")
            return redirect('/hodprofile/')
    return render(request, 'SUPERUSER/hod_profile.html',{'user':user})
    
    
    

# SUPERVIZOR ( TEAM LEADER ) BY SUPERADMIN


def SUPERVIZOR_REGISTER(request):
    if request.method == 'POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        designation=request.POST.get('designation')
        
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already exist")
            return redirect('supervizor-sign')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"Username is already exist")
            return redirect('supervizor-sign')
        
        
        else:
            user=CustomUser(
                first_name = first_name,
                last_name =last_name,
                email = email,
                username=username,
                profile_pic = profile_pic,
                user_type = 3
                
            )   
            user.set_password(password)
            user.save()
            supervizor=Supervizor(
                    profile_img = profile_pic,
                    admin = user,
                    designation = designation,
            )
            supervizor.save()
            messages.success(request, user.first_name + "  "+ user.last_name + ' Are Successfully Added !!' )
            return redirect('supervizor-sign')
    return render(request , 'SUPERUSER/supervizor-sign.html')

def SUPERVIZOR_VIEWS(request):
    sub=Supervizor.objects.all()
    user=CustomUser.objects.all()
    context = {
        'sub':sub,
        'user':user
    }
    return render(request , 'SUPERUSER/supervizor_views.html' , context)

def SUPERVIZOR_EDIT(request ,id):
    edit = Supervizor.objects.filter(id = id)
    context ={
        'edit':edit,
    }
    return render(request , 'SUPERUSER/edit_supervizor.html' ,context)

def SUPERVIZOR_UPADTE(request):
    if request.method == 'POST':
        user_id=request.POST.get('id') 
        user=CustomUser.objects.get(id=user_id)
        profile_pic=request.FILES.get('profile_pic')
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.username=request.POST['username']
        password=request.POST.get('password')
        if password !=None and password != "":
            user.set_password(password)
            
        # if profile_pic != None and profile_pic !="":
        #     user.profile_img = profile_pic        
        user.save()
        
        update = Supervizor.objects.get(admin = user_id)
        if profile_pic != None and profile_pic !="":
            update.profile_img = profile_pic 
        update.designation = request.POST['designation']
        # if profile_pic != None and profile_pic !="":
        #     update.profile_img = profile_pic
        # update.profile_img = profile_pic
        update.save()
        messages.success(request, "Supervizor Are Successfully Updated")
        print("h\//\/\/\/\/\/\/\/\/\/\/\/\h")
        return redirect('supervizor-views-update')
    edit = Supervizor.objects.all()
    context ={
        'edit':edit,
    }
    return render(request , 'SUPERUSER/edit_supervizor.html' ,context)
    
def SUPERVIZOR_DELETE(request ,id ):
    # if request.method == 'POST':
        user = CustomUser.objects.get(id =id) 
        user.delete()
        messages.success(request , "Record are Successfully Deleted")  
        return redirect('supervizor_add_list_delete') 
    
def  SUPERVIZOR_DLIST(request):
    # user = CustomUser.objects.all()  
    sub=Supervizor.objects.all()
    context = {
        'sub':sub
    }
    return render(request , 'SUPERUSER/supervizor_views.html' , context)
    
 
 
# CREATE TABLE BY SUPERADMIN


def SUPERVIZOR_TABLE_ADD(request):
    user=request.user
    staff=CustomUser.objects.all() 
    siid = Supervizor.objects.all()
    context={
        'staff':staff,
        'siid':siid
    }   
    if request.method =="POST":
        line_no = request.POST.get('line_no')
        manpower = request.POST.get('manpower')
        target = request.POST.get('target')
        all_user_id = request.POST.get('all_user_id')
        
        
        if Staff_TL.objects.filter(Line_No = line_no).exists():
            messages.warning(request, "Line is already Taken Used Another name")
            return redirect('/supervizor-table-add/')
        
        else:
            IDd=Supervizor.objects.get(id=all_user_id) 
            Staff = Staff_TL(
                    Line_No=line_no , 
                    Manpowers=manpower ,
                    Target=target,
                    fk =request.user,
                    user_asign_id = IDd
                    )
            Staff.save()
           
            messages.success(request,"Line Are Successfully Add")
    return render(request, 'SUPERUSER/supervizor-add-table.html',context)
         
# def SUPERVIZOR_TABLE_VIEWS(request):
#     for st in  Staff_TL.objects.all():
#         x=st.user_asign_id.id
#         # print(x ,"HHHHHHHHH")
#     for u in Supervizor.objects.all():
#         y=u.id
#         xx=u.admin.id
#         print(xx , "JJJJJIIII" , request.user.id)
        
#         if y == x:
#             print(u.id, "KKKKK" ,x)
#             staff=Staff_TL.objects.filter(user_asign_id=y)
#             context = {
#                 'staff_T':staff, 
#             }
#             return render(request, 'SUPERUSER/supervizor-read-table.html' ,context )
#         # else:
#         #     if request.user.id == u.admin.id:
#         #         staff=Staff_TL.objects.all()    
#         #         context = {
#         #             'staff_T':staff, 
#         #         }
#         #         return render(request, 'SUPERUSER/supervizor-read-table.html')
#     # staff=Staff_TL.objects.all()    
#     # context = {
#     #     'staff_T':staff, 
#     # }
#     # return render(request, 'SUPERUSER/supervizor-read-table.html' ,context )        
    
    
def SUPERVIZOR_TABLE_VIEWS(request): 
    if request.user.user_type == '1':
        staff=Staff_TL.objects.all() 
    else:  
    # print(Supervizor.objects.get(admin=request.user))
        demo = Supervizor.objects.get(admin=request.user)
        staff=Staff_TL.objects.filter(user_asign_id=demo)
        xc=staff.count()
        print(xc)
    # print("stttttt",staff.Line_No)
    context = {
        'staff_T':staff, 
    }
    return render(request, 'SUPERUSER/supervizor-read-table.html' ,context )        

def SUPERVIZOR_TABLE_EDIT(request,id):
        upd= Staff_TL.objects.filter(id = id)
        context={
            'upd':upd,
        }
        return render(request, 'SUPERUSER/edit-supervizor-update-table.html' ,context)
        
def SUPERVIZOR_TABLE_UPDATE(request , id):
    user=request.user
    if request.method =="POST":
        for st in Staff_TL.objects.all():
            print(st.user_asign_id.id)
            oid=st.user_asign_id.id
        staff = Staff_TL.objects.get(id=id)
        
        # staff.Line_No = request.POST['line_no']
        # staff.Manpowers = request.POST['manpower']
        # staff.Target = request.POST['target']
        
        staff.nine_to_ten_in = request.POST['input1']
        staff.ten_to_eleven_in = request.POST['input2']
        staff.eleven_to_twelve_in = request.POST['input3']
        staff.twelve_to_one_in = request.POST['input4']
        staff.one_to_two_in= request.POST['input5']
        staff.two_to_three_in = request.POST['input6']
        staff.three_to_four_in = request.POST['input7']
        staff.four_to_five_in = request.POST['input8']
        
        staff.nine_to_ten_out = request.POST['output1']
        staff.ten_to_eleven_out = request.POST['output2']
        staff.eleven_to_twelve_out = request.POST['output3']
        staff.twelve_to_one_out = request.POST['output4']
        staff.one_to_two_out= request.POST['output5']
        staff.two_to_three_out = request.POST['output6']
        staff.three_to_four_out = request.POST['output7']
        staff.four_to_five_out = request.POST['output8']
        
        staff.nine_to_ten_dis = request.POST['dispatch1']
        staff.ten_to_eleven_dis = request.POST['dispatch2']
        staff.eleven_to_twelve_dis = request.POST['dispatch3']
        staff.twelve_to_one_dis = request.POST['dispatch4']
        staff.one_to_two_dis= request.POST['dispatch5']
        staff.two_to_three_dis = request.POST['dispatch6']
        staff.three_to_four_dis = request.POST['dispatch7']
        staff.four_to_five_dis = request.POST['dispatch8']
        staff.save()
        messages.success(request, "Line Are Successfully Updated")
        return redirect('supervizor-read')

def SUPERVIZOR_LIST_TABLE(request):
    staff=Staff_TL.objects.all()
    context = {
        'staff_T':staff,
    }
    return render(request, 'SUPERUSER/supervizor-read-table.html' ,context )

def SUPERVIZOR_TABLE_DELETE(request,id):
    # if request.method == 'POST':
        delete_id = Staff_TL.objects.get(pk=id)
        print("KKKKKKKKKKKKKK",delete_id)
        delete_id.delete()
        messages.success(request,"Line are successfully Deleted")
        return redirect('/supervizor-table-list-detail/')

     

     

    
    

     
         
  
         
# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product=Product.objects.get(id=product_id)
#     Cart(user=user , product=product).save()
#     return redirect('/cart/')   



