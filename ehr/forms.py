# -*- coding: utf-8 -*-
from datetime import date

from django.forms import ModelForm, TextInput, RadioSelect, CheckboxSelectMultiple
from .models import *


# 个人基本信息表
class PersonalInfoForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'birthday': TextInput(attrs={'class': 'easyui-datebox',
                                         'data-options': 'formatter: myformatter, parser: myparser, '
                                                         'width: 100, required: true, editable: false'}),
            'identity': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 160, required: true'}),
            'work_company': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),
            'phone': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 100, required: true'}),
            'contact_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100, required: true'}),
            'contact_phone': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 100, required: true'}),

            'residence_type': RadioSelect,
            'nation': RadioSelect,
            'nation_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'blood_type': RadioSelect,
            'blood_rh': RadioSelect,
            'education': RadioSelect,
            'occupation': RadioSelect,
            'marriage': RadioSelect,
            'payment_way': CheckboxSelectMultiple,
            'payment_way_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 300'}),
            'allergy_history': CheckboxSelectMultiple,
            'allergy_history_yes_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),
            'expose_history': CheckboxSelectMultiple,
            'disease_history': CheckboxSelectMultiple,
            'disease_history_cancer': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'disease_history_occupational': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'disease_history_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'diagnose_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_3': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_4': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_5': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_6': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_7': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_8': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_9': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser, '
                                                                'width: 100, editable: false'}),
            'diagnose_date_10': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter: myformatter, parser: myparser, '
                                                                 'width: 100, editable: false'}),
            'diagnose_date_11': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter: myformatter, parser: myparser, '
                                                                 'width: 100, editable: false'}),
            'diagnose_date_12': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter: myformatter, parser: myparser, '
                                                                 'width: 100, editable: false'}),
            'diagnose_date_13': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter: myformatter, parser: myparser, '
                                                                 'width: 100, editable: false'}),

            'surgery_history': RadioSelect,
            'surgery_1_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'surgery_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                               'data-options': 'formatter: myformatter, parser: myparser, '
                                                               'width: 100, editable: false'}),
            'surgery_2_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'surgery_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                               'data-options': 'formatter: myformatter, parser: myparser, '
                                                               'width: 100, editable: false'}),
            'injury_history': RadioSelect,
            'injury_1_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'injury_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                              'data-options': 'formatter: myformatter, parser: myparser, '
                                                              'width: 100, editable: false'}),
            'injury_2_name': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'injury_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                              'data-options': 'formatter: myformatter, parser: myparser, '
                                                              'width: 100, editable: false'}),
            'transfusion_history': RadioSelect,
            'transfusion_1_reason': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'transfusion_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                                   'data-options': 'formatter: myformatter, parser: myparser, '
                                                                   'width: 100, editable: false'}),
            'transfusion_2_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'transfusion_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                                   'data-options': 'formatter: myformatter, parser: myparser, '
                                                                   'width: 100, editable: false'}),
            'family_history_father': CheckboxSelectMultiple,
            'family_history_father_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'family_history_mother': CheckboxSelectMultiple,
            'family_history_mother_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'family_history_sibling': CheckboxSelectMultiple,
            'family_history_sibling_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'family_history_children': CheckboxSelectMultiple,
            'family_history_children_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),

            'genetic_disease': RadioSelect,
            'genetic_disease_yes': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),
            'disability': CheckboxSelectMultiple,
            'disability_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'surroundings_kitchen_exhaust': RadioSelect,
            'surroundings_fuel_type': RadioSelect,
            'surroundings_water': RadioSelect,
            'surroundings_toilet': RadioSelect,
            'surrounding_livestock_fence': RadioSelect,
        }


# 一般体格检查：主要用于验证提交的内容是否完整，可以算作一次工作量
class PhysicalExaminationForm(ModelForm):
    class Meta:
        model = PhysicalExamination
        alias = 'physical_examination'
        fields = '__all__'


# 血常规：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodRoutineTestForm(ModelForm):
    class Meta:
        model = BloodRoutineTest
        fields = '__all__'
        alias = 'blood_routine_test'


# 尿常规：主要用于验证提交的内容是否完整，可以算作一次工作量
class UrineRoutineTestForm(ModelForm):
    class Meta:
        model = UrineRoutineTest
        alias = 'urine_routine_test'
        fields = '__all__'


# 血糖：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodGlucoseForm(ModelForm):
    class Meta:
        model = BloodGlucose
        alias = 'blood_glucose'
        fields = '__all__'

    def clean(self):
        cleaned_data = super(BloodGlucoseForm, self).clean()
        if cleaned_data.get('blood_glucose_mmol') is None and cleaned_data.get('blood_glucose_mg') is None:
            msg = "请选填一类血糖值"
            self.add_error('blood_glucose_mmol', msg)


# 心电图：主要用于验证提交的内容是否完整，可以算作一次工作量
class ElectrocardiogramForm(ModelForm):
    class Meta:
        model = Electrocardiogram
        alias = 'electrocardiogram'
        fields = '__all__'


# 谷丙转氨酶：主要用于验证提交的内容是否完整，可以算作一次工作量
class AlanineAminotransferaseForm(ModelForm):
    class Meta:
        model = AlanineAminotransferase
        alias = 'alanine_aminotransferase'
        fields = '__all__'


# 谷草转氨酶：主要用于验证提交的内容是否完整，可以算作一次工作量
class GlutamicOxalaceticTransaminaseForm(ModelForm):
    class Meta:
        model = GlutamicOxalaceticTransaminase
        alias = 'glutamic_oxalacetic_transaminase'
        fields = '__all__'


# 血清肌酐：主要用于验证提交的内容是否完整，可以算作一次工作量
class SerumCreatinineForm(ModelForm):
    class Meta:
        model = SerumCreatinine
        alias = 'serum_creatinine'
        fields = '__all__'


# 血尿素氮：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodUreaNitrogenForm(ModelForm):
    class Meta:
        model = BloodUreaNitrogen
        alias = 'blood_urea_nitrogen'
        fields = '__all__'


# 总胆红素：主要用于验证提交的内容是否完整，可以算作一次工作量
class TotalBilirubinForm(ModelForm):
    class Meta:
        model = TotalBilirubin
        alias = 'total_bilirubin'
        fields = '__all__'


# 血脂：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodFatForm(ModelForm):
    class Meta:
        model = BloodFat
        alias = 'blood_fat'
        fields = '__all__'


# 彩超
class BUltrasonicForm(ModelForm):
    class Meta:
        model = BUltrasonic
        alias = 'b_ultrasonic'
        fields = '__all__'


# 中医体质辨识：主要用于验证提交的内容是否完整，可以算作一次工作量
class ConstitutionIdentificationForm(ModelForm):
    class Meta:
        model = ConstitutionIdentification
        alias = 'constitution_identification'
        fields = '__all__'


# 20150907，当前考虑用一个model来记录所有服务类型的体检数据，
# 一个人一年只能填写一张体检表

class BodyExamForm(ModelForm):

    class Meta:
        model = BodyExam
        alias = 'body_exam'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter, parser:myparser, '
                                                           'width: 100, required: true, editable: false'}),
            'doctor': TextInput(attrs={'class': 'easyui-textbox',
                                       'data-options': 'width: 100,required: true'}),
            'body_temperature': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'data-options': 'width:40, min: 20, max: 50, '
                                                                 'precision: 1, required: true'}),
            'pulse': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, min: 50, max: 150, required: true'}),
            'breath_frequency': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'data-options': 'width: 40, required: true'}),
            'blood_pressure_left_sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'}),
            'blood_pressure_left_dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'}),
            'blood_pressure_right_sbp': TextInput(attrs={'class': 'easyui-numberbox',
                                                         'data-options': 'width: 40, required: true'}),
            'blood_pressure_right_dbp': TextInput(attrs={'class': 'easyui-numberbox',
                                                         'data-options': 'width: 40, required: true'}),
            'height': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40,  precision: 1, required: true'}),
            #'height': TextInput(),
            'weight': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40,  precision: 1, required: true'}),
            'waistline': TextInput(attrs={'class': 'easyui-numberbox',
                                          'data-options': 'width: 40,  precision: 1, required: true'}),
            'body_mass_index': TextInput(attrs={'class': 'easyui-numberbox',
                                                'data-options': 'width: 40,  precision: 2, '
                                                                'required: true, editable: false'}),
            'mouth_lip': RadioSelect,
            'mouth_tooth': RadioSelect,
            'mouth_tooth_missing_upleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 20'}),
            'mouth_tooth_missing_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 20'}),
            'mouth_tooth_missing_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 20'}),
            'mouth_tooth_missing_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 20'}),
            'mouth_tooth_decayed_upleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 20'}),
            'mouth_tooth_decayed_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 20'}),
            'mouth_tooth_decayed_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 20'}),
            'mouth_tooth_decayed_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 20'}),
            'mouth_tooth_denture_upleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 20'}),
            'mouth_tooth_denture_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 20'}),
            'mouth_tooth_denture_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 20'}),
            'mouth_tooth_denture_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 20'}),
            'mouth_throat': RadioSelect,
            'eyesight_left': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 40, required: true, precision: 1'}),
            'eyesight_right': TextInput(attrs={'class': 'easyui-numberbox',
                                               'data-options': 'width: 40, required: true, precision: 1'}),
            'eyesight_left_rectified': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true, precision: 1'}),
            'eyesight_right_rectified': TextInput(attrs={'class': 'easyui-numberbox',
                                                         'data-options': 'width: 40, required: true, precision: 1'}),
            'hearing': RadioSelect,
            'movement_function': RadioSelect,
            'skin': RadioSelect,
            'skin_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'lymph_node': RadioSelect,
            'lymph_node_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'lung_barrel_chested': RadioSelect,
            'lung_breath_sound': RadioSelect,
            'lung_breath_sound_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'lung_rale': RadioSelect,
            'lung_rale_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'heart_rate': TextInput(attrs={'class': 'easyui-numberbox',
                                           'data-options': 'width: 40, min: 0, max: 150, required: true'}),
            'heart_rhythm': RadioSelect,
            'heart_noise': RadioSelect,
            'heart_noise_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'stomach_tenderness': RadioSelect,
            'stomach_tenderness_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'stomach_enclosed_mass': RadioSelect,
            'stomach_enclosed_mass_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'stomach_hepatomegaly': RadioSelect,
            'stomach_hepatomegaly_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'stomach_slenauxe': RadioSelect,
            'stomach_slenauxe_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'stomach_shifting_dullness': RadioSelect,
            'stomach_shifting_dullness_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                                'data-options': 'width: 80'}),

            # 血常规
            'hemoglobin': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, min: 0, '
                                                                                        'max: 300, precision: 1'}),
            'leucocyte': TextInput(attrs={'class': 'easyui-numberbox',
                                          'data-options': 'width: 40, min: 0, max: 20, precision: 1'}),
            'blood_platelets': TextInput(attrs={'class': 'easyui-numberbox',
                                                'data-options': 'width: 40, min: 0, max: 600, precision: 1'}),
            'blood_routine_test_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:200'}),

            # 尿常规
            'urine_protein': TextInput(attrs={'class': 'easyui-textbox',
                                              'data-options': 'width: 60, validType: "posNeg", required: true'}),
            'urine_glucose': TextInput(attrs={'class': 'easyui-textbox',
                                              'data-options': 'width: 60, validType: "posNeg", required: true'}),
            'ketone_bodies': TextInput(attrs={'class': 'easyui-textbox',
                                              'data-options': 'width: 60, validType: "posNeg", required: true'}),
            'occult_blood': TextInput(attrs={'class': 'easyui-textbox',
                                             'data-options': 'width: 60, validType: "posNeg", required: true'}),
            'routine_urine_test_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                         'data-options': 'width: 200'}),

            # 血糖
            'blood_glucose_mmol': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 60'}),
            'blood_glucose_mg': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 60'}),

            # 心电图
            'electr_gram': RadioSelect,
            'electr_gram_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            # 血清谷丙转氨酶
            'alt': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 60, precision: 1'}),

            # 血清谷草转氨酶
            'ast': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 60, precision: 1'}),

            # 总胆红素
            'tbil': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, min: 0, max: 30, precision: 1'}),

            # 血清肌酐
            'scr': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 200, precision: 1'}),

            # 血尿素氮
            'bun': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 15, precision: 1'}),

            # 血脂
            'tc': TextInput(attrs={'class': 'easyui-numberbox',
                                   'data-options': 'width: 40, min: 0, max: 15, precision: 1'}),
            'tg': TextInput(attrs={'class': 'easyui-numberbox',
                                   'data-options': 'width: 40, min: 0, max: 10, precision: 1'}),
            'ldl_c': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, min: 0, max: 10, precision: 1'}),
            'hdl_c': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, min: 0, max: 11, precision: 1'}),

            # 彩超
            'b_ultrasonic': TextInput(attrs={'class': 'easyui-textbox',
                                             'data-options': 'width: 500, required: true'}),

            # 中医体质辨识
            'pinghe': RadioSelect,      # 平和
            'qixu': RadioSelect,        # 气虚
            'yangxu': RadioSelect,      # 阳虚
            'yinxu': RadioSelect,       # 阴虚
            'tanshi': RadioSelect,      # 痰湿
            'shire': RadioSelect,       # 湿热
            'xueyu': RadioSelect,       # 血瘀
            'qiyu': RadioSelect,        # 气郁
            'tebing': RadioSelect,      # 特秉

        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(BodyExamForm, self).__init__(*args, **kwargs)