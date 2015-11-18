from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^$', 'public_health.views.login', name='login'),
                       url(r'^logout/$', 'public_health.views.logout', name='logout'),

                       url(r'^backend/', include('backend.urls', namespace='backend')),
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
