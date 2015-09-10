# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from diabetes.preview import *

from services.views import service_index
from ehr.preview import PhyExamFormPreview
from ehr.forms import PhysicalExaminationForm
from .forms import Aftercare1Form, Aftercare2Form, Aftercare3Form, Aftercare4Form
import views

urlpatterns = patterns('',
    url(r'^$', service_index, {'type_label': 'diabetes'}, name='index'),
    url(r'^physical_examination/$', PhyExamFormPreview(PhysicalExaminationForm),
        {'type_alias': 'diabetes', 'item_alias': 'physical_examination', 'model_name': 'PhysicalExamination'},
        name='physical_examination'),
    #url(r'^aftercare_1/$', service_disposal,
    #    {'content_form': Aftercare1Form, 'type_label': 'diabetes', 'item_label': 'aftercare_1'},
    #    name='aftercare_1'),
    #url(r'^aftercare_2/$', service_disposal,
    #    {'content_form': Aftercare2Form, 'type_label': 'diabetes', 'item_label': 'aftercare_2'},
    #    name='aftercare_2'),
    #url(r'^aftercare_3/$', service_disposal,
    #    {'content_form': Aftercare3Form, 'type_label': 'diabetes', 'item_label': 'aftercare_3'},
    #    name='aftercare_3'),
    #url(r'^aftercare_4/$', service_disposal,
    #    {'content_form': Aftercare4Form, 'type_label': 'diabetes', 'item_label': 'aftercare_4'},
    #    name='aftercare_4'),
    url(r'^aftercare_1/$', Aftercare1FormPreview(Aftercare1Form), name='aftercare_1'),
    url(r'^aftercare_2/$', Aftercare2FormPreview(Aftercare2Form), name='aftercare_2'),
    url(r'^aftercare_3/$', Aftercare3FormPreview(Aftercare3Form), name='aftercare_3'),
    url(r'^aftercare_4/$', Aftercare4FormPreview(Aftercare4Form), name='aftercare_4'),

    url(r'^aftercare_page/$', views.aftercare_page, name='aftercare_page'),
    url(r'^aftercare_form/$', views.aftercare_form, name='aftercare_form'),
    url(r'^aftercare_submit/$', views.aftercare_submit, name='aftercare_submit'),
    url(r'^aftercare_review/$', views.aftercare_review, name='aftercare_review'),

    url(r'^body_exam_page/$', views.body_exam_page, name='body_exam_page'),
    url(r'^body_exam_form/$', views.body_exam_form, name='body_exam_form'),
    url(r'^body_exam_submit/$', views.body_exam_submit, name='body_exam_submit'),

)