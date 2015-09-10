from django.shortcuts import render_to_response
from django.template import RequestContext
from education.forms import AdBoardForm

__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from datetime import datetime
import logging

from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Resident, Service, WorkRecord

debug = logging.getLogger('debug')


class EducationRecordFormPreview(FormPreview):
    form_template = 'education/education_record_form_1.html'
    preview_template = 'education/education_record_preview.html'
    file = None
    post = None

    def parse_params(self, *args, **kwargs):
        self.state['type_alias'] = kwargs['type_alias']
        self.state['item_alias'] = kwargs['item_alias']
        self.state['form_name'] = kwargs['form_name']

    def get_context(self, request, form):
        service_type = Service.objects.get(alias=self.state['type_alias'])
        service_item = Service.items.get(alias=self.state['item_alias'])
        debug.info('The method is {0}'.format(request.method))

        return {'form': form, 'service_type': service_type,
                'service_item': service_item,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def preview_post(self, request):
        "Validates the POST data. If valid, displays the preview page. Else, redisplays form."
        f = self.form(request.POST, request.FILES, auto_id=self.get_auto_id())
        self.post = request.POST
        self.file = request.FILES
        context = self.get_context(request, f)
        if f.is_valid():
            debug.info('0The filename of {0} is {1}.post is {2}.file is {3}'.format('upload', request.FILES.get('upload'), request.POST, request.FILES))
            self.process_preview(request, f, context)
            context['hash_field'] = self.unused_name('hash')
            context['hash_value'] = self.security_hash(request, f)
            debug.info('1The filename of {0} is {1}.post is {2}.file is {3}'.format('upload', request.FILES.get('upload'), request.POST, request.FILES))
            return render_to_response(self.preview_template, context, context_instance=RequestContext(request))
        else:
            return render_to_response(self.form_template, context, context_instance=RequestContext(request))

    def post_post(self, request):
        "Validates the POST data. If valid, calls done(). Else, redisplays form."
        f = self.form(request.POST, request.FILES, auto_id=self.get_auto_id())
        debug.info('2The filename of {0} is {1}.post is {2}.files is {3}'.format('upload', request.FILES.get('upload'), request.POST, request.FILES))
        if f.is_valid():
            debug.info('3The filename of {0} is {1}.post is {2}.files is {3}'.format('upload', request.FILES.get('upload'), request.POST, request.FILES))
            if not self._check_security_hash(request.POST.get(self.unused_name('hash'), ''),
                                             request, f):
                return self.failed_hash(request)  # Security hash failed.
            return self.done(request, f.cleaned_data)
        else:
            return render_to_response(self.form_template,
                self.get_context(request, f),
                context_instance=RequestContext(request))

    def done(self, request, cleaned_data):
        #form_name = self.state['form_name']
        form = AdBoardForm(request.POST, request.FILES)
        debug.info('The filename of {0} is {1}'.format('upload', request.FILES.get('upload')))

        result = form.save()
        debug.info('The filename of {0} is {1}'.format('upload', result.upload))

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias=self.state['type_alias']). \
            get(alias=self.state['item_alias'])
        record.app_label = self.state['type_alias']
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = self.state['item_alias']
        record.item_id = result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        for session_para in ['resident_id', 'resident_name',
                             'service_items_id_highlight']:
            try:
                request.session[session_para]
            except KeyError:
                pass
            else:
                del request.session[session_para]
        return HttpResponseRedirect('/management/index/')