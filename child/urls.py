from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^newborn_visit_page/$', views.newborn_visit_page, name='newborn_visit_page'),
        url(r'^newborn_visit_submit/$', views.newborn_visit_submit, name='newborn_visit_submit'),
        url(r'^newborn_visit_table/$', views.newborn_visit_table, name='newborn_visit_table'),

        url(r'^health_0_1_page/$', views.health_0_1_page, name='health_0_1_page'),
        url(r'^health_0_1_review/$', views.health_0_1_review, name='health_0_1_review'),
        url(r'^health_0_1_form/$', views.health_0_1_form, name='health_0_1_form'),
        url(r'^health_0_1_submit/$', views.health_0_1_submit, name='health_0_1_submit'),

        url(r'^health_1_2_page/$', views.health_1_2_page, name='health_1_2_page'),
        url(r'^health_1_2_review/$', views.health_1_2_review, name='health_1_2_review'),
        url(r'^health_1_2_form/$', views.health_1_2_form, name='health_1_2_form'),
        url(r'^health_1_2_submit/$', views.health_1_2_submit, name='health_1_2_submit'),

        url(r'^health_3_6_page/$', views.health_3_6_page, name='health_3_6_page'),
        url(r'^health_3_6_review/$', views.health_3_6_review, name='health_3_6_review'),
        url(r'^health_3_6_form/$', views.health_3_6_form, name='health_3_6_form'),
        url(r'^health_3_6_submit/$', views.health_3_6_submit, name='health_3_6_submit'),
)