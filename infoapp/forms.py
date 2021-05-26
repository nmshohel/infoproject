from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User

class PbsInfoBERCForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= PbsInfoBERC
        fields=['complain_nos','month','year','complain_solve','complain_unsolve_case','complain_remark']

        widgets={
            'complain_nos':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'complain_solve':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'complain_unsolve_case':forms.Textarea(attrs={'class':'form form-control bg-light','rows':4, 'cols':40}),
            'complain_remark':forms.Textarea(attrs={'class':'form form-control bg-light','rows':4, 'cols':40}),       
        } 
        labels={
            'complain_nos':'অভিযোগ প্রাপ্তির সংখ্যা ',
            'complain_solve':'অভিযোগ নিষ্পত্তির সংখ্যা ',
            'complain_unsolve_case':'অনিস্পন্ন আবেদন সংখ্যা ',
            'complain_remark':'অভিযোগ অনিস্পনের কারণ'
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
            'username':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'email':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'first_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'last_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),    
        }
        labels={
            'username':'Username',
            'email':'Email',
            'first_name':'First Name',
            'last_name':'Last Name' 
        }
class PBSInfoForm(forms.ModelForm):
    management = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'rounded form form-control bg-light col-md-8',}), queryset =ManagementInfo.objects.all())

    class Meta:
        model=PbsInfo
        fields=['pbs_name','pbs_name_benglai','pbs_code','management','address','mobile_no']
        widgets={
            'pbs_name':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'pbs_name_benglai':forms.TextInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'address':forms.Textarea(attrs={'class':'rounded form form-control bg-light col-md-8','rows':4, 'cols':80}),
            'mobile_no':forms.NumberInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),
            'pbs_code':forms.NumberInput(attrs={'class':'rounded form form-control bg-light col-md-8'}),    
        }
        labels={
            'pbs_name':'PBS Name',
            'pbs_name_benglai':'PBS Name Bengali',
            'address':'Address',
            'mobile_no':'Mobile No',
            'pbs_code':'PBS Code' 
        }

class NewOnlineConnectionForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= NewOnlineConnection
        fields=['total_app','month','year','total_solve_app','cause_of_unsolve','remark']

        widgets={
            'total_app':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'total_solve_app':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'cause_of_unsolve':forms.Textarea(attrs={'class':'form form-control bg-light','rows':4, 'cols':40}),
            'remark':forms.Textarea(attrs={'class':'form form-control bg-light','rows':4, 'cols':40}),
                 
        }
        labels={
            'total_app':'নতুন বিদ্যুৎ সংযোগের ক্ষেত্রে অনলাইন এ প্রাপ্ত আবেদনের সংখ্যা ',
            'total_solve_app':'নতুন বিদ্যুৎ সংযোগের ক্ষেত্রে অনলাইন এ প্রাপ্ত নিস্পন্ন আবেদনের সংখ্যা',
            'cause_of_unsolve':'নতুন বিদ্যুৎ সংযোগের ক্ষেত্রে অনলাইন এ প্রাপ্ত অনিস্পন্ন আবেদনের সংখ্যা ',
            'remark':'অনিস্পন্ন থাকলে তার কারণ' 
        }

class IndustryCommercialDcRcForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= IndustryCommercialDcRc
        fields=['total_dc_app','month','year','total_app_get_for_rc','complete_rc_app','illegal_app_for_dc']

        widgets={
            'total_dc_app':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'total_app_get_for_rc':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'complete_rc_app':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'illegal_app_for_dc':forms.NumberInput(attrs={'class':'form form-control bg-light'}),       
        } 
        labels={
            'total_dc_app':'বকেয়ার কারণে বিবেচ্য মাসে বিচ্ছিন্নকৃত শিল্প/বাণিজ্যিক গ্রাহক সংখ্যা ',
            'total_app_get_for_rc':'পুনঃসংযোগ গ্রহণের জন্য বিবেচ্য মাসে প্রাপ্ত আবেদন সংখ্যা ',
            'complete_rc_app':'বিবেচ্য মাসে পুনঃসংযোগ প্রদানকৃত শিল্প/বাণিজ্যিক গ্রাহক সংখ্যা ',
            'illegal_app_for_dc':'সংযোগ বিচ্ছিন্নের পর বিবেচ্য মাসে অবৈধ বিদ্যুৎ ব্যবহারকারী শিল্প/বাণিজ্যিক গ্রাহকের সংখ্যা ',
             
        }
class DcConsumerInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= DcConsumerInfo
        fields=['domestic','month','year','industry','commercial','irrigation','govt_institute','other','total_amount','taken_action']

        widgets={
            'domestic':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'industry':forms.NumberInput(attrs={'class':'form form-control bg-light',}),
            'commercial':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'irrigation':forms.NumberInput(attrs={'class':'form form-control bg-light',}),
            'govt_institute':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'other':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'total_amount':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'taken_action':forms.TextInput(attrs={'class':'form form-control bg-light'}),         
        }
        labels={
            'domestic':'আবাসিক',
            'industry':'শিল্প',
            'commercial':'বানিজ্যিক',
            'irrigation':'সেচ',
            'govt_institute':'সরকারী প্রতিষ্ঠান',
            'other':'অন্যান্য',
            'total_amount':'মোট',
            'taken_action': 'বকেয়ার কারনে গৃহীত কার্যব্যবস্থা(লাল নোটিশ, উকিল নোটিশ, মামলা/জিডি ইত্যাদি' 
        }

class ConnectedConsumerInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= ConnectedConsumerInfo
        fields=['domestic','month','year','industry','commercial','irrigation','govt_institute','other','total_amount','taken_action']

        widgets={
            'domestic':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'industry':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'commercial':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'irrigation':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'govt_institute':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'other':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'total_amount':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'taken_action':forms.TextInput(attrs={'class':'form form-control bg-light'}),         
        }
        labels={
            'domestic':'আবাসিক',
            'industry':'শিল্প',
            'commercial':'বানিজ্যিক',
            'irrigation':'সেচ',
            'govt_institute':'সরকারী প্রতিষ্ঠান',
            'other':'অন্যান্য',
            'total_amount':'মোট',
            'taken_action': 'বকেয়ার কারনে গৃহীত কার্যব্যবস্থা(লাল নোটিশ, উকিল নোটিশ, মামলা/জিডি ইত্যাদি' 
        }
class DomesticConnectionSevenDayForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= DomesticConnectionSevenDay
        fields=['total_app','month','year','con_within_seven_day_app','con_without_seven_day_app','process_seven_day_app','reason_not_con_of_seven_day','remarks']

        widgets={
            'total_app':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'con_within_seven_day_app':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'con_without_seven_day_app':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'process_seven_day_app':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'reason_not_con_of_seven_day':forms.TextInput( attrs={'class':'form form-control bg-light'}),
            'remarks':forms.TextInput(attrs={'class':'form form-control bg-light'}),
            
        }
        labels={
            'total_app':'আবাসিক সংযোগের জন্য প্রাপ্ত মোট আবেদন সংখ্যা ',
            'con_within_seven_day_app':'আবেদনের ০৭ দিনের মধ্যে প্রদানকৃত সংযোগ(টি)',
            'con_without_seven_day_app':'আবেদনের ০৭ অধিক সময়ে প্রদানকৃত সংযোগ(টি)',
            'process_seven_day_app':'আবেদনের তারিখ হতে ০৭ দিনের মধ্যে প্রক্রিয়াধীন আবেদনের সংখ্যা(টি)',
            'reason_not_con_of_seven_day':'০৭ দিনের মধ্যে সংযোগ না হওয়ার কারণ ',
            'remarks':'মন্তব্য'
        }

class MonthlyCoordinationMeetingInfoForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= MonthlyCoordinationMeetingInfo
        fields=['consumer_meeting_nos','month','year','previous_month_unsolve_objection','current_month_unsolve_objection','total_objection','current_month_solve_objection','unsolve_objection','remarks']

        widgets={
            'consumer_meeting_nos':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'previous_month_unsolve_objection':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'current_month_unsolve_objection':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'total_objection':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'current_month_solve_objection':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'unsolve_objection':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'remarks':forms.TextInput(attrs={'class':'form form-control bg-light'}),
            
        }
        labels={
            'consumer_meeting_nos':'গ্রহক সমাবেশ ',
            'previous_month_unsolve_objection':'পূর্ববর্তী মাস সমূহের অনিস্পন্ন আপত্তি',
            'current_month_unsolve_objection':'বিবেচ্য মাসের অনিস্পন্ন আপত্তি',
            'total_objection':'মোট আপত্তি ',
            'current_month_solve_objection':'বিবেচ্য মাসের নিস্পত্তি',
            'unsolve_objection':'অনিস্পন্ন আপত্তি',
            'remarks':'মন্তব্য'
        }
class NecessaryActionAgainstAccidentForm(forms.ModelForm):
    month = forms.ModelChoiceField(label= 'মাস',widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Month.objects.all())
    year = forms.ModelChoiceField( label='বছর', widget=forms.Select(attrs={'class':'form form-control bg-light col-md-6',}), queryset =Year.objects.all())
    class Meta:
        model= NecessaryActionAgainstAccident
        fields=['shift_cable','month','year','install_pole_for_unshift_cable','cover_cable_for_non_install_pole','span_length_sag_visit','risk_unfit_pole_change','pdb_risk_pole_check_change','electric_line_maintainance_by_instraction']

        widgets={
            'shift_cable':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'install_pole_for_unshift_cable':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'cover_cable_for_non_install_pole':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'span_length_sag_visit':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'risk_unfit_pole_change':forms.NumberInput( attrs={'class':'form form-control bg-light'}),
            'pdb_risk_pole_check_change':forms.NumberInput(attrs={'class':'form form-control bg-light'}),
            'electric_line_maintainance_by_instraction':forms.TextInput(attrs={'class':'form form-control bg-light'}),
            
        }
        labels={
            'shift_cable':'বিভিন্ন স্থাপনার উপর দিয়ে টানানো তার দ্রুত স্থানান্তরের ব্যবস্থা গ্রহণ করা হয়েছে কিনা',
            'install_pole_for_unshift_cable':'স্থানান্তরের সুযোগ না থাকলে যথাযথ উচ্চতাসম্পন্ন পোল স্থাপনের ব্যবস্থা করা হয়েছে কিনা ',
            'cover_cable_for_non_install_pole':'লাইন স্থানান্তরের সুযোগ না থাকলে কভার তার ব্যবহৃত হচ্ছে কিনা',
            'span_length_sag_visit':'স্প্যান লেন্থ এবং স্যাগ নিয়মিত পরিদর্শন করে সমস্যা থাকলে দ্রুত সমাধানের ব্যবস্থা করা হয়েছে কিনা ',
            'risk_unfit_pole_change':'ঝুঁকিপূর্ণ ও ব্যবহার অনুপযোগী পোল দ্রুত পরিবর্তনের ব্যবস্থা গ্রহণ করা হয়েছে কিনা',
            'pdb_risk_pole_check_change':'পিডিবি হতে অধিগ্রহণকৃত এবং পুরাতন পরিক্ষা-নিরীক্ষা পূর্বক খুঁজে করে দ্রুত সংস্কারের ব্যবস্থা গ্রহন করা হয়েছে কিনা ',
            'electric_line_maintainance_by_instraction':'বৈদ্যুতিক লাইন সমুহ পবিস নির্দেশিকা অনুযায়ী নিয়মিত রক্ষণাবেক্ষণ করা হচ্ছে কিনা'
        }





