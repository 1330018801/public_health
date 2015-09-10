from datetime import datetime
from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from hypertension.forms import *
from management.models import Service, WorkRecord, Resident

__author__ = 'Administrator'


class Aftercare1FormPreview(FormPreview):
    form_template = 'hypertension/aftercare_1_form.html'
    preview_template = 'hypertension/aftercare_1_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='hypertension')
        service_items = Service.items.filter(service_type__alias='hypertension')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare1Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='hypertension')\
            .get(alias='aftercare_1')
        record.app_label = 'hypertension'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_1'
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

        return HttpResponseRedirect('/services/service_grid/')


class Aftercare2FormPreview(FormPreview):
    form_template = 'hypertension/aftercare_2_form.html'
    preview_template = 'hypertension/aftercare_2_preview.html'

    def get_context(self, request, form):
        aftercare1 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_1')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare1, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare1_result = None
        else:
            aftercare1_result = Aftercare1.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='hypertension')
        service_items = Service.items.filter(service_type__alias='hypertension')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare1': aftercare1_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare2Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='hypertension')\
            .get(alias='aftercare_2')
        record.app_label = 'hypertension'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_2'
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

        return HttpResponseRedirect('/services/service_grid/')
 
    
class Aftercare3FormPreview(FormPreview):
    form_template = 'hypertension/aftercare_3_form.html'
    preview_template = 'hypertension/aftercare_3_preview.html'

    def get_context(self, request, form):
        aftercare1 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_1')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare1, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare1_result = None
        else:
            aftercare1_result = Aftercare1.objects.get(id=record.item_id)

        aftercare2 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_2')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare2, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare2_result = None
        else:
            aftercare2_result = Aftercare2.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='hypertension')
        service_items = Service.items.filter(service_type__alias='hypertension')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare1': aftercare1_result,
                'aftercare2': aftercare2_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare3Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='hypertension')\
            .get(alias='aftercare_3')
        record.app_label = 'hypertension'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_3'
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

        return HttpResponseRedirect('/services/service_grid/')
    
    
class Aftercare4FormPreview(FormPreview):
    form_template = 'hypertension/aftercare_4_form.html'
    preview_template = 'hypertension/aftercare_4_preview.html'

    def get_context(self, request, form):
        aftercare1 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_1')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare1, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare1_result = None
        else:
            aftercare1_result = Aftercare1.objects.get(id=record.item_id)

        aftercare2 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_2')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare2, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare2_result = None
        else:
            aftercare2_result = Aftercare2.objects.get(id=record.item_id)

        aftercare3 = Service.objects.filter(service_type__alias='hypertension').get(alias='aftercare_3')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare3, submit_time__year=datetime.today().year)
        except WorkRecord.DoesNotExist:
            aftercare3_result = None
        else:
            aftercare3_result = Aftercare3.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='hypertension')
        service_items = Service.items.filter(service_type__alias='hypertension')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare1': aftercare1_result,
                'aftercare2': aftercare2_result, 'aftercare3': aftercare3_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare4Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='hypertension')\
            .get(alias='aftercare_4')
        record.app_label = 'hypertension'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_4'
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

        return HttpResponseRedirect('/services/service_grid/')