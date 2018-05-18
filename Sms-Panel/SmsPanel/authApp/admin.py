from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

from .models import UserProfileModel
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import tbl_signup

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = tbl_signup
#     list_display = ['email', 'emp_name']
#
# admin.site.register(tbl_signup, CustomUserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'gender', 'age', 'department']

admin.site.register(UserProfileModel, UserProfileAdmin)
