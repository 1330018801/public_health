# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from psychiatric import views

urlpatterns = patterns('',
    url(r'^aftercare_page/$', views.aftercare_page, name='aftercare_page'),
    url(r'^aftercare_form/$', views.aftercare_form, name='aftercare_form'),
    url(r'^aftercare_submit/$', views.aftercare_submit, name='aftercare_submit'),
    url(r'^aftercare_review/$', views.aftercare_review, name='aftercare_review'),

    url(r'^personal_info_page/$', views.personal_info_page, name='personal_info_page'),
    url(r'^personal_info_table/$', views.personal_info_table, name='personal_info_table'),
    url(r'^personal_info_submit/$', views.personal_info_submit, name='personal_info_submit'),

    url(r'^body_exam_page/$', views.body_exam_page, name='body_exam_page'),
    url(r'^body_exam_form/$', views.body_exam_form, name='body_exam_form'),
    url(r'^body_exam_submit/$', views.body_exam_submit, name='body_exam_submit'),

)
