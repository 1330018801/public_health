# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Service, WorkRecord, Resident
from ehr.models import ConstitutionIdentification
from .models import *


class ConstitutionIdentificationFormPreview(FormPreview):
    form_template = 'ehr/phy_exam_form.html'
    preview_template = 'ehr/phy_exam_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='tcm')
        service_items = Service.items.filter(service_type__alias='tcm')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        service_result = ConstitutionIdentification(**cleaned_data)
        service_result.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='tcm'). \
            get(alias='constitution_identification')
        record.app_label = 'tcm'
        record.model_name = 'ConstitutionIdentification'
        record.service_item_alias = 'constitution_identification'
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        return HttpResponseRedirect('/tcm/')


class ChildAftercareFromPreview(FormPreview):
    form_template = 'tcm/tcm_child_form.html'
    preview_template = 'tcm/tcm_child_preview.html'
    
    def parse_params(self, *args, **kwargs):
        self.state['item_alias'] = kwargs['item_alias']
        self.state['model_name'] = kwargs['model_name']

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='tcm')
        service_items = Service.items.filter(service_type__alias='tcm')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        ModelName = apps.get_model(app_label='tcm', model_name=self.state['model_name'])
        guide = cleaned_data.pop('guide')
        service_result = ModelName(**cleaned_data)
        service_result.save()

        for item in guide:
            service_result.guide.add(item)

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='tcm'). \
            get(alias=self.state['item_alias'])
        record.app_label = 'tcm'
        record.model_name = self.state['model_name']
        record.service_item_alias = self.state['item_alias']
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        return HttpResponseRedirect('/tcm/')
