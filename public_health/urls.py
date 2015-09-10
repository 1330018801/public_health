from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'public_health.views.login', name='home'),
                       url(r'^logout/$', 'public_health.views.logout', name='logout'),
                       url(r'^logout_new/$', 'public_health.views.logout_new', name='logout_new'),
                       url(r'^admin_new/$', 'public_health.views.admin_new', name='admin_new'),

                       url(r'^management/', include('management.urls', namespace='management')),
                       url(r'^services/', include('services.urls', namespace='services')),
                       url(r'^hypertension/', include('hypertension.urls', namespace='hypertension')),
                       url(r'^diabetes/', include('diabetes.urls', namespace='diabetes')),
                       url(r'^vaccine/', include('vaccine.urls', namespace='vaccine')),
                       url(r'^child/', include('child.urls', namespace='child')),
                       url(r'^old/', include('old.urls', namespace='old')),
                       url(r'^tcm/', include('tcm.urls', namespace='tcm')),
                       url(r'^psychiatric/', include('psychiatric.urls', namespace='psychiatric')),
                       url(r'^pregnant/', include('pregnant.urls', namespace='pregnant')),
                       url(r'^ehr/', include('ehr.urls', namespace='ehr')),
                       url(r'^education/', include('education.urls', namespace='education')),
                       url(r'^supervision/', include('supervision.urls', namespace='supervision'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^test/$', 'public_health.views.test', name='test'),
        url(r'^test2/$', 'public_health.views.test2', name='test2'),
        url(r'^test3/$', 'public_health.views.test3', name='test3'),
        url(r'^test4/$', 'public_health.views.test4', name='test4'),
        url(r'^xhr_test/$', 'public_health.views.xhr_test', name='xhr_test'),
        url(r'^graphs/$', 'public_health.views.graphs', name='graphs'),
        url(r'^graph_clinics/$', 'public_health.views.graph_clinics', name='graph_clinics'),
    )
