# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import tbl_signup
from django import forms

# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         model = tbl_signup
#         fields = ('emp_name', 'username', 'department', 'designation', 'email', 'login_permission', )
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = tbl_signup
#         fields = UserChangeForm.Meta.fields

class tbl_signup_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = tbl_signup
        fields = ['emp_no', 'emp_name', 'email', 'password' ]
