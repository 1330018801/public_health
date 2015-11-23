#-*- coding=utf-8 -*-
from datetime import date, timedelta
from django.forms import ModelForm, RadioSelect, TextInput, CheckboxSelectMultiple, DateInput, Textarea
from .models import *


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,'
                                                           'parser:myparser, '
                                                           'width: 100,'
                                                           'required: true,'
                                                           'editable: false'}),
            'visit_way': RadioSelect,
            'symptom': CheckboxSelectMultiple,
            'symptom_extra': Textarea(attrs={'class': 'easyui-textbox',
                                             'data-options': 'multiline: true,'
                                                             'width: 128, height: 50'},),
            'sign_sbp': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, required: true'}),
            'sign_dbp': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 40, required: true'}),
            'sign_weight': TextInput(attrs={'class': 'easyui-numberbox',
                                            'data-options': 'width: 40, precision: 1,'
                                                            'required: true'}),
            'sign_weight_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                    'data-options': 'width: 40, precision: 1,'
                                                                    'required: true'}),
            'sign_bmi': TextInput(attrs={'class': 'easyui-numberbox',
                                         'data-options': 'width: 40, precision: 2,'
                                                         'required: true, editable: false'}),
            'sign_bmi_next': TextInput(attrs={'class': 'easyui-numberbox',
                                              'data-options': 'width: 40, precision: 2,'
                                                              'required: true, editable: false'}),

            'sign_acrotarsium_artery_pulse': RadioSelect,
            'sign_extra': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width:128'}),
            'life_style_guide_smoke': TextInput(attrs={'class': 'easyui-numberbox',
                                                       'data-options': 'width:40, required: true'}),
            'life_style_guide_smoke_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                            'data-options': 'width:40, required: true'}),
            'life_style_guide_liquor': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:40, required: true'}),
            'life_style_guide_liquor_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                             'data-options': 'width:40, required: true'}),
            'life_style_guide_sport1': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:25, required: true'}),
            'life_style_guide_sport2': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:25, required: true'}),
            'life_style_guide_sport3': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:25, required: true'}),
            'life_style_guide_sport4': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:25, required: true'}),
            'life_style_guide_staple': TextInput(attrs={'class': 'easyui-numberbox',
                                                        'data-options': 'width:40, precision: 1, required: true'}),
            'life_style_guide_staple_next': TextInput(attrs={'class': 'easyui-numberbox',
                                                             'data-options': 'width:40, precision: 1, required: true'}),
            'life_style_guide_mentality': RadioSelect,
            'life_style_guide_medical_compliance': RadioSelect,
            'auxiliary_examination_fbg_value': TextInput(attrs={'class': 'easyui-numberbox',
                                                                'data-options': 'width:40, precision: 1, required: true'}),
            'auxiliary_examination_extra_hemoglobin': TextInput(attrs={'class': 'easyui-numberbox',
                                                                       'data-options': 'width:30,'
                                                                                       'min: 0, max: 300, precision: 2'}),
            'auxiliary_examination_extra_examination_date': DateInput(attrs={'class': 'easyui-datebox',
                                                                             'data-options': 'formatter: myformatter,'
                                                                                             'parser:myparser,'
                                                                                             'width: 128, '
                                                                                             'editable: false'}),
            'auxiliary_examination_extra_examination': TextInput(attrs={'class': 'easyui-textbox',
                                                                        'data-options': 'width: 128'}),
            'take_medicine_compliance': RadioSelect,
            'medicine_untoward_effect': RadioSelect,
            'hypoglycemia_reaction': RadioSelect,
            'visit_classification': RadioSelect,
            'take_medicine_1': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'take_medicine_1_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_1_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_2': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'take_medicine_2_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_2_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_3': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'take_medicine_3_day': TextInput(attrs={'class': 'easyui-numberbox', 'data-options': 'width: 30'}),
            'take_medicine_3_time': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'data-options': 'width: 30, precision: 1'}),
            'take_medicine_insulin': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 80'}),
            'take_medicine_insulin_volume': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'transfer_treatment_reason': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'transfer_treatment_institution': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 128'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, parser: myparser,'
                                                                'width: 100,required: true, editable:false'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100, required: true'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)

    '''
    def clean(self):
        cleaned_data = super(AftercareForm, self).clean()
        if cleaned_data.get('auxiliary_examination_extra_hemoglobin') < 0 or \
                        cleaned_data.get('auxiliary_examination_extra_hemoglobin') > 300:
            msg = ""
            self.add_error('auxiliary_examination_extra_hemoglobin', msg)
    '''