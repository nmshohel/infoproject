from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User

class PbsInfoBERCForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= PbsInfoBERC
        fields=['complain_nos','month','year','complain_solve','complain_unsolve_case','complain_remark']

        widgets={
            'complain_nos':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Complain Nos"}),
            'complain_solve':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Complain Solve Nos"}),
            'complain_unsolve_case':forms.Textarea(attrs={'class':'form form-control bg-light', 'placeholder':"Complain Unsolve Case",'rows':4, 'cols':40}),
            'complain_remark':forms.Textarea(attrs={'class':'form form-control bg-light', 'placeholder':"Remarks",'rows':4, 'cols':40}),
                 
        } 
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Enter Password..."}))
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        # fields='__all__'
        help_texts={
            'username':None, 
            'email':None
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Enter UserName..."}),
            'email':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Enter Email..."}),
            'first_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Enter First Name..."}),
            'last_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Enter Last Name..."}),    
        } 
class PBSInfoForm(forms.ModelForm):
    management = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'rounded form form-control bg-light col-md-8',}), queryset =ManagementInfo.objects.all())

    class Meta:
        model=PbsInfo
        fields=['pbs_name','pbs_name_benglai','pbs_code','management','address','mobile_no']
        widgets={
            'pbs_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"PBS Name"}),
            'pbs_name_benglai':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"PBS Name Bengali"}),
            'address':forms.Textarea(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Address",'rows':4, 'cols':80}),
            'mobile_no':forms.NumberInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"Mobile No"}),
            'pbs_code':forms.NumberInput(attrs={'class':'rounded form form-control bg-light col-md-8', 'placeholder':"PBS Code"}),    
        } 

class NewOnlineConnectionForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= NewOnlineConnection
        fields=['total_app','month','year','total_solve_app','cause_of_unsolve','remark']

        widgets={
            'total_app':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Complain Nos"}),
            'total_solve_app':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Complain Solve Nos"}),
            'cause_of_unsolve':forms.Textarea(attrs={'class':'form form-control bg-light', 'placeholder':"Complain Unsolve Case",'rows':4, 'cols':40}),
            'remark':forms.Textarea(attrs={'class':'form form-control bg-light', 'placeholder':"Remarks",'rows':4, 'cols':40}),
                 
        } 

class IndustryCommercialDcRcForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= IndustryCommercialDcRc
        fields=['total_dc_app','month','year','total_app_get_for_rc','complete_rc_app','illegal_app_for_dc']

        widgets={
            'total_dc_app':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'total_app_get_for_rc':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'complete_rc_app':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'illegal_app_for_dc':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            
                 
        } 
class DcConsumerInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= DcConsumerInfo
        fields=['domestic','month','year','industry','commercial','irrigation','govt_institute','other','total_amount','taken_action']

        widgets={
            'domestic':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'industry':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'commercial':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'irrigation':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            'govt_institute':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'other':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'total_amount':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'taken_action':forms.TextInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),         
        }

class ConnectedConsumerInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= ConnectedConsumerInfo
        fields=['domestic','month','year','industry','commercial','irrigation','govt_institute','other','total_amount','taken_action']

        widgets={
            'domestic':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'industry':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'commercial':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'irrigation':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            'govt_institute':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'other':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'total_amount':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'taken_action':forms.TextInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),         
        }
class DomesticConnectionSevenDayForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= DomesticConnectionSevenDay
        fields=['total_app','month','year','con_within_seven_day_app','con_without_seven_day_app','process_seven_day_app','reason_not_con_of_seven_day','remarks']

        widgets={
            'total_app':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'con_within_seven_day_app':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'con_without_seven_day_app':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'process_seven_day_app':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            'reason_not_con_of_seven_day':forms.TextInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'remarks':forms.TextInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            
        }

class MonthlyCoordinationMeetingInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= MonthlyCoordinationMeetingInfo
        fields=['consumer_meeting_nos','month','year','previous_month_unsolve_objection','current_month_unsolve_objection','total_objection','current_month_solve_objection','unsolve_objection','remarks']

        widgets={
            'consumer_meeting_nos':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'previous_month_unsolve_objection':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'current_month_unsolve_objection':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'total_objection':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            'current_month_solve_objection':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'unsolve_objection':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'remarks':forms.TextInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            
        }
class NecessaryActionAgainstAccidentForm(forms.ModelForm):
    month = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= NecessaryActionAgainstAccident
        fields=['shift_cable','month','year','install_pole_for_unshift_cable','cover_cable_for_non_install_pole','span_length_sag_visit','risk_unfit_pole_change','pdb_risk_pole_check_change','electric_line_maintainance_by_instraction']

        widgets={
            'shift_cable':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'install_pole_for_unshift_cable':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'cover_cable_for_non_install_pole':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Colplete rc app"}),
            'span_length_sag_visit':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"Illegal app for dc"}),
            'risk_unfit_pole_change':forms.NumberInput( attrs={'class':'form form-control bg-light', 'placeholder':"Total Dc"}),
            'pdb_risk_pole_check_change':forms.NumberInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            'electric_line_maintainance_by_instraction':forms.TextInput(attrs={'class':'form form-control bg-light', 'placeholder':"total app get for rc"}),
            
        }





