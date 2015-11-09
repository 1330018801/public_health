# -*- coding: utf-8 -*-
from datetime import datetime, date

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from supervision.models import Inspection, InfoReport
from management.models import WorkRecord, Resident, Service

import logging
debug = logging.getLogger('debug')

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


def inspection_page(request):
    return render(request, 'supervision/inspection.html')


from django.forms.models import model_to_dict
from django.http import JsonResponse


def inspection_list(request):
    # 列表中应该显示该项纪录是否已经被计费和支付（暂时不支持这项功能）
    # 另外，是否应该在WorkRecord中查找呢，有这个必要吗
    begin_date = request.POST.get('begin_date')
    end_date = request.POST.get('end_date')

    begin_date = datetime.strptime(begin_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    inspections = Inspection.objects.filter(inspection_date__range=(begin_date, end_date))

    json_items = []
    for inspection in inspections:
        try:
            WorkRecord.objects.get(app_label='supervision', service_item__alias='patrol',
                                   item_id=inspection.id, provider=request.user)
        except WorkRecord.DoesNotExist:
            pass
        else:
            item = model_to_dict(inspection, fields=['id', 'place_content', 'main_problem',
                                                     'inspector', 'remarks'])
            item['institution'] = inspection.institution.name
            item['inspection_date'] = inspection.inspection_date.strftime('%Y-%m-%d')
            item['create_by'] = inspection.create_by.username
            item['create_time'] = inspection.create_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M')
            item['update_time'] = inspection.update_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M')

            json_items.append(item)
    return JsonResponse(json_items, safe=False)

from management.models import Clinic
from datetime import datetime


def inspection_add(request):
    place_content = request.POST.get('place_content')
    main_problem = request.POST.get('main_problem')
    inspection_date = request.POST.get('inspection_date')
    inspector = request.POST.get('inspector')
    remarks = request.POST.get('remarks')

    inspection = Inspection(institution=Clinic.objects.get(id=1), place_content=place_content,
                            main_problem=main_problem, inspector=inspector, remarks=remarks,
                            inspection_date=datetime.strptime(inspection_date, '%Y-%m-%d').date(),
                            create_by=request.user)
    inspection.save()

    # 保存服务记录，用于统计工作量
    try:
        resident = Resident.objects.get(name='群体')
    except Resident.DoesNotExist:
        resident = Resident(name='群体', gender=2, nation='汉族', birthday=timezone.now().date())
        resident.save()
    service_item = Service.objects.get(service_type__alias='supervision', alias='patrol')
    record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                        app_label='supervision', model_name='Inspection',
                        service_item_alias=service_item.alias, item_id=inspection.id)
    record.save()

    return JsonResponse({'success': True})


def inspection_del(request):
    success = True
    inspection_id = int(request.POST.get('id'))
    try:
        inspection = Inspection.objects.get(id=inspection_id)
    except Inspection.DoesNotExist:
        success = False
    else:
        try:
            record = WorkRecord.objects.get(app_label='supervision',
                                            service_item_alias='patrol',
                                            item_id=inspection.id)
        except WorkRecord.DoesNotExist:
            success = False
        else:
            record.delete()
            inspection.delete()

    return JsonResponse({'success': success})


def info_report_page(request):
    return render(request, 'supervision/info_report.html')


def info_report_list(request):
    begin_date = datetime.strptime(request.POST.get('begin_date'), '%Y-%m-%d')
    begin_date = bj_tz.localize(begin_date)
    end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
    end_date = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
    end_date = bj_tz.localize(end_date)

    info_reports = InfoReport.objects.filter(report_time__range=(begin_date, end_date))

    json_items = []
    for report in info_reports:
        try:
            WorkRecord.objects.get(app_label='supervision', service_item__alias='information_report',
                                   item_id=report.id, provider=request.user)
        except WorkRecord.DoesNotExist:
            pass
        else:
            debug.info('bbb')
            item = model_to_dict(report, fields=['id', 'info_type', 'info_content', 'reporter'])
            item['discover_time'] = report.discover_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
            item['report_time'] = report.report_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
            json_items.append(item)

    return JsonResponse(json_items, safe=False)


def info_report_add(request):
    discover_time = datetime.strptime(request.POST.get('discover_time'), '%Y-%m-%d %H:%M:%S')
    discover_time = bj_tz.localize(discover_time)
    info_type = request.POST.get('info_type')
    info_content = request.POST.get('info_content', '')
    reporter = request.POST.get('reporter')

    # 保存服务结果的内容
    info_report = InfoReport(institution=Clinic.objects.get(id=1), discover_time=discover_time,
                             info_type=info_type, info_content=info_content, reporter=reporter)
    info_report.save()

    # 保存服务记录，用于统计工作量
    try:
        crowd = Resident.objects.get(name='群体')
    except Resident.DoesNotExist:
        crowd = Resident(name='群体', gender=2, nation='汉族', birthday=date.today())
        crowd.save()
    service_item = Service.objects.get(service_type__alias='supervision', alias='information_report')
    record = WorkRecord(provider=request.user, resident=crowd, service_item=service_item,
                        app_label='supervision', model_name='InfoReport',
                        service_item_alias=service_item.alias, item_id=info_report.id)
    record.save()
    return JsonResponse({'success': True})


def info_report_del(request):
    success = True
    info_report_id = int(request.POST.get('id'))
    try:
        info_report = InfoReport.objects.get(id=info_report_id)
    except InfoReport.DoesNotExist:
        success = False
    else:
        try:
            record = WorkRecord.objects.get(app_label='supervision',
                                            service_item_alias='information_report',
                                            item_id=info_report.id)
        except WorkRecord.DoesNotExist:
            success = False
        else:
            record.delete()
            info_report.delete()
    return JsonResponse({'success': success})
