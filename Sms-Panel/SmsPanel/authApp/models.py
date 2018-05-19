from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_no = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length = 100)
    department = models.CharField(max_length=50, default='Others')
    designation = models.CharField(max_length=50, default='Others')
    email = models.EmailField(null=False, default="")
    password = models.CharField(max_length=200, default="")
    created_on = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=200, blank=True, default="")
    created_time = models.TimeField(auto_now=True)
    created_ip = models.GenericIPAddressField(null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=200, null=True)
    updated_time = models.TimeField(auto_now=True, null=True)
    updated_ip = models.GenericIPAddressField(null=True)
    # login_permission = models.BooleanField(blank=True, null=False)

    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)
    instance.profiles.save()
