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
    path('my-industry-commercial-dc-rc', views.my_industry_commercial_dc_rc , name='my_industry_commercial_dc_rc'), 
    path('new-online-connection', views.new_online_connection , name='new_online_connection'), 
    path('my-new-con-info', views.my_new_con_info , name='my_new_con_info'),  
    path('my-dc-consumer', views.my_dc_consumer , name='my_dc_consumer'), 
    path('my-connected-consumer', views.my_connected_consumer , name='my_connected_consumer'),  
    path('my-domestic-connection-seven-day', views.my_domestic_connection_seven_day , name='my_domestic_connection_seven_day'),
    path('my-monthly-coordination-meeting', views.my_monthly_coordination_meeting , name='my_monthly_coordination_meeting'),  
    path('my-actin-against-accident', views.my_actin_against_accident , name='my_actin_against_accident'),
    path('monthly-coordination-meeting-info', views.monthly_coordination_meeting_info , name='monthly_coordination_meeting_info'),  
    path('industry-comercial-consumer-dc-rc', views.industry_comercial_consumer_dc_rc , name='industry_comercial_consumer_dc_rc'),
    path('dc-consumer', views.dc_consumer , name='dc_consumer'),
    path('connected-consumer', views.connected_consumer , name='connected_consumer'),
    path('domestic-connection-seven-day', views.domestic_connection_seven_day , name='domestic_connection_seven_day'),
    path('necessary-action-against-accident', views.necessary_action_against_accident , name='necessary_action_against_accident'),
    path('m-berc-info', views.m_berc_info , name='m_berc_info'),
    path('m-new-con-info', views.m_new_con_info , name='m_new_con_info'),
    path('m-industry-commercial-dc-rc', views.m_industry_commercial_dc_rc , name='m_industry_commercial_dc_rc'),
    path('m-dc-consumer', views.m_dc_consumer , name='m_dc_consumer'),
    path('m-connected-consumer', views.m_connected_consumer , name='m_connected_consumer'),
    path('m-domestic-connection-seven-day', views.m_domestic_connection_seven_day , name='m_domestic_connection_seven_day'),
    path('m-monthly-coordination-meeting', views.m_monthly_coordination_meeting , name='m_monthly_coordination_meeting'),
    path('m-actin-against-accident', views.m_actin_against_accident , name='m_actin_against_accident'),

    



    

    






    

    


    


    


     


]