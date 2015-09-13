#-*- coding: utf-8 -*-
import logging
import simplejson

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from management.models import WorkRecord, Resident, Service
from .forms import VaccineCardForm
from .models import Vaccination

debug = logging.getLogger('debug')


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
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


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
