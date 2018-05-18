from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views import View
from django.views.generic import CreateView
# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterUserForm
from .models import UserProfileModel
# from .forms import tbl_signup_form

# from .forms import CustomUserCreationForm

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

# def signup(request):
#     if request.method == 'POST':
#         form = tbl_signup_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({ 'message': 'Form submitted...'})
#     else :
#         form = tbl_signup_form()
#     return render(request, 'signup.html', { 'form': form})


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'signup.html'
    # success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        UserProfileModel.objects.create(user = user)
        return HttpResponse('User Registered')
