# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^vaccine_page/$', views.vaccine_page, name='vaccine_page'),
    url(r'^vaccine_records/$', views.vaccine_records, name='vaccine_records'),
    url(r'^vaccine_card_head/$', views.vaccine_card_head, name='vaccine_card_head'),
    url(r"^vaccine_card_head_save/$", views.vaccine_card_head_save, name='vaccine_card_head_save'),
    url(r"^vaccinate_submit/$", views.vaccinate_submit, name='vaccinate_submit'),

)



