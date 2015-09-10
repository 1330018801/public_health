# -*- coding: utf-8 -*-
from datetime import datetime
import logging

from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from django.apps import apps

from management.models import Service, WorkRecord, Resident
from .forms import *

log = logging.getLogger('debug')


'''
class Aftercare1FormPreview(FormPreview):
    form_template = 'pregnant/antenatal_1_form.html'
    preview_template = 'pregnant/antenatal_1_preview.html'

    def parse_params(self, *args, **kwargs):
        self.state['item_alias'] = kwargs['item_alias']
        self.state['model_name'] = kwargs['model_name']

    def get_context(self, request, form):
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)

        m10_ago = date.today() - timedelta(days=300)
        records = WorkRecord.objects.filter(app_label='pregnant', resident=resident,
                                            submit_time__gt=m10_ago).order_by('submit_time')
        results = {}
        for record in records:
            try:
                ModelName = apps.get_model(app_label='pregnant', model_name=record.model_name)
            except LookupError:
                continue
            record_detail = ModelName.objects.get(id=record.item_id)
            results[record.service_item.alias] = record_detail

        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return dict({'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}.items() + results.items())

    def done(self, request, cleaned_data):
        ModelName = apps.get_model(app_label='pregnant', model_name=self.state['model_name'])

        if self.state['item_alias'] == 'physical_examination':
            disease_history = cleaned_data.pop('disease_history')
            family_history = cleaned_data.pop('family_history')
            personal_history = cleaned_data.pop('personal_history')
            guide = cleaned_data.pop('guide')

            service_result = ModelName(**cleaned_data)
            service_result.save()

            for item in disease_history:
                service_result.disease_history.add(item)
            for item in family_history:
                service_result.family_history.add(item)
            for item in personal_history:
                service_result.personal_history.add(item)
            for item in guide:
                service_result.guide.add(item)
        else:
            service_result = ModelName(**cleaned_data)
            service_result.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant'). \
            get(alias=self.state['item_alias'])
        record.app_label = 'pregnant'
        record.model_name = self.state['model_name']
        record.service_item_alias = self.state['item_alias']
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        return HttpResponseRedirect('/pregnant/')
'''


class Aftercare1FormPreview(FormPreview):
    form_template = 'pregnant/antenatal_1_form.html'
    preview_template = 'pregnant/antenatal_1_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
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

        # 一般体格检查服务记录
        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant'). \
            get(alias='physical_examination')
        record.app_label = 'pregnant'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'physical_examination'
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.status = WorkRecord.FINISHED
        record.submit_time = datetime.now()
        record.save()

        # 妇科检查服务记录
        if cleaned_data.get('vulva') \
                and cleaned_data.get('vagina') \
                and cleaned_data.get('cervix') \
                and cleaned_data.get('uteri') \
                and cleaned_data.get('accessory'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant'). \
                get(alias='gynaecological_examination')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'gynaecological_examination'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 血常规服务记录
        if cleaned_data.get('hemoglobin') \
                and cleaned_data.get('leukocyte') \
                and cleaned_data.get('thrombocyte'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='blood_routine_test')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'blood_routine_test'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 尿常规服务记录
        if cleaned_data.get('urine_protein') \
                and cleaned_data.get('urine_glucose') \
                and cleaned_data.get('urine_ket') \
                and cleaned_data.get('urine_ery'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='urine_routine_test')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'urine_routine_test'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 血型服务记录
        if cleaned_data.get('blood_type_abo') and cleaned_data.get('blood_type_rh'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='blood_type')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'blood_type'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 谷丙转氨酶服务记录
        if cleaned_data.get('sgpt'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='alanine_aminotransferase')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'alanine_aminotransferase'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 谷草转氨酶服务记录
        if cleaned_data.get('sgot'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='glutamic_oxalacetic_transaminase')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'glutamic_oxalacetic_transaminase'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 总胆红素服务记录
        if cleaned_data.get('tbil'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='total_bilirubin')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'total_bilirubin'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 血清肌酐服务记录
        if cleaned_data.get('scr'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='serum_creatinine')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'serum_creatinine'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 血尿素氮服务记录
        if cleaned_data.get('bun'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='blood_urea_nitrogen')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'blood_urea_nitrogen'
            record.item_id = service_result.id
            record.evaluation = WorkRecord.SATISFIED
            record.status = WorkRecord.FINISHED
            record.submit_time = datetime.now()
            record.save()

        # 乙型肝炎五项服务记录

        if cleaned_data.get('surface_antigen') \
                and cleaned_data.get('surface_antibody') \
                and cleaned_data.get('e_antigen') \
                and cleaned_data.get('e_antibody') \
                and cleaned_data.get('core_antibody'):
            record = WorkRecord()
            record.provider = request.user
            record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
            record.service_item = Service.objects.filter(service_type__alias='pregnant')\
                .get(alias='hepatitis_b_five_item')
            record.app_label = 'pregnant'
            record.model_name = form.Meta.model.__name__  # Test
            record.service_item_alias = 'hepatitis_b_five_item'
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
    form_template = 'pregnant/antenatal_2_form.html'
    preview_template = 'pregnant/antenatal_2_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare2Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='aftercare_2')
        record.app_label = 'pregnant'
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
    form_template = 'pregnant/antenatal_3_form.html'
    preview_template = 'pregnant/antenatal_3_preview.html'

    def get_context(self, request, form):
        aftercare2 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_2')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare2)
        except WorkRecord.DoesNotExist:
            aftercare2_result = None
        else:
            aftercare2_result = Aftercare2.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare2': aftercare2_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare3Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='aftercare_3')
        record.app_label = 'pregnant'
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
    form_template = 'pregnant/antenatal_4_form.html'
    preview_template = 'pregnant/antenatal_4_preview.html'

    def get_context(self, request, form):
        aftercare2 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_2')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare2)
        except WorkRecord.DoesNotExist:
            aftercare2_result = None
        else:
            aftercare2_result = Aftercare2.objects.get(id=record.item_id)

        aftercare3 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_3')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare3)
        except WorkRecord.DoesNotExist:
            aftercare3_result = None
        else:
            aftercare3_result = Aftercare3.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare2': aftercare2_result,
                'aftercare3': aftercare3_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare4Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='aftercare_4')
        record.app_label = 'pregnant'
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


class Aftercare5FormPreview(FormPreview):
    form_template = 'pregnant/antenatal_5_form.html'
    preview_template = 'pregnant/antenatal_5_preview.html'

    def get_context(self, request, form):
        aftercare2 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_2')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare2)
        except WorkRecord.DoesNotExist:
            aftercare2_result = None
        else:
            aftercare2_result = Aftercare2.objects.get(id=record.item_id)

        aftercare3 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_3')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare3)
        except WorkRecord.DoesNotExist:
            aftercare3_result = None
        else:
            aftercare3_result = Aftercare3.objects.get(id=record.item_id)

        aftercare4 = Service.objects.filter(service_type__alias='pregnant').get(alias='aftercare_4')
        resident = Resident.objects.get(id=request.session.get('resident_id'))
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=aftercare4)
        except WorkRecord.DoesNotExist:
            aftercare4_result = None
        else:
            aftercare4_result = Aftercare4.objects.get(id=record.item_id)

        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type, 'aftercare2': aftercare2_result,
                'aftercare3': aftercare3_result, 'aftercare4': aftercare4_result,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Aftercare5Form(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='aftercare_5')
        record.app_label = 'pregnant'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'aftercare_5'
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


class PostpartumVisitFromPreview(FormPreview):
    form_template = 'pregnant/postpartum_form.html'
    preview_template = 'pregnant/postpartum_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = PostpartumVisitForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='postpartum_visit')
        record.app_label = 'pregnant'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'postpartum_visit'
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


class Postpartum42ExamFormPreview(FormPreview):
    form_template = 'pregnant/postpartum42_form.html'
    preview_template = 'pregnant/postpartum42_preview.html'

    def get_context(self, request, form):
        service_type = Service.objects.get(alias='pregnant')
        service_items = Service.items.filter(service_type__alias='pregnant')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
        return {'form': form, 'service_type': service_type,
                'service_items_id_highlight': service_items_id_highlight,
                'stage_field': self.unused_name('stage'), 'state': self.state}

    def done(self, request, cleaned_data):
        form = Postpartum42ExamForm(request.POST)
        service_result = form.save()

        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias='pregnant')\
            .get(alias='postpartum_42_day_examination')
        record.app_label = 'pregnant'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = 'postpartum_42_day_examination'
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