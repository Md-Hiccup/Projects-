from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length=1, choices = ( ('M', 'Male'), ('F', 'Female')), blank = True)
    age = models.PositiveIntegerField(blank = True, null = True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def get_absolute_url(self):
        from django.urls import reverse
        return redirect('signup')
####### Trying to Inserting the Data to Postgres DB ##################
# class tbl_signup(AbstractUser):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     emp_no = models.AutoField(primary_key=True)
#     emp_name = models.CharField(max_length = 100)
#     department = models.CharField(max_length=50, default='Others')
#     designation = models.CharField(max_length=50, default='Others')
#     login_permission = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.email


####### For Manually Inserting the Data to Postgres DB ##################

# class tbl_signup(models.Model):
#
#     emp_no = models.AutoField(primary_key=True)
#     emp_name = models.CharField(max_length=255, verbose_name = 'Employee Name')
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#
#     # REQUIRED_FIELDS = ('emp_no', 'emp_name',)
#     # USERNAME_FIELD = 'emp_name'
#
#     def __str__(self):
#         return self.emp_name
