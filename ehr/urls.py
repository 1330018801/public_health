# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from ehr import views

urlpatterns = patterns('',
    url(r'^ehr_page/$', views.ehr_page, name='ehr_page'),
    url(r'^family_list/$', views.family_list, name='family_list'),
    url(r'^child_add_new/$', views.child_add_new, name='child_add_new'),
    url(r'^family_add_adult/$', views.family_add_adult, name='family_add_adult'),
    url(r'^family_add_adult_query/$', views.family_add_adult_query, name='family_add_adult_query'),
    url(r'^family_add_adult/$', views.family_add_adult, name='family_add_adult'),
    url(r'^family_member_rm/$', views.family_member_rm, name='family_member_rm'),
    url(r'^change_resident/$', views.change_resident, name='change_resident'),

    url(r'^personal_info_submit/$', views.personal_info_submit, name='personal_info_submit'),
    url(r'^personal_info_review/$', views.personal_info_review, name='personal_info_review'),

    url(r'^record_list/$', views.record_list, name='record_list'),
    url(r'^record_detail_review/$', views.record_detail_review, name='record_detail_review'),

    url(r'^body_exam_table/$', views.body_exam_table, name='body_exam_table'),
    url(r'^body_exam_submit/$', views.body_exam_submit, name='body_exam_submit'),

)
