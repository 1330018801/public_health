# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, RadioSelect
from .models import *


# 预防接种卡
class VaccineCardForm(ModelForm):
    class Meta:
        model = VaccineCard
        exclude = ('resident',)
        widgets = {
            'name': TextInput(attrs={'class': 'easyui-textbox'}),
            'number': TextInput(attrs={'class': 'easyui-textbox'}),
            'gender': RadioSelect,
            'birth_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'guardian_name': TextInput(attrs={'class': 'easyui-textbox'}),
            'relation_to_child': TextInput(attrs={'class': 'easyui-textbox'}),
            'contact_number':  TextInput(attrs={'class': 'easyui-textbox'}),
            'home_address': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'}),
            'census_register_address': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 200px'}),
            'census_register_address_extra': TextInput(attrs={'class': 'easyui-textbox'}),
            'immigrate_time': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'emigrate_time': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'emigrate_reason': TextInput(attrs={'class': 'easyui-textbox'}),
            'vaccine_abnormal_reaction_history': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 400px'}),
            'vaccinate_taboo': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 400px'}),
            'infection_history': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 400px'}),
            'found_card_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'found_card_person': TextInput(attrs={'class': 'easyui-textbox'}),
        }