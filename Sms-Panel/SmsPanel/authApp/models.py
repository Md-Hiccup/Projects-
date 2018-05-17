from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class tbl_signup(AbstractUser):
#     emp_no = models.AutoField(primary_key=True)
#     emp_name = models.CharField(max_length = 100)
#     department = models.CharField(max_length=50, default='Others')
#     designation = models.CharField(max_length=50, default='Others')
#     login_permission = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.email

class tbl_signup(models.Model):

    emp_no = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=255, verbose_name = 'Employee Name')
    email = models.EmailField()
    password = models.CharField(max_length=255)

    # REQUIRED_FIELDS = ('emp_no', 'emp_name',)
    # USERNAME_FIELD = 'emp_name'

    def __str__(self):
        return self.emp_name
