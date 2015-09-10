# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from services.views import service_index, service_disposal
from ehr.forms import ConstitutionIdentificationForm
from ehr.preview import PhyExamFormPreview
from .forms import *
from .preview import ChildAftercareFromPreview
import views

urlpatterns = patterns('',
        url(r'^$', service_index, {'type_label': 'tcm'}, name='index'),
        url(r'^constitution_identification/$', PhyExamFormPreview(ConstitutionIdentificationForm),
            {'type_alias': 'tcm','item_alias': 'constitution_identification', 'model_name': 'ConstitutionIdentification'},
            name='constitution_identification'),
        #url(r'^aftercare_3_year/$', service_disposal,
        #    {'content_form': Aftercare3YearForm, 'type_label': 'tcm', 'item_label': 'aftercare_3_year'},
        #    name='aftercare_3_year'),
        #url(r'^aftercare_30_month/$', service_disposal,
        #    {'content_form': Aftercare30MonthForm, 'type_label': 'tcm', 'item_label': 'aftercare_30_month'},
        #    name='aftercare_30_month'),
        #url(r'^aftercare_24_month/$', service_disposal,
        #    {'content_form': Aftercare24MonthForm, 'type_label': 'tcm', 'item_label': 'aftercare_24_month'},
        #    name='aftercare_24_month'),
        #url(r'^aftercare_18_month/$', service_disposal,
        #    {'content_form': Aftercare18MonthForm, 'type_label': 'tcm', 'item_label': 'aftercare_18_month'},
        #    name='aftercare_18_month'),
        #url(r'^aftercare_12_month/$', service_disposal,
        #    {'content_form': Aftercare12MonthForm, 'type_label': 'tcm', 'item_label': 'aftercare_12_month'},
        #    name='aftercare_12_month'),

        url(r'^aftercare_6_month/$', ChildAftercareFromPreview(Aftercare6MonthForm),
            {'item_alias': 'aftercare_6_month', 'model_name': 'Aftercare6Month'},
            name='aftercare_6_month'),
        url(r'^aftercare_12_month/$', ChildAftercareFromPreview(Aftercare12MonthForm),
            {'item_alias': 'aftercare_12_month', 'model_name': 'Aftercare12Month'},
            name='aftercare_12_month'),
        url(r'^aftercare_18_month/$', ChildAftercareFromPreview(Aftercare18MonthForm),
            {'item_alias': 'aftercare_18_month', 'model_name': 'Aftercare18Month'},
            name='aftercare_18_month'),
        url(r'^aftercare_24_month/$', ChildAftercareFromPreview(Aftercare24MonthForm),
            {'item_alias': 'aftercare_24_month', 'model_name': 'Aftercare24Month'},
            name='aftercare_24_month'),
        url(r'^aftercare_30_month/$', ChildAftercareFromPreview(Aftercare30MonthForm),
            {'item_alias': 'aftercare_30_month', 'model_name': 'Aftercare30Month'},
            name='aftercare_30_month'),
        url(r'^aftercare_3_year/$', ChildAftercareFromPreview(Aftercare3YearForm),
            {'item_alias': 'aftercare_3_year', 'model_name': 'Aftercare3Year'},
            name='aftercare_3_year'),

        #url(r'^aftercare_6_month/$', service_disposal,
        #    {'content_form': Aftercare6MonthForm, 'type_label': 'tcm', 'item_label': 'aftercare_6_month'},
        #    name='aftercare_6_month'),
        url(r'^old_identify_page/$', views.old_identify_page, name='old_identify_page'),
        url(r'^old_identify_form/$', views.old_identify_form, name='old_identify_form'),
        url(r'^old_identify_submit/$', views.old_identify_submit, name='old_identify_submit'),

        url(r'^child_page/$', views.child_page, name='child_page'),
        url(r'^child_form/$', views.child_form, name='child_form'),
        url(r'^child_review/$', views.child_review, name='child_review'),
        url(r'^child_submit/$', views.child_submit, name='child_submit'),

)