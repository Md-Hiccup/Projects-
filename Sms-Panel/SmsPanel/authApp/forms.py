from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    emp_name = forms.CharField(help_text='Required correct employee name')
    department = forms.CharField(help_text='Required correct department')
    designation = forms.CharField(help_text='Required correct designation')
    email = forms.EmailField(help_text='Required email address')
    # login_permission = forms.BooleanField(help_text='True or False')

    class Meta:
        model = User
        fields = ('username', 'emp_name', 'department', 'designation','email', 'password1', 'password2', )
