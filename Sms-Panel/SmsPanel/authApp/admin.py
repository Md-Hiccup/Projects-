from django.contrib import admin
from .models import Profiles
from .forms import SignupForm
#
class CustomUserAdmin(admin.ModelAdmin):
    form = SignupForm
    model = Profiles
    list_display = ['emp_name',]

admin.site.register(Profiles, CustomUserAdmin)
