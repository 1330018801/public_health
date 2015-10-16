# -*- coding: utf-8 -*-
import logging
import simplejson

from django.http import HttpResponse
from django.shortcuts import render

from management.models import Service, WorkRecord
from services.utils import get_resident, new_year_day
from ehr.models import BodyExam
from ehr.forms import BodyExamForm, PhysicalExaminationForm, BloodRoutineTestForm,  \
    BloodGlucoseForm, ElectrocardiogramForm, AlanineAminotransferaseForm, \
    GlutamicOxalaceticTransaminaseForm
from .forms import AftercareForm, PsychiatricInfoForm
from .models import Aftercare

debug = logging.getLogger('debug')


def personal_info_page(request):
    resident = get_resident(request)
    form = PsychiatricInfoForm()
    return render(request, 'psychiatric/personal_info.html',
                  {'form': form, 'resident': resident})


def personal_info_table(request):
    resident = get_resident(request)
    if resident.psychiatric_info_table:
        form = PsychiatricInfoForm(instance=resident.psychiatric_info_table)
        return render(request, 'psychiatric/psychiatric_info_review_content.html',
                      {'form': form, 'resident': resident})
    else:
        form = PsychiatricInfoForm()
        return render(request, 'psychiatric/psychiatric_info_form_content.html',
                      {'form': form, 'resident': resident})


def personal_info_submit(request):
    form = PsychiatricInfoForm(request.POST)
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        resident.psychiatric_info_table = result
        resident.psychiatric = True
        resident.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def aftercare_page(request):
    return render(request, 'psychiatric/aftercare_page.html')


def aftercare_review(request):
    resident = get_resident(request)
    aftercare_status = dict()
    for item in range(1, 9):
        aftercare = 'aftercare_' + str(item)
        service_item = Service.items.get(alias=aftercare, service_type__alias='psychiatric')
        try:
            WorkRecord.objects.get(resident=resident, service_item=service_item, submit_time__gte=new_year_day())
        except WorkRecord.DoesNotExist:
            aftercare_status[aftercare] = False
        else:
            aftercare_status[aftercare] = True
    from django.http import JsonResponse
    return JsonResponse(aftercare_status)


def aftercare_form(request):
    resident = get_resident(request)
    item_alias = request.POST.get('item_alias')
    service_item = Service.objects.get(alias=item_alias, service_type__alias='psychiatric')
    try:
        record = WorkRecord.objects.get(resident=resident,
                                        service_item=service_item,
                                        submit_time__gte=new_year_day())
    except WorkRecord.DoesNotExist:
        form = AftercareForm()
        return render(request, 'psychiatric/psy_visit_form_content.html',
                      {'form': form, 'resident': resident})
    else:
        result = Aftercare.objects.get(id=record.item_id)
        form = AftercareForm(instance=result)
        return render(request, 'psychiatric/aftercare_review.html',
                      {'form': form, 'resident': resident})


def aftercare_submit(request):
    success = False
    form = AftercareForm(request.POST)
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        item_alias = request.POST.get('item_alias')
        service_item = Service.items.get(alias=item_alias,
                                         service_type__alias='psychiatric')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='psychiatric', model_name='Aftercare',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success})


def body_exam_page(request):
    return render(request, 'psychiatric/body_exam_page.html')


def body_exam_form(request):
    resident = get_resident(request)
    record = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                       submit_time__gte=new_year_day()).first()
    if record:
        result = BodyExam.objects.get(id=record.item_id)
        form = BodyExamForm(instance=result)
    else:
        form = BodyExamForm()
    return render(request, 'ehr/body_exam_form.html',
                  {'form': form, 'resident': resident, 'type_alias': 'psychiatric'})


def body_exam_suspend_submit(request, record):
    form = BodyExamForm(request.POST)
    if form.is_valid():
        submit_data = {field: value for field, value in form.cleaned_data.items() if value}
        result, created = BodyExam.objects.update_or_create(id=record.item_id, defaults=submit_data)
        if created:
            debug.info('create a new record BodyExam !!!')
        body_exam_commit_workrecord(request, record.resident, result)
        record.status = WorkRecord.SUSPEND_SUBMIT
        record.save()
        success = True
    else:
        success = False
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def body_exam_save(request, save_type):
    success = True
    resident = get_resident(request)
    record = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                       submit_time__gte=new_year_day()).first()
    form = BodyExamForm(request.POST)
    if form.is_valid():
        if record:
            submit_data = {field: value for field, value in form.cleaned_data.items() if value or value == 0}
            result, created = BodyExam.objects.update_or_create(id=record.item_id, defaults=submit_data)
            if created:
                debug.info('create a new record BodyExam !!!')
        else:
            result = form.save()
        body_exam_commit_workrecord(request, resident, result)
        if save_type == WorkRecord.SUSPEND:
            service_item = Service.objects.get(alias='body_exam_table', service_type__alias='psychiatric')
            WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                      app_label='psychiatric', model_name='BodyExam', status=save_type,
                                      item_id=result.id, service_item_alias=service_item.alias)
    else:
        success = False
    return success


def body_exam_submit(request):
    success = body_exam_save(request, WorkRecord.FINISHED)
    return HttpResponse(simplejson.dumps({'success': success}), content_type='text/html; charset=UTF-8')


def body_exam_suspend(request):
    success = body_exam_save(request, WorkRecord.SUSPEND)
    return HttpResponse(simplejson.dumps({'success': success}), content_type='text/html; charset=UTF-8')


def body_exam_commit_workrecord(request, resident, result):
    if PhysicalExaminationForm(request.POST).is_valid():
        service_item = Service.items.get(alias='physical_examination',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BloodRoutineTestForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_routine_test',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BloodGlucoseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_glucose',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if ElectrocardiogramForm(request.POST).is_valid():
        service_item = Service.items.get(alias='electrocardiogram',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if AlanineAminotransferaseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='alanine_aminotransferase',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if GlutamicOxalaceticTransaminaseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='glutamic_oxalacetic_transaminase',
                                         service_type__alias='psychiatric')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='psychiatric', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)