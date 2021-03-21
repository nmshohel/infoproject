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
class ManagementInfo(models.Model):
    m_name=models.CharField(max_length=100)
    m_id=models.IntegerField(blank=True,null=True)

    def __str__ (self):
        return self.m_name


class PbsInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    management=models.ForeignKey(ManagementInfo,on_delete=models.CASCADE, blank=True, null=True)
    pbs_name=models.CharField(max_length=50)
    pbs_name_benglai=models.CharField(max_length=50)
    pbs_code=models.IntegerField(blank=True, null= True)
    address=models.TextField(blank=True, null=True)
    mobile_no=models.TextField(blank=True , null=True)

    def __str__(self):
        return self.pbs_name
    
class PbsInfoBERC(models.Model):
    pbs_code=models.IntegerField(blank=True, null=True)
    complain_nos=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=10, blank=True, null=True)
    year=models.CharField(max_length=10,blank=True, null=True)
    complain_solve=models.IntegerField(blank=True, null=True)
    complain_unsolve_case=models.TextField(max_length=300, blank=True, null=True)
    complain_remark=models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.complain_nos)
