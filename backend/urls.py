from django.conf.urls import patterns, url
from backend import views


urlpatterns = patterns('',
                       url(r'^users/$', views.users),
                       url(r'^login/$', views.login),
                       url(r'^register/$', views.register),
                       url(r'^personal_info/$', views.personal_info),
                       url(r'^summarys/$', views.service_list),
                       url(r'^detail/$', views.record_detail),
)