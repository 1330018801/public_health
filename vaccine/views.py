#-*- coding: utf-8 -*-

from datetime import datetime, date
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from management.models import WorkRecord, Resident, Service
from management.views import getmodelfield
from vaccine.forms import VaccineCardForm
from vaccine.models import VaccineCard, Vaccination

import logging
debug = logging.getLogger('debug')


def vaccine_index(request):
        resident_id = int(request.session.get('resident_id'))
        resident = Resident.objects.get(id=resident_id)
        try:
            resident.vaccinecard
        except ObjectDoesNotExist:
            vaccine_card = None
        else:
            vaccine_card = resident.vaccinecard

        records = WorkRecord.objects.filter(resident=resident, app_label='vaccine')
        results = dict()
        for record in records:
            ModelName = apps.get_model(app_label=record.app_label, model_name=record.model_name)
            record_detail = ModelName.objects.get(id=record.item_id)
            results[record.service_item.alias] = record_detail

        service_type = Service.objects.get(alias='vaccine')
        service_items = Service.items.filter(service_type__alias='vaccine')
        service_items_id = []
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

        return render(request, 'vaccine/vaccine_form.html',
                      dict(
                           {'service_type': service_type,
                            'service_items_id_highlight': service_items_id_highlight,
                            'vaccine_card': vaccine_card}.items()
                           + results.items()
        ))


def vaccine_card(request):
    resident = Resident.objects.get(id=int(request.session.get('resident_id')))
    card = None

    if request.method == 'POST':
        form = VaccineCardForm(request.POST)
        try:
            #card = VaccineCard.objects.get(name=resident.name)
            work_record = WorkRecord.objects.get(resident=resident, service_item_alias='vaccine_card')
        except WorkRecord.DoesNotExist:
            if form.is_valid():
                item = form.save()
                record = WorkRecord()
                record.provider = request.user
                record.resident = resident
                record.service_item = Service.objects.filter(service_type__alias='vaccine').\
                    get(alias='vaccine_card')
                record.app_label = 'vaccine'
                record.model_name = form.Meta.model.__name__
                record.service_item_alias = 'vaccine_card'
                record.item_id = item.id
                record.evaluation = WorkRecord.SATISFIED
                record.submit_time = datetime.now()
                record.status = WorkRecord.FINISHED
                record.save()
                if request.session['resident_id']:
                    del request.session['resident_id']
                return HttpResponseRedirect(reverse('services:service_grid'))

        else:
            if form.is_valid():
                card = VaccineCard.objects.get(id=work_record.item_id)
                card.name = request.POST.get('name')
                card.number = request.POST.get('number')
                card.gender = request.POST.get('gender')
                if request.POST.get('birth_date'):
                    birth_date = datetime.strptime(request.POST.get('birth_date'), '%Y-%m-%d')
                    card.birth_date = birth_date
                card.guardian_name = request.POST.get('guardian_name')
                card.relation_to_child = request.POST.get('relation_to_child')
                card.contact_number = request.POST.get('contact_number')
                card.home_address = request.POST.get('home_address')
                card.census_register_address_extra = request.POST.get('census_register_address_extra')
                if request.POST.get('immigrate_time'):
                    immigrate_time = datetime.strptime(request.POST.get('immigrate_time'), '%Y-%m-%d')
                    card.immigrate_time = immigrate_time.date()
                if request.POST.get('emigrate_time'):
                    emigrate_time = datetime.strptime(request.POST.get('emigrate_time'), '%Y-%m-%d')
                    card.emigrate_time = emigrate_time.date()
                card.emigrate_reason = request.POST.get('emigrate_reason')
                card.vaccine_abnormal_reaction_history = request.POST.get('vaccine_abnormal_reaction_history')
                card.vaccinate_taboo = request.POST.get('vaccinate_taboo')
                card.infection_history = request.POST.get('infection_history')
                card.save()
                return HttpResponseRedirect(reverse('services:service_grid'))

    else:
        try:
            #card = VaccineCard.objects.get(name=resident.name)
            work_record = WorkRecord.objects.get(resident=resident, service_item_alias='vaccine_card')
        except WorkRecord.DoesNotExist:
            form = VaccineCardForm()
        else:
            card = VaccineCard.objects.get(id=work_record.item_id)
            form = card

    service_items = Service.items.filter(service_type__alias='vaccine')
    service_items_id = []

    for item in service_items:
        service_items_id.append(item.id)
    service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

    field_card = getmodelfield('vaccine', 'VaccineCard')
    service_type = Service.objects.get(alias='vaccine')
    service_item = service_type.service_items.get(alias='vaccine_card')
    found_card_date = date.today().strftime('%Y-%m-%d')
    return render(request, 'vaccine/vaccine_card.html', {
        'field_card': field_card,
        'service_type': service_type,
        'service_item': service_item,
        'found_card_date': found_card_date,
        'form': form,
        'card': card,
        'service_items_id_highlight': service_items_id_highlight
    })

from django.forms.models import model_to_dict
from django.http import JsonResponse


def vaccine_page(request):
    return render(request, 'vaccine/vaccine_card_new.html')


def vaccine_records(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    vaccine_service_items = Service.items.filter(service_type__alias='vaccine')

    json_items = []
    for service_item in vaccine_service_items:
        if service_item.name != u'预防接种卡':
            item = model_to_dict(service_item, fields=['id', 'name'])
            try:
                record = WorkRecord.objects.get(resident=resident, service_item=service_item)
            except WorkRecord.DoesNotExist:
                pass
            else:
                '''
                vaccine_service = apps.get_model(app_label=record.app_label, model_name=record.model_name)
                service_result = vaccine_service.objects.get(id=record.item_id)
                '''
                service_result = Vaccination.objects.get(id=record.item_id)
                item['doctor_signature'] = record.provider.username
                item['visit_date'] = service_result.visit_date.strftime('%Y-%m-%d')
                item['vaccinate_position'] = service_result.vaccinate_position
                item['batch_number'] = service_result.batch_number
                item['remarks'] = service_result.remarks
                item['next_vaccinate_date'] = service_result.next_vaccinate_date.strftime('%Y-%m-%d')

            json_items.append(item)

    return JsonResponse(json_items, safe=False)


def vaccine_card_head(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    '''
    try:
        record = WorkRecord.objects.get(resident=resident, service_item__alias='vaccine_cared')
    except WorkRecord.DoesNotExist:
        success = False
        message = ''
    else:
        success = True
        vaccine_card = apps.get_model(app_label='vaccine', model_name=record.model_name)
        service_result = vaccine_card.objects.get(id=record.item_id)
        form = VaccineCardForm(instance=service_result)
        message = render(request, 'vaccine/vaccine_card_preview_content.html', {'form': form}).content
    '''
    if resident.vaccine_card:
        success = True
        message = render(request, 'vaccine/vaccine_card_review_content.html',
                         {'form': resident.vaccine_card, 'resident': resident}).content
    else:
        success = False
        message = '未建卡'
    return JsonResponse({'success': success, 'message': message})


def vaccine_card_head_save(request):
    form = VaccineCardForm(request.POST)
    if form.is_valid():
        result = form.save()
        resident = Resident.objects.get(id=int(request.POST.get('resident_id')))
        resident.vaccine_card = result
        if resident.ehr_no is None:
            if result.register_local:
                resident.ehr_no = result.home_town.id + result.ehr_village_no + result.ehr_unique_no
            else:
                resident.ehr_no = '131082900' + result.ehr_village_no + result.ehr_unique_no
        resident.save()
        service_item = Service.items.get(alias='vaccine_card')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='vaccine', model_name='VaccineCard', item_id=result.id,
                            service_item_alias='vaccine_card', evaluation=WorkRecord.SATISFIED,
                            status=WorkRecord.FINISHED)
        record.save()
        success = True
        message = u'新生儿建卡完成'
    else:
        debug.info(form.errors.as_data())
        success = False
        message = u'新生儿建卡失败'

    return JsonResponse({'success': success, 'message': message})


def vaccinate_submit(request):
    service_item = Service.items.get(id=int(request.POST.get('id')))
    vaccine = Vaccination(vaccine=service_item,
                          visit_date=request.POST.get('visit_date'),
                          vaccinate_position=request.POST.get('vaccinate_position'),
                          batch_number=request.POST.get('batch_number'),
                          remarks=request.POST.get('remarks'),
                          doctor_signature=request.POST.get('doctor_signature'),
                          next_vaccinate_date=request.POST.get('next_vaccinate_date'))
    vaccine.save()
    resident_id = request.session.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))
    record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                        app_label='vaccine', model_name='Vaccination', item_id=vaccine.id,
                        service_item_alias=service_item.alias, evaluation=WorkRecord.SATISFIED,
                        status=WorkRecord.FINISHED)

    record.save()

    return JsonResponse({'success': True})
