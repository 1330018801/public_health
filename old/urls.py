# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .forms import *
from services.views import service_index, service_disposal
from ehr.forms import PhysicalExaminationForm, BloodRoutineTestForm, \
    UrineRoutineTestForm, BloodGlucoseForm, ElectrocardiogramForm, \
    AlanineAminotransferaseForm, GlutamicOxalaceticTransaminaseForm, \
    SerumCreatinineForm, BloodUreaNitrogenForm, BloodFatForm, TotalBilirubinForm, OldBodyCheckForm
from ehr.preview import PhyExamFormPreview

import views

urlpatterns = patterns('',
        url(r'^$', service_index, {'type_label': 'old'}, name='index'),
        url(r'^physical_examination/$', PhyExamFormPreview(PhysicalExaminationForm),
            {'type_alias': 'old', 'item_alias': 'physical_examination', 'model_name': 'PhysicalExamination'},
            name='physical_examination'),
        url(r'^electrocardiogram/$', PhyExamFormPreview(ElectrocardiogramForm),
            {'type_alias': 'old', 'item_alias': 'electrocardiogram', 'model_name': 'Electrocardiogram'},
            name='electrocardiogram'),
        url(r'^blood_routine_test/$', PhyExamFormPreview(BloodRoutineTestForm),
            {'type_alias': 'old', 'item_alias': 'blood_routine_test', 'model_name': 'BloodRoutineTest'},
            name='blood_routine_test'),
        url(r'^urine_routine_test/$', PhyExamFormPreview(UrineRoutineTestForm),
            {'type_alias': 'old', 'item_alias': 'urine_routine_test', 'model_name': 'UrineRoutineTest'},
            name='urine_routine_test'),
        url(r'^blood_glucose/$', PhyExamFormPreview(BloodGlucoseForm),
            {'type_alias': 'old', 'item_alias': 'blood_glucose', 'model_name': 'BloodGlucose'},
            name='blood_glucose'),
        url(r'^blood_fat/$', PhyExamFormPreview(BloodFatForm),
            {'type_alias': 'old', 'item_alias': 'blood_fat', 'model_name': 'BloodFat'},
            name='blood_fat'),
        url(r'^glutamic_oxalacetic_transaminase/$', PhyExamFormPreview(GlutamicOxalaceticTransaminaseForm),
            {'type_alias': 'old', 'item_alias': 'glutamic_oxalacetic_transaminase', 'model_name': 'GlutamicOxalaceticTransaminase'},
            name='glutamic_oxalacetic_transaminase'),
        url(r'^alanine_aminotransferase/$', PhyExamFormPreview(AlanineAminotransferaseForm),
            {'type_alias': 'old', 'item_alias': 'alanine_aminotransferase', 'model_name': 'AlanineAminotransferase'},
            name='alanine_aminotransferase'),
        url(r'^total_bilirubin/$', PhyExamFormPreview(TotalBilirubinForm),
            {'type_alias': 'old', 'item_alias': 'total_bilirubin', 'model_name': 'TotalBilirubin'},
            name='total_bilirubin'),
        url(r'^serum_creatinine/$', PhyExamFormPreview(SerumCreatinineForm),
            {'type_alias': 'old', 'item_alias': 'serum_creatinine', 'model_name': 'SerumCreatinine'},
            name='serum_creatinine'),
        url(r'^blood_urea_nitrogen/$', PhyExamFormPreview(BloodUreaNitrogenForm),
            {'type_alias': 'old', 'item_alias': 'blood_urea_nitrogen', 'model_name': 'BloodUreaNitrogen'},
            name='blood_urea_nitrogen'),

        # 老年人健康体检
        url(r'^body_check/$', PhyExamFormPreview(OldBodyCheckForm),
            {'type_alias': 'old', 'item_alias': 'body_check', 'model_name': 'OldBodyCheck'},
            name='old_body_check'),

        # 生活自理能力评估表
        url(r'^living_selfcare_appraisal/$', service_disposal,
            {'content_form': LivingSelfcareAppraisalForm, 'type_label': 'old', 'item_label': 'living_selfcare_appraisal'},
            name='living_selfcare_appraisal'),

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
