# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.forms import ModelForm, TextInput, CheckboxSelectMultiple, RadioSelect
from tcm.models import *


class AftercareForm(ModelForm):
    class Meta:
        model = Aftercare
        alias = 'aftercare'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter: myformatter, '
                                                           'parser: myparser, '
                                                           'width: 100, required: true, editable: false'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'data-options': 'width: 90'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser, '
                                                                'width: 100, required: true, editable: false'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'data-options': 'width: 100, required: true'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        next_visit_date = date.today() + timedelta(days=6*30)
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)


class OldIdentifyForm(ModelForm):
    class Meta:
        model = OldIdentify
        fields = '__all__'
        widgets = {
            'q1': RadioSelect,
            'q2': RadioSelect,
            'q3': RadioSelect,
            'q4': RadioSelect,
            'q5': RadioSelect,
            'q6': RadioSelect,
            'q7': RadioSelect,
            'q8': RadioSelect,
            'q9': RadioSelect,
            'q10': RadioSelect,
            'q11': RadioSelect,
            'q12': RadioSelect,
            'q13': RadioSelect,
            'q14': RadioSelect,
            'q15': RadioSelect,
            'q16': RadioSelect,
            'q17': RadioSelect,
            'q18': RadioSelect,
            'q19': RadioSelect,
            'q20': RadioSelect,
            'q21': RadioSelect,
            'q22': RadioSelect,
            'q23': RadioSelect,
            'q24': RadioSelect,
            'q25': RadioSelect,
            'q26': RadioSelect,
            'q27': RadioSelect,
            'q28': RadioSelect,
            'q29': RadioSelect,
            'q30': RadioSelect,
            'q31': RadioSelect,
            'q32': RadioSelect,
            'q33': RadioSelect,
            'constitution_identify_points_qixu': TextInput(attrs={'class': 'easyui-numberbox',
                                                                  'data-options': 'width: 30, required: true, '
                                                                                  'editable: false'}),
            'constitution_identify_points_yangxu': TextInput(attrs={'class': 'easyui-numberbox',
                                                                    'data-options': 'width: 30, required: true, '
                                                                                    'editable: false'}),
            'constitution_identify_points_yinxu': TextInput(attrs={'class': 'easyui-numberbox',
                                                                   'data-options': 'width: 30, required: true,'
                                                                                   'editable: false'}),
            'constitution_identify_points_tanshi': TextInput(attrs={'class': 'easyui-numberbox',
                                                                    'data-options': 'width: 30, required: true,'
                                                                                    'editable: false'}),
            'constitution_identify_points_shire': TextInput(attrs={'class': 'easyui-numberbox',
                                                                   'data-options': 'width: 30, required: true,'
                                                                                   'editable: false'}),
            'constitution_identify_points_xueyu': TextInput(attrs={'class': 'easyui-numberbox',
                                                                   'data-options': 'width: 30, required: true,'
                                                                                   'editable: false'}),
            'constitution_identify_points_qiyu': TextInput(attrs={'class': 'easyui-numberbox',
                                                                  'data-options': 'width: 30, required: true, '
                                                                                  'editable: false'}),
            'constitution_identify_points_tebing': TextInput(attrs={'class': 'easyui-numberbox',
                                                                    'data-options': 'width: 30, required: true,'
                                                                                    'editable: false'}),
            'constitution_identify_points_pinghe': TextInput(attrs={'class': 'easyui-numberbox',
                                                                    'data-options': 'width: 30, required: true,'
                                                                                    'editable: false'}),
            'constitution_identify_yes_trend_qixu': RadioSelect,
            'constitution_identify_yes_trend_yangxu': RadioSelect,
            'constitution_identify_yes_trend_yinxu': RadioSelect,
            'constitution_identify_yes_trend_tanshi': RadioSelect,
            'constitution_identify_yes_trend_shire': RadioSelect,
            'constitution_identify_yes_trend_xueyu': RadioSelect,
            'constitution_identify_yes_trend_qiyu': RadioSelect,
            'constitution_identify_yes_trend_tebing': RadioSelect,
            'constitution_identify_yes_trend_pinghe': RadioSelect,
            'health_care_guide_qixu': CheckboxSelectMultiple,
            'health_care_guide_yangxu': CheckboxSelectMultiple,
            'health_care_guide_yinxu': CheckboxSelectMultiple,
            'health_care_guide_tanshi': CheckboxSelectMultiple,
            'health_care_guide_shire': CheckboxSelectMultiple,
            'health_care_guide_xueyu': CheckboxSelectMultiple,
            'health_care_guide_qiyu': CheckboxSelectMultiple,
            'health_care_guide_tebing': CheckboxSelectMultiple,
            'health_care_guide_pinghe': CheckboxSelectMultiple,
            'health_care_guide_extra_qixu': TextInput(attrs={'class': 'easyui-textbox',
                                                             'data-options': 'width: 60'}),
            'health_care_guide_extra_yangxu': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 60'}),
            'health_care_guide_extra_yinxu': TextInput(attrs={'class': 'easyui-textbox',
                                                              'data-options': 'width: 60'}),
            'health_care_guide_extra_tanshi': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 60'}),
            'health_care_guide_extra_shire': TextInput(attrs={'class': 'easyui-textbox',
                                                              'data-options': 'width: 60'}),
            'health_care_guide_extra_xueyu': TextInput(attrs={'class': 'easyui-textbox',
                                                              'data-options': 'width: 60'}),
            'health_care_guide_extra_qiyu': TextInput(attrs={'class': 'easyui-textbox',
                                                             'data-options': 'width: 60'}),
            'health_care_guide_extra_tebing': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 60'}),
            'health_care_guide_extra_pinghe': TextInput(attrs={'class': 'easyui-textbox',
                                                               'data-options': 'width: 60'}),
            'fill_table_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'width: 100, formatter: myformatter, parser: myparser,'
                                                                'editable: false, required: true'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'data-options': 'width: 100, required: true'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        fill_table_date = date.today()
        initial['fill_table_date'] = fill_table_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(OldIdentifyForm, self).__init__(*args, **kwargs)