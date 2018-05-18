# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# # from .models import tbl_signup
# # from .models import employee
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         # model = tbl_signup
#         # fields = ('emp_name', 'department', 'designation', 'login_permission', )
#         model = employee
#         fields = ['department']
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = employee
#         # model = tbl_signup
#         fields = UserChangeForm.Meta.fields
#
# # class tbl_signup_form(forms.ModelForm):
# #     password = forms.CharField(widget=forms.PasswordInput)
# #     class Meta:
# #         model = tbl_signup
# #         fields = ['emp_no', 'emp_name', 'email', 'password' ]

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    # validate password2
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']
