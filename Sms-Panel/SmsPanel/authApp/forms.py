from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
from .models import Profiles

class SignupForm(UserCreationForm):
    emp_name = forms.CharField(help_text='Required correct employee name')
    department = forms.CharField(help_text='Required correct department')
    designation = forms.CharField(help_text='Required correct designation')
    email = forms.EmailField(help_text='Required email address')
    # login_permission = forms.BooleanField(help_text='True or False')

    class Meta:
        model = User
        fields = ('username', 'emp_name', 'department', 'designation','email', )

class EditProfileForm(UserChangeForm):
    emp_name = forms.CharField(help_text='Required correct employee name')
    department = forms.CharField(help_text='Required correct department')
    designation = forms.CharField(help_text='Required correct designation')
    email = forms.EmailField(help_text='Required email address')

    class Meta:
        model = Profiles
        # fields = UserChangeForm.Meta.fields
        fields = ['emp_name', 'department', 'designation','email', ]
        exclude = ['username','password1', 'password2', ]
