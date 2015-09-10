from django.conf.urls import patterns, url
from supervision import views
from supervision.forms import PatrolForm, InformationReportForm
from supervision.preview import PatrolFormPreview, InformationReportFormPreview

__author__ = 'Administrator'

urlpatterns = patterns('',
    url(r'^patrol/$', PatrolFormPreview(PatrolForm), name='patrol'),
    url(r'^information_report/$', InformationReportFormPreview(InformationReportForm), name='information_report'),
    url(r'patrol/(?P<year>\d+)/former_records/$', views.get_former_records, name='get_former_records'),
    url(r'^inspection/$', views.inspection_page, name='inspection_page'),
    url(r'^inspection_list/$', views.inspection_list, name='inspection_list'),
    url(r'^inspection_add/$', views.inspection_add, name='inspection_add'),
    url(r'^inspection_del/$', views.inspection_del, name='inspection_del'),
    url(r'^info_report/$', views.info_report_page, name='info_report_page'),
    url(r'^info_report_list/$', views.info_report_list, name='info_report_list'),
    url(r'^info_report_add/$', views.info_report_add, name='info_report_add'),
    url(r'^info_report_del/$', views.info_report_del, name='info_report_del'),
)
