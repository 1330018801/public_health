# -*- coding: utf-8 -*-
from datetime import date
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
                                                           'parser: myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter,'
                                                                'parser: myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        visit_date = date.today()
        initial['visit_date'] = visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(AftercareForm, self).__init__(*args, **kwargs)
