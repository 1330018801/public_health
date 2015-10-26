# -*- coding: utf-8 -*-
import logging
import simplejson

from django.http import HttpResponse
from django.shortcuts import render

from services.utils import get_resident
from management.models import WorkRecord, Service
from services.utils import new_year_day
from ehr.forms import BodyExamForm
from ehr.models import BodyExam

from .forms import AftercareForm, OldIdentifyForm
from .models import Aftercare, OldIdentify

debug = logging.getLogger('debug')


def old_identify_page(request):
    return render(request, 'tcm/old_identify_page.html')


'''
def old_identify_form(request):
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
                                                       'type_alias': 'tcm'})
'''


def old_identify_form(request):
    resident = get_resident(request)
    records = WorkRecord.objects.filter(resident=resident,
                                        model_name='OldIdentify',
                                        submit_time__gte=new_year_day())
    if records.count():
        result = OldIdentify.objects.get(id=records[0].item_id)
        form = OldIdentifyForm(instance=result)
    else:
        form = OldIdentifyForm()
    return render(request, 'tcm/old_identify_form.html', {'form': form, 'resident': resident, 'type_alias': 'tcm'})


def old_identify_submit(request):
    """
    由于在old_identify_form函数中传递了type_alias参数，因此在页面上只显示老年人
    体制辨识的输入元素，在页面上通过js控制输入的完整性，在此函数中就不必在做过多的
    验证，这样可以保证页面数据提交的完整性。
    """
    resident = get_resident(request)

    # 找到此居民本年的健康体检记录，记录中的item_id是体检表中的该居民的唯一体检数据项
    record = WorkRecord.objects.filter(resident=resident, model_name='BodyExam',
                                       submit_time__gte=new_year_day()).first()
    if record:
        result, created = BodyExam.objects.update_or_create(id=record.item_id, defaults=request.POST)
        success = True
    else:
        form = BodyExamForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.resident = resident
            result.save()
            success = True
        else:
            debug.info(form.errors.as_data())
            success = False
    if success:
        service_item = Service.items.get(alias='constitution_identification',
                                         service_type__alias='tcm')
        WorkRecord.objects.create(provider=request.user, resident=resident, service_item=service_item,
                                  app_label='tcm', model_name='BodyExam', item_id=result.id,
                                  service_item_alias=service_item.alias)
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def child_page(request):
    return render(request, 'tcm/child_page.html')


def child_review(request):
    resident = get_resident(request)
    context = {'aftercare_6_month': None, 'aftercare_12_month': None, 'aftercare_18_month': None,
               'aftercare_24_month': None, 'aftercare_30_month': None, 'aftercare_3_year': None}
    for aftercare in context:
        service_item = Service.items.get(alias=aftercare, service_type__alias='tcm')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            context[aftercare] = Aftercare.objects.get(id=record.item_id)
    context['resident'] = resident
    return render(request, 'tcm/child_review.html', context)


def child_form(request):
    item_alias = request.POST.get('item_alias')
    form = AftercareForm()
    resident = get_resident(request)
    template = 'tcm/child_form.html'
    return render(request, template, {'form': form, 'resident': resident, 'item_alias': item_alias})


def child_submit(request):
    success = False
    resident = get_resident(request)
    item_alias = request.POST.get('item_alias')
    service_item = Service.items.get(alias=item_alias, service_type__alias='tcm')
    form = AftercareForm(request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='tcm', model_name='Aftercare',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
