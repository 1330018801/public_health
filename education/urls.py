from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^activity/$', views.activity_page, name='activity_page'),
    url(r'^activity_table/$', views.activity_table, name='activity_table'),
    url(r'^activity_list/$', views.activity_list, name='activity_list'),
    url(r'^activity_review/$', views.activity_review, name='activity_review'),
)
