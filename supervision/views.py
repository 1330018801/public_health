# -*- coding: utf-8 -*-
from datetime import datetime, date

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from supervision.models import Patrol, Inspection, InfoReport
from management.models import WorkRecord, Resident, Service

import logging
debug = logging.getLogger('debug')

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


def get_former_records(request, year):
    if year == '0':
        former_records = Patrol.objects.filter(institution=request.user.userprofile.clinic.name)
        debug.info('Year1 is {0},type is {1}.Length of records is {2}'.format(year, type(year), len(former_records)))
    else:
        former_records = Patrol.objects.filter(institution=request.user.userprofile.clinic.name, patrol_date__year=year)
        debug.info('Year2 is {0},type is {1}.Length of records is {2}'.format(year, type(year), len(former_records)))
    json_former_records = serializers.serialize("json", former_records)

    return HttpResponse(json_former_records, content_type="application/javascript")


def inspection_page(request):
    return render(request, 'supervision/inspection.html')


from django.forms.models import model_to_dict
from django.http import JsonResponse


def inspection_list(request):
    # 列表中应该显示该项纪录是否已经被计费和支付（暂时不支持这项功能）
    # 另外，是否应该在WorkRecord中查找呢，有这个必要吗
    begin_date = request.POST.get('begin_date')
    end_date = request.POST.get('end_date')
    inspector = request.POST.get('inspector')

    begin_date = datetime.strptime(begin_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    inspections = Inspection.objects.all()
    inspections = inspections.filter(inspection_date__range=(begin_date, end_date))
    if inspector:
        inspections = inspections.filter(inspector__contains=inspector)

    json_items = []
    for inspection in inspections:
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

    inspection = Inspection()
    inspection.institution = Clinic.objects.get(id=1)
    inspection.place_content = place_content
    inspection.main_problem = main_problem
    inspection.inspection_date = datetime.strptime(inspection_date, '%Y-%m-%d').date()
    inspection.inspector = inspector
    inspection.remarks = remarks
    inspection.create_by = request.user
    inspection.save()

    # 保存服务记录，用于统计工作量
    record = WorkRecord()
    record.provider = request.user
    try:
        resident = Resident.objects.get(name='群体')
    except Resident.DoesNotExist:
        resident = Resident(name='群体', gender=2, nation='汉族', birthday=timezone.now().date())
        resident.save()

    record.resident = resident
    record.service_item = Service.objects.filter(service_type__alias='supervision')\
        .get(alias='patrol')
    record.app_label = 'supervision'
    record.model_name = 'Inspection'
    record.service_item_alias = 'patrol'
    record.item_id = inspection.id
    record.evaluation = WorkRecord.SATISFIED
    record.status = WorkRecord.FINISHED
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
    info_reports = InfoReport.objects.all()

    json_items = []
    for report in info_reports:
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
    info_report = InfoReport()
    info_report.institution = Clinic.objects.get(id=1)
    info_report.discover_time = discover_time
    info_report.info_type = info_type
    info_report.info_content = info_content
    info_report.reporter = reporter
    info_report.save()

    # 保存服务记录，用于统计工作量
    record = WorkRecord()
    record.provider = request.user
    try:
        resident = Resident.objects.get(name='群体')
    except Resident.DoesNotExist:
        resident = Resident(name='群体', gender=2, nation='汉族', birthday=date.today())
        resident.save()

    record.resident = resident
    record.service_item = Service.objects.filter(service_type__alias='supervision')\
        .get(alias='information_report')
    record.app_label = 'supervision'
    record.model_name = 'InfoReport'
    record.service_item_alias = 'information_report'
    record.item_id = info_report.id
    record.evaluation = WorkRecord.SATISFIED
    record.status = WorkRecord.FINISHED
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
