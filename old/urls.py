# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^body_exam_page/$', views.body_exam_page, name='body_exam_page'),
    url(r'^body_exam_form/$', views.body_exam_form, name='body_exam_form'),
    url(r'^body_exam_submit/$', views.body_exam_submit, name='body_exam_submit'),

    url(r'^living_selfcare_appraisal_page/$', views.living_selfcare_appraisal_page,
        name='living_selfcare_appraisal_page'),
    url(r'^living_selfcare_appraisal_review/$', views.living_selfcare_appraisal_review,
        name='living_selfcare_appraisal_review'),
    url(r'^living_selfcare_appraisal_submit/$', views.living_selfcare_appraisal_submit,
        name='living_selfcare_appraisal_submit'),
)
