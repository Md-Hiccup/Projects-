from django.conf.urls import url

from .views import signup, edit_profile

urlpatterns = [
    url(r'^signup/$', signup,  name='signup'),
    url(r'^profile_edit/(?P<pk>[0-9]+)/$', edit_profile, name='profile_edit'),
]
