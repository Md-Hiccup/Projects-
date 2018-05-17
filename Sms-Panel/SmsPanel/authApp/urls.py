from django.conf.urls import url

# from .views import SignUp
from . import views

urlpatterns = [
    # url(r'signup/', SignUp.as_view(), name='signup'),
    url(r'singup/', views.signup, name='signup'),
]
