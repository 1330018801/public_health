# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^old_identify_page/$', views.old_identify_page, name='old_identify_page'),
        url(r'^old_identify_form/$', views.old_identify_form, name='old_identify_form'),
        url(r'^old_identify_submit/$', views.old_identify_submit, name='old_identify_submit'),

        url(r'^child_page/$', views.child_page, name='child_page'),
        url(r'^child_form/$', views.child_form, name='child_form'),
        url(r'^child_review/$', views.child_review, name='child_review'),
        url(r'^child_submit/$', views.child_submit, name='child_submit'),

)