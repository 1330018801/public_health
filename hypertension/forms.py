# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.forms import TextInput, RadioSelect, ModelForm, CheckboxSelectMultiple, DateInput, Textarea
from .models import Aftercare


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser,'
                                                           'width: 100,'
                                                           'required: true,'
                                                           'editable: false'},),
            'visit_way':  RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox',
                                             'data-options': 'multiline: true,'
                                                             'width: 130, height: 50'},),
            'sign_sbp':  TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, required: true'},),
            'sign_dbp':  TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width:40, required: true'},),
            'sign_weight':  TextInput(attrs={'class': 'easyui-numberbox',
                                             'data-options': 'width: 40, precision: 1, required: true'},),
            'sign_weight_next':  TextInput(attrs={'class': 'easyui-numberbox',
                                                  'data-options': 'width: 40, precision: 1,required: true'},),
            'sign_bmi':  TextInput(attrs={'class': 'easyui-numberbox',
                                          'data-options': 'width: 40, precision: 2, required: true, editable: false'},),
            'sign_bmi_next':  TextInput(attrs={'class': 'easyui-numberbox',
                                               'data-options': 'width: 40, precision: 2, '
                                                               'required: true, editable: false'},),
            'sign_heart_rhythm': TextInput(attrs={'class': 'easyui-numberbox',
                                                  'data-options': 'width: 40, required: true'},),
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'},),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-numberbox',
                                                       'data-options': 'width: 40, required: true'},),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width: 40, required: true'},),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'},),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                             'data-options': 'width: 40, required: true'},),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'},),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'},),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'},),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width: 40, required: true'},),

            'life_style_guide_salt': RadioSelect,
            'life_style_guide_salt_next': RadioSelect,
            'life_style_guide_mentality':  RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination': Textarea(attrs={'class': 'easyui-textbox',
                                                     'data-options': 'multiline:true,width: 130, height: 100'},),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'medicine_untoward_effect_yes': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'take_medicine_3_day':TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_qt': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'take_medicine_qt_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_qt_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                      'data-options': 'width: 30, precision: 1'}),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 130'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, '
                                                                'parser: myparser,'
                                                                'width: 100, required: true'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100, required: true'},)
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)
