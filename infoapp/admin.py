from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# class MeterDataReadFinalAdmin(admin.ModelAdmin):
#     list_display = ('id', 'date_time_date','kvah', 'hex','current1', 'current2', 'current3','meter_no','month','year','pbs_code')
# # Register your models here.
# @admin.register(MeterDataRead)
class MeterDataReadadmin(ImportExportModelAdmin):
     list_display = ('id', 'date_time_date','kvah','current1', 'current2', 'current3','sub_station_name','feeder_no','month','year')
class MeterDataReadFinaladmin(ImportExportModelAdmin):
     list_display = ('id', 'date_time_date','kvah', 'current1', 'current2', 'current3','sub_station_name','feeder_no','month','year')

class MeterDataReadDhakapbs1Admin(ImportExportModelAdmin):
     list_display = ('id', 'date_time_date','kvah', 'current1', 'current2', 'current3','sub_station_name','feeder_no','month','year')
class SubstationFeederadmin(ImportExportModelAdmin):
     list_display = ('id', 'substation_name','feeder_no','no_of_consummer')


admin.site.register(MeterDataReadFinal, MeterDataReadFinaladmin)
admin.site.register(MeterDataReadDhakapbs1, MeterDataReadDhakapbs1Admin)
admin.site.register(PbsInfo)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(MeterDataRead,MeterDataReadadmin)
admin.site.register(Substation)
admin.site.register(Feeder)
admin.site.register(SubstationFeeder,SubstationFeederadmin)
