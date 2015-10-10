# -*- coding:utf8 -*-

from django.forms import ModelForm, TextInput, RadioSelect, Textarea, CheckboxSelectMultiple
from datetime import date, timedelta
from .models import *


# 一般体格检查
class PhyExamAbstractForm(ModelForm):
    class Meta:
        model = PhyExamAbstract
        alias = 'physical_examination'
        fields = '__all__'


# 妇科检查
class GynaecologicalExaminationForm(ModelForm):
    class Meta:
        model = GynaecologicalExamination
        fields = '__all__'


# 血常规
class BloodRoutineTestForm(ModelForm):
    class Meta:
        model = BloodRoutineTest
        alias = 'blood_routine_test'
        fields = '__all__'
    '''
    def clean(self):
        cleaned_data = super(BloodRoutineTestForm, self).clean()
        if cleaned_data.get('hemoglobin') < 0 or cleaned_data.get('hemoglobin') > 300:
            msg = ""
            self.add_error('hemoglobin', msg)
        if cleaned_data.get('leukocyte') < 0 or cleaned_data.get('leukocyte') > 20:
            msg = ""
            self.add_error('leukocyte', msg)
        if cleaned_data.get('thrombocyte') < 0 or cleaned_data.get('thrombocyte') > 600:
            msg = ""
            self.add_error('thrombocyte', msg)
    '''


# 尿常规
class UrineRoutineTestForm(ModelForm):
    class Meta:
        model = UrineRoutineTest
        alias = 'urine_routine_test'
        fields = '__all__'
    '''
    def clean(self):
        cleaned_data = super(UrineRoutineTestForm, self).clean()
        if cleaned_data.get('urine_protein') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿蛋白的合理取值是：-, + , ++, +++, ++++"
            self.add_error('urine_protein', msg)
        if cleaned_data.get('urine_glucose') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿糖的合理取值是：-, + , ++, +++, ++++"
            self.add_error('urine_glucose', msg)
        if cleaned_data.get('urine_ket') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿糖的合理取值是：-, + , ++, +++, ++++"
            self.add_error('urine_ket', msg)
        if cleaned_data.get('urine_ery') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿酮体的合理取值是：-, + , ++, +++, ++++"
            self.add_error('urine_ery', msg)
    '''


# 血型
class BloodTypeForm(ModelForm):
    class Meta:
        model = BloodType
        alias = 'blood_type'
        fields = '__all__'


# 谷丙转氨酶
class AlanineAminotransferaseForm(ModelForm):
    class Meta:
        model = AlanineAminotransferase
        alias = 'alanine_aminotransferase'
        fields = '__all__'
    '''
    def clean(self):
        cleaned_data = super(AlanineAminotransferaseForm, self).clean()
        if cleaned_data.get('sgpt') < 0 or cleaned_data.get('sgpt') > 60:
            msg = "谷丙转氨酶的合理取值范围是0-60"
            self.add_error('sgpt', msg)
    '''


# 谷草转氨酶
class GlutamicOxalaceticTransaminaseForm(ModelForm):
    class Meta:
        model = GlutamicOxalaceticTransaminase
        alias = 'glutamic_oxalacetic_transaminase'
        fields = '__all__'
    '''
    def clean(self):
        cleaned_data = super(GlutamicOxalaceticTransaminaseForm, self).clean()
        if cleaned_data.get('sgot') < 0 or cleaned_data.get('sgot') > 60:
            msg = "谷草转氨酶的合理取值范围是0-60"
            self.add_error('sgot', msg)
    '''


# 总胆红素
class TotalBilirubinForm(ModelForm):
    class Meta:
        model = TotalBilirubin
        alias = 'total_bilirubin'
        fields = '__all__'

    '''
    def clean(self):
        cleaned_data = super(TotalBilirubinForm, self).clean()
        if cleaned_data.get('tbil') < 0 or cleaned_data.get('tbil') > 30:
            msg = "总胆红素的合理取值范围是0-30"
            self.add_error('tbil', msg)
    '''


# 血清肌酐
class SerumCreatinineForm(ModelForm):
    class Meta:
        model = SerumCreatinine
        alias = 'serum_creatinine'
        fields = '__all__'

    '''
    def clean(self):
        cleaned_data = super(SerumCreatinineForm, self).clean()
        if cleaned_data.get('scr') < 0 or cleaned_data.get('scr') > 200:
            msg = "血清肌酐的合理取值范围是0-200"
            self.add_error('scr', msg)
    '''


# 血尿素氮
class BloodUreaNitrogenForm(ModelForm):
    class Meta:
        model = BloodUreaNitrogen
        alias = 'blood_urea_nitrogen'
        fields = '__all__'

    '''
    def clean(self):
        cleaned_data = super(BloodUreaNitrogenForm, self).clean()
        if cleaned_data.get('bun') < 0 or cleaned_data.get('bun') > 15:
            msg = "血尿素氮的合理取值范围是0-15"
            self.add_error('bun', msg)
    '''


# 乙型肝炎五项
class HepatitisBFiveItemForm(ModelForm):
    class Meta:
        model = HepatitisBFiveItem
        alias = 'hepatitis_b_five_item'
        fields = '__all__'


class Aftercare1Form(ModelForm):
    class Meta:
        model = Aftercare1
        alias = 'aftercare_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter,'
                                                           'parser: myparser, '
                                                           'width: 100,'
                                                           'required: true, '
                                                           'editable: false'}),
            'weeks': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, '
                                                      'required: true'}),
            'age': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, '
                                                    'required: true'}),
            'husband_name': TextInput(attrs={'class': 'easyui-textbox',
                                             'data-options': 'width: 70, '
                                                      'required: true'}),
            'husband_age': TextInput(attrs={'class': 'easyui-numberbox',
                                            'data-options': 'width: 40,'
                                                            'required: true'}),
            'husband_phone': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 120,'
                                                              'required: true'}),
            'pregnant_times': TextInput(attrs={'class': 'easyui-numberbox',
                                               'data-options': 'width: 40,'
                                                               'required: true'}),
            'natural_production': TextInput(attrs={'class': 'easyui-numberbox',
                                                   'data-options': 'width: 40,'
                                                                   'required: true'}),
            'surgery_production': TextInput(attrs={'class': 'easyui-numberbox',
                                                   'data-options': 'width: 40,'
                                                                   'required: true'}),
            'last_menstruation': TextInput(attrs={'class': 'easyui-datebox',
                                                  'data-options': 'formatter: myformatter, '
                                                                  'parser: myparser, '
                                                                  'width: 100, '
                                                                  'required: true,'
                                                                  'editable: false'}),
            'due_date': TextInput(attrs={'class': 'easyui-datebox',
                                         'data-options': 'formatter: myformatter, '
                                                         'parser: myparser, '
                                                         'width: 100, '
                                                         'required: true,'
                                                         'editable: false'}),
            'disease_history': CheckboxSelectMultiple,
            'disease_history_other': TextInput(attrs={'class': 'easyui-textbox',
                                                      'data-options': 'width: 150'}),
            'family_history': CheckboxSelectMultiple,
            'family_history_other': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'personal_history': CheckboxSelectMultiple,
            'personal_history_other': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'gynaecology_surgery_history': RadioSelect,
            'gynaecology_surgery_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'miscarriage': TextInput(attrs={'class': 'easyui-numberbox',
                                            'data-options': 'width: 40,'
                                                            'required: true'}),
            'dead_fetus': TextInput(attrs={'class': 'easyui-numberbox',
                                           'data-options': 'width: 40,'
                                                           'required: true'}),
            'still_birth': TextInput(attrs={'class': 'easyui-numberbox',
                                            'data-options': 'width: 40,'
                                                            'required: true'}),
            'newnatal_death': TextInput(attrs={'class': 'easyui-numberbox',
                                               'data-options': 'width: 40,'
                                                               'required: true'}),
            'birth_defect': TextInput(attrs={'class': 'easyui-numberbox',
                                             'data-options': 'width: 40, '
                                                      'required: true'}),
            'height': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40, precision: 1,'
                                                       'required: true'}),
            'weight': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40, precision: 1,'
                                                       'required: true'}),
            'bmi': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, precision: 2,'
                                                    'required: true'}),
            'sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,'
                                                    'required: true'}),
            'dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,'
                                                    'required: true'}),
            'ausculate_heart': RadioSelect,
            'ausculate_heart_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                         'data-options': 'width: 90'}),
            'ausculate_lung': RadioSelect,
            'ausculate_lung_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                        'data-options': 'width: 90'}),
            'vulva': RadioSelect,
            'vulva_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                               'data-options': 'width: 90'}),
            'vagina': RadioSelect,
            'vagina_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 90'}),
            'cervix': RadioSelect,
            'cervix_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 90'}),
            'uteri': RadioSelect,
            'uteri_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                               'data-options': 'width: 90'}),
            'accessory': RadioSelect,
            'accessory_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                   'data-options': 'width: 90'}),
            'leukocyte': TextInput(attrs={'class': 'easyui-numberbox',
                                          'data-options': 'width: 40, min: 0, max: 20, precision: 1'}),
            'hemoglobin': TextInput(attrs={'class': 'easyui-numberbox',
                                           'data-options': 'width: 40, min: 0, max: 300, precision: 1'}),
            'thrombocyte': TextInput(attrs={'class': 'easyui-numberbox',
                                            'data-options': 'width: 40, min: 0, max: 600, precision: 1'}),
            'blood_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 40'}),
            'urine_protein': TextInput(attrs={"class": "easyui-textbox",
                                              'data-options': 'width: 40, validType:"posNeg"'}),
            'urine_glucose': TextInput(attrs={'class': 'easyui-textbox',
                                              'data-options': 'width: 40, validType: "posNeg"'}),
            'urine_ket': TextInput(attrs={'class': 'easyui-textbox',
                                          'data-options': 'width: 40, validType: "posNeg"'}),
            'urine_ery': TextInput(attrs={'class': 'easyui-textbox',
                                          'data-options': 'width: 40, validType: "posNeg"'}),
            'urine_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 40'}),
            'blood_type_abo': RadioSelect,
            'blood_type_abo_other': TextInput(attrs={'class': 'easyui-textbox',
                                                     'data-options': 'width: 80'}),
            'blood_type_rh': RadioSelect,
            'blood_glucose': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 40, precision: 1'}),
            'sgpt': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, min: 0, max: 60, precision: 1'}),
            'sgot': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, min: 0, max: 60, precision: 1'}),
            'albumin': TextInput(attrs={'class': 'easyui-numberbox',
                                        'data-options': 'width: 40, precision: 1'}),
            'tbil': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, min: 0, max: 30, precision: 1'}),
            'dbil': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, precision: 1'}),
            'scr': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 200, precision: 1'}),
            'bun': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 15, precision: 1'}),
            'vaginal_secretion': RadioSelect,
            'vaginal_secretion_other': TextInput(attrs={'class': 'easyui-textbox',
                                                        'data-options': 'width: 80'}),
            'vaginal_clean_degree': RadioSelect,
            'surface_antigen': RadioSelect,
            'surface_antibody': RadioSelect,
            'e_antigen': RadioSelect,
            'e_antibody': RadioSelect,
            'core_antibody': RadioSelect,
            'vdrl': RadioSelect,
            'hiv_antibody': RadioSelect,
            'b_scan': TextInput(attrs={'class': 'easyui-textbox',
                                       'data-options': 'width: 80'}),
            'total_evaluation': RadioSelect,
            'total_evaluation_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                          'data-options': 'width: 150'}),
            'guide': CheckboxSelectMultiple,
            'guide_other': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 100'}),
            'transfer': RadioSelect,
            'transfer_reason': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 120'}),
            'transfer_hospital': TextInput(attrs={'class': 'easyui-textbox',
                                                  'data-options': 'width: 120'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, '
                                                                'parser: myparser, '
                                                                'width: 100,'
                                                                'required: true, '
                                                                'editable: false'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'data-options': 'width: 100,'
                                                                 'required: true'}),
        }

    def __init__(self, *args, **kwargs):
        if 'instance' not in kwargs:
            initial = kwargs.get('initial', {})
            visit_date = date.today()
            next_visit_date = date.today() + timedelta(days=28)
            initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
            initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
            kwargs['initial'] = initial

        super(Aftercare1Form, self).__init__(*args, **kwargs)


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter,'
                                                           'parser: myparser,'
                                                           'width: 100, '
                                                           'required: true, '
                                                           'editable: false'}),
            'gestational_weeks': TextInput(attrs={'class': 'easyui-numberbox',
                                                  'data-options': 'width: 40, required: true,'}, ),
            'complaint': Textarea(attrs={'class': 'easyui-textbox',
                                         'data-options': 'multiline:true, '
                                                         'width: 128, '
                                                         'height: 100, '
                                                         'required: true'}),
            'weight': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40, precision: 1, required: true'}, ),
            'examination_before_parturition_uteri_bottom_height': TextInput(
                attrs={'class': 'easyui-numberbox',
                       'data-options': 'width: 40, precision: 1, required: true'}, ),
            'examination_before_parturition_abdomen_circumference': TextInput(
                attrs={'class': 'easyui-numberbox',
                       'data-options': 'width: 40, precision: 1, required: true'}, ),
            'examination_before_parturition_fetus_position': TextInput(
                attrs={'class': 'easyui-textbox',
                       'data-options': 'width: 128, required: true'}, ),
            'examination_before_parturition_fetal_heart_rate': TextInput(
                attrs={'class': 'easyui-numberbox',
                       'data-options': 'width: 40, '
                                       'min: 90,'
                                       'max: 200,'
                                       'required: true'}, ),
            'sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, required: true'}),
            'dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, required: true'}),
            'hemoglobin': TextInput(attrs={'class': 'easyui-numberbox',
                                           'data-options': 'width: 40, '
                                                           'min: 0, '
                                                           'max: 300, precision: 1,'
                                                           'required: true'}, ),
            'urine_protein': TextInput(attrs={'class': 'easyui-textbox',
                                              'data-options': 'width: 50, validType: "posNeg", required: true'}, ),
            'extra_auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox',
                                                           'data-options': 'multiline:true,'
                                                                           'width: 128,'
                                                                           ' height: 100'}),
            'classification': RadioSelect,
            'classification_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:80'}, ),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:80'}, ),
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:80'}, ),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:125'}, ),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,'
                                                                'parser:myparser,'
                                                                'width: 100, '
                                                                'required: true, '
                                                                'editable: false'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100, required: true'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        next_visit_date = date.today() + timedelta(days=63)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)

    '''
    def clean(self):
        cleaned_data = super(AftercareForm, self).clean()
        if cleaned_data.get('examination_before_parturition_fetal_heart_rate') < 90 or cleaned_data.get(
                'examination_before_parturition_fetal_heart_rate') > 200:
            msg = ""
            self.add_error('examination_before_parturition_fetal_heart_rate', msg)
        if cleaned_data.get('hemoglobin') < 0 or cleaned_data.get('hemoglobin') > 300:
            msg = ""
            self.add_error('hemoglobin', msg)
    '''


class PostpartumVisitForm(ModelForm):
    class Meta:
        model = PostpartumVisit
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter, '
                                                           'parser: myparser, '
                                                           'width: 100, '
                                                           'required: true, '
                                                           'editable: false'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser,'
                                                                'width: 100,'
                                                                'required: true,'
                                                                'editable: false'}),
            'breast': RadioSelect,
            'lochia': RadioSelect,
            'uterus': RadioSelect,
            'wound': RadioSelect,
            'classification': RadioSelect,
            'transfer_treatment': RadioSelect,
            'guide': CheckboxSelectMultiple,
            'body_temperature': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'data-options': 'width: 40, min: 20, max: 50, precision: 1,'
                                                                 'required: true'}),
            'sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,'
                                                    'required: true'}),
            'dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,'
                                                    'required: true'}),
            'general_health_situation': Textarea(attrs={'class': 'easyui-textbox',
                                                        'data-options': 'multiline:true,'
                                                                        'width: 550, '
                                                                        'height: 100,'
                                                                        'required: true'}),
            'general_mentality_situation': Textarea(attrs={'class': 'easyui-textbox',
                                                           'data-options': 'multiline:true,'
                                                                           'width: 550, '
                                                                           'height: 100,'
                                                                           'required: true'}),
            'extra': Textarea(attrs={'class': 'easyui-textbox',
                                     'data-options': 'multiline:true,'
                                                     'width: 550, '
                                                     'height: 100'}),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox',
                                                          'data-options': 'width: 200'}),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 200'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'data-options': 'width: 100,'
                                                                 'required: true'}),
            'classification_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                        'data-options': 'width: 300'}),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 150'}),
            'breast_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'lochia_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'uterus_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'wound_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                               'data-options': 'width: 300'}),

        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        next_visit_date = date.today() + timedelta(days=42)
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(PostpartumVisitForm, self).__init__(*args, **kwargs)


class Postpartum42ExamForm(ModelForm):
    class Meta:
        model = Postpartum42Exam
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter, '
                                                           'parser: myparser,'
                                                           'width: 100,'
                                                           'required: true,'
                                                           'editable: false'}),
            'general_health_situation': Textarea(attrs={'class': 'easyui-textbox',
                                                        'data-options': 'multiline:true,'
                                                                        'width: 550, '
                                                                        'height:100,'
                                                                        'required: true'}),
            'general_mentality_situation': Textarea(attrs={'class': 'easyui-textbox',
                                                           'data-options': 'multiline:true,'
                                                                           'width: 550,'
                                                                           'height:100,'
                                                                           'required: true'}),
            'sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,'
                                                    'required: true'}),
            'dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40,,'
                                                    'required: true'}),
            'breast': RadioSelect,
            'breast_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'lochia': RadioSelect,
            'lochia_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'uterus': RadioSelect,
            'uterus_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                'data-options': 'width: 300'}),
            'wound': RadioSelect,
            'wound_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                               'data-options': 'width: 300'}),
            'extra': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                     'style': 'width: 550px; height: 100px'}),
            'classification': RadioSelect,
            'classification_not_recovery': TextInput(attrs={'class': 'easyui-textbox',
                                                            'data-options': 'width: 300'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 150'}),
            'dispose': RadioSelect,
            'dispose_transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox',
                                                                  'data-options': 'width: 200'}),
            'dispose_transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox',
                                                                       'data-options': 'width: 200'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'data-options': 'width: 100,'
                                                                 'required: true'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Postpartum42ExamForm, self).__init__(*args, **kwargs)