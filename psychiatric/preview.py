# -*- coding: utf-8 -*-
from datetime import datetime
import logging

from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Resident, Service, WorkRecord

log = logging.getLogger('debug')


class PsyVisitFormPreview(FormPreview):
    form_template = 'psychiatric/psy_visit_form.html'
    preview_template = 'psychiatric/psy_visit_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['type_alias'] = kwargs['type_alias']
        self.state['item_alias'] = kwargs['item_alias']
        self.state['model_name'] = kwargs['model_name']

    def get_context(self, request, form):
        service_type = Service.objects.get(alias=self.state['type_alias'])
        service_items = Service.items.filter(service_type__alias=self.state['type_alias'])
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        ModelName = apps.get_model(app_label=self.state['type_alias'], model_name=self.state['model_name'])

        if self.state['type_alias'] == 'psychiatric':
            now_symptom = cleaned_data.pop('now_symptom')
            recovery_measure = cleaned_data.pop('recovery_measure')
            data = ModelName(**cleaned_data)
            data.save()

            for item in now_symptom:
                data.now_symptom.add(item)

            for item in recovery_measure:
                data.recovery_measure.add(item)
        else:
            data = ModelName(**cleaned_data)
            data.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
            get(alias=self.state['item_alias'])
        record.app_label = self.state['type_alias']
        record.model_name = self.state['model_name']  # Test
        record.service_item_alias = self.state['item_alias']
        record.item_id = data.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        #for session_para in ['resident_id', 'resident_name',
        #                     'service_items_id_highlight']:
        #    try:
        #        request.session[session_para]
        #    except KeyError:
        #        pass
        #    else:
        #        del request.session[session_para]
        return HttpResponseRedirect('/services/service_grid/')
