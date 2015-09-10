# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.forms import ModelForm, DateInput, TextInput, CheckboxSelectMultiple
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


# 6月龄儿童随访
class Aftercare6MonthForm(ModelForm):
    class Meta:
        model = Aftercare6Month
        alias = 'aftercare_6_month'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare6MonthForm, self).__init__(*args, **kwargs)


# 12月龄儿童随访
class Aftercare12MonthForm(ModelForm):
    class Meta:
        model = Aftercare12Month
        alias = 'aftercare_12_month'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare12MonthForm, self).__init__(*args, **kwargs)


# 18月龄儿童随访
class Aftercare18MonthForm(ModelForm):
    class Meta:
        model = Aftercare18Month
        alias = 'aftercare_18_month'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare18MonthForm, self).__init__(*args, **kwargs)


# 24月龄儿童随访
class Aftercare24MonthForm(ModelForm):
    class Meta:
        model = Aftercare24Month
        alias = 'aftercare_24_month'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare24MonthForm, self).__init__(*args, **kwargs)


# 30月龄儿童随访
class Aftercare30MonthForm(ModelForm):
    class Meta:
        model = Aftercare30Month
        alias = 'aftercare_30_month'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'next_visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare30MonthForm, self).__init__(*args, **kwargs)


# 3岁龄儿童随访
class Aftercare3YearForm(ModelForm):
    class Meta:
        model = Aftercare3Year
        alias = 'aftercare_3_year'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guide': CheckboxSelectMultiple,
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 100px'}),
        }





