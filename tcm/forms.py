# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.forms import ModelForm, TextInput, CheckboxSelectMultiple
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
