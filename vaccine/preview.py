# -*- coding: utf-8 -*-
from datetime import datetime
import logging

from django.contrib.formtools.preview import FormPreview
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Resident, WorkRecord, Service
from models import VaccineCard

log = logging.getLogger('debug')


class VaccineFormPreview(FormPreview):
    form_template = 'vaccine/vaccine_form.html'
    preview_template = 'vaccine/vaccine_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['type_alias'] = kwargs['type_alias']
        self.state['item_alias'] = kwargs['item_alias']
        self.state['model_name'] = kwargs['model_name']

        #self.form_template = kwargs['type_alias'] + '/' + kwargs['item_alias'] + '_form.html'
        #self.preview_template = kwargs['type_alias'] + '/' + kwargs['item_alias'] + '_preview.html'

    def get_context(self, request, form):
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)
        vaccine_card = resident.vaccinecard

        records = WorkRecord.objects.filter(resident=resident, app_label=self.state['type_alias'])
        results = dict()
        for record in records:
            ModelName = apps.get_model(app_label=record.app_label, model_name=record.model_name)
            record_detail = ModelName.objects.get(id=record.item_id)
            results[record.service_item.alias] = record_detail

        service_type = Service.objects.get(alias=self.state['type_alias'])
        service_items = Service.items.filter(service_type__alias=self.state['type_alias'])
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

        return dict({
                'form': form,
                'service_type': service_type,
                'vaccine_card': vaccine_card,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'),
                'state': self.state}.items() + results.items())

    def done(self, request, cleaned_data):
        ModelName = apps.get_model(app_label=self.state['type_alias'], model_name=self.state['model_name'])
        data = ModelName(**cleaned_data)
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)
        data.resident = resident
        data.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = resident
        record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
            get(alias=self.state['item_alias'])
        record.app_label = self.state['type_alias']
        record.model_name = self.state['model_name']
        record.service_item_alias = self.state['item_alias']
        record.item_id = data.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        return HttpResponseRedirect('/' + self.state['type_alias'] + '/')


class VaccineCardFormPreview(FormPreview):
    form_template = 'vaccine/vaccine_card_setup_form.html'
    preview_template = 'vaccine/vaccine_card_setup_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='vaccine')
        service_items = Service.items.filter(service_type__alias='vaccine')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)

        try:
            resident.vaccinecard
        except ObjectDoesNotExist:
            pass
        else:
            existing_card = VaccineCard.objects.get(resident=resident)
            existing_card.delete()

        card = VaccineCard(**cleaned_data)
        card.resident = resident
        card.save()

        return HttpResponseRedirect('/vaccine/')
