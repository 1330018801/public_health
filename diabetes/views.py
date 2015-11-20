# -*- coding: utf-8 -*-
import logging
import simplejson

from django.shortcuts import render
from django.http import HttpResponse

from management.models import WorkRecord, Service
from services.utils import get_resident, new_year_day
from ehr.forms import BodyExamForm
from ehr.models import BodyExam

from .forms import AftercareForm
from .models import Aftercare

debug = logging.getLogger('debug')


def aftercare_page(request):
    return render(request, 'diabetes/aftercare_page.html')


def aftercare_review(request):
    resident = get_resident(request)

    context = {'aftercare_1': None, 'aftercare_2': None,
               'aftercare_3': None, 'aftercare_4': None}

    for aftercare in context:
        service_item = Service.items.get(alias=aftercare, service_type__alias='diabetes')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            context[aftercare] = Aftercare.objects.get(id=record.item_id)
    context['resident'] = resident
    return render(request, 'diabetes/aftercare_review.html', context)


def aftercare_form(request):
    aftercare = request.POST.get('aftercare')
    form = AftercareForm()
    resident = get_resident(request)
    template = 'diabetes/aftercare_%s_form_content.html' % aftercare
    return render(request, template, {'form': form, 'resident': resident})


def aftercare_submit(request):
    success = False
    resident = get_resident(request)
    item_alias = request.POST.get('aftercare')
    service_item = Service.items.get(alias=item_alias, service_type__alias='diabetes')
    form = AftercareForm(request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='diabetes', model_name='Aftercare',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        debug.info(form.errors.as_data())

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def aftercare_supplement_page(request):
    return render(request, 'diabetes/aftercare_supplement_page.html')


def aftercare_supplement_review(request):
    resident = get_resident(request)
    context = {'aftercare_5': None, 'aftercare_6': None}
    for aftercare in context:
        service_item = Service.items.get(alias=aftercare, service_type__alias='diabetes')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            context[aftercare] = Aftercare.objects.get(id=record.item_id)
    context['resident'] = resident

    return render(request, 'diabetes/aftercare_supplement_review.html', context)


def body_exam_page(request):
    return render(request, 'diabetes/body_exam_page.html')


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
                                                       'type_alias': 'diabetes'})


def body_exam_submit(request):
    submit_data = request.POST.copy()
    if 'csrfmiddlewaretoken' in submit_data:
        submit_data.pop('csrfmiddlewaretoken')

    if submit_data:
        resident = get_resident(request)
        record = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                           submit_time__gte=new_year_day()).first()
        if record:
            result, created = BodyExam.objects.update_or_create(id=record.item_id, defaults=submit_data)
            success = True
        else:
            form = BodyExamForm(submit_data)
            if form.is_valid():
                result = form.save(commit=False)
                result.resident = resident
                result.save()
                success = True
            else:
                success, message = False, u'数据保存到数据库时失败'
        if success:
            service_item = Service.items.get(alias='physical_examination',
                                             service_type__alias='diabetes')
            WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                      app_label='diabetes', model_name='BodyExam', item_id=result.id,
                                      service_item_alias=service_item.alias)
            message = u'记录保存成功'
    else:
        success, message = False, u'没有提交任何数据结果'

    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
