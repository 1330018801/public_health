# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.forms import ModelForm, TextInput, DateInput, RadioSelect, Select
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


# 乙肝疫苗①
class HepatitisBVaccine1Form(ModelForm):
    class Meta:
        model = HepatitisBVaccine1
        alias = 'hepatitis_b_vaccine_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(HepatitisBVaccine1Form, self).__init__(*args, **kwargs)


# 乙肝疫苗②
class HepatitisBVaccine2Form(ModelForm):
    class Meta:
        model = HepatitisBVaccine2
        alias = 'hepatitis_b_vaccine_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(HepatitisBVaccine2Form, self).__init__(*args, **kwargs)


# 乙肝疫苗③
class HepatitisBVaccine3Form(ModelForm):
    class Meta:
        model = HepatitisBVaccine3
        alias = 'hepatitis_b_vaccine_3'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 卡介苗
class BcgVaccineForm(ModelForm):
    class Meta:
        model = BcgVaccine
        alias = 'bcg_vaccine'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 脊灰疫苗①
class PoliomyelitisVaccine1Form(ModelForm):
    class Meta:
        model = PoliomyelitisVaccine1
        alias = 'poliomyelitis_vaccine_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(PoliomyelitisVaccine1Form, self).__init__(*args, **kwargs)


# 脊灰疫苗②
class PoliomyelitisVaccine2Form(ModelForm):
    class Meta:
        model = PoliomyelitisVaccine2
        alias = 'poliomyelitis_vaccine_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(PoliomyelitisVaccine2Form, self).__init__(*args, **kwargs)


# 脊灰疫苗③
class PoliomyelitisVaccine3Form(ModelForm):
    class Meta:
        model = PoliomyelitisVaccine3
        alias = 'poliomyelitis_vaccine_3'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(PoliomyelitisVaccine3Form, self).__init__(*args, **kwargs)


# 脊灰疫苗④
class PoliomyelitisVaccine4Form(ModelForm):
    class Meta:
        model = PoliomyelitisVaccine4
        alias = 'poliomyelitis_vaccine_4'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 百白破疫苗①
class DiphtheriaPertussisTetanus1Form(ModelForm):
    class Meta:
        model = DiphtheriaPertussisTetanus1
        alias = 'diphtheria_pertussis_tetanus_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(DiphtheriaPertussisTetanus1Form, self).__init__(*args, **kwargs)


# 百白破疫苗②
class DiphtheriaPertussisTetanus2Form(ModelForm):
    class Meta:
        model = DiphtheriaPertussisTetanus2
        alias = 'diphtheria_pertussis_tetanus_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(DiphtheriaPertussisTetanus2Form, self).__init__(*args, **kwargs)


# 百白破疫苗③
class DiphtheriaPertussisTetanus3Form(ModelForm):
    class Meta:
        model = DiphtheriaPertussisTetanus3
        alias = 'diphtheria_pertussis_tetanus_3'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=28)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(DiphtheriaPertussisTetanus3Form, self).__init__(*args, **kwargs)


# 百白破疫苗④
class DiphtheriaPertussisTetanus4Form(ModelForm):
    class Meta:
        model = DiphtheriaPertussisTetanus4
        alias = 'diphtheria_pertussis_tetanus_4'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 白破疫苗
class DiphtheriaTetanusVaccineForm(ModelForm):
    class Meta:
        model = DiphtheriaTetanusVaccine
        alias = 'diphtheria_tetanus_vaccine'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 麻风疫苗
class MeaslesRubellaForm(ModelForm):
    class Meta:
        model = MeaslesRubella
        alias = 'measles_rubella'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 麻腮风疫苗①
class MeaslesMumpsRubella1Form(ModelForm):
    class Meta:
        model = MeaslesMumpsRubella1
        alias = 'measles_mumps_rubella_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }


# 麻腮风疫苗②
class MeaslesMumpsRubella2Form(ModelForm):
    class Meta:
        model = MeaslesMumpsRubella2
        alias = 'measles_mumps_rubella_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }


# 麻腮疫苗
class MeaslesMumpsForm(ModelForm):
    class Meta:
        model = MeaslesMumps
        alias = 'measles_mumps'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 麻疹疫苗①
class Measles1Form(ModelForm):
    class Meta:
        model = Measles1
        alias = 'measles_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }


# 麻疹疫苗②
class Measles2Form(ModelForm):
    class Meta:
        model = Measles2
        alias = 'measles_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# A群流脑疫苗①
class MeningitisA1Form(ModelForm):
    class Meta:
        model = MeningitisA1
        alias = 'meningitis_a_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*3)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(MeningitisA1Form, self).__init__(*args, **kwargs)


# A群流脑疫苗②
class MeningitisA2Form(ModelForm):
    class Meta:
        model = MeningitisA2
        alias = 'meningitis_a_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(MeningitisA2Form, self).__init__(*args, **kwargs)


# A+C群流脑疫苗①
class MeningitisAc1Form(ModelForm):
    class Meta:
        model = MeningitisAc1
        alias = 'meningitis_ac_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365*3)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(MeningitisAc1Form, self).__init__(*args, **kwargs)


# A+C群流脑疫苗②
class MeningitisAc2Form(ModelForm):
    class Meta:
        model = MeningitisAc2
        alias = 'meningitis_ac_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 乙脑减毒活疫苗①
class JapaneseEncephalitisAttenuated1Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisAttenuated1
        fields = '__all__'
        alias = 'japanese_encephalitis_attenuated_1'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365+30*4)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(JapaneseEncephalitisAttenuated1Form, self).__init__(*args, **kwargs)


# 乙脑减毒活疫苗②
class JapaneseEncephalitisAttenuated2Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisAttenuated2
        alias = 'japanese_encephalitis_attenuated_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 乙脑灭活疫苗①
class JapaneseEncephalitisInactivated1Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisInactivated1
        alias = 'japanese_encephalitis_inactivated_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=7)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(JapaneseEncephalitisInactivated1Form, self).__init__(*args, **kwargs)


# 乙脑灭活疫苗②
class JapaneseEncephalitisInactivated2Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisInactivated2
        alias = 'japanese_encephalitis_inactivated_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(JapaneseEncephalitisInactivated2Form, self).__init__(*args, **kwargs)


# 乙脑灭活疫苗③
class JapaneseEncephalitisInactivated3Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisInactivated3
        alias = 'japanese_encephalitis_inactivated_3'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365*4)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(JapaneseEncephalitisInactivated3Form, self).__init__(*args, **kwargs)


# 乙脑灭活疫苗④
class JapaneseEncephalitisInactivated4Form(ModelForm):
    class Meta:
        model = JapaneseEncephalitisInactivated4
        alias = 'japanese_encephalitis_inactivated_4'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 甲肝减毒疫苗
class HepatitisAAttenuatedForm(ModelForm):
    class Meta:
        model = HepatitisAAttenuated
        alias = 'hepatitis_a_attenuated'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 甲肝灭活疫苗①
class HepatitisAInactivated1Form(ModelForm):
    class Meta:
        model = HepatitisAInactivated1
        alias = 'hepatitis_a_inactivated_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=30*6)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(HepatitisAInactivated1Form, self).__init__(*args, **kwargs)


# 甲肝灭活疫苗②
class HepatitisAInactivated2Form(ModelForm):
    class Meta:
        model = HepatitisAInactivated2
        alias = 'hepatitis_a_inactivated_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 炭疽疫苗
class AnthraxVaccineForm(ModelForm):
    class Meta:
        model = AnthraxVaccine
        alias = 'anthrax_vaccine'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 钩体疫苗①
class LeptospiraVaccine1Form(ModelForm):
    class Meta:
        model = LeptospiraVaccine1
        alias = 'leptospira_vaccine_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=7)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(LeptospiraVaccine1Form, self).__init__(*args, **kwargs)


# 钩体疫苗②
class LeptospiraVaccine2Form(ModelForm):
    class Meta:
        model = LeptospiraVaccine2
        alias = 'leptospira_vaccine_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }


# 出血热疫苗（双价）①
class HemorrhagicIII1Form(ModelForm):
    class Meta:
        model = HemorrhagicIII1
        alias = 'hemorrhagic_i_ii_1'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=14)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(HemorrhagicIII1Form, self).__init__(*args, **kwargs)


# 出血热疫苗（双价）②
class HemorrhagicIII2Form(ModelForm):
    class Meta:
        model = HemorrhagicIII2
        alias = 'hemorrhagic_i_ii_2'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'next_vaccinate_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=180-14)
        initial['next_vaccinate_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(HemorrhagicIII2Form, self).__init__(*args, **kwargs)


# 出血热疫苗（双价）③
class HemorrhagicIII3Form(ModelForm):
    class Meta:
        model = HemorrhagicIII3
        alias = 'hemorrhagic_i_ii_3'
        fields = '__all__'
        widgets = {
            'visit_date': TextInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'vaccine_dose': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'vaccinate_position': Select(attrs={'class': 'easyui-combobox', 'style': 'width: 100px'}),
            'batch_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'remarks': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width: 80px'},),
        }