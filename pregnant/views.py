# -*- coding: utf-8 -*-
import logging
import simplejson

from django.shortcuts import render
from django.http import HttpResponse

from management.models import WorkRecord, Service
from services.utils import get_resident, get_model_name

from .forms import *
from .models import *

debug = logging.getLogger('debug')


def get_form(item_alias):
    model_name = get_model_name(item_alias)
    return globals()[''.join([model_name, 'Form'])]


def aftercare_1_page(request):
    return render(request, 'pregnant/pregnant_aftercare_1.html')


def aftercare_1_suspend_submit(request, record):
    result, created = Aftercare1.objects.update_or_create(id=record.item_id, defaults=request.POST)
    aftercare_1_commit_workrecord(request, record.resident, result)
    record.status = WorkRecord.SUSPEND_SUBMIT
    record.save()
    return HttpResponse(simplejson.dumps({'success': True}),
                        content_type='text/html; charset=UTF-8')


def aftercare_1_submit(request):
    form = Aftercare1Form(request.POST)
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        service_item = Service.objects.get(alias='aftercare_1', service_type__alias='pregnant')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='pregnant', model_name='Aftercare1',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        aftercare_1_commit_workrecord(request, resident, result)
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def aftercare_1_suspend(request):
    success = True
    resident = get_resident(request)
    form = Aftercare1Form(request.POST)
    if form.is_valid():
        result = form.save()
        service_item = Service.objects.get(alias='aftercare_1', service_type__alias='pregnant')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='pregnant', model_name='Aftercare1', status=WorkRecord.SUSPEND,
                                  item_id=result.id, service_item_alias=service_item.alias)
    else:
        debug.info(form.errors.as_data())
        success = False
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def aftercare_1_table(request):
    resident = get_resident(request)
    service_item = Service.objects.get(alias='aftercare_1', service_type__alias='pregnant')
    try:
        record = WorkRecord.objects.get(resident=resident, service_item=service_item)
    except WorkRecord.DoesNotExist:
        form = Aftercare1Form()
        return render(request, 'pregnant/antenatal_1_form_content.html',
                      {'form': form, 'resident': resident})
    else:
        result = Aftercare1.objects.get(id=record.item_id)
        return render(request, 'pregnant/aftercare_1_review_content.html',
                      {'form': result, 'resident': resident})


def aftercare_2_5_page(request):
    return render(request, 'pregnant/pregnant_aftercare_2_5.html',)


def aftercare_2_5_review(request):
    resident = get_resident(request)
    context = {'aftercare_2': None, 'aftercare_3': None,
               'aftercare_4': None, 'aftercare_5': None}
    for aftercare in context:
        service_item = Service.items.get(alias=aftercare, service_type__alias='pregnant')
        records = WorkRecord.objects.filter(resident=resident, service_item=service_item).order_by('-submit_time')
        if records.count():
            record = records[0]
            try:
                context[aftercare] = Aftercare.objects.get(id=record.item_id)
            except Aftercare.DoesNotExist:
                pass
    context['resident'] = resident
    return render(request, 'pregnant/aftercare_2_5_review.html', context)


def aftercare_2_5_form(request):
    aftercare = request.POST.get('aftercare')
    form = AftercareForm()
    resident = get_resident(request)
    template = 'pregnant/antenatal_%s_form_content.html' % aftercare
    return render(request, template, {'form': form, 'resident': resident})


def aftercare_2_5_submit(request):
    success = False
    resident = get_resident(request)
    item_alias = request.POST.get('aftercare')
    service_item = Service.items.get(alias=item_alias, service_type__alias='pregnant')
    form = AftercareForm(request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='pregnant', model_name='Aftercare',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def postpartum_visit(request):
    return render(request, 'pregnant/pregnant_postpartum_visit.html')


def postpartum_visit_table(request):
    resident = get_resident(request)
    service_item = Service.objects.get(alias='postpartum_visit', service_type__alias='pregnant')
    try:
        record = WorkRecord.objects.get(resident=resident, service_item=service_item)
    except WorkRecord.DoesNotExist:
        form = PostpartumVisitForm()
        return render(request, 'pregnant/postpartum_form_content.html',
                      {'form': form, 'resident': resident})
    else:
        # result = PostpartumVisit.objects.get(id=record.item_id)
        # form = PostpartumVisitForm(instance=result)
        # return render(request, 'pregnant/postpartum_review_content.html', {'form': form, 'resident': resident})
        form = PostpartumVisit.objects.get(id=record.item_id)
        return render(request, 'pregnant/postpartum_visit_review_content.html',
                      {'form': form, 'resident': resident})


def postpartum_visit_submit(request):
    form = PostpartumVisitForm(request.POST)
    success = False
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        service_item = Service.objects.get(alias='postpartum_visit', service_type__alias='pregnant')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='pregnant', model_name='PostpartumVisit',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success})


def postpartum_42day(request):
    return render(request, 'pregnant/pregnant_postpartum_42_day_examination.html')


def postpartum_42day_table(request):
    resident = get_resident(request)
    service_item = Service.objects.get(alias='postpartum_42_day_examination',
                                       service_type__alias='pregnant')
    try:
        record = WorkRecord.objects.get(resident=resident, service_item=service_item)
    except WorkRecord.DoesNotExist:
        form = Postpartum42ExamForm()
        return render(request, 'pregnant/postpartum42_form_content.html',
                      {'form': form, 'resident': resident})
    else:
        form = Postpartum42Exam.objects.get(id=record.item_id)
        return render(request, 'pregnant/postpartum_42_day_examination_review_content.html',
                      {'form': form, 'resident': resident})


def postpartum_42day_submit(request):
    form = Postpartum42ExamForm(request.POST)
    success = False
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        service_item = Service.objects.get(alias='postpartum_42_day_examination',
                                           service_type__alias='pregnant')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='pregnant', model_name='Postpartum42Exam',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def aftercare_1_commit_workrecord(request, resident, result):
        # 体格检查计费项目
        form = PhyExamAbstractForm(request.POST)
        if form.is_valid():
            service_item = Service.objects.get(alias='physical_examination', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        else:
            form.errors.as_data()
        # 妇科检查计费项目
        form = GynaecologicalExaminationForm(request.POST)
        if form.is_valid():
            service_item = Service.objects.get(alias='gynaecological_examination', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        else:
            form.errors.as_data()
        # 血常规计费项目
        if result.hemoglobin and result.leukocyte and result.thrombocyte:
            service_item = Service.objects.get(alias='blood_routine_test', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 尿常规计费项目
        if result.urine_protein and result.urine_glucose and result.urine_ket and result.urine_ery:
            service_item = Service.objects.get(alias='urine_routine_test', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 血型计费项目
        if result.blood_type_abo:
            service_item = Service.objects.get(alias='blood_type', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 谷丙转氨酶计费项目
        if result.sgpt:
            service_item = Service.objects.get(alias='alanine_aminotransferase', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 谷草转氨酶计费项目
        if result.sgot:
            service_item = Service.objects.get(alias='glutamic_oxalacetic_transaminase', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 总胆红素计费项目
        if result.tbil:
            service_item = Service.objects.get(alias='total_bilirubin', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 血清肌酐计费项目
        if result.scr:
            service_item = Service.objects.get(alias='serum_creatinine', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 血尿素氮计费项目
        if result.bun:
            service_item = Service.objects.get(alias='blood_urea_nitrogen', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
        # 乙肝五项计费项目
        if result.surface_antigen and result.surface_antibody and result.e_antigen\
                and result.e_antibody and result.core_antibody:
            service_item = Service.objects.get(alias='hepatitis_b_five_item', service_type__alias='pregnant')
            record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                                app_label='pregnant', model_name='Aftercare1',
                                item_id=result.id, service_item_alias=service_item.alias)
            record.save()
