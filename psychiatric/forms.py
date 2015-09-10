# -*- coding: utf-8 -*-

from datetime import date, timedelta
from django.forms import ModelForm, TextInput, RadioSelect, DateInput, CheckboxSelectMultiple
from psychiatric.models import *


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)


class Aftercare1Form(ModelForm):
    class Meta:
        model = Aftercare1
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare1Form, self).__init__(*args, **kwargs)


class Aftercare2Form(ModelForm):
    class Meta:
        model = Aftercare2
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare2Form, self).__init__(*args, **kwargs)


class Aftercare3Form(ModelForm):
    class Meta:
        model = Aftercare3
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare3Form, self).__init__(*args, **kwargs)


class Aftercare4Form(ModelForm):
    class Meta:
        model = Aftercare4
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare4Form, self).__init__(*args, **kwargs)


class Aftercare5Form(ModelForm):
    class Meta:
        model = Aftercare5
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare5Form, self).__init__(*args, **kwargs)


class Aftercare6Form(ModelForm):
    class Meta:
        model = Aftercare6
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare6Form, self).__init__(*args, **kwargs)


class Aftercare7Form(ModelForm):
    class Meta:
        model = Aftercare7
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare7Form, self).__init__(*args, **kwargs)


class Aftercare8Form(ModelForm):
    class Meta:
        model = Aftercare8
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'laboratory_examination': RadioSelect,
            'laboratory_examination_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'treatment_effect': RadioSelect,
            'transfer_treatment': RadioSelect,
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'},),
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_1_per': RadioSelect,
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_1_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_2_per': RadioSelect,
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_2_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'take_medicine_3_per': RadioSelect,
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'take_medicine_3_mg': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'},),
            'recovery_measure': CheckboxSelectMultiple,
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare8Form, self).__init__(*args, **kwargs)
