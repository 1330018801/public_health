from django.forms import ModelForm, TextInput
from .models import *


class LivingSelfcareAppraisalForm(ModelForm):
    class Meta: 
        model = LivingSelfcareAppraisal
        fields = '__all__'
        widgets = {
            'eat': TextInput(attrs={'class': 'easyui-numberbox',
                                    'data-options': 'width: 40, min: 0, max: 5, required: true'}),
            'wash': TextInput(attrs={'class': 'easyui-numberbox',
                                     'data-options': 'width: 40, min: 0, max: 7, required: true'}),
            'dress': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, min: 0, max: 5, required: true'}),
            'toilet': TextInput(attrs={'class': 'easyui-numberbox',
                                       'data-options': 'width: 40, min: 0, max: 10, required: true'}),
            'activity': TextInput(attrs={'class': 'easyui-numberbox',
                                         'data-options': 'width: 40, min: 0, max: 10, required: true'}),
            'total': TextInput(attrs={'class': 'easyui-numberbox',
                                      'data-options': 'width: 40, min: 0, max: 37, required: true, editable: false'}),
        }
