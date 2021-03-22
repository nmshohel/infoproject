from django.contrib import admin
from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('forgot-password', forgot_password, name='forgot_password'),
    path('logout', user_logout, name='user_logout'),
    path('', user_login , name='user_login'),
    path('home-page', home_page , name='home_page'),
    path('loged-user', loged_user , name='loged_user'),
    path('pbs-info', pbs_info , name='pbs_info'),
    path('change-password', change_password , name='change_password'),
    path('pbs-info-berc-form', pbs_info_berc_form , name='pbs_info_berc_form'), 
    path('user_register', user_register , name='user_register'),
    path('my-berc-info', my_berc_info , name='my_berc_info'),  
    path('new-online-connection', new_online_connection , name='new_online_connection'), 
    path('my-new-con-info', my_new_con_info , name='my_new_con_info'),  
    path('industry-comercial-consumer-dc-rc', industry_comercial_consumer_dc_rc , name='industry_comercial_consumer_dc_rc'),


     


]