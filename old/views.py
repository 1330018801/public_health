# -*- coding: utf-8 -*-
import logging
import simplejson

from django.shortcuts import render 
from django.http import HttpResponse

from management.models import WorkRecord, Service
from services.utils import get_resident

debug = logging.getLogger('debug')


def body_exam_page(request):
    return render(request, 'old/body_exam_page.html')

from ehr.forms import BodyExamForm
from ehr.models import BodyExam
from services.utils import new_year_day


def body_exam_form(request):
    resident = get_resident(request)
    records = WorkRecord.objects.filter(resident=resident,
                                        model_name='BodyExam',
                                        submit_time__gte=new_year_day())
    if records.count():
        result = BodyExam.objects.get(id=records[0].item_id)
        form = BodyExamForm(instance=result)
    else:
        form = BodyExamForm()

    return render(request, 'ehr/body_exam_form.html', {'form': form, 'resident': resident,
                                                       'type_alias': 'old'})

from ehr.forms import PhysicalExaminationForm, BloodRoutineTestForm, UrineRoutineTestForm, \
    BloodGlucoseForm, ElectrocardiogramForm, GlutamicOxalaceticTransaminaseForm, BloodFatForm, \
    AlanineAminotransferaseForm, TotalBilirubinForm, SerumCreatinineForm, BloodUreaNitrogenForm


def body_exam_submit(request):
    submit_data = request.POST.copy()
    if 'csrfmiddlewaretoken' in submit_data:
        submit_data.pop('csrfmiddlewaretoken')

    if submit_data:
        success = True
        message = u'记录保存成功'
        resident = get_resident(request)
        record = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                           submit_time__gte=new_year_day()).first()
        if record:
            result, created = BodyExam.objects.update_or_create(id=record.item_id, defaults=submit_data)
        else:
            form = BodyExamForm(submit_data)  # 这里为什么不能用create函数呢
            if form.is_valid():
                result = form.save()
            else:
                success = False
                message = u'记录数据存在问题'
        if success:
            if PhysicalExaminationForm(submit_data).is_valid():
                service_item = Service.items.get(alias='physical_examination',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if BloodRoutineTestForm(submit_data).is_valid():
                service_item = Service.items.get(alias='blood_routine_test',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if UrineRoutineTestForm(submit_data).is_valid():
                service_item = Service.items.get(alias='urine_routine_test',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if BloodGlucoseForm(submit_data).is_valid():
                service_item = Service.items.get(alias='blood_glucose',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if ElectrocardiogramForm(submit_data).is_valid():
                service_item = Service.items.get(alias='electrocardiogram',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if AlanineAminotransferaseForm(submit_data).is_valid():
                service_item = Service.items.get(alias='alanine_aminotransferase',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if GlutamicOxalaceticTransaminaseForm(submit_data).is_valid():
                service_item = Service.items.get(alias='glutamic_oxalacetic_transaminase',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if TotalBilirubinForm(submit_data).is_valid():
                service_item = Service.items.get(alias='total_bilirubin',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if SerumCreatinineForm(submit_data).is_valid():
                service_item = Service.items.get(alias='serum_creatinine',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if BloodUreaNitrogenForm(submit_data).is_valid():
                service_item = Service.items.get(alias='blood_urea_nitrogen',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)

            if BloodFatForm(submit_data).is_valid():
                service_item = Service.items.get(alias='blood_fat',
                                                 service_type__alias='old')
                WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                          app_label='old', model_name='BodyExam',
                                          item_id=result.id, service_item_alias=service_item.alias)
    else:
        success = False
        message = u'没有提交任何数据结果'

    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': message})


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
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='old', model_name='LivingSelfcareAppraisal',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success})