from datetime import date, timedelta
from .models import *

from django.forms import ModelForm, RadioSelect, DateInput, TextInput, CheckboxSelectMultiple


class HealthManualForm(ModelForm):
    class Meta:
        model = HealthManual
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'birth_date': DateInput(attrs={'size': 20}),
            'id_number': TextInput(attrs={'size': 20}),
            'home_address': TextInput(attrs={'size': 50}),
            'father_name': TextInput(attrs={'size': 20}),
            'father_occupation': TextInput(attrs={'size': 20}),
            'father_contact_number': TextInput(attrs={'size': 20}),
            'father_birth_date': TextInput(attrs={'size': 20}),
            'mother_name': TextInput(attrs={'size': 20}),
            'mother_occupation': TextInput(attrs={'size': 20}),
            'mother_contact_number': TextInput(attrs={'size': 20}),
            'mother_birth_date': TextInput(attrs={'size': 20}),
            'gestational_weeks': TextInput(attrs={'size': 8}),
            'mother_gestational_disease': RadioSelect,
            'mother_gestational_disease_extra': TextInput(attrs={'size': 15}),
            'deliver_institution': TextInput(attrs={'size': 39}),
            'birth_situation': CheckboxSelectMultiple,
            'birth_situation_extra': TextInput(attrs={'size': 15}),
            'newborn_asphyxia': RadioSelect,
            'newborn_asphyxia_yes': RadioSelect,
            'apgan_score': RadioSelect,
            'birth_malformation': RadioSelect,
            'birth_malformation_extra': TextInput(attrs={'size': 20}),
            'newborn_birth_weight': TextInput(attrs={'size': 8}),
            'birth_height': TextInput(attrs={'size': 8}),
            'feed_way': RadioSelect,
            'drink_milk_volume': TextInput(attrs={'size': 8}),
            'drink_milk_times': TextInput(attrs={'size': 8}),
            'emesis': RadioSelect,
            'shit_times': TextInput(attrs={'size': 8}),
            'kajiemiao_vaccinate': RadioSelect,
            'yigan_vaccinate': RadioSelect,
            'newborn_hearing_screening': RadioSelect,
            'pku_screening': RadioSelect,
            'thyroid_screening': RadioSelect,
            'extra_disease_screening': TextInput(attrs={'size': 30}),
            'extra_disease_screening_pass': RadioSelect,
        }

    def clean(self):
        cleaned_data = super(HealthManualForm, self).clean()
        if cleaned_data.get('birth_height') < 1 or cleaned_data.get('birth_height') > 150:
            msg = ""
            self.add_error('birth_height', msg)


class NewbornFamilyVisitForm(ModelForm):
    class Meta:
        model = NewbornFamilyVisit
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'birthday': DateInput(attrs={'class': 'easyui-datebox',
                                         'data-options': 'formatter: myformatter, '
                                                         'parser: myparser, '
                                                         'required: true, '
                                                         'editable: false,'
                                                         'width: 100'}),
            'identity': TextInput(attrs={'class': 'easyui-textbox',
                                         'style': 'width: 150px'}),
            'address': TextInput(attrs={'class': 'easyui-textbox',
                                        'style': 'width: 250px',
                                        'data-options': 'required: true'}),
            'father_name': TextInput(attrs={'class': 'easyui-textbox',
                                            'style': 'width: 80px',
                                            'data-options': 'required: true'}),
            'father_occupation': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width: 80px',
                                                  'data-options': 'required: true'}),
            'father_contact_number': TextInput(attrs={'class': 'easyui-numberbox',
                                                      'style': 'width: 85px',
                                                      'data-options': 'required: true'}),
            'father_birthday': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, '
                                                                'parser: myparser, '
                                                                'required: true, '
                                                                'editable: false,'
                                                                'width: 100'}),
            'mother_name': TextInput(attrs={'class': 'easyui-textbox',
                                            'style': 'width: 80px',
                                            'data-options': 'required: true'}),
            'mother_occupation': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width:80px',
                                                  'data-options': 'required: true'}),
            'mother_contact_number': TextInput(attrs={'class': 'easyui-numberbox',
                                                      'style': 'width: 85px',
                                                      'data-options': 'required: true'}),
            'mother_birthday': TextInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter: myformatter, '
                                                                'parser: myparser, '
                                                                'required: true, '
                                                                'editable: false,'
                                                                'width: 100'}),
            'gestational_weeks': TextInput(attrs={'class': 'easyui-numberbox',
                                                  'style': 'width:40px',
                                                  'data-options': 'required: true'}),
            'mother_gestational_disease': RadioSelect,
            'mother_gestational_disease_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'style': 'width:100px'}),
            'deliver_institution': TextInput(attrs={'class': 'easyui-textbox',
                                                    'style': 'width: 70px',
                                                    'data-options': 'required: true'}),
            'birth_situation': CheckboxSelectMultiple,
            'birth_situation_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                      'style': 'width: 60px'}),
            'newborn_asphyxia': RadioSelect,
            'apgar_score': RadioSelect,
            'malformation_or_not': RadioSelect,
            'malformation_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                   'style': 'width:128px'}),
            'newborn_hearing_screening': RadioSelect,
            'newborn_disease_screening': RadioSelect,
            'newborn_disease_screening_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                                'style': 'width:200px'}),
            'newborn_birth_weight': TextInput(attrs={'class': 'easyui-numberbox',
                                                     'style': 'width:40px',
                                                     'data-options': 'required: true'}),
            'now_weight': TextInput(attrs={'class': 'easyui-numberbox',
                                           'style': 'width:40px',
                                           'data-options': 'required: true'}),
            'birth_height': TextInput(attrs={'class': 'easyui-numberbox',
                                             'style': 'width:40px',
                                             'data-options': 'required: true'}),
            'feed_way': RadioSelect,
            'drink_milk_volume': TextInput(attrs={'class': 'easyui-textbox',
                                                  'style': 'width:40px'}),
            'drink_milk_times': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width:40px'}),
            'emesis': RadioSelect,
            'shit': RadioSelect,
            'shit_times': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'body_temperature': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'style': 'width: 40px',
                                                 'data-options': 'required: true'}),
            'pulse': TextInput(attrs={'class': 'easyui-numberbox',
                                      'style': 'width:40px',
                                      'data-options': 'required: true'}),
            'breath_frequency': TextInput(attrs={'class': 'easyui-numberbox',
                                                 'style': 'width:40px',
                                                 'data-options': 'required: true'}),
            'complexion': RadioSelect,
            'complexion_extra': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width:80px'}),
            'icterus_position': RadioSelect,
            'bregma_x': TextInput(attrs={'class': 'easyui-numberbox',
                                         'style': 'width: 40px',
                                         'data-options': 'required: true'}),
            'bregma_y': TextInput(attrs={'class': 'easyui-numberbox',
                                         'style': 'width: 40px',
                                         'data-options': 'required: true'}),
            'bregma_1': RadioSelect,
            'bregma_1_extra': TextInput(attrs={'class': 'easyui-textbox',
                                               'style': 'width:80px'}),
            'eye_appearance': RadioSelect,
            'eye_appearance_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                        'style': 'width:128px'}),
            'ear_appearance': RadioSelect,
            'ear_appearance_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                        'style': 'width:128px'}),
            'nose': RadioSelect,
            'nose_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                              'style': 'width:128px'}),
            'oral_cavity': RadioSelect,
            'oral_cavity_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                     'style': 'width:128px'}),
            'heart_lung_auscultation': RadioSelect,
            'heart_lung_auscultation_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                                 'style': 'width:128px'}),
            'abdomen_palpation': RadioSelect,
            'abdomen_palpation_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                           'style': 'width:128px'}),
            'all_fours_activity': RadioSelect,
            'all_fours_activity_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                            'style': 'width:128px'}),
            'neck_enclosed_mass': RadioSelect,
            'neck_enclosed_mass_yes': TextInput(attrs={'class': 'easyui-textbox',
                                                       'style': 'width:128px'}),
            'skin': RadioSelect,
            'skin_extra': TextInput(attrs={'class': 'easyui-textbox',
                                           'style': 'width: 60px'}),
            'anus': RadioSelect,
            'anus_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                              'style': 'width: 128px'}),
            'externalia': RadioSelect,
            'externalia_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                                    'style': 'width:128px'}),
            'spine': RadioSelect,
            'spine_abnormal': TextInput(attrs={'class': 'easyui-textbox',
                                               'style': 'width: 128px'}),
            'navel': RadioSelect,
            'navel_extra': TextInput(attrs={'class': 'easyui-textbox',
                                            'style': 'width: 128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(attrs={'class': 'easyui-textbox',
                                                                     'style': 'width:200px'}),
            'transfer_treatment_suggestion_institution': TextInput(attrs={'class': 'easyui-textbox',
                                                                          'style': 'width:200px'}),
            'guide': CheckboxSelectMultiple,
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'required: true, '
                                                           'formatter: myformatter,'
                                                           'parser: myparser,'
                                                           'width: 100'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'required: true, '
                                                                'formatter: myformatter, '
                                                                'parser: myparser,'
                                                                'width: 100'}),
            'next_visit_place': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 128px',
                                                 'data-options': 'required: true'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox',
                                                 'style': 'width: 80px',
                                                 'data-options': 'required: true'})
        }

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            pass
        else:
            initial = kwargs.get('initial', {})
            initial['visit_date'] = date.today().strftime('%Y-%m-%d')
            next_visit_date = date.today() + timedelta(days=30)
            initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
            kwargs['initial'] = initial
        super(NewbornFamilyVisitForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(NewbornFamilyVisitForm, self).clean()
        if cleaned_data.get('body_temperature') < 20 or cleaned_data.get('body_temperature') > 50:
            msg = ""
            self.add_error('body_temperature', msg)
        if cleaned_data.get('pulse') < 50 or cleaned_data.get('pulse') > 150:
            msg = ""
            self.add_error('pulse', msg)
        if cleaned_data.get('birth_height') < 1 or cleaned_data.get('birth_height') > 150:
            msg = ""
            self.add_error('birth_height', msg)


class Aftercare1MonthForm(ModelForm):
    class Meta:
        model = Aftercare1Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'head_circumference': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'neck_enclosed_mass': RadioSelect,
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'oral_cavity': RadioSelect,
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'navel': RadioSelect,
            'all_fours': RadioSelect,
            'rickets_sign': RadioSelect,
            'anus_externalia': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=60)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare1MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare1MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare3MonthForm(ModelForm):
    class Meta:
        model = Aftercare3Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'head_circumference': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'neck_enclosed_mass': RadioSelect,
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'oral_cavity': RadioSelect,
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'navel': RadioSelect,
            'all_fours': RadioSelect,
            'rickets_symptom': RadioSelect,
            'rickets_sign': RadioSelect,
            'anus_externalia': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=90)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare3MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare3MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare6MonthForm(ModelForm):
    class Meta:
        model = Aftercare6Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'head_circumference': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'neck_enclosed_mass': RadioSelect,
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'hearing': RadioSelect,
            'oral_cavity': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'rickets_symptom': RadioSelect,
            'rickets_sign': RadioSelect,
            'anus_externalia': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=60)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare6MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare6MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare8MonthForm(ModelForm):
    class Meta:
        model = Aftercare8Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'head_circumference': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'oral_cavity': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'rickets_symptom': RadioSelect,
            'rickets_sign': RadioSelect,
            'anus_externalia': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=120)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare8MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare8MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare12MonthForm(ModelForm):
    class Meta:
        model = Aftercare12Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'hearing': RadioSelect,
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'rickets_sign': RadioSelect,
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=180)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare12MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare12MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)


class Aftercare18MonthForm(ModelForm):
    class Meta:
        model = Aftercare18Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'step': RadioSelect,
            'rickets_sign': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=180)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare18MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare18MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare24MonthForm(ModelForm):
    class Meta:
        model = Aftercare24Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'bregma': RadioSelect,
            'bregma_length': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'bregma_width': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:35px'}),
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'hearing': RadioSelect,
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'step': RadioSelect,
            'rickets_sign': RadioSelect,
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'take_vitamin_d': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'growth_evaluate': RadioSelect,
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=180)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare24MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare24MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)


class Aftercare30MonthForm(ModelForm):
    class Meta:
        model = Aftercare30Month
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'complexion': RadioSelect,
            'skin': RadioSelect,
            'eye_appearance': RadioSelect,
            'ear_appearance': RadioSelect,
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'all_fours': RadioSelect,
            'step': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'outdoor_activities': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'two_visit_disease': RadioSelect,
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=180)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare30MonthForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare30MonthForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare3YearForm(ModelForm):
    class Meta:
        model = Aftercare3Year
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'body_growth_evaluate': RadioSelect,
            'hearing': RadioSelect,
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'two_visit_disease': CheckboxSelectMultiple(),
            'pneumonia': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'diarrhea': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'traumatism': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'two_visit_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare3YearForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare3YearForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare4YearForm(ModelForm):
    class Meta:
        model = Aftercare4Year
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'body_growth_evaluate': RadioSelect,
            'eye_sight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'two_visit_disease': CheckboxSelectMultiple(),
            'pneumonia': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'diarrhea': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'traumatism': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'two_visit_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare4YearForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare4YearForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare5YearForm(ModelForm):
    class Meta:
        model = Aftercare5Year
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'body_growth_evaluate': RadioSelect,
            'eye_sight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'two_visit_disease': CheckboxSelectMultiple(),
            'pneumonia': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'diarrhea': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'traumatism': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'two_visit_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        next_visit_date = date.today() + timedelta(days=365)
        initial['next_visit_date'] = next_visit_date.strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare5YearForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare5YearForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)


class Aftercare6YearForm(ModelForm):
    class Meta:
        model = Aftercare6Year
        fields = '__all__'
        widgets = {
            'visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                           'data-options': 'formatter:myformatter,parser:myparser'}),
            'weight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'weight_grade': RadioSelect,
            'height': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'height_grade': RadioSelect,
            'body_growth_evaluate': RadioSelect,
            'eye_sight': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'decayed_tooth': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'heart_lung': RadioSelect,
            'abdomen': RadioSelect,
            'hemoglobin_value': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'two_visit_disease': CheckboxSelectMultiple(),
            'pneumonia': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'diarrhea': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'traumatism': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:40px'}),
            'two_visit_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'transfer_treatment_suggestion': RadioSelect,
            'transfer_treatment_suggestion_reason': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'transfer_treatment_suggestion_institution': TextInput(
                attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'guide': CheckboxSelectMultiple(),
            'guide_extra': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'next_visit_date': DateInput(attrs={'class': 'easyui-datebox',
                                                'data-options': 'formatter:myformatter,parser:myparser'}),
            'doctor_signature': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial['next_visit_date'] = date.today().strftime('%Y-%m-%d')
        kwargs['initial'] = initial
        super(Aftercare6YearForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Aftercare6YearForm, self).clean()
        if cleaned_data.get('height') < 1 or cleaned_data.get('height') > 150:
            msg = ""
            self.add_error('height', msg)
        if cleaned_data.get('hemoglobin_value') < 0 or cleaned_data.get('hemoglobin_value') > 300:
            msg = ""
            self.add_error('hemoglobin_value', msg)
