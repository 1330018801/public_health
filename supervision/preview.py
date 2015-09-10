# -*- coding: utf-8 -*-
from datetime import datetime, date
import logging

from django.contrib.formtools.preview import FormPreview
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from management.models import Service, WorkRecord, Resident
from .forms import *

log = logging.getLogger('debug')


class PatrolFormPreview(FormPreview):
    form_template = 'supervision/patrol_form.html'
    preview_template = 'supervision/patrol_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='supervision')
        if request.user.is_superuser or request.user.userprofile.role.name == u'全局管理员':
            records = Patrol.objects.filter(patrol_date__year=date.today().year)
        else:
            try:
                records = Patrol.objects.filter(patrol_date__year=date.today().year, institution=request.user.userprofile.clinic.name)
            except Patrol.DoesNotExist:
                records = None
            else:
                pass

        return {'form': form, 'service_type': service_type,
                'records': records, 'year': request.POST.get('year'),
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = PatrolForm(request.POST)
        service_result = form.save()

        # 一般体格检查服务记录
        record = WorkRecord()
        record.provider = request.user
        try:
            resident = Resident.objects.get(name='没有人')
        except Resident.DoesNotExist:
            resident = Resident(name='没有人', gender=2, nation='汉族', birthday=date(1900, 1, 1))
            resident.save()
        else:
            pass
        record.resident = resident
        record.service_item = Service.objects.filter(service_type__alias='supervision'). \
            get(alias='patrol')
        record.app_label = 'supervision'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'patrol'
        record.item_id = service_result.id
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

        return HttpResponseRedirect(reverse('management:index'))


class InformationReportFormPreview(FormPreview):
    form_template = 'supervision/information_report_form.html'
    preview_template = 'supervision/information_report_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='supervision')
        if request.user.is_superuser or request.user.userprofile.role.name == u'全局管理员' :
            records = InformationReport.objects.all()
        else:
            try:
                records = InformationReport.objects.filter(institution=request.user.userprofile.clinic.name)
            except InformationReport.DoesNotExist:
                records = None
            else:
                pass

        return {'form': form, 'service_type': service_type,
                'records': records,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = InformationReportForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        try:
            resident = Resident.objects.get(name='没有人')
        except Resident.DoesNotExist:
            resident = Resident(name='没有人', gender=2, nation='汉族', birthday=date(1900, 1, 1))
            resident.save()
        else:
            pass
        record.resident = resident
        record.service_item = Service.objects.filter(service_type__alias='supervision')\
            .get(alias='information_report')
        record.app_label = 'supervision'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'information_report'
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED
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

        return HttpResponseRedirect(reverse('management:index'))


