from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from reports.views import* 
from reports.supervizorviews import*
from reports.SUPERUSERADMIN_views import*



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', SUPERUSER_DASHBOARD , name='SUPERUSER_DASHBOARD'),
    path('SUPERVIZOR_DASHBOARD/',     SUPERVIZOR_DASHBOARD , name='SUPERVIZOR_DASHBOARD'),

    # SUPERVIZOR TABLE 

    
    path('supervizor-table-add/' , SUPERVIZOR_TABLE_ADD  ,    name='supervizor-add'),
    path('supervizor-table-views/' ,  SUPERVIZOR_TABLE_VIEWS,    name='supervizor-read'),
    path('supervizor-table-edit/<int:id>/' , SUPERVIZOR_TABLE_EDIT ,  name='supervizor-edit'),
    path('supervizor-table-update/<int:id>' , SUPERVIZOR_TABLE_UPDATE ,  name='supervizor-update'),
    path('supervizor-table-confirm-delete/<int:id>/', SUPERVIZOR_TABLE_DELETE ,  name='supervizor-data-delete'),
    path('supervizor-table-list-detail/' , SUPERVIZOR_LIST_TABLE,    name='supervizor-line_detail'),
    
    # LOGIN USER OR LOGOUT  
   
    path('dologin/', Login_All_User , name='dologin'),
    path('login/', user_login , name='user_login'),
    path('logout/', logout_user , name='user_logout'),
    # path('fund/',     fund_export_csv , name='user_logout'),
    
    
    #   SUPERVIZOR  ''''''''//////``````  FUNCTION
    
    path('manager-views/', Manager_Add , name='manager-data'),
    path('supervizor_ragister/' ,  SUPERVIZOR_REGISTER,    name='supervizor-sign'),
    path('supervizor-views/' ,  SUPERVIZOR_VIEWS,    name='supervizor-views-all'),
    path('supervizor-edit/<int:id>/' ,   SUPERVIZOR_EDIT,  name='supervizor-views-edit'),
    path('supervizor-update/' , SUPERVIZOR_UPADTE, name='supervizor-views-update'),
    path('supervizor-delete/<int:id>/' ,     SUPERVIZOR_DELETE, name='supervizor-views-delete'),
    path('supervizor-delete-List/' ,  SUPERVIZOR_DLIST, name='supervizor_add_list_delete'),
    
    #SUPERUSER '''''''''''##########'''''''''''''' FUNCTION 
   
    # path('super-admin-edit/<str:id>', SUPERADMIN_EDIT, name='user-edit'),
    # path('super-admin-update/', SUPERADMIN_UPDATE, name='user-update'),
    path('hodprofile/',     hod_profile, name='hodprofile'),
    
    path('super-admin-update/',     HOD_UPDATE, name='user-update'),
    
    
    
    
    #SUPERVIZOR DASHBOARD FILTER
    
       
      
    
    
    
    
    
    
    
] 
# +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)