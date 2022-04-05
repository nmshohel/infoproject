from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User


class PersonData(forms.Form):
    class meta:
        model = MeterDataRead
        fields = '__all__'

class MeterDataReadForm(forms.ModelForm):
    month = forms.ModelChoiceField(label='Month', widget=forms.Select(
        attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Month.objects.all())
    year = forms.ModelChoiceField(label='Year', widget=forms.Select(
        attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Year.objects.all())
    # sub_station_name = forms.ModelChoiceField(label='Substation',initial='FIXED', widget=forms.Select(
    #     attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Substation.objects.all())
    feeder_no = forms.ModelChoiceField(label='Feeder', widget=forms.Select(
        attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Feeder.objects.all())

    class Meta:
        model = MeterDataRead
        fields = [ 'month', 'year', 'feeder_no']

        widgets = {
            # 'feeder_no': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
            # 'sub_station_name': forms.TextInput(attrs={'class': 'form form-control bg-light'}),
            # 'month': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
            # 'year': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
        }