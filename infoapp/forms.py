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




