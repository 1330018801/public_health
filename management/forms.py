#-*- coding=utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms import ModelForm, RadioSelect, TextInput, DateInput, Select

from .models import Resident, Region, Service, UserProfile, SmsTime


class TestForm(ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'size': 20}, ),
            'sex': RadioSelect,
            'birthday': DateInput(attrs={'size': 20}, ),
            'nation': TextInput(attrs={'size': 20}, ),
            'town': Select(attrs={'size': 20}, ),
            'village': Select(attrs={'size': 20}, ),
            'identity': TextInput(attrs={'size': 20}, ),
            'address': TextInput(attrs={'size': 20}, ),
            'mobile': TextInput(attrs={'size': 20}, ),
            'email': TextInput(attrs={'size': 20}, ),
        }


class ResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'gender', 'nation', 'identity', 'birthday', 'address', 'mobile', 'email']
        widgets = {
            'name': TextInput(attrs={'size': 20},),
            'gender': RadioSelect,
            'nation': TextInput(attrs={'size': 20},),
            'identity': TextInput(attrs={'size': 20},),
            'birthday': DateInput(attrs={'size': 20},),
            'address': TextInput(attrs={'size': 20},),
            'mobile': TextInput(attrs={'size': 20},),
            'email': TextInput(attrs={'size': 20},),
        }


class Resident2Form(ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'gender', 'nation', 'identity', 'birthday', 'address', 'mobile', 'email', 'town', 'village']
        widgets = {
            'name': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'gender': RadioSelect(attrs={'class': 'form-control'},),
            'nation': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'identity': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'birthday': DateInput(attrs={'size': 20, 'class': 'form-control'},),
            'address': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'mobile': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'email': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'town': Select(attrs={'class': 'form-control'},),
            'village': Select(attrs={'class': 'form-control'},)
        }

    def __init__(self, *args, **kwargs):
        super(Resident2Form, self).__init__(*args, **kwargs)
        self.fields['town'].queryset = Region.towns.all()


class ServiceTypeForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'should_weight', 'real_weight']
        widgets = {
            'name': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'should_weight': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'real_weight': TextInput(attrs={'size': 20, 'class': 'form-control'},)
        }


class ServiceItemForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'unit', 'price', 'service_type']
        widgets = {
            'name': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'unit': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'price': TextInput(attrs={'size': 20, 'class': 'form-control'},),
            'service_type': Select(attrs={'class': 'form-control'},)
        }

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)
        self.fields['service_type'].queryset = Service.types.all()


class ChangePwdForm(forms.Form):
    old_password = forms.CharField(required=True, label=u"原密码", error_messages={'required': u'请输入原密码'},
                                   widget=forms.PasswordInput(attrs={'placeholder': u"原密码"},),)

    new_password1 = forms.CharField(required=True, label=u"新密码", error_messages={'required': u'请输入新密码'},
                                    widget=forms.PasswordInput(attrs={'placeholder': u"新密码"},),)
    new_password2 = forms.CharField(required=True, label=u"确认密码", error_messages={'required': u'请再次输入新密码'},
                                    widget=forms.PasswordInput(attrs={'placeholder': u"确认密码"}),)


class SmsTimeForm(ModelForm):
    class Meta:
        model = SmsTime
        fields = ['service_type', 'service_item', 'service_time']
        widgets = {
            'service_type': Select(attrs={'class': 'form-control'},),
            'service_item': Select(attrs={'class': 'form-control'},),
            'service_time': DateInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(SmsTimeForm, self).__init__(*args, **kwargs)
        self.fields['service_type'].queryset = Service.types.filter(Q(alias='old') | Q(alias='diabetes') |
                                                                    Q(alias='hypertension') | Q(alias='psychiatric') |
                                                                    Q(alias='tcm'))