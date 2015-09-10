from django.conf.urls import patterns, url
#from pregnant import views
from .forms import *
from services.views import service_index, service_disposal
from .preview import *
from pregnant import views

urlpatterns = patterns('',
    url(r'^$', service_index, {'type_label': 'pregnant'}, name='index'),
    url(r'^physical_examination/$', Aftercare1FormPreview(PhysicalExaminationForm),
        {'item_alias': 'physical_examination', 'model_name': 'PhysicalExamination'},
        name='physical_examination'),
    url(r'^gynaecological_examination/$', Aftercare1FormPreview(GynaecologicalExaminationForm),
        {'item_alias': 'gynaecological_examination', 'model_name': 'GynaecologicalExamination'},
        name='gynaecological_examination'),
    url(r'^blood_routine_test/$', Aftercare1FormPreview(BloodRoutineTestForm),
        {'item_alias': 'blood_routine_test', 'model_name': 'BloodRoutineTest'},
        name='blood_routine_test'),
    url(r'^urine_routine_test/$', Aftercare1FormPreview(UrineRoutineTestForm),
        {'item_alias': 'urine_routine_test', 'model_name': 'UrineRoutineTest'},
        name='urine_routine_test'),
    url(r'^blood_type/$', Aftercare1FormPreview(BloodTypeForm),
        {'item_alias': 'blood_type', 'model_name': 'BloodType'},
        name='blood_type'),
    url(r'^glutamic_oxalacetic_transaminase/$', Aftercare1FormPreview(GlutamicOxalaceticTransaminaseForm),
        {'item_alias': 'glutamic_oxalacetic_transaminase', 'model_name': 'GlutamicOxalaceticTransaminase'},
        name='glutamic_oxalacetic_transaminase'),
    url(r'^alanine_aminotransferase/$', Aftercare1FormPreview(AlanineAminotransferaseForm),
        {'item_alias': 'alanine_aminotransferase', 'model_name': 'AlanineAminotransferase'},
        name='alanine_aminotransferase'),
    url(r'^serum_creatinine/$', Aftercare1FormPreview(SerumCreatinineForm),
        {'item_alias': 'serum_creatinine', 'model_name': 'SerumCreatinine'},
        name='serum_creatinine'),
    url(r'^blood_urea_nitrogen/$', Aftercare1FormPreview(BloodUreaNitrogenForm),
        {'item_alias': 'blood_urea_nitrogen', 'model_name': 'BloodUreaNitrogen'},
        name='blood_urea_nitrogen'),
    url(r'^hepatitis_b_five_item/$', Aftercare1FormPreview(HepatitisBFiveItemForm),
        {'item_alias': 'hepatitis_b_five_item', 'model_name': 'HepatitisBFiveItem'},
        name='hepatitis_b_five_item'),
    url(r'^total_bilirubin/$', Aftercare1FormPreview(TotalBilirubinForm),
        {'item_alias': 'total_bilirubin', 'model_name': 'TotalBilirubin'},
        name='total_bilirubin'),

    url(r'^aftercare_1/$', Aftercare1FormPreview(Aftercare1Form), name='aftercare_1'),
    url(r'^aftercare_2/$', Aftercare2FormPreview(Aftercare2Form), name='aftercare_2'),
    url(r'^aftercare_3/$', Aftercare3FormPreview(Aftercare3Form), name='aftercare_3'),
    url(r'^aftercare_4/$', Aftercare4FormPreview(Aftercare4Form), name='aftercare_4'),
    url(r'^aftercare_5/$', Aftercare5FormPreview(Aftercare5Form), name='aftercare_5'),
    # url(r'^postpartum_visit/$', PostpartumVisitFromPreview(PostpartumVisitForm), name='post_visit'),
    url(r'^postpartum_42_day_examination/$', Postpartum42ExamFormPreview(Postpartum42ExamForm), name='post42_visit'),
    
    url(r'^aftercare_1_page/$', views.aftercare_1_page, name='pregnant_aftercare_1'),
    url(r'^aftercare_1_submit/$', views.aftercare_1_submit, name='pregnant_aftercare_1_submit'),
    url(r'^aftercare_1_review/$', views.aftercare_1_review, name='pregnant_aftercare_1_review'),

    url(r'^aftercare_2_5_page/$', views.aftercare_2_5_page, name='pregnant_aftercare_2_5'),
    url(r'^aftercare_2_5_review/$', views.aftercare_2_5_review, name='pregnant_aftercare_2_5_review'),
    url(r'^aftercare_2_5_form/$', views.aftercare_2_5_form, name='pregnant_aftercare_2_5_form'),
    url(r'^aftercare_2_5_submit/$', views.aftercare_2_5_submit, name='pregnant_aftercare_2_5_submit'),

    url(r'^postpartum_visit/$', views.postpartum_visit, name='pregnant_postpartum_visit'),
    url(r'^postpartum_visit_review/$', views.postpartum_visit_review, name='pregnant_postpartum_visit_review'),
    url(r'^postpartum_visit_submit/$', views.postpartum_visit_submit, name='pregnant_postpartum_visit_submit'),

    url(r'^postpartum_42day/$', views.postpartum_42day, name='pregnant_postpartum_42day'),
    url(r'^postpartum_42day_review/$', views.postpartum_42day_review, name='pregnant_postpartum_42day_review'),
    url(r'^postpartum_42day_submit/$', views.postpartum_42day_submit, name='pregnant_postpartum_42day_submit'),
    
)
