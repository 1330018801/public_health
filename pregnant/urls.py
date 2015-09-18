# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from pregnant import views

urlpatterns = patterns('',
    url(r'^aftercare_1_page/$', views.aftercare_1_page, name='aftercare_1'),
    url(r'^aftercare_1_submit/$', views.aftercare_1_submit, name='aftercare_1_submit'),
    url(r'^aftercare_1_table/$', views.aftercare_1_table, name='aftercare_1_table'),
    url(r'^aftercare_1_suspend/$', views.aftercare_1_suspend, name='aftercare_1_suspend'),

    url(r'^aftercare_2_5_page/$', views.aftercare_2_5_page, name='aftercare_2_5'),
    url(r'^aftercare_2_5_review/$', views.aftercare_2_5_review, name='aftercare_2_5_review'),
    url(r'^aftercare_2_5_form/$', views.aftercare_2_5_form, name='aftercare_2_5_form'),
    url(r'^aftercare_2_5_submit/$', views.aftercare_2_5_submit, name='aftercare_2_5_submit'),

    url(r'^postpartum_visit/$', views.postpartum_visit, name='postpartum_visit'),
    url(r'^postpartum_visit_table/$', views.postpartum_visit_table, name='postpartum_visit_table'),
    url(r'^postpartum_visit_submit/$', views.postpartum_visit_submit, name='postpartum_visit_submit'),

    url(r'^postpartum_42day/$', views.postpartum_42day, name='postpartum_42day'),
    url(r'^postpartum_42day_table/$', views.postpartum_42day_table, name='postpartum_42day_table'),
    url(r'^postpartum_42day_submit/$', views.postpartum_42day_submit, name='postpartum_42day_submit'),

)
