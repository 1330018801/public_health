from django.conf.urls import patterns, url
from services import views

urlpatterns = patterns('',
    #url(r'^grid/$', views.service_grid, name='service_grid'),
    url(r'^service_grid/$', views.service_grid, name='service_grid'),
    url(r'^reading_card/$', views.reading_card, name='reading_card'),  # for AJAX
    url(r'^test_card/$', views.test_card, name='test_card'),
    url(r'^mobile_submit/$', views.mobile_submit, name='mobile_submit'),
    url(r'^resident_chosen/$', views.resident_chosen, name='resident_chosen'),  # for AJAX
    url(r'^break_service/$', views.break_the_service, name='break_service'),
    url(r'^svc_nav/$', views.svc_nav, name='svc_nav'),
    url(r'^doc_nav/$', views.doc_nav, name='doc_nav'),
    url(r'^doc_workload/$', views.doc_workload_page, name='doc_workload_page'),
    url(r'^doc_workload_list/$', views.doc_workload_list, name='doc_workload_list'),
    url(r'^reading_card_new/$', views.reading_card_new, name='reading_card_new'),
    url(r'^quit_card/$', views.quit_card, name='quit_card'),
    url(r'^read_card/$', views.read_card, name='read_card'),
    url(r'^provide_service/$', views.provide_service, name='provide_service'),
)