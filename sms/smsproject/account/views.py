from django.shortcuts import render
from django.views.generic import CreateView
from account.forms import RegisterUserForm
from django.http import HttpResponse, HttpResponseForbidden

from account.forms import RegisterUserForm
from account.models import UserProfileModel

# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
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
