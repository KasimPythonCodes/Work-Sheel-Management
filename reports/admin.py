from django.contrib import admin
from reports.models import*

# Register your models here.

admin.site.register(Staff_TL)
# admin.site.register(Supervizor)
# admin.site.register(AdminManager)
# admin.site.register(Dispatch_Table)


class Admincustomer(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','user_type' ,'profile_pic' ]
admin.site.register(CustomUser ,Admincustomer)
    
    
class Supervizorcustomer(admin.ModelAdmin):
    list_display = ['id', 'admin' ,]
admin.site.register(Supervizor ,Supervizorcustomer)
        