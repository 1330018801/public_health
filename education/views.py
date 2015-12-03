# -*- coding: utf-8 -*-
import simplejson
import logging
import pytz

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.forms.models import model_to_dict
from management.models import WorkRecord, Resident, Service
from .forms import *

bj_tz = pytz.timezone('Asia/Shanghai')
debug = logging.getLogger('debug')


def activity_page(request):
    return render(request, 'education/activity.html')


def activity_list(request):
    begin_date = request.POST.get('begin_date')
    end_date = request.POST.get('end_date')
    act_type = request.POST.get('act_type')

    activities = EducationActivity.objects.filter(act_time__range=(begin_date, end_date))

    if act_type != u'全部':
        debug.info(act_type)
        activities = activities.filter(act_type=act_type)

    json_items = []
    for act in activities:
        records = WorkRecord.objects.filter(app_label='education', item_id=act.id, provider=request.user)
        if records.count() > 0:
            record = records.first()
            item = model_to_dict(act, fields=['id', 'scene', 'act_type', 'subject'])
            item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
            item['act_time'] = act.act_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M')
            json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')


def activity_table(request):
    form = EducationActivityForm(request.POST, request.FILES)
    if form.is_valid():
        result = form.save()
        try:
            resident = Resident.objects.get(name='群体')
        except Resident.DoesNotExist:
            resident = Resident(name='群体', gender=2, nation='汉族', birthday=timezone.now().date())
        record = WorkRecord(provider=request.user, resident=resident, app_label='education',
                            model_name='EducationActivity', item_id=result.id,
                            evaluation=WorkRecord.SATISFIED, status=WorkRecord.FINISHED)
        service_item = Service.items.get(name=result.act_type)
        record.service_item = service_item
        record.service_item_alias = service_item.alias
        record.save()
        if result.material_type and result.material_num:
            service_item = Service.items.get(name=result.material_type)
            for i in range(result.material_num):
                record = WorkRecord(provider=request.user, resident=resident, app_label='education',
                                    model_name='EducationActivity', item_id=result.id,
                                    evaluation=WorkRecord.SATISFIED, status=WorkRecord.FINISHED)
                record.service_item = service_item
                record.service_item_alias = service_item.alias
                record.save()

        success, message = True, u'健康教育活动记录保存完成'
    else:
        success, message = False, u'健康教育活动数据验证失败'

    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


def activity_review(request):
    act_id = int(request.POST.get('id'))
    form = EducationActivity.objects.get(id=act_id)
    # form = EducationActivityForm(instance=activity)

    return render(request, 'education/activity_table_review.html', {'form': form})
