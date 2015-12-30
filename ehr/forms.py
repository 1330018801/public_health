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
                                                           'data-options': 'width: 50'}),
            'mouth_tooth_missing_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 50'}),
            'mouth_tooth_missing_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 50'}),
            'mouth_tooth_missing_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 50'}),
            'mouth_tooth_decayed_upleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 50'}),
            'mouth_tooth_decayed_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 50'}),
            'mouth_tooth_decayed_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 50'}),
            'mouth_tooth_decayed_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 50'}),
            'mouth_tooth_denture_upleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 50'}),
            'mouth_tooth_denture_bottomleft': TextInput(attrs={'class': 'easyui-numberbox',
                                                               'data-options': 'width: 50'}),
            'mouth_tooth_denture_upright': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 50'}),
            'mouth_tooth_denture_bottomright': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 50'}),
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

            # B超
            'b_ultrasonic': RadioSelect,
            'b_ultrasonic_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

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

            #一般状况
            'old_health_situation_appraisal': RadioSelect,
            'old_living_selfcare_appraisal': TextInput,

            #生活方式

            #体育锻炼
            'exercise_rate': RadioSelect,
            'exercise_time': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 40, min: 0'}),
            'exercise_years': TextInput(attrs={'class': 'easyui-numberbox',
                                               'data-options': 'width: 40, min: 0, precision: 1'}),
            'exercise_way': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 370'}),

            #饮食习惯
            'diet_habit': CheckboxSelectMultiple,

            #吸烟情况
            'smoke_situation': RadioSelect,
            'smoke_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, min: 0'}),
            'smoke_begin_age': TextInput(attrs={'class': 'easyui-numberbox',
                                                'data-options': 'width: 40, min: 0, precision: 1'}),
            'smoke_cessation_age': TextInput(attrs={'class': 'easyui-numberbox',
                                                'data-options': 'width: 40, min: 0, precision: 1'}),

            #饮酒情况
            'liquor_rate': RadioSelect,
            'liquor_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, min: 0'}),
            'liquor_cessation': RadioSelect,
            'liquor_cessation_age': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 40, min: 0, precision: 1'}),
            'liquor_begin_age': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'data-options': 'width: 40, min: 0, precision: 1'}),
            'liquor_drunkenness': RadioSelect,
            'liquor_kind': CheckboxSelectMultiple,
            'liquor_kind_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 60'}),

            #职业病危害因素接触史
            'occupational_disease_yes_or_not': RadioSelect,
            'occupational_disease_profession': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 60'}),
            'occupational_disease_employment': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width: 40, min: 0, precision: 1'}),
            'occupational_disease_dust': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'occupational_disease_dust_safeguard': RadioSelect,
            'occupational_disease_dust_yes': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),

            'occupational_disease_radioactive': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'occupational_disease_radioactive_safeguard': RadioSelect,
            'occupational_disease_radioactive_yes': TextInput(attrs={'class': 'easyui-textbox',
                                                                     'data-options': 'width: 150'}),

            'occupational_disease_physical': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'occupational_disease_physical_safeguard': RadioSelect,
            'occupational_disease_physical_yes': TextInput(attrs={'class': 'easyui-textbox',
                                                                  'data-options': 'width: 150'}),

            'occupational_disease_chemical': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'occupational_disease_chemical_safeguard': RadioSelect,
            'occupational_disease_chemical_yes': TextInput(attrs={'class': 'easyui-textbox',
                                                                  'data-options': 'width: 150'}),

            'occupational_disease_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100'}),
            'occupational_disease_extra_safeguard': RadioSelect,
            'occupational_disease_extra_yes': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 150'}),

            #查体
            'legs_edema': RadioSelect,
            'acrotarsium_artery_pulse': RadioSelect,

            #辅助检查
            #尿微量白蛋白
            'urine_microalbumin': TextInput(attrs={'class': 'easyui-numberbox',
                                                   'data-options': 'width: 100, min: 0, precision: 2'}),
            'fecal_occult_blood': RadioSelect,

            #糖化血红蛋白
            'glycosylated_hemoglobin': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 100, min: 0, precision: 2'}),

            #乙型肝炎表面抗原
            'hepatitis_b_surface_antigen': RadioSelect,

            #肝功能（增加）
            'albumin': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 60, min: 0, precision: 2'}),
            'conjugated_bilirubin': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 60, min: 0, precision: 2'}),

            #肾功能（增加）
            'blood_potassium_concentration': TextInput(attrs={'class': 'easyui-numberbox',
                                                              'data-options': 'width: 60, min: 0, precision: 2'}),
            'blood_sodium_concentration': TextInput(attrs={'class': 'easyui-numberbox',
                                                           'data-options': 'width: 60, min: 0, precision: 2'}),

            #胸部X线片
            'chest_x_ray': RadioSelect,
            'chest_x_ray_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            #宫颈涂片
            'cervical_smear': RadioSelect,
            'cervical_smear_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            #其他
            'extra': TextInput(attrs={'class': 'easyui-textbox',
                                      'data-options': 'multiline: true, width: 500, height: 50'}),

            #现存主要健康问题
            'cerebrovascular': CheckboxSelectMultiple,
            'cerebrovascular_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'kidney': CheckboxSelectMultiple,
            'kidney_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'cardiac': CheckboxSelectMultiple,
            'cardiac_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'vessel': CheckboxSelectMultiple,
            'vessel_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'eye': CheckboxSelectMultiple,
            'eye_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'nervous_system': RadioSelect,
            'nervous_system_yes': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            'extra_system': RadioSelect,
            'extra_system_yes': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 200'}),

            #住院治疗情况
            #住院史
            'hospitalization_history_in_date_1': TextInput(attrs={'class': 'easyui-datebox',
                                                                  'data-options': 'formatter: myformatter, '
                                                                                  'paser: myparser, '
                                                                                  'width: 85, editable: false'}),
            'hospitalization_history_out_date_1': TextInput(attrs={'class': 'easyui-datebox',
                                                                   'data-options': 'formatter: myformatter, '
                                                                                   'paser: myparser,'
                                                                                   'width: 85, editable: false'}),
            'hospitalization_history_reason_1': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'data-options': 'width: 91'}),
            'hospitalization_history_medical_institution_1': TextInput(attrs={'class': 'easyui-textbox',
                                                                              'data-options': 'width: 180'}),
            'hospitalization_history_case_number_1': TextInput(attrs={'class': 'easyui-textbox',
                                                                      'data-options': 'width: 91'}),


            'hospitalization_history_in_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                                  'data-options': 'formatter: myformatter, '
                                                                                  'paser: myparser, '
                                                                                  'width: 85, editable: false'}),
            'hospitalization_history_out_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                                   'data-options': 'formatter: myformatter, '
                                                                                   'paser: myparser,'
                                                                                   'width: 85, editable: false'}),
            'hospitalization_history_reason_2': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'data-options': 'width: 91'}),
            'hospitalization_history_medical_institution_2': TextInput(attrs={'class': 'easyui-textbox',
                                                                              'data-options': 'width: 180'}),
            'hospitalization_history_case_number_2': TextInput(attrs={'class': 'easyui-textbox',
                                                                      'data-options': 'width: 91'}),

            #家庭病床史
            'family_bed_history_build_date_1': TextInput(attrs={'class': 'easyui-datebox',
                                                                'data-options': 'formatter: myformatter,'
                                                                                'paser: myparser,'
                                                                                'width: 85, editable: false'}),
            'family_bed_history_remove_date_1': TextInput(attrs={'class': 'easyui-datebox',
                                                                 'data-options': 'formatter: myformatter,'
                                                                                 'paser: myparser,'
                                                                                 'width: 85, editable: false'}),
            'family_bed_history_reason_1': TextInput(attrs={'class': 'easyui-textbox',
                                                            'data-options': 'width: 91'}),
            'family_bed_history_medical_institution_1': TextInput(attrs={'class': 'easyui-textbox',
                                                                         'data-options': 'width: 180'}),
            'family_bed_history_case_number_1': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'data-options': 'width: 91'}),


            'family_bed_history_build_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                                'data-options': 'formatter: myformatter,'
                                                                                'paser: myparser,'
                                                                                'width: 85, editable: false'}),
            'family_bed_history_remove_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                                 'data-options': 'formatter: myformatter,'
                                                                                 'paser: myparser,'
                                                                                 'width: 85, editable: false'}),
            'family_bed_history_reason_2': TextInput(attrs={'class': 'easyui-textbox',
                                                            'data-options': 'width: 91'}),
            'family_bed_history_medical_institution_2': TextInput(attrs={'class': 'easyui-textbox',
                                                                         'data-options': 'width: 180'}),
            'family_bed_history_case_number_2': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'data-options': 'width: 91'}),

            #主要用药情况
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_1_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_1_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_1_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_1_take_medicine_compliance': RadioSelect,

            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_2_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_2_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_2_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_2_take_medicine_compliance': RadioSelect,

            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_3_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_3_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_3_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_3_take_medicine_compliance': RadioSelect,

            'take_medicine_4': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_4_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_4_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_4_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_4_take_medicine_compliance': RadioSelect,

            'take_medicine_5': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_5_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_5_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_5_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_5_take_medicine_compliance': RadioSelect,

            'take_medicine_6': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_6_method': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_6_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'take_medicine_6_period': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 182'}),
            'take_medicine_6_take_medicine_compliance': RadioSelect,

            #非免疫规划预防接种史
            'vaccine_name_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'vaccine_date_1': TextInput(attrs={'class': 'easyui-datebox', 'data-options': 'width: 100, '
                                                                                          'formatter: myformatter, '
                                                                                          'parser: myparser, '
                                                                                          'editable: false'}),
            'vaccine_institution_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 370'}),

            'vaccine_name_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'vaccine_date_2': TextInput(attrs={'class': 'easyui-datebox', 'data-options': 'width: 100, '
                                                                                          'formatter: myformatter, '
                                                                                          'parser: myparser, '
                                                                                          'editable: false'}),
            'vaccine_institution_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 370'}),

            'vaccine_name_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 90'}),
            'vaccine_date_3': TextInput(attrs={'class': 'easyui-datebox', 'data-options': 'width: 100, '
                                                                                          'formatter: myformatter, '
                                                                                          'parser: myparser, '
                                                                                          'editable: false'}),
            'vaccine_institution_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 370'}),

            #健康评价
            'normal_or_abnormal': RadioSelect,
            'abnormal_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 500'}),
            'abnormal_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 500'}),
            'abnormal_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 500'}),
            'abnormal_4': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 500'}),

            #健康指导
            'health_guide': CheckboxSelectMultiple,
            'dangerous_factor_control': CheckboxSelectMultiple,
            'lose_weight': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'vaccinate_suggestion': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 150'}),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 202'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(BodyExamForm, self).__init__(*args, **kwargs)