# -*- coding: utf-8 -*-

from django.utils import timezone
from django.forms import Form, ModelForm, TextInput, RadioSelect, \
    DateInput, Textarea, CheckboxSelectMultiple
from management.models import Resident
from .models import *


# 个人基本信息表
class PersonalInfoForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'birthday': TextInput(attrs={'class': 'easyui-datebox',
                                         'style': 'width: 100px',
                                         'data-options': 'formatter: myformatter,'
                                                         'parser: myparser'}),
            'identity': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 160px'}),
            'work_company': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 160px'}),
            'phone': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'contact_name': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'contact_phone': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'residence_type': RadioSelect,
            'nation': RadioSelect,
            'nation_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'blood_type': RadioSelect,
            'blood_rh': RadioSelect,
            'education': RadioSelect,
            'occupation': RadioSelect,
            'marriage': RadioSelect,
            'payment_way': CheckboxSelectMultiple,
            'payment_way_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'allergy_history': CheckboxSelectMultiple,
            'allergy_history_yes_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'expose_history': CheckboxSelectMultiple,
            'disease_history': CheckboxSelectMultiple,
            'disease_history_cancer': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'disease_history_occupational': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'disease_history_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'diagnose_date_2': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_3': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_4': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_5': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_6': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_7': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_8': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_9': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser',
                                                'style': 'width: 100px'}),
            'diagnose_date_10': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter:myformatter,parser:myparser',
                                                 'style': 'width: 100px'}),
            'diagnose_date_11': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter:myformatter,parser:myparser',
                                                 'style': 'width: 100px'}),
            'diagnose_date_12': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter:myformatter,parser:myparser',
                                                 'style': 'width: 100px'}),
            'diagnose_date_13': TextInput(attrs={'class': 'easyui-datebox',
                                                 'data-options': 'formatter:myformatter,parser:myparser',
                                                 'style': 'width: 100px'}),

            'surgery_history': RadioSelect,
            'surgery_1_name': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'surgery_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                               'data-options': 'formatter:myformatter,parser:myparser',
                                               'style': 'width: 100px'}),
            'surgery_2_name': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'surgery_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                               'data-options': 'formatter:myformatter,parser:myparser',
                                               'style': 'width: 100px'}),
            'injury_history': RadioSelect,
            'injury_1_name': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'injury_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                              'data-options': 'formatter:myformatter,parser:myparser',
                                              'style': 'width: 100px'}),
            'injury_2_name': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'injury_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                              'data-options': 'formatter:myformatter,parser:myparser',
                                              'style': 'width: 100px'}),
            'transfusion_history': RadioSelect,
            'transfusion_1_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'transfusion_1_date': TextInput(attrs={'class': 'easyui-datebox',
                                                   'data-options': 'formatter:myformatter,parser:myparser',
                                                   'style': 'width: 100px'}),
            'transfusion_2_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'}),
            'transfusion_2_date': TextInput(attrs={'class': 'easyui-datebox',
                                                   'data-options': 'formatter:myformatter,parser:myparser',
                                                   'style': 'width: 100px'}),
            'family_history_father': CheckboxSelectMultiple,
            'family_history_father_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'family_history_mother': CheckboxSelectMultiple,
            'family_history_mother_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'family_history_sibling': CheckboxSelectMultiple,
            'family_history_sibling_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'family_history_children': CheckboxSelectMultiple,
            'family_history_children_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),

            'genetic_disease': RadioSelect,
            'genetic_disease_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 120px'}),
            'disability': CheckboxSelectMultiple,
            'disability_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),

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
        widgets = {
            'body_temperature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'pulse': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'breath_frequency': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_left_sbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_left_dbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_right_sbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_right_dbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'waistline': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'body_mass_index': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'mouth_lip': RadioSelect,
            'mouth_tooth': RadioSelect,
            'mouth_tooth_missing_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_throat': RadioSelect,
            'eyesight_left': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_right': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_left_rectified': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_right_rectified': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'hearing': RadioSelect,
            'movement_function': RadioSelect,
            'skin': RadioSelect,
            'skin_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lymph_node': RadioSelect,
            'lymph_node_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lung_barrel_chested': RadioSelect,
            'lung_breath_sound': RadioSelect,
            'lung_breath_sound_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lung_rale': RadioSelect,
            'lung_rale_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'heart_rate': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_rhythm': RadioSelect,
            'heart_noise': RadioSelect,
            'heart_noise_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_tenderness': RadioSelect,
            'stomach_tenderness_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_enclosed_mass': RadioSelect,
            'stomach_enclosed_mass_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_hepatomegaly': RadioSelect,
            'stomach_hepatomegaly_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_slenauxe': RadioSelect,
            'stomach_slenauxe_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_shifting_dullness': RadioSelect,
            'stomach_shifting_dullness_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(PhysicalExaminationForm, self).clean()
        if cleaned_data.get('body_temperature') < 20 or cleaned_data.get('body_temperature') > 50:
            msg = "体温的合理范围在20-50℃"
            self.add_error('body_temperature', msg)
        if cleaned_data.get('pulse') < 50 or cleaned_data.get('pulse') > 150:
            msg = "脉率的合理范围在50-150次/分钟"
            self.add_error('pulse', msg)
        if cleaned_data.get('heart_rate') < 0 or cleaned_data.get('heart_rate') > 150:
            msg = "心率的合理范围在0-150次/分钟"
            self.add_error('heart_rate', msg)
    '''


# 血常规：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodRoutineTestForm(ModelForm):
    class Meta:
        model = BloodRoutineTest
        fields = '__all__'
        alias = 'blood_routine_test'
        widgets = {
            'hemoglobin': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'leucocyte': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_platelets': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_routine_test_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:150px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(BloodRoutineTestForm, self).clean()
        if cleaned_data.get('hemoglobin') < 0 or cleaned_data.get('hemoglobin') > 300:
            msg = "血红蛋白的合理范围值是0-300"
            self.add_error('hemoglobin', msg)
        if cleaned_data.get('leucocyte') < 0 or cleaned_data.get('leucocyte') > 20:
            msg = "白细胞的合理范围值是0-20"
            self.add_error('leucocyte', msg)
        if cleaned_data.get('blood_platelets') < 0 or cleaned_data.get('blood_platelets') > 600:
            msg = "血小板的合理范围值是0-600"
            self.add_error('blood_platelets', msg)
    '''


# 尿常规：主要用于验证提交的内容是否完整，可以算作一次工作量
class UrineRoutineTestForm(ModelForm):
    class Meta:
        model = UrineRoutineTest
        alias = 'urine_routine_test'
        fields = '__all__'
        widgets = {
            'urine_protein': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'urine_glucose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'ketone_bodies': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'occult_blood': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'routine_urine_test_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(UrineRoutineTestForm, self).clean()
        if cleaned_data.get('urine_protein') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿蛋白请填写：-, +, ++, +++, ++++"
            self.add_error('urine_protein', msg)
        if cleaned_data.get('urine_glucose') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿糖请填写：-, +, ++, +++, ++++"
            self.add_error('urine_glucose', msg)
        if cleaned_data.get('ketone_bodies') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿酮体请填写：-, +, ++, +++, ++++"
            self.add_error('ketone_bodies', msg)
        if cleaned_data.get('occult_blood') not in ['-', '+', '++', '+++', '++++']:
            msg = "尿潜血请填写：-, +, ++, +++, ++++"
            self.add_error('occult_blood', msg)
    '''


# 血糖：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodGlucoseForm(ModelForm):
    class Meta:
        model = BloodGlucose
        alias = 'blood_glucose'
        fields = '__all__'
        widgets = {
            'blood_glucose_mmol': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:60px'}),
            'blood_glucose_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:60px'}),
        }

    def clean(self):
        cleaned_data = super(BloodGlucoseForm, self).clean()
        if cleaned_data.get('blood_glucose_mmol') is None and cleaned_data.get('blood_glucose_mg') is None:
            msg = "请选填一类血糖值"
            self.add_error('alt', msg)


# 心电图：主要用于验证提交的内容是否完整，可以算作一次工作量
class ElectrocardiogramForm(ModelForm):
    class Meta:
        model = Electrocardiogram
        alias = 'electrocardiogram'
        fields = '__all__'
        widgets = {
            'electr_gram': RadioSelect,
            'electr_gram_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
        }


# 谷丙转氨酶：主要用于验证提交的内容是否完整，可以算作一次工作量
class AlanineAminotransferaseForm(ModelForm):
    class Meta:
        model = AlanineAminotransferase
        alias = 'alanine_aminotransferase'
        fields = '__all__'
        widgets = {
            'alt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(AlanineAminotransferaseForm, self).clean()
        if cleaned_data.get('alt') < 0 or cleaned_data.get('alt') > 60:
            msg = "血清谷丙转氨酶的合理范围是0-60"
            self.add_error('alt', msg)
    '''


# 谷草转氨酶：主要用于验证提交的内容是否完整，可以算作一次工作量
class GlutamicOxalaceticTransaminaseForm(ModelForm):
    class Meta:
        model = GlutamicOxalaceticTransaminase
        alias = 'glutamic_oxalacetic_transaminase'
        fields = '__all__'
        widgets = {
            'ast': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(GlutamicOxalaceticTransaminaseForm, self).clean()
        if cleaned_data.get('ast') < 0 or cleaned_data.get('ast') > 60:
            msg = "血清谷草转氨酶的合理范围是0-60"
            self.add_error('ast', msg)
    '''


# 血清肌酐：主要用于验证提交的内容是否完整，可以算作一次工作量
class SerumCreatinineForm(ModelForm):
    class Meta:
        model = SerumCreatinine
        alias = 'serum_creatinine'
        fields = '__all__'
        widgets = {
            'scr': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(SerumCreatinineForm, self).clean()
        if cleaned_data.get('scr') < 0 or cleaned_data.get('scr') > 200:
            msg = "血清肌酐的合理范围是0-200"
            self.add_error('scr', msg)
    '''


# 血尿素氮：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodUreaNitrogenForm(ModelForm):
    class Meta:
        model = BloodUreaNitrogen
        alias = 'blood_urea_nitrogen'
        fields = '__all__'
        widgets = {
            'bun': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(BloodUreaNitrogenForm, self).clean()
        if cleaned_data.get('bun') < 0 or cleaned_data.get('bun') > 15:
            msg = "血尿素氮的合理范围是0-15"
            self.add_error('bun', msg)
    '''


# 总胆红素：主要用于验证提交的内容是否完整，可以算作一次工作量
class TotalBilirubinForm(ModelForm):
    class Meta:
        model = TotalBilirubin
        alias = 'total_bilirubin'
        fields = '__all__'
        widgets = {
            'tbil': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(TotalBilirubinForm, self).clean()
        if cleaned_data.get('tbil') < 0 or cleaned_data.get('tbil') > 30:
            msg = "总胆红素的合理范围是0-30"
            self.add_error('tbil', msg)
    '''


# 血脂：主要用于验证提交的内容是否完整，可以算作一次工作量
class BloodFatForm(ModelForm):
    class Meta:
        model = BloodFat
        alias = 'blood_fat'
        fields = '__all__'
        widgets = {
            'tc': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'tg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'ldl_c': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'hdl_c': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
        }
    '''
    def clean(self):
        cleaned_data = super(BloodFatForm, self).clean()
        if cleaned_data.get('tc') < 0 or cleaned_data.get('tc') > 15:
            msg = "总胆固醇的合理范围是0-15"
            self.add_error('tc', msg)
        if cleaned_data.get('tg') < 0 or cleaned_data.get('tg') > 10:
            msg = "甘油三酯的合理范围是0-10"
            self.add_error('tg', msg)
        if cleaned_data.get('ldl_c') < 0 or cleaned_data.get('ldl_c') > 10:
            msg = "血清低密度脂蛋白胆固醇的合理范围是0-10"
            self.add_error('ldl_c', msg)
        if cleaned_data.get('hdl_c') < 0 or cleaned_data.get('hdl_c') > 11:
            msg = "血清高密度脂蛋白胆固醇的合理范围是0-11"
            self.add_error('hdl_c', msg)
    '''


# 中医体质辨识：主要用于验证提交的内容是否完整，可以算作一次工作量
class ConstitutionIdentificationForm(ModelForm):
    class Meta:
        model = ConstitutionIdentification
        alias = 'constitution_identification'
        fields = '__all__'
        widgets = {
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


'''
class CombinedFormBase(Form):
    form_classes = []

    def __init__(self, *args, **kwargs):
        super(CombinedFormBase, self).__init__(*args, **kwargs)
        for f in self.form_classes:
            name = f.__name__.lower()
            setattr(self, name, f(*args, **kwargs))
            form = getattr(self, name)
            self.fields.update(form.fields)
            self.initial.update(form.initial)

    def is_valid(self):
        isValid = True
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            if not form.is_valid():
                isValid = False

        if not super(CombinedFormBase, self).is_valid():
            isValid = False
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            self.errors.update(form.errors)
        return isValid

    def clean(self):
        cleaned_data = super(CombinedFormBase, self).clean()
        for f in self.form_classes:
            name = f.__name__.lower()
            form = getattr(self, name)
            cleaned_data.update(form.cleaned_data)
        return cleaned_data


class OldBodyCheckForm(CombinedFormBase):
    form_classes = [
        PhysicalExaminationForm, BloodRoutineTestForm, UrineRoutineTestForm, BloodGlucoseForm,
        ElectrocardiogramForm, AlanineAminotransferaseForm, GlutamicOxalaceticTransaminaseForm,
        SerumCreatinineForm, BloodUreaNitrogenForm, TotalBilirubinForm, BloodFatForm
    ]

    class Meta:
        alias = 'old_body_check'
'''


# 20150907，当前考虑用一个model来记录所有服务类型的体检数据，
# 一个人一年只能填写一张体检表

class BodyExamForm(ModelForm):

    class Meta:
        model = BodyExam
        alias = 'body_exam'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'body_temperature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'pulse': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'breath_frequency': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_left_sbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_left_dbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_right_sbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_pressure_right_dbp': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'waistline': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'body_mass_index': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'mouth_lip': RadioSelect,
            'mouth_tooth': RadioSelect,
            'mouth_tooth_missing_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_missing_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_decayed_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_upleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_bottomleft': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_upright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_tooth_denture_bottomright': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:20px'}),
            'mouth_throat': RadioSelect,
            'eyesight_left': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_right': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_left_rectified': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'eyesight_right_rectified': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'hearing': RadioSelect,
            'movement_function': RadioSelect,
            'skin': RadioSelect,
            'skin_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lymph_node': RadioSelect,
            'lymph_node_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lung_barrel_chested': RadioSelect,
            'lung_breath_sound': RadioSelect,
            'lung_breath_sound_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'lung_rale': RadioSelect,
            'lung_rale_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'heart_rate': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_rhythm': RadioSelect,
            'heart_noise': RadioSelect,
            'heart_noise_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_tenderness': RadioSelect,
            'stomach_tenderness_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_enclosed_mass': RadioSelect,
            'stomach_enclosed_mass_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_hepatomegaly': RadioSelect,
            'stomach_hepatomegaly_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_slenauxe': RadioSelect,
            'stomach_slenauxe_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'stomach_shifting_dullness': RadioSelect,
            'stomach_shifting_dullness_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),

            # 血常规
            'hemoglobin': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'leucocyte': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_platelets': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'blood_routine_test_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:150px'}),

            # 尿常规
            'urine_protein': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'urine_glucose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'ketone_bodies': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'occult_blood': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'routine_urine_test_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),

            # 血糖
            'blood_glucose_mmol': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:60px'}),
            'blood_glucose_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:60px'}),

            # 心电图
            'electr_gram': RadioSelect,
            'electr_gram_abnormal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),

            # 血清谷丙转氨酶
            'alt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

            # 血清谷草转氨酶
            'ast': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

            # 血清肌酐
            'scr': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

            # 血尿素氮
            'bun': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

            # 总胆红素
            'tbil': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

            # 血脂
            'tc': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'tg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'ldl_c': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'hdl_c': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),

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
    '''
    def clean(self):
        cleaned_data = super(BodyExamForm, self).clean()
        if cleaned_data.get('body_temperature') < 20 or cleaned_data.get('body_temperature') > 50:
            msg = "体温的合理范围在20-50℃"
            self.add_error('body_temperature', msg)
        if cleaned_data.get('pulse') < 50 or cleaned_data.get('pulse') > 150:
            msg = "脉率的合理范围在50-150次/分钟"
            self.add_error('pulse', msg)
        if cleaned_data.get('heart_rate') < 0 or cleaned_data.get('heart_rate') > 150:
            msg = "心率的合理范围在0-150次/分钟"
            self.add_error('heart_rate', msg)
        if cleaned_data.get('hemoglobin'):
            if cleaned_data.get('hemoglobin') < 0 or cleaned_data.get('hemoglobin') > 300:
                msg = "血红蛋白的合理范围值是0-300"
                self.add_error('hemoglobin', msg)
        if cleaned_data.get('leucocyte'):
            if cleaned_data.get('leucocyte') < 0 or cleaned_data.get('leucocyte') > 20:
                msg = "白细胞的合理范围值是0-20"
                self.add_error('leucocyte', msg)
        if cleaned_data.get('blood_platelets'):
            if cleaned_data.get('blood_platelets') < 0 or cleaned_data.get('blood_platelets') > 600:
                msg = "血小板的合理范围值是0-600"
                self.add_error('blood_platelets', msg)
        if cleaned_data.get('urine_protein'):
            if cleaned_data.get('urine_protein') not in ['-', '+', '++', '+++', '++++']:
                msg = "尿蛋白请填写：-, +, ++, +++, ++++"
                self.add_error('urine_protein', msg)
        if cleaned_data.get('urine_glucose'):
            if cleaned_data.get('urine_glucose') not in ['-', '+', '++', '+++', '++++']:
                msg = "尿糖请填写：-, +, ++, +++, ++++"
                self.add_error('urine_glucose', msg)
        if cleaned_data.get('ketone_bodies'):
            if cleaned_data.get('ketone_bodies') not in ['-', '+', '++', '+++', '++++']:
                msg = "尿酮体请填写：-, +, ++, +++, ++++"
                self.add_error('ketone_bodies', msg)
        if cleaned_data.get('occult_blood'):
            if cleaned_data.get('occult_blood') not in ['-', '+', '++', '+++', '++++']:
                msg = "尿潜血请填写：-, +, ++, +++, ++++"
                self.add_error('occult_blood', msg)
        if cleaned_data.get('alt'):
            if cleaned_data.get('alt') < 0 or cleaned_data.get('alt') > 60:
                msg = "血清谷丙转氨酶的合理范围是0-60"
                self.add_error('alt', msg)
        if cleaned_data.get('ast'):
            if cleaned_data.get('ast') < 0 or cleaned_data.get('ast') > 60:
                msg = "血清谷草转氨酶的合理范围是0-60"
                self.add_error('ast', msg)
        if cleaned_data.get('scr'):
            if cleaned_data.get('scr') < 0 or cleaned_data.get('scr') > 200:
                msg = "血清肌酐的合理范围是0-200"
                self.add_error('scr', msg)
        if cleaned_data.get('bun'):
            if cleaned_data.get('bun') < 0 or cleaned_data.get('bun') > 15:
                msg = "血尿素氮的合理范围是0-15"
                self.add_error('bun', msg)
        if cleaned_data.get('tbil'):
            if cleaned_data.get('tbil') < 0 or cleaned_data.get('tbil') > 30:
                msg = "总胆红素的合理范围是0-30"
                self.add_error('tbil', msg)
        if cleaned_data.get('tc'):
            if cleaned_data.get('tc') < 0 or cleaned_data.get('tc') > 15:
                msg = "总胆固醇的合理范围是0-15"
                self.add_error('tc', msg)
        if cleaned_data.get('tg'):
            if cleaned_data.get('tg') < 0 or cleaned_data.get('tg') > 10:
                msg = "甘油三酯的合理范围是0-10"
                self.add_error('tg', msg)
        if cleaned_data.get('ldl_c'):
            if cleaned_data.get('ldl_c') < 0 or cleaned_data.get('ldl_c') > 10:
                msg = "血清低密度脂蛋白胆固醇的合理范围是0-10"
                self.add_error('ldl_c', msg)
        if cleaned_data.get('hdl_c'):
            if cleaned_data.get('hdl_c') < 0 or cleaned_data.get('hdl_c') > 11:
                msg = "血清高密度脂蛋白胆固醇的合理范围是0-11"
                self.add_error('hdl_c', msg)
    '''