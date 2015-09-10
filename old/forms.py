from django.forms import ModelForm, RadioSelect, TextInput
from .models import *


class LivingSelfcareAppraisalForm(ModelForm):
    class Meta: 
        model = LivingSelfcareAppraisal
        fields = '__all__'
        widgets = {
            'eat': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
            'wash': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
            'dress': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
            'toilet': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
            'activity': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
            'total': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 40px'}),
        }
