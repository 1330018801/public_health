# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Resident, Service, WorkRecord
from psychiatric.models import PsychiatricInfo
from .models import PersonalInfo
from .forms import *

import logging

log = logging.getLogger('debug')


class PersonalInfoFormPreview(FormPreview):
    form_template = 'ehr/personal_info_form.html'
    preview_template = 'ehr/personal_info_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['resident_id'] = kwargs.pop('resident_id')

    def done(self, request, cleaned_data):
        payment_way = cleaned_data.pop('payment_way')
        allergy_history = cleaned_data.pop('allergy_history')
        expose_history = cleaned_data.pop('expose_history')
        disease_history = cleaned_data.pop('disease_history')
        family_history_father = cleaned_data.pop('family_history_father')
        family_history_mother = cleaned_data.pop('family_history_mother')
        family_history_sibling = cleaned_data.pop('family_history_sibling')
        family_history_children = cleaned_data.pop('family_history_children')
        disability = cleaned_data.pop('disability')

        personal_info = PersonalInfo(**cleaned_data)
        resident = Resident.objects.get(id=self.state['resident_id'])
        personal_info.resident = resident
        personal_info.save()

        for item in payment_way:
            personal_info.payment_way.add(item)
        for item in allergy_history:
            personal_info.allergy_history.add(item)
        for item in expose_history:
            personal_info.expose_history.add(item)
        for item in disease_history:
            personal_info.disease_history.add(item)
        for item in family_history_father:
            personal_info.family_history_father.add(item)
        for item in family_history_mother:
            personal_info.family_history_mother.add(item)
        for item in family_history_sibling:
            personal_info.family_history_sibling.add(item)
        for item in family_history_children:
            personal_info.family_history_children.add(item)
        for item in disability:
            personal_info.disability.add(item)

        return HttpResponseRedirect('/ehr/')


class PsychiatricInfoFormPreview(FormPreview):
    form_template = 'ehr/psychiatric_info_form.html'
    preview_template = 'ehr/psychiatric_info_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['resident_id'] = kwargs.pop('resident_id')

    def done(self, request, cleaned_data):
        symptom = cleaned_data.pop('symptom')
        psychiatric_info = PsychiatricInfo(**cleaned_data)
        resident_id = int(self.state['resident_id'])
        psychiatric_info.resident = Resident.objects.get(id=resident_id)
        psychiatric_info.save()

        for item in symptom:
            psychiatric_info.symptom.add(item)

        return HttpResponseRedirect('/ehr/')


'''
form_sections = {'old_body_check': [
    PhysicalExaminationForm, BloodRoutineTestForm, UrineRoutineTestForm, BloodGlucoseForm,
    ElectrocardiogramForm, AlanineAminotransferaseForm, GlutamicOxalaceticTransaminaseForm,
    SerumCreatinineForm, BloodUreaNitrogenForm, TotalBilirubinForm, BloodFatForm
]}
'''


class PhyExamFormPreview(FormPreview):
    form_template = 'ehr/phy_exam_form.html'
    preview_template = 'ehr/phy_exam_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['type_alias'] = kwargs['type_alias']
        self.state['item_alias'] = kwargs['item_alias']
        self.state['model_name'] = kwargs['model_name']

    def get_context(self, request, form):
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)

        new_year_day = datetime(datetime.today().year, 1, 1)

        records = WorkRecord.objects.filter(resident=resident, begin_time__gt=new_year_day).order_by('submit_time')
        results = {'doctor_name': request.user.username, 'check_date': datetime.today()}
        for record in records:
            try:
                ModelName = apps.get_model(app_label='ehr', model_name=record.model_name)
            except LookupError:
                continue
            record_detail = ModelName.objects.get(id=record.item_id)
            results[record.service_item.alias] = record_detail

        service_type = Service.objects.get(alias=self.state['type_alias'])
        service_items = Service.items.filter(service_type__alias=self.state['type_alias'])
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return dict({'form': form, 'service_type': service_type,
                     'service_items_id_highlight': service_items_id_highlight,
                     'stage_field': self.unused_name('stage'), 'state': self.state}.items() + results.items())

    def done(self, request, cleaned_data):
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            form = OldBodyCheckForm(request.POST)
        elif self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'psychiatric':
            form = PsyBodyCheckForm(request.POST)
        group_result = form.save()

        if True:
            # 一般体格检查
            form = PhysicalExaminationForm(request.POST)
            service_result = form.save()

            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                get(alias=form.Meta.alias)
            record.app_label = self.state['type_alias']
            record.model_name = form.Meta.model.__name__
            record.service_item_alias = form.Meta.alias
            record.item_id = service_result.id
            record.group_item_id = group_result.id
            record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 血常规服务记录
        if True:
            if cleaned_data.get('hemoglobin') \
                    and cleaned_data.get('leucocyte') \
                    and cleaned_data.get('blood_platelets'):

                form = BloodRoutineTestForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.submit_time = datetime.now()
                    record.item_id = service_result.id
                    record.status = WorkRecord.FINISHED
                    record.save()

        # 尿常规服务记录
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            if cleaned_data.get('urine_protein') \
                    and cleaned_data.get('urine_glucose') \
                    and cleaned_data.get('ketone_bodies') \
                    and cleaned_data.get('occult_blood'):

                form = UrineRoutineTestForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.submit_time = datetime.now()
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.status = WorkRecord.FINISHED
                    record.save()

        # 血糖
        if True:
            if cleaned_data.get('blood_glucose_mmol') \
                    or cleaned_data.get('blood_glucose_mg'):

                form = BloodGlucoseForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 心电图
        if True:
            if cleaned_data.get('electr_gram'):
                form = ElectrocardiogramForm(request.POST)
                if form.is_valid():
                    service_result = form.save()

                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 血清谷丙转氨酶
        if True:
            if cleaned_data.get('alt'):
                form = AlanineAminotransferaseForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 血清谷草转氨酶
        if True:
            if cleaned_data.get('ast'):
                form = GlutamicOxalaceticTransaminaseForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 血清肌酐
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            if cleaned_data.get('scr'):
                form = SerumCreatinineForm(request.POST)
                if form.is_valid():
                    service_result = form.save()

                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 血尿素氮
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            if cleaned_data.get('bun'):
                form = BloodUreaNitrogenForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 总胆红素
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            if cleaned_data.get('tbil'):
                form = TotalBilirubinForm(request.POST)
                if form.is_valid():
                    service_result = form.save()
                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()

        # 血脂
        if self.state['item_alias'] == 'body_check' and self.state['type_alias'] == 'old':
            if cleaned_data.get('tc') and cleaned_data.get('tg') and cleaned_data.get('ldl_c') \
                    and cleaned_data.get('hdl_c'):
                form = BloodFatForm(request.POST)
                if form.is_valid():
                    service_result = form.save()

                    record = WorkRecord()
                    record.provider = request.user
                    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
                    record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
                        get(alias=form.Meta.alias)
                    record.app_label = self.state['type_alias']
                    record.model_name = form.Meta.model.__name__
                    record.service_item_alias = form.Meta.alias
                    record.group_item_id = group_result.id
                    record.item_id = service_result.id
                    record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
                    record.status = WorkRecord.FINISHED
                    record.submit_time = datetime.now()
                    record.save()


        # for session_para in ['resident_id', 'resident_name',
        # 'service_items_id_highlight']:
        # try:
        # request.session[session_para]
        #    except KeyError:
        #        pass
        #    else:
        #        del request.session[session_para]
        return HttpResponseRedirect('/services/service_grid/')