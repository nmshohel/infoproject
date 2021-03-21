from django.contrib import admin
from .models import *

class ManagementInfoadmin(admin.ModelAdmin):
    list_display=('m_name','m_id')

class PbsInfoadmin(admin.ModelAdmin):
    list_display=('user','management_id','pbs_code','mobile_no')

class PbsInfoBERCadmin(admin.ModelAdmin):
    list_display=('pbs_code','complain_nos','complain_solve','complain_unsolve_case','complain_remark')

class NewOnlineConnectionadmin(admin.ModelAdmin):
    list_display=('pbs_code','total_app','total_solve_app','cause_of_unsolve','remark')
# Register your models here.

admin.site.register(NewOnlineConnection,NewOnlineConnectionadmin)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(PbsInfo,PbsInfoadmin)
admin.site.register(ManagementInfo,ManagementInfoadmin)
admin.site.register(PbsInfoBERC,PbsInfoBERCadmin)
