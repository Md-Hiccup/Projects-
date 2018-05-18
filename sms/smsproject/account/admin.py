from django.contrib import admin
from account.models import UserProfileModel

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'age']

admin.site.register(UserProfileModel, UserProfileAdmin)
