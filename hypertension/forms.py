from datetime import date, timedelta

from django.forms import TextInput, RadioSelect, ModelForm, CheckboxSelectMultiple, DateInput, Textarea

from .models import *
from .models import Aftercare


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'},),
            'visit_way':  RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox',
                                             'data-options': 'multiline: true',
                                             'style': 'width: 128px; height: 50px'},),
            'sign_blood_pressure':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_heart_rhythm': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_salt': RadioSelect,
            'life_style_guide_salt_next': RadioSelect,
            'life_style_guide_mentality':  RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                                     'style': 'width: 128px; height: 100px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'take_medicine_3_day':TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_qt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'take_medicine_qt_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'take_medicine_qt_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 30px'}),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, '
                                                                'parser: myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},)
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)


class Aftercare2Form(ModelForm):
    class Meta:
        model = Aftercare2
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'},),
            'visit_way':  RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 128px; height: 100px'},),
            'sign_blood_pressure':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_heart_rhythm': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_salt': RadioSelect,
            'life_style_guide_salt_next': RadioSelect,
            'life_style_guide_mentality':  RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                     'style': 'width: 128px; height: 100px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_3_day':TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_qt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_qt_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_qt_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'},)
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare2Form, self).__init__(*args, **kwargs)


class Aftercare3Form(ModelForm):
    class Meta:
        model = Aftercare3
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'},),
            'visit_way':  RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                     'style': 'width: 128px; height: 100px'},),
            'sign_blood_pressure':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_heart_rhythm': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_salt': RadioSelect,
            'life_style_guide_salt_next': RadioSelect,
            'life_style_guide_mentality':  RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                     'style': 'width: 128px; height: 100px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_3_day':TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_qt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_qt_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_qt_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'},)
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare3Form, self).__init__(*args, **kwargs)


class Aftercare4Form(ModelForm):
    class Meta:
        model = Aftercare4
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'},),
            'visit_way':  RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 128px; height: 100px'},),
            'sign_blood_pressure':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_weight_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_bmi_next':  TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_heart_rhythm': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'life_style_guide_salt': RadioSelect,
            'life_style_guide_salt_next': RadioSelect,
            'life_style_guide_mentality':  RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
                                     'style': 'width: 128px; height: 100px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_3_day':TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_medicine_qt': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'take_medicine_qt_day': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'take_medicine_qt_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'},),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'},)
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare4Form, self).__init__(*args, **kwargs)