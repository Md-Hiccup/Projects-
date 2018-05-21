from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup,  name='signup'),
    url(r'^profile_edit/(?P<pk>[0-9]+)/$', views.edit_profile, name='profile_edit'),
    url(r'^password_change/$', views.change_password, name='change_password'),

    # url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
