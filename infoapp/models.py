from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Month(models.Model):
    name=models.CharField(max_length=20,blank=True, null=True)
    def __str__(self):
        return self.name

class Year(models.Model):
    name=models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return str(self.name)
class Otp(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    status=models.BooleanField(default=True, blank=True,null=True)
    def __str__(self):
        return self.name
class ManagementInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    name_bengali=models.CharField(max_length=250, blank=True, null=True)
    management_status=models.BooleanField(default=True, blank=True, null=True)
    management_code=models.IntegerField(blank=True, null=True)


    def __str__ (self):
        return self.name


class PbsInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # management=models.ForeignKey(ManagementInfo,on_delete=models.CASCADE, blank=True, null=True)
    pbs_name=models.CharField(max_length=50)
    pbs_name_benglai=models.CharField(max_length=50)
    pbs_code=models.IntegerField(blank=True, null= True)
    management_code=models.IntegerField(blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    mobile_no=models.TextField(blank=True , null=True)

    def __str__(self):
        return self.pbs_name
    
class PbsInfoBERC(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    complain_nos=models.CharField(max_length=250, blank=True, null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    complain_solve=models.CharField(max_length=250, blank=True, null=True)
    complain_unsolve_case=models.TextField(max_length=300, blank=True, null=True)
    complain_remark=models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.complain_nos)

class NewOnlineConnection(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    total_app=models.CharField(max_length=250, blank=True,null=True)
    total_solve_app=models.CharField(max_length=250, blank=True, null=True)
    cause_of_unsolve=models.TextField(max_length=250, blank=True, null=True)
    remark=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.total_app)

class IndustryCommercialDcRc(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    total_dc_app=models.CharField(max_length=250, blank=True,null=True)
    total_app_get_for_rc=models.CharField(max_length=250, blank=True, null=True)
    complete_rc_app=models.CharField(max_length=250, blank=True, null=True)
    illegal_app_for_dc=models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.total_dc_app)

class DcConsumerInfo(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    domestic=models.CharField(max_length=250, blank=True,null=True)
    industry=models.CharField(max_length=250, blank=True, null=True)
    commercial=models.CharField(max_length=250, blank=True, null=True)
    irrigation=models.CharField(max_length=250, blank=True, null=True)
    govt_institute=models.CharField(max_length=250, blank=True, null=True)
    other=models.CharField(max_length=250, blank=True, null=True)
    total_amount=models.CharField(max_length=250, blank=True, null=True)
    taken_action=models.TextField(max_length=250, blank=True, null=True)
    def __str__(self):
        return str(self.pbs_code)

class ConnectedConsumerInfo(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    domestic=models.CharField(max_length=250, blank=True,null=True)
    industry=models.CharField(max_length=250, blank=True, null=True)
    commercial=models.CharField(max_length=250, blank=True, null=True)
    irrigation=models.CharField(max_length=250, blank=True, null=True)
    govt_institute=models.CharField(max_length=250, blank=True, null=True)
    other=models.CharField(max_length=250, blank=True, null=True)
    total_amount=models.CharField(max_length=250, blank=True, null=True)
    taken_action=models.TextField(max_length=250, blank=True, null=True)
    def __str__(self):
        return str(self.pbs_code)
class DomesticConnectionSevenDay(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    total_app=models.CharField(max_length=250, blank=True,null=True)
    con_within_seven_day_app=models.CharField(max_length=250, blank=True, null=True)
    con_without_seven_day_app=models.CharField(max_length=250, blank=True, null=True)
    process_seven_day_app=models.CharField(max_length=250, blank=True, null=True)
    reason_not_con_of_seven_day=models.TextField(max_length=250, blank=True, null=True)
    remarks=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.pbs_code)

class MonthlyCoordinationMeetingInfo(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    consumer_meeting_nos=models.CharField(max_length=250, blank=True,null=True)
    previous_month_unsolve_objection=models.CharField(max_length=250, blank=True, null=True)
    current_month_unsolve_objection=models.CharField(max_length=250, blank=True, null=True)
    total_objection=models.CharField(max_length=250, blank=True, null=True)
    current_month_solve_objection=models.CharField(max_length=250, blank=True, null=True)
    unsolve_objection=models.CharField(max_length=250, blank=True, null=True)
    remarks=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.pbs_code)

class NecessaryActionAgainstAccident(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    management_code=models.IntegerField(blank=True,null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    shift_cable=models.CharField(max_length=250, blank=True,null=True)
    install_pole_for_unshift_cable=models.CharField(max_length=250, blank=True, null=True)
    cover_cable_for_non_install_pole=models.CharField(max_length=250, blank=True, null=True)
    span_length_sag_visit=models.CharField(max_length=250, blank=True, null=True)
    risk_unfit_pole_change=models.CharField(max_length=250, blank=True, null=True)
    pdb_risk_pole_check_change=models.CharField(max_length=250, blank=True, null=True)
    electric_line_maintainance_by_instraction=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.pbs_code)