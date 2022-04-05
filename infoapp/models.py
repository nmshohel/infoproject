from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class PbsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pbs_name = models.CharField(max_length=50, blank=True, null=True)
    pbs_name_benglai = models.CharField(max_length=50,blank=True, null=True)
    address = models.TextField(max_length=50,blank=True, null=True)
    mobile_no = models.TextField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.pbs_name
class MeterDataRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_time_date = models.CharField(max_length=100, blank=True, null=True)
    hex = models.CharField(max_length=100, blank=True, null=True)
    kwh = models.CharField(max_length=100, blank=True, null=True)
    kwh2 = models.CharField(max_length=100, blank=True, null=True)
    kvarh = models.CharField(max_length=100, blank=True, null=True)
    kvarh2 = models.CharField(max_length=100, blank=True, null=True)
    kvah = models.CharField(max_length=100, blank=True, null=True)
    avah2 = models.CharField(max_length=100, blank=True, null=True)
    voltage1 = models.CharField(max_length=100, blank=True, null=True)
    voltage2 = models.CharField(max_length=100, blank=True, null=True)
    voltage3 = models.CharField(max_length=100, blank=True, null=True)
    current1 = models.CharField(max_length=100, blank=True, null=True)
    current2 = models.CharField(max_length=100, blank=True, null=True)
    current3 = models.CharField(max_length=100, blank=True, null=True)
    sub_station_name = models.CharField(max_length=100, blank=True, null=True)
    feeder_no=models.CharField(max_length=100,blank=True, null=True)
    month=models.CharField(max_length=100,blank=True, null=True)
    year=models.CharField(max_length=100,blank=True, null=True)
    


    def __str__(self):
        return str(self.current3)

class MeterDataReadFinal(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_time_date = models.CharField(max_length=100, blank=True, null=True)
    hex = models.CharField(max_length=100, blank=True, null=True)
    kwh = models.CharField(max_length=100, blank=True, null=True)
    kwh2 = models.CharField(max_length=100, blank=True, null=True)
    kvarh = models.CharField(max_length=100, blank=True, null=True)
    kvarh2 = models.CharField(max_length=100, blank=True, null=True)
    kvah = models.CharField(max_length=100, blank=True, null=True)
    avah2 = models.CharField(max_length=100, blank=True, null=True)
    voltage1 = models.CharField(max_length=100, blank=True, null=True)
    voltage2 = models.CharField(max_length=100, blank=True, null=True)
    voltage3 = models.CharField(max_length=100, blank=True, null=True)
    current1 = models.CharField(max_length=100, blank=True, null=True)
    current2 = models.CharField(max_length=100, blank=True, null=True)
    current3 = models.CharField(max_length=100, blank=True, null=True)
    sub_station_name = models.CharField(max_length=100, blank=True, null=True)
    feeder_no=models.CharField(max_length=100,blank=True, null=True)
    month=models.CharField(max_length=100,blank=True, null=True)
    year=models.CharField(max_length=100,blank=True, null=True)
    

    def __str__(self):
        return str(self.current3)

class Month(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)
class Substation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)
class Feeder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)
class SubstationFeeder(models.Model):
    id = models.AutoField(primary_key=True)
    substation_name = models.CharField(max_length=20, blank=True, null=True)
    feeder_no = models.CharField(max_length=20, blank=True, null=True)
    no_of_consummer = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return str(self.substation_name)


class MeterDataReadDhakapbs1(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_time_date = models.CharField(max_length=100, blank=True, null=True)
    hex = models.CharField(max_length=100, blank=True, null=True)
    kwh = models.CharField(max_length=100, blank=True, null=True)
    kwh2 = models.CharField(max_length=100, blank=True, null=True)
    kvarh = models.CharField(max_length=100, blank=True, null=True)
    kvarh2 = models.CharField(max_length=100, blank=True, null=True)
    kvah = models.CharField(max_length=100, blank=True, null=True)
    avah2 = models.CharField(max_length=100, blank=True, null=True)
    voltage1 = models.CharField(max_length=100, blank=True, null=True)
    voltage2 = models.CharField(max_length=100, blank=True, null=True)
    voltage3 = models.CharField(max_length=100, blank=True, null=True)
    current1 = models.CharField(max_length=100, blank=True, null=True)
    current2 = models.CharField(max_length=100, blank=True, null=True)
    current3 = models.CharField(max_length=100, blank=True, null=True)
    sub_station_name = models.CharField(max_length=100, blank=True, null=True)
    feeder_no=models.CharField(max_length=100,blank=True, null=True)
    month=models.CharField(max_length=100,blank=True, null=True)
    year=models.CharField(max_length=100,blank=True, null=True)
    

    def __str__(self):
        return str(self.current3)
