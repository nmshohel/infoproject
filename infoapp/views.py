from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import models
from .models import *
from .forms import *
# Create your views here.



def user_login(request):

    if request.method=='POST':
        username=request.POST['uname1']
        password=request.POST['pwd1']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('/home-page')

    return render(request,'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('/')

def home_page(request):
    print('hello')
    pbs=PbsInfo.objects.all()
    print('hello1')
    context={'pbs_info':pbs}
    return render(request,'home_page.html',context)

def loged_user(request):
    user=request.user
    context={'user':user}
    return render(request, 'base.html',context)

def pbs_info(request):
    return render(request, 'home_page.html',context)


def pbs_info_berc_form(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        print(current_user)
        print(user_id)
        # user_basic_info=User.objects.get(pk=user_id)
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        print(user_pbs_info.pbs_code)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        # month=request.POST.get('month')
        # year=request.POST.get('year')
        comp_nos=request.POST.get('complain_nos')
        comp_solve=request.POST.get('complain_solve')
        com_unsolve_case=request.POST.get('complain_unsolve_case')
        com_remarks=request.POST.get('complain_remark')
        # pbs_cod=user_pbs_info.pbs_code
        # print(pbs_code)
        PbsInfoBERC.objects.create(pbs_code=user_pbs_info.pbs_code,complain_nos = comp_nos, complain_solve = comp_solve,complain_unsolve_case=com_unsolve_case,complain_remark=com_remarks,month=month,year=year)
        berc_form= PbsInfoBERCForm()
        message = "Successfully Added!"
        context = {'berc_form':berc_form, 'message':message}
        return render(request, 'berc_form.html', context)
    else:
        berc_form=PbsInfoBERCForm()
        context={'berc_form':berc_form}
        return render(request,'berc_form.html',context)


def my_berc_info(request):

    current_user=request.user
    user_id=current_user.id
    # print(current_user)
    # print(user_id)
    print()



    # user_basic_info=User.objects.get(pk=user_id)
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    
    pbs_code=user_pbs_info.pbs_code
    my_data=PbsInfoBERC.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_brec_info.html',context)

def user_register(request):
    if request.method=='POST':
        u_first_name=request.POST.get('first_name')
        u_last_name=request.POST.get('last_name')
        user_name=request.POST.get('username')
        user_pass=request.POST.get('password')
        u_email=request.POST.get('email')

        management_id=request.POST['management']

        management=ManagementInfo.objects.get(id=management_id)
        # m_id=request.POST.get('management_id')

        u_pbs_name=request.POST.get('pbs_name')
        u_pbs_name_benglai=request.POST.get('pbs_name_benglai')
        u_pbs_code=request.POST.get('pbs_code')
        u_address=request.POST.get('address')
        u_mob_no=request.POST.get('mobile_no')
        user=User.objects.create_user(first_name=u_first_name, last_name=u_last_name, username=user_name, password=user_pass, email=u_email)
        pbsinfo_user=PbsInfo.objects.create(user=user,management = management, pbs_name = u_pbs_name,pbs_name_benglai=u_pbs_name_benglai,pbs_code=u_pbs_code,address=u_address,mobile_no=u_mob_no)
        register_form=UserForm()
        pbs_info_register_form= PBSInfoForm()
        message="User Successfully Added"
        context={'register_form':register_form,'pbs_info_register_form':pbs_info_register_form,'message':message}
        return render(request,'user_register.html',context)
        
    else:
        register_form=UserForm()
        pbs_info_register_form= PBSInfoForm()
        context={'register_form':register_form,'pbs_info_register_form':pbs_info_register_form}
        return render(request,'user_register.html',context)


def change_password(request):
    if request.method=='POST':
        old_pass=request.POST['oop']
        new_pass=request.POST['np']
        re_type_pass=request.POST['rp']
        user = authenticate(username = request.user.username, password = old_pass)
        if user:
            if new_pass==re_type_pass:
                user = request.user
                print(user)
                user.set_password(new_pass)
                user.save()
                msg1="Password Successfully Changed"
                context={'msg1':msg1}
                return render(request, 'user_login.html',context)
            else:
                msg="New Password and Re-type password not Match"
                context={'msg':msg}
                return render(request, 'change_password.html',context)
        else:
            msg2="Old Password Invalid"
            context={'msg2':msg2}
            return render(request, 'change_password.html',context)
    return render(request, 'change_password.html')