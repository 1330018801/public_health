# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^aftercare_page/$', views.aftercare_page, name='aftercare_page'),
    url(r'^aftercare_form/$', views.aftercare_form, name='aftercare_form'),
    url(r'^aftercare_submit/$', views.aftercare_submit, name='aftercare_submit'),
    url(r'^aftercare_review/$', views.aftercare_review, name='aftercare_review'),

    url(r'^body_exam_page/$', views.body_exam_page, name='body_exam_page'),
    url(r'^body_exam_form/$', views.body_exam_form, name='body_exam_form'),
    url(r'^body_exam_submit/$', views.body_exam_submit, name='body_exam_submit'),

)