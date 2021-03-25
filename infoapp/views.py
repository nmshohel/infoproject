from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import models
from infoapp.models import *
from infoapp.forms import *
# from django import bangla
from django.core.mail import send_mail
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

def forgot_password(request):
    # if request.method=='POST':
    #     u_email=request.POST.get('uname1')
    send_mail('dffdgvfg','fgghgfhg','nur.mohammad525452@gmail.com',['sunampbs@gmail.com'])
        # user=User.objects.get
        # print(u_email)
        # msg="Please Check your email"
        # context={'msg':msg}
    return HttpResponse("OK")
    # return render(request, 'forgot_password.html')

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
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        # print(user_pbs_info.management_code)
        # print(user_pbs_info.management__management_code)
        # print(user_id)
        # u_management_code=PbsInfo.objects.get(management__management_code=user_id)



        # user_management_info=ManagementInfo.objects.get(management_code=1)
        # print(user_management_info.name)
        


        # management_info=PbsInfo.objects.filter(management__management_code='1')
      
        # print(management_info.management.name)
        # print(management_info__management_code)

        # print(management_info.management)
        # user_management_info=ManagementInfo.objects.get()

        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        # b_month=bangla.convert_english_digit_to_bangla_digit(month)
        # b_year=bangla.convert_english_digit_to_bangla_digit(year)
        comp_nos=request.POST.get('complain_nos')
        comp_solve=request.POST.get('complain_solve')
        # b_comp_nos=bangla.convert_english_digit_to_bangla_digit(comp_nos)
        # b_comp_solve=bangla.convert_english_digit_to_bangla_digit(comp_solve)

        com_unsolve_case=request.POST.get('complain_unsolve_case')
        com_remarks=request.POST.get('complain_remark')

        PbsInfoBERC.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,complain_nos = comp_nos, complain_solve = comp_solve,complain_unsolve_case=com_unsolve_case,complain_remark=com_remarks,month=month,year=year)
        berc_form= PbsInfoBERCForm()
        message = "Information Successfully Added!"
        context = {'berc_form':berc_form, 'message':message}
        return render(request, 'berc_form.html', context)
    else:
        berc_form=PbsInfoBERCForm()
        context={'berc_form':berc_form}
        return render(request,'berc_form.html',context)
def new_online_connection(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        u_total_app=request.POST.get('total_app')
        u_total_solve_app=request.POST.get('total_solve_app')
        u_cause_of_unsolve=request.POST.get('cause_of_unsolve')
        u_remark=request.POST.get('remark')
        NewOnlineConnection.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,total_app = u_total_app, total_solve_app = u_total_solve_app,cause_of_unsolve=u_cause_of_unsolve,remark=u_remark,month=month,year=year)
        new_con_form= NewOnlineConnectionForm()
        message = "Information Successfully Added!"
        context = {'new_con_form':new_con_form, 'message':message}
        return render(request, 'new_online_connection.html', context)
    else:
        new_con_form=NewOnlineConnectionForm()
        context={'new_con_form':new_con_form}
        return render(request,'new_online_connection.html',context)

def industry_comercial_consumer_dc_rc(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        u_total_dc_app=request.POST.get('total_dc_app')
        u_total_app_get_for_rc=request.POST.get('total_app_get_for_rc')
        u_complete_rc_app=request.POST.get('complete_rc_app')
        u_illegal_app_for_dc=request.POST.get('illegal_app_for_dc')
        IndustryCommercialDcRc.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,total_dc_app = u_total_dc_app, complete_rc_app = u_complete_rc_app,illegal_app_for_dc=u_illegal_app_for_dc,total_app_get_for_rc=u_total_app_get_for_rc,month=month,year=year)
        new_form= IndustryCommercialDcRcForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'industry_commercial_consumer.html', context)
    else:
        new_form=IndustryCommercialDcRcForm()
        context={'new_form':new_form}
        return render(request,'industry_commercial_consumer.html',context)


def dc_consumer(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        domestic=request.POST.get('domestic')
        industry=request.POST.get('industry')
        commercial=request.POST.get('commercial')
        irrigation=request.POST.get('irrigation')
        govt_institute=request.POST.get('govt_institute')
        other=request.POST.get('other')
        total_amount=request.POST.get('total_amount')
        taken_action=request.POST.get('taken_action')
        DcConsumerInfo.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,domestic = domestic, industry = industry,commercial=commercial,irrigation=irrigation,month=month,year=year,govt_institute=govt_institute,other=other,total_amount=total_amount,taken_action=taken_action)
        new_form= DcConsumerInfoForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'dc_consumer.html', context)
    else:
        new_form=DcConsumerInfoForm()
        context={'new_form':new_form}
        return render(request,'dc_consumer.html',context)

def connected_consumer(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        domestic=request.POST.get('domestic')
        industry=request.POST.get('industry')
        commercial=request.POST.get('commercial')
        irrigation=request.POST.get('irrigation')
        govt_institute=request.POST.get('govt_institute')
        other=request.POST.get('other')
        total_amount=request.POST.get('total_amount')
        taken_action=request.POST.get('taken_action')
        ConnectedConsumerInfo.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,domestic = domestic, industry = industry,commercial=commercial,irrigation=irrigation,month=month,year=year,govt_institute=govt_institute,other=other,total_amount=total_amount,taken_action=taken_action)
        new_form= ConnectedConsumerInfoForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'connected_consumer.html', context)
    else:
        new_form=ConnectedConsumerInfoForm()
        context={'new_form':new_form}
        return render(request,'connected_consumer.html',context)


def domestic_connection_seven_day(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        total_app=request.POST.get('total_app')
        con_within_seven_day_app=request.POST.get('con_within_seven_day_app')
        con_without_seven_day_app=request.POST.get('con_without_seven_day_app')
        process_seven_day_app=request.POST.get('process_seven_day_app')
        reason_not_con_of_seven_day=request.POST.get('reason_not_con_of_seven_day')
        remarks=request.POST.get('remarks')
        DomesticConnectionSevenDay.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,total_app = total_app, con_within_seven_day_app = con_within_seven_day_app,con_without_seven_day_app=con_without_seven_day_app,process_seven_day_app=process_seven_day_app,month=month,year=year,reason_not_con_of_seven_day=reason_not_con_of_seven_day,remarks=remarks)
        new_form= DomesticConnectionSevenDayForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'demestic_connection_seven_day.html', context)
    else:
        new_form=DomesticConnectionSevenDayForm()
        context={'new_form':new_form}
        return render(request,'demestic_connection_seven_day.html',context)

def monthly_coordination_meeting_info(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        consumer_meeting_nos=request.POST.get('consumer_meeting_nos')
        previous_month_unsolve_objection=request.POST.get('previous_month_unsolve_objection')
        current_month_unsolve_objection=request.POST.get('current_month_unsolve_objection')
        total_objection=request.POST.get('total_objection')
        current_month_solve_objection=request.POST.get('current_month_solve_objection')
        unsolve_objection=request.POST.get('unsolve_objection')
        remarks=request.POST.get('remarks')
        MonthlyCoordinationMeetingInfo.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,consumer_meeting_nos = consumer_meeting_nos, previous_month_unsolve_objection = previous_month_unsolve_objection,current_month_unsolve_objection=current_month_unsolve_objection,total_objection=total_objection,month=month,year=year,current_month_solve_objection=current_month_solve_objection,remarks=remarks,unsolve_objection=unsolve_objection)
        new_form= MonthlyCoordinationMeetingInfoForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'monthly_coordination_meeting.html', context)
    else:
        new_form=MonthlyCoordinationMeetingInfoForm()
        context={'new_form':new_form}
        return render(request,'monthly_coordination_meeting.html',context)

def necessary_action_against_accident(request):
    if request.method=='POST':
        current_user=request.user
        user_id=current_user.id
        user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
        month_id=request.POST['month']
        year_id=request.POST['year']
        month=Month.objects.get(id=month_id)
        year=Year.objects.get(id=year_id)
        shift_cable=request.POST.get('shift_cable')
        install_pole_for_unshift_cable=request.POST.get('install_pole_for_unshift_cable')
        cover_cable_for_non_install_pole=request.POST.get('cover_cable_for_non_install_pole')
        span_length_sag_visit=request.POST.get('span_length_sag_visit')
        risk_unfit_pole_change=request.POST.get('risk_unfit_pole_change')
        pdb_risk_pole_check_change=request.POST.get('pdb_risk_pole_check_change')
        electric_line_maintainance_by_instraction=request.POST.get('electric_line_maintainance_by_instraction')
        NecessaryActionAgainstAccident.objects.create(pbs_code=user_pbs_info.pbs_code,management_code=user_pbs_info.management_code,shift_cable = shift_cable, install_pole_for_unshift_cable = install_pole_for_unshift_cable,cover_cable_for_non_install_pole=cover_cable_for_non_install_pole,span_length_sag_visit=span_length_sag_visit,month=month,year=year,risk_unfit_pole_change=risk_unfit_pole_change,pdb_risk_pole_check_change=pdb_risk_pole_check_change,electric_line_maintainance_by_instraction=electric_line_maintainance_by_instraction)
        new_form= NecessaryActionAgainstAccidentForm()
        message = "Information Successfully Added!"
        context = {'new_form':new_form, 'message':message}
        return render(request, 'necessary_action_against_accident.html', context)
    else:
        new_form=NecessaryActionAgainstAccidentForm()
        context={'new_form':new_form}
        return render(request,'necessary_action_against_accident.html',context)

















def my_berc_info(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    my_data=PbsInfoBERC.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_brec_info.html',context)

def m_berc_info(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=PbsInfoBERC.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_brec_info.html',context)


def my_new_con_info(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=NewOnlineConnection.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_new_con_info.html',context)
def m_new_con_info(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=NewOnlineConnection.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_new_con_info.html',context)
def my_industry_commercial_dc_rc(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=IndustryCommercialDcRc.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_industry_commercial_dc_rc.html',context)
def m_industry_commercial_dc_rc(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=IndustryCommercialDcRc.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_industry_commercial_dc_rc.html',context)

def my_dc_consumer(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=DcConsumerInfo.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_dc_consumer.html',context)

def m_dc_consumer(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=DcConsumerInfo.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_dc_consumer.html',context)

def my_connected_consumer(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=ConnectedConsumerInfo.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_connected_consumer.html',context)
def m_connected_consumer(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=ConnectedConsumerInfo.objects.filter(management_code=user_management_info.management_code)

    context={'user_pbs_management_info':user_pbs_management_info}

    return render(request, 'm_connected_consumer.html',context)

def my_domestic_connection_seven_day(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=DomesticConnectionSevenDay.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_domestic_connection_seven_day.html',context)

def m_domestic_connection_seven_day(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=DomesticConnectionSevenDay.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_domestic_connection_seven_day.html',context)

def my_monthly_coordination_meeting(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=MonthlyCoordinationMeetingInfo.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_monthly_coordination_meeting.html',context)

def m_monthly_coordination_meeting(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=MonthlyCoordinationMeetingInfo.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_monthly_coordination_meeting.html',context)
def my_actin_against_accident(request):
    current_user=request.user
    user_id=current_user.id
    user_pbs_info=PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    print(pbs_code)
    my_data=NecessaryActionAgainstAccident.objects.filter(pbs_code=pbs_code)
    context={'my_data':my_data,'user_pbs_info':user_pbs_info}
    return render(request, 'my_action_against_accident.html',context)

def m_actin_against_accident(request):
    current_user=request.user
    user_id=current_user.id
    user_management_info=ManagementInfo.objects.get(user__pk=user_id)
    user_pbs_management_info=PbsInfo.objects.filter(management_code=user_management_info.management_code)
    my_data=NecessaryActionAgainstAccident.objects.filter(management_code=user_management_info.management_code)
    context={'my_data':my_data,'user_pbs_management_info':user_pbs_management_info}
    return render(request, 'm_actin_against_accident.html',context)


def user_register(request):
    if request.method=='POST':
        u_first_name=request.POST.get('first_name')
        u_last_name=request.POST.get('last_name')
        user_name=request.POST.get('username')
        user_pass=request.POST.get('password')
        u_email=request.POST.get('email')

        management_id=request.POST['management']
        print("management id:")
        print(management_id)

        management=ManagementInfo.objects.get(id=management_id)
        # m_id=request.POST.get('management_id')

        u_pbs_name=request.POST.get('pbs_name')
        u_pbs_name_benglai=request.POST.get('pbs_name_benglai')
        u_pbs_code=request.POST.get('pbs_code')
        u_address=request.POST.get('address')
        u_mob_no=request.POST.get('mobile_no')
        user=User.objects.create_user(first_name=u_first_name, last_name=u_last_name, username=user_name, password=user_pass, email=u_email)
        pbsinfo_user=PbsInfo.objects.create(user=user,management_code = management_id, pbs_name = u_pbs_name,pbs_name_benglai=u_pbs_name_benglai,pbs_code=u_pbs_code,address=u_address,mobile_no=u_mob_no)
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