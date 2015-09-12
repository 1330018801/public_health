# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.utils import timezone
from django.forms import ModelForm, TextInput, RadioSelect, CheckboxSelectMultiple, Textarea
from psychiatric.models import Aftercare, PsychiatricInfo


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter,'
                                                           'parser: myparser,'
                                                           'width: 100'}),
            'dangerousness': RadioSelect,
            'now_symptom': CheckboxSelectMultiple,
            'now_symptom_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width: 60px'},),
            'insight': RadioSelect,
            'sleep_situation': RadioSelect,
            'diet_situation': RadioSelect,
            'society_function_individual_life_care': RadioSelect,
            'society_function_housework': RadioSelect,
            'society_function_productive_work': RadioSelect,
            'society_function_learn_ability': RadioSelect,
            'society_function_social_interpersonal': RadioSelect,
            'disease_family_society_effect_mild_disturbance': TextInput(attrs={'class': 'easyui-textbox',
                                                                               'style': 'width: 40px'},),
            'disease_family_society_effect_disturbance': TextInput(attrs={'class': 'easyui-textbox',
                                                                          'style': 'width: 40px'},),
            'disease_family_society_effect_accident': TextInput(attrs={'class': 'easyui-textbox',
                                                                       'style': 'width: 40px'},),
            'disease_family_society_effect_autolesion': TextInput(attrs={'class': 'easyui-textbox',
                                                                         'style': 'width: 40px'},),
            'disease_family_society_effect_attempted_suicide': TextInput(attrs={'class': 'easyui-textbox',
                                                                                'style': 'width: 40px'},),
            'disease_family_society_effect_nothing': TextInput(attrs={'class': 'easyui-textbox',
                                                                      'style': 'width: 40px'},),
            'lock_situation': RadioSelect,
            'hospitalized_situation': RadioSelect,
            'last_hospitalized_date': TextInput(attrs={'class': 'easyui-datebox',
                                                       'data-options': 'formatter: myformatter,'
                                                                       'parser: myparser,'
                                                                       'width: 100'}),
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
            'recovery_measure_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                       'style': 'width: 100px'},),
            'visit_classification': RadioSelect,
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser,'
                                                                'width: 100'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 100px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=45)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)


# 重性精神疾病患者信息补充表
class PsychiatricInfoForm(ModelForm):
    class Meta:
        model = PsychiatricInfo
        fields = '__all__'
        widgets = {
            'guardian_name': TextInput(attrs={'class': 'easyui-textbox',
                                              'style': 'width: 80px',
                                              'data-options': 'required: true'}),
            'guardian_relation': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width: 120px',
                                                  'data-options': 'required: true'}),
            'guardian_address': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 150px',
                                                 'data-options': 'required: true'}),
            'guardian_phone': TextInput(attrs={'class': 'easyui-textbox',
                                               'style': 'width: 120px',
                                               'data-options': 'required: true'}),
            'community_contact_name': TextInput(attrs={'class': 'easyui-textbox',
                                                       'style': 'width: 80px',
                                                       'data-options': 'required: true'}),
            'community_contact_phone': TextInput(attrs={'class': 'easyui-textbox',
                                                        'style': 'width: 120px',
                                                        'data-options': 'required: true'}),
            'assent': RadioSelect,
            'signature_date': TextInput(attrs={'class': 'easyui-datebox',
                                               'data-options': 'formatter: myformatter, '
                                                               'parser: myparser, '
                                                               'required: true, '
                                                               'editable: false, '
                                                               'width: 100'}),
            'disease_begin_date': TextInput(attrs={'class': 'easyui-datebox',
                                                   'data-options': 'formatter: myformatter,'
                                                                   'parser: myparser, '
                                                                   'required: true, '
                                                                   'editable: false,'
                                                                   'width: 100'}),
            'symptom': CheckboxSelectMultiple,
            'symptom_other': TextInput(attrs={'class': 'easyui-textbox',
                                              'style': 'width: 80px'}),
            'cure_outpatient': RadioSelect,
            'drug_first_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser, '
                                                                'required: true, '
                                                                'editable: false,'
                                                                'width: 100'}),
            'cure_hospital': TextInput(attrs={'class': 'easyui-numberbox',
                                              'style': 'width: 40px',
                                              'data-options': 'required: true'}),
            'diagnose': TextInput(attrs={'class': 'easyui-textbox',
                                         'style': 'width: 120px',
                                         'data-options': 'required: true'}),
            'diagnose_hospital': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width: 120px',
                                                  'data-options': 'required: true'}),
            'diagnose_date': TextInput(attrs={'class': 'easyui-datebox',
                                              'data-options': 'formatter: myformatter,'
                                                              'parser: myparser, '
                                                              'required: true, '
                                                              'editable: false,'
                                                              'width: 100'}),
            'cure_effect': RadioSelect,
            'social_effect_minor': TextInput(attrs={'class': 'easyui-numberbox',
                                                    'style': 'width: 40px',
                                                    'data-options': 'required: true'}),
            'social_effect_trouble': TextInput(attrs={'class': 'easyui-numberbox',
                                                      'style': 'width: 40px',
                                                      'data-options': 'required: true'}),
            'social_effect_disaster': TextInput(attrs={'class': 'easyui-numberbox',
                                                       'style': 'width: 40px',
                                                       'data-options': 'required: true'}),
            'social_effect_self_injury': TextInput(attrs={'class': 'easyui-numberbox',
                                                          'style': 'width: 40px',
                                                          'data-options': 'required: true'}),
            'social_effect_suicide': TextInput(attrs={'class': 'easyui-numberbox',
                                                      'style': 'width: 40px',
                                                      'data-options': 'required: true'}),
            'lock': RadioSelect,
            'economy': RadioSelect,
            'doctor_advice': Textarea(attrs={'class': 'easyui-textbox',
                                             'data-options': 'multiline:true',
                                             'style': 'width: 500px; height: 100px'}),
            'fill_table_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser, '
                                                                'required: true, '
                                                                'editable: false,'
                                                                'width: 100'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 80px',
                                                 'data-options': 'required: true'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        fill_table_date = timezone.now().date()
        initial['fill_table_date'] = fill_table_date.strftime('%Y-%m-%d')
        signature_date = timezone.now().date()
        initial['signature_date'] = signature_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(PsychiatricInfoForm, self).__init__(*args, **kwargs)