from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .forms import SignupForm, EditProfileForm
from .models import Profiles

import ipgetter, datetime       # ipgetter for Getting user IP, and datetime for getting current date and time

####    Home Page     ####
@login_required
def home(request):
    return render(request, 'home.html')


####    Signup form     ####
def signup(request):
    print('signup form')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profiles.emp_name=form.cleaned_data['emp_name']
            user.profiles.department=form.cleaned_data['department']
            user.profiles.designation=form.cleaned_data['designation']
            user.profiles.email = form.cleaned_data['email']
            user.profiles.password = form.cleaned_data['password1']
            user.profiles.created_on = datetime.date.today()
            user.profiles.created_by = form.cleaned_data['emp_name']
            user.profiles.created_time = datetime.time()
            user.profiles.created_ip = get_client_ip(request)
            user.profiles.updated_on = datetime.date.today()
            user.profiles.updated_by = form.cleaned_data['emp_name']
            user.profiles.updated_time = datetime.time()
            user.profiles.updated_ip = get_client_ip(request)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


####    Profile Edit form     ####
def edit_profile(request, pk):
    print('edit profile pk', pk)
    profile = get_object_or_404(Profiles, pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            print('inside post method')
            user = form.save(commit=False)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profiles.emp_name=form.cleaned_data['emp_name']
            user.profiles.department=form.cleaned_data['department']
            user.profiles.designation=form.cleaned_data['designation']
            user.profiles.email = form.cleaned_data['email']
            # user.profiles.password = form.cleaned_data['password1']
            user.profiles.updated_on = datetime.date.today()
            user.profiles.updated_by = form.cleaned_data['emp_name']
            user.profiles.updated_time = datetime.time()
            user.profiles.updated_ip = get_client_ip(request)
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            # return redirect('home')
            return JsonResponse({ 'message': 'Successfully edit'})
    else:
        print('else condition edit profile')
        form = EditProfileForm(instance = request.user.profiles)
    return render(request, 'edit_user.html', {'form': form})


####    To Getting Client IP     ####
def get_client_ip(request):
    ip = ipgetter.myip()
    return ip
