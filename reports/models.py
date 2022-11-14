from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here. 

class CustomUser(AbstractUser):
    USER = (
        ('1', 'Super-Admin'), # only views
        ('2', 'Manager'),       # add and views
        ('3', 'Supervizor'), # only crud oprations
    )
    user_type = models.CharField(choices=USER, max_length=150)
    profile_pic = models.ImageField(upload_to = 'SuperAdmin/profile_pic' )
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
   
    


    


class Supervizor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to = 'Supervizor/Staff_profile_pic')
    designation = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return str(  self.admin.first_name + " " + self.admin.last_name  ) and self.id
    
 
# class AdminManager(models.Model):
#     manager = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     profile_m_img = models.ImageField(upload_to = 'Manager/Manager_profile_pic')
#     position = models.CharField(max_length=40)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return str(self.manager.first_name + " " + self.manager.last_name)
    
        



class Staff_TL(models.Model):
    fk = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    user_asign_id=models.ForeignKey(Supervizor, on_delete=models.CASCADE )
    Line_No =  models.CharField(max_length=15)
    # Line_id = models.IntegerField(primary_key=True)
    Manpowers = models.CharField(blank=True , null=True ,max_length=10)
    Target = models.CharField(blank=True , null=True , max_length=10)
    # Input_c = models.CharField(blank=True , null=True , max_length=10)
    # Output_c= models.CharField(blank=True , null=True , max_length=10)
    # Dispatch_c = models.CharField(blank=True , null=True , max_length=10)
    nine_to_ten_in=models.CharField(blank=True , null=True ,max_length=10)
    ten_to_eleven_in=models.CharField(blank=True , null=True,max_length=10)
    eleven_to_twelve_in=models.CharField(blank=True , null=True,max_length=10)
    twelve_to_one_in=models.CharField(blank=True , null=True,max_length=10)
    one_to_two_in=models.CharField(blank=True , null=True,max_length=10)
    two_to_three_in=models.CharField(blank=True , null=True,max_length=10)
    three_to_four_in=models.CharField(blank=True , null=True,max_length=10)
    four_to_five_in=models.CharField(blank=True , null=True,max_length=10)
    
    nine_to_ten_out=models.CharField(blank=True , null=True ,max_length=10)
    ten_to_eleven_out=models.CharField(blank=True , null=True,max_length=10)
    eleven_to_twelve_out=models.CharField(blank=True , null=True,max_length=10)
    twelve_to_one_out=models.CharField(blank=True , null=True,max_length=10)
    one_to_two_out=models.CharField(blank=True , null=True,max_length=10)
    two_to_three_out=models.CharField(blank=True , null=True,max_length=10)
    three_to_four_out=models.CharField(blank=True , null=True,max_length=10)
    four_to_five_out=models.CharField(blank=True , null=True,max_length=10)
    
    
    nine_to_ten_dis=models.CharField(blank=True , null=True ,max_length=10)
    ten_to_eleven_dis=models.CharField(blank=True , null=True,max_length=10)
    eleven_to_twelve_dis=models.CharField(blank=True , null=True,max_length=10)
    twelve_to_one_dis=models.CharField(blank=True , null=True,max_length=10)
    one_to_two_dis=models.CharField(blank=True , null=True,max_length=10)
    two_to_three_dis=models.CharField(blank=True , null=True,max_length=10)
    three_to_four_dis=models.CharField(blank=True , null=True,max_length=10)
    four_to_five_dis=models.CharField(blank=True , null=True,max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
      verbose_name = "TABLE DATA"
      
    def __str__(self):
        return str( self.user_asign_id.admin.first_name + " " + self.user_asign_id.admin.last_name )
      

    








