# -*- coding: utf-8 -*-
import logging
import simplejson

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from management.models import WorkRecord, Service
from services.utils import get_resident
from .forms import AftercareForm
from .models import Aftercare

debug = logging.getLogger('debug')


def aftercare_page(request):
    return render(request, 'hypertension/aftercare_page.html')


def aftercare_review(request):
    resident = get_resident(request)

    context = {'aftercare_1': None, 'aftercare_2': None,
               'aftercare_3': None, 'aftercare_4': None}

    for aftercare in context:
        service_item = Service.items.get(alias=aftercare, service_type__alias='hypertension')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            context[aftercare] = Aftercare.objects.get(id=record.item_id)
    context['resident'] = resident
    return render(request, 'hypertension/aftercare_review.html', context)


def aftercare_form(request):
    aftercare = request.POST.get('aftercare')
    form = AftercareForm()
    resident = get_resident(request)
    template = 'hypertension/aftercare_%s_form_content.html' % aftercare
    return render(request, template, {'form': form, 'resident': resident})


def aftercare_submit(request):
    success = False
    resident = get_resident(request)
    item_alias = request.POST.get('aftercare')
    service_item = Service.items.get(alias=item_alias, service_type__alias='hypertension')
    form = AftercareForm(request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='hypertension', model_name='Aftercare',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')

    #return JsonResponse({'success': success})

from ehr.forms import BodyExamForm
from ehr.models import BodyExam
from services.utils import new_year_day


def body_exam_page(request):
    return render(request, 'hypertension/body_exam_page.html')


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
                                                       'type_alias': 'hypertension'})


def body_exam_submit(request):
    """
    首先，检查是否提交了数据，如果没有提交数据返回失败
    其次，如果提交了数据，由于有前端js的检查，一般体格检查的所有数据字段都应该存在并符合取值范围
    :param request:
    :return:
    """
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
                result = form.save()
                success = True
            else:
                success = False
                message = u'数据保存到数据库时失败'
        if success:
            service_item = Service.items.get(alias='physical_examination',
                                             service_type__alias='hypertension')
            WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                      app_label='hypertension', model_name='BodyExam',
                                      item_id=result.id, service_item_alias=service_item.alias)
            message = u'记录保存成功'
    else:
        success = False
        message = u'没有提交任何数据结果'

    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')

    # return JsonResponse({'success': success, 'message': message})
