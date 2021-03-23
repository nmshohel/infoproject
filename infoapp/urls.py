# from django.contrib import admin
from django.urls import path
from infoapp import views
# from .models import *

app_name = 'infoapp'
urlpatterns = [
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('logout', views.user_logout, name='user_logout'),
    path('', views.user_login , name='user_login'),
    path('home-page', views.home_page , name='home_page'),
    path('loged-user', views.loged_user , name='loged_user'),
    path('pbs-info', views.pbs_info , name='pbs_info'),
    path('change-password', views.change_password , name='change_password'),
    path('pbs-info-berc-form', views.pbs_info_berc_form , name='pbs_info_berc_form'), 
    path('user_register', views.user_register , name='user_register'),
    path('my-berc-info', views.my_berc_info , name='my_berc_info'),  
    path('new-online-connection', views.new_online_connection , name='new_online_connection'), 
    path('my-new-con-info', views.my_new_con_info , name='my_new_con_info'),  
    
    path('monthly-coordination-meeting-info', views.monthly_coordination_meeting_info , name='monthly_coordination_meeting_info'),  
    path('industry-comercial-consumer-dc-rc', views.industry_comercial_consumer_dc_rc , name='industry_comercial_consumer_dc_rc'),
    path('dc-consumer', views.dc_consumer , name='dc_consumer'),
    path('connected-consumer', views.connected_consumer , name='connected_consumer'),
    path('domestic-connection-seven-day', views.domestic_connection_seven_day , name='domestic_connection_seven_day'),
    path('necessary-action-against-accident', views.necessary_action_against_accident , name='necessary_action_against_accident'),


    


     


]