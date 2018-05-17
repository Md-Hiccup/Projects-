from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import tbl_signup_form
# from .forms import CustomUserCreationForm

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def signup(request):
    if request.method == 'POST':
        form = tbl_signup_form(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({ 'message': 'Form submitted...'})
    else :
        form = tbl_signup_form()
    return render(request, 'signup.html', { 'form': form})
