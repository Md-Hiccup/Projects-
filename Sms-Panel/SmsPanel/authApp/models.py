from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    employee_name = models.CharField(max_length = 100)
    department = models.CharField(max_length=50, default='Others')
    designation = models.CharField(max_length=50, default='Others')
    login_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.email
