from datetime import datetime
from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from child.forms import *
from management.models import Service, WorkRecord, Resident

__author__ = 'Administrator'


class NewbornFamilyVisitFormPreview(FormPreview):
    form_template = 'child/newborn_family_visit_form.html'
    preview_template = 'child/newborn_family_visit_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = NewbornFamilyVisitForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='newborn_family_visit')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'newborn_family_visit'
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
    
    
class Aftercare1MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_1_month_form.html'
    preview_template = 'child/aftercare_1_month_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare1MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_1_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_1_month'
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


class Aftercare3MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_3_month_form.html'
    preview_template = 'child/aftercare_3_month_preview.html'

    def get_context(self, request, form):
        aftercare_1_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_1_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_1_month)
        except WorkRecord.DoesNotExist:
            aftercare_1_month_result = None
        else:
            aftercare_1_month_result = Aftercare1Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_1_month': aftercare_1_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare3MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_3_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_3_month'
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
 
    
class Aftercare6MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_6_month_form.html'
    preview_template = 'child/aftercare_6_month_preview.html'

    def get_context(self, request, form):
        aftercare_1_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_1_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_1_month)
        except WorkRecord.DoesNotExist:
            aftercare_1_month_result = None
        else:
            aftercare_1_month_result = Aftercare1Month.objects.get(id=record.item_id)

        aftercare_3_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_3_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_3_month)
        except WorkRecord.DoesNotExist:
            aftercare_3_month_result = None
        else:
            aftercare_3_month_result = Aftercare3Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_1_month': aftercare_1_month_result,
                'aftercare_3_month': aftercare_3_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare6MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_6_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_6_month'
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
    
    
class Aftercare8MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_8_month_form.html'
    preview_template = 'child/aftercare_8_month_preview.html'

    def get_context(self, request, form):
        aftercare_1_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_1_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_1_month)
        except WorkRecord.DoesNotExist:
            aftercare_1_month_result = None
        else:
            aftercare_1_month_result = Aftercare1Month.objects.get(id=record.item_id)

        aftercare_3_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_3_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_3_month)
        except WorkRecord.DoesNotExist:
            aftercare_3_month_result = None
        else:
            aftercare_3_month_result = Aftercare3Month.objects.get(id=record.item_id)

        aftercare_6_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_6_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_6_month)
        except WorkRecord.DoesNotExist:
            aftercare_6_month_result = None
        else:
            aftercare_6_month_result = Aftercare6Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_1_month': aftercare_1_month_result,
                'aftercare_3_month': aftercare_3_month_result, 'aftercare_6_month': aftercare_6_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare8MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_8_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_8_month'
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


class Aftercare12MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_12_month_form.html'
    preview_template = 'child/aftercare_12_month_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare12MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_12_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_12_month'
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


class Aftercare18MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_18_month_form.html'
    preview_template = 'child/aftercare_18_month_preview.html'

    def get_context(self, request, form):
        aftercare_12_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_12_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_12_month)
        except WorkRecord.DoesNotExist:
            aftercare_12_month_result = None
        else:
            aftercare_12_month_result = Aftercare12Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_12_month': aftercare_12_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare18MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_18_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_18_month'
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


class Aftercare24MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_24_month_form.html'
    preview_template = 'child/aftercare_24_month_preview.html'

    def get_context(self, request, form):
        aftercare_12_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_12_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_12_month)
        except WorkRecord.DoesNotExist:
            aftercare_12_month_result = None
        else:
            aftercare_12_month_result = Aftercare12Month.objects.get(id=record.item_id)

        aftercare_18_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_18_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_18_month)
        except WorkRecord.DoesNotExist:
            aftercare_18_month_result = None
        else:
            aftercare_18_month_result = Aftercare18Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_12_month': aftercare_12_month_result,
                'aftercare_18_month': aftercare_18_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare24MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_24_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_24_month'
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


class Aftercare30MonthFormPreview(FormPreview):
    form_template = 'child/aftercare_30_month_form.html'
    preview_template = 'child/aftercare_30_month_preview.html'

    def get_context(self, request, form):
        aftercare_12_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_12_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_12_month)
        except WorkRecord.DoesNotExist:
            aftercare_12_month_result = None
        else:
            aftercare_12_month_result = Aftercare12Month.objects.get(id=record.item_id)

        aftercare_18_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_18_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_18_month)
        except WorkRecord.DoesNotExist:
            aftercare_18_month_result = None
        else:
            aftercare_18_month_result = Aftercare18Month.objects.get(id=record.item_id)

        aftercare_24_month = Service.objects.filter(service_type__alias='child').get(alias='aftercare_24_month')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_24_month)
        except WorkRecord.DoesNotExist:
            aftercare_24_month_result = None
        else:
            aftercare_24_month_result = Aftercare24Month.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_12_month': aftercare_12_month_result,
                'aftercare_18_month': aftercare_18_month_result, 'aftercare_24_month': aftercare_24_month_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare30MonthForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_30_month')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_30_month'
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


class Aftercare3YearFormPreview(FormPreview):
    form_template = 'child/aftercare_3_year_form.html'
    preview_template = 'child/aftercare_3_year_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare3YearForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_3_year')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_3_year'
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


class Aftercare4YearFormPreview(FormPreview):
    form_template = 'child/aftercare_4_year_form.html'
    preview_template = 'child/aftercare_4_year_preview.html'

    def get_context(self, request, form):
        aftercare_3_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_3_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_3_year)
        except WorkRecord.DoesNotExist:
            aftercare_3_year_result = None
        else:
            aftercare_3_year_result = Aftercare3Year.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_3_year': aftercare_3_year_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare4YearForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_4_year')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_4_year'
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


class Aftercare5YearFormPreview(FormPreview):
    form_template = 'child/aftercare_5_year_form.html'
    preview_template = 'child/aftercare_5_year_preview.html'

    def get_context(self, request, form):
        aftercare_3_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_3_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_3_year)
        except WorkRecord.DoesNotExist:
            aftercare_3_year_result = None
        else:
            aftercare_3_year_result = Aftercare3Year.objects.get(id=record.item_id)

        aftercare_4_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_4_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_4_year)
        except WorkRecord.DoesNotExist:
            aftercare_4_year_result = None
        else:
            aftercare_4_year_result = Aftercare4Year.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_3_year': aftercare_3_year_result,
                'aftercare_4_year': aftercare_4_year_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare5YearForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_5_year')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_5_year'
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


class Aftercare6YearFormPreview(FormPreview):
    form_template = 'child/aftercare_6_year_form.html'
    preview_template = 'child/aftercare_6_year_preview.html'

    def get_context(self, request, form):
        aftercare_3_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_3_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_3_year)
        except WorkRecord.DoesNotExist:
            aftercare_3_year_result = None
        else:
            aftercare_3_year_result = Aftercare3Year.objects.get(id=record.item_id)

        aftercare_4_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_4_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_4_year)
        except WorkRecord.DoesNotExist:
            aftercare_4_year_result = None
        else:
            aftercare_4_year_result = Aftercare4Year.objects.get(id=record.item_id)

        aftercare_5_year = Service.objects.filter(service_type__alias='child').get(alias='aftercare_5_year')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare_5_year)
        except WorkRecord.DoesNotExist:
            aftercare_5_year_result = None
        else:
            aftercare_5_year_result = Aftercare5Year.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='child')
        service_items = Service.items.filter(service_type__alias='child')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare_3_year': aftercare_3_year_result,
                'aftercare_4_year': aftercare_4_year_result, 'aftercare_5_year': aftercare_5_year_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare6YearForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='child')\
            .get(alias='aftercare_6_year')
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_6_year'
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