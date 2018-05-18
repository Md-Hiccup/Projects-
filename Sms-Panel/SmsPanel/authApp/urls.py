from django.conf.urls import url

from .views import RegisterUserView
# from . import views

urlpatterns = [
    url(r'signup/', RegisterUserView.as_view(), name='signup'),
    # url(r'singup/', views.signup, name='signup'),
]
