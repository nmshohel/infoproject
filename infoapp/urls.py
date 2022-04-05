# from django.contrib import admin
from django.urls import path
from infoapp import views
# from .models import *
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
app_name = 'infoapp'
urlpatterns = [
   
    # path('meter-data-calculation', views.meter_data_calculation,
    #      name='meter_data_calculation'),
    path('', views.simple_upload, name='data-import'),
    path('delete-page', views.delete_page, name='delete-page'),
    path('data-delete', views.data_delete, name='data_delete'),
    path('view-result', views.view_result, name='view-result'),
    path('meter-data-calculation', views.meter_data_calculation, name='meter-data-calculation'),
    path('home-page', views.home_page, name='home-page'),
    path('user-login', views.user_login, name='user-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('meter-info', views.meter_info, name='meter-info'),
    path('upload-history', views.upload_history, name='upload-history'),
    

    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
