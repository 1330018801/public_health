# -*- coding: utf-8 -*-
import logging
import simplejson

from django.shortcuts import render 
from django.http import HttpResponse
from ehr.forms import PhysicalExaminationForm, BloodRoutineTestForm, UrineRoutineTestForm, \
    BloodGlucoseForm, ElectrocardiogramForm, GlutamicOxalaceticTransaminaseForm, BloodFatForm, \
    AlanineAminotransferaseForm, TotalBilirubinForm, SerumCreatinineForm, BloodUreaNitrogenForm, \
    BUltrasonicForm
from management.models import WorkRecord, Service
from services.utils import get_resident, new_year_day
from ehr.forms import BodyExamForm
from ehr.models import BodyExam

debug = logging.getLogger('debug')


def body_exam_page(request):
    return render(request, 'old/body_exam_page.html')


def body_exam_form(request):
    resident = get_resident(request)
    records = WorkRecord.objects.filter(resident=resident,
                                        model_name='BodyExam',
                                        submit_time__gte=new_year_day())
    debug.info(records.count())
    if records.count():
        result = BodyExam.objects.get(id=records[0].item_id)
        debug.info(result.doctor)
        form = BodyExamForm(instance=result)
        debug.info(form.Meta)
    else:
        form = BodyExamForm()
    return render(request, 'ehr/body_exam_form.html',
                 {'form': form, 'resident': resident, 'type_alias': 'old'})
    #return render(request, 'ehr/text.html', {'form': form, 'resident': resident, 'type_alias': 'old'})


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
            result = form.save(commit=False)
            result.resident = resident
            result.save()
        body_exam_commit_workrecord(request, resident, result)
        if save_type == WorkRecord.SUSPEND:
            service_item = Service.objects.get(alias='body_exam_table', service_type__alias='old')
            WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                      app_label='old', model_name='BodyExam', status=save_type,
                                      item_id=result.id, service_item_alias=service_item.alias)
    else:
        success = False
        debug.info(form.errors.as_data())
    return success


def body_exam_submit(request):
    success = body_exam_save(request, WorkRecord.FINISHED)
    return HttpResponse(simplejson.dumps({'success': success}), content_type='text/html; charset=UTF-8')


def body_exam_suspend(request):
    success = body_exam_save(request, WorkRecord.SUSPEND)
    return HttpResponse(simplejson.dumps({'success': success}), content_type='text/html; charset=UTF-8')


def living_selfcare_appraisal_page(request):
    return render(request, 'old/living_selfcare_appraisal_page.html')

from .forms import LivingSelfcareAppraisalForm
from .models import LivingSelfcareAppraisal


def living_selfcare_appraisal_review(request):
    resident = get_resident(request)
    service_item = Service.items.get(alias='living_selfcare_appraisal')
    try:
        record = WorkRecord.objects.get(resident=resident, service_item=service_item)
    except WorkRecord.DoesNotExist:
        form = LivingSelfcareAppraisalForm()
    else:
        form = LivingSelfcareAppraisal.objects.get(id=record.item_id)

    return render(request, 'old/living_selfcare_appraisal_review_content.html',
                  {'form': form, 'resident': resident})


def living_selfcare_appraisal_submit(request):
    resident = get_resident(request)
    service_item = Service.items.get(alias='living_selfcare_appraisal')
    form = LivingSelfcareAppraisalForm(request.POST)
    degree = None
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='old', model_name='LivingSelfcareAppraisal',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        if result.total>=0 and result.total<=3:
            degree = u'可自理（0~3分）'
        elif result.total >=4 and result.total<=8:
            degree = u'轻度依赖（4~8分）'
        elif result.total>=9 and result.total<=18:
            degree = u'中度依赖（9~18分）'
        else:
            degree = u'不能自理（≥19分）'

        success = True
    else:
        success = False

    if success:
        record0 = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                            submit_time__gte=new_year_day()).first()
        if record0:
            result0 = BodyExam.objects.get(id=record0.item_id)

            result0.old__living_selfcare_appraisal = degree
            result0.save()
        else:
            form0 = BodyExam({'old_living_selfcare_appraisal': degree})

            if form0.is_valid():
                form0.save()

            service_item = Service.objects.get(alias='body_exam_table', service_type__alias='old')
            WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                      app_label='old', model_name='BodyExam',
                                      item_id=form0.id, service_item_alias=service_item.alias)

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def body_exam_commit_workrecord(request, resident, result):
    if PhysicalExaminationForm(request.POST).is_valid():
        service_item = Service.items.get(alias='physical_examination',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BloodRoutineTestForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_routine_test',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if UrineRoutineTestForm(request.POST).is_valid():
        service_item = Service.items.get(alias='urine_routine_test',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)
    if BloodGlucoseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_glucose',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)
    if ElectrocardiogramForm(request.POST).is_valid():

        service_item = Service.items.get(alias='electrocardiogram',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if AlanineAminotransferaseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='alanine_aminotransferase',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if GlutamicOxalaceticTransaminaseForm(request.POST).is_valid():
        service_item = Service.items.get(alias='glutamic_oxalacetic_transaminase',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if TotalBilirubinForm(request.POST).is_valid():
        service_item = Service.items.get(alias='total_bilirubin',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if SerumCreatinineForm(request.POST).is_valid():
        service_item = Service.items.get(alias='serum_creatinine',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BloodUreaNitrogenForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_urea_nitrogen',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BloodFatForm(request.POST).is_valid():
        service_item = Service.items.get(alias='blood_fat',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)

    if BUltrasonicForm(request.POST).is_valid():
        service_item = Service.items.get(alias='b_ultrasonic',
                                         service_type__alias='old')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='old', model_name='BodyExam',
                                  item_id=result.id, service_item_alias=service_item.alias)
