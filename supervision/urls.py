from django.conf.urls import patterns, url
from supervision import views

urlpatterns = patterns('',
    url(r'^inspection/$', views.inspection_page, name='inspection_page'),
    url(r'^inspection_list/$', views.inspection_list, name='inspection_list'),
    url(r'^inspection_add/$', views.inspection_add, name='inspection_add'),
    url(r'^inspection_del/$', views.inspection_del, name='inspection_del'),
    url(r'^info_report/$', views.info_report_page, name='info_report_page'),
    url(r'^info_report_list/$', views.info_report_list, name='info_report_list'),
    url(r'^info_report_add/$', views.info_report_add, name='info_report_add'),
    url(r'^info_report_del/$', views.info_report_del, name='info_report_del'),
)
