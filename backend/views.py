# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.apps import apps

from management.models import Resident
from .models import AppUser

import logging
debug = logging.getLogger('debug')

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


@csrf_exempt
def users(request):
    response = []

    for user in AppUser.objects.all():
        item = model_to_dict(user)
        response.append(item)
    return JsonResponse(response, safe=False)


@csrf_exempt
def login(request):
    response = {}
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')

    if mobile and password:
        try:
            app_user = AppUser.objects.get(mobile=mobile, password=password)
        except AppUser.DoesNotExist:
            response['error'] = True
            response['error_msg'] = 'Wrong mobile or password'
        else:
            response = model_to_dict(app_user, fields=['name', 'identity', 'mobile', 'password'])
            response['resident_id'] = app_user.resident.id
            response['created_at'] = app_user.created_at
            response['updated_at'] = app_user.updated_at
            response['error'] = False
    else:
        response['error'] = True
        response['error_msg'] = 'Please input mobile and password to login'

    return JsonResponse(response)


@csrf_exempt
def register(request):
    response = {}
    name = request.POST.get('name')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')
    identity = request.POST.get('identity')

    if name and password and mobile and identity:
        try:
            #  here should consider the mobile or identity has been registered
            AppUser.objects.get(mobile=mobile)
        except AppUser.DoesNotExist:
            try:
                resident = Resident.objects.get(identity=identity)
            except Resident.DoesNotExist:
                response['error'] = True
                response['error_msg'] = 'There is no information about the resident in the system.'
            else:
                app_user = AppUser(name=name, password=password, mobile=mobile, identity=identity)
                app_user.resident = resident
                app_user.save()
                response = model_to_dict(app_user, fields=['name', 'identity', 'mobile', 'password'])
                response['resident_id'] = resident.id
                response['created_at'] = app_user.created_at
                response['updated_at'] = app_user.updated_at
                response['error'] = False
        else:
            response['error'] = True
            response['error_msg'] = 'The mobile has registered'

    return JsonResponse(response)


@csrf_exempt
def personal_info(request):
    resident_id = request.POST.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))

    if resident.personal_info_table is None:
        response = {'error': True,
                    'error_msg': 'The resident has not fill the personal info table'}
    else:
        response = model_to_dict(resident.personal_info_table)
        response['ehr_no'] = resident.ehr_no
        response['error'] = False

    return JsonResponse(response)

from management.models import WorkRecord


@csrf_exempt
def service_list(request):
    response = []
    service_provided = []
    resident_id = request.POST.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))

    for record in WorkRecord.objects.filter(resident=resident,
                                            service_item__isnull=False).order_by('-submit_time'):
        service = record.service_item
        if service.service_group is not None:
            service = service.service_group
        s = dict()
        s['item_id'] = record.item_id
        s['type_alias'] = service.service_type.alias
        s['item_alias'] = service.alias
        if s in service_provided:
            continue
        else:
            service_provided.append(s)
        item = dict()
        item['record_id'] = record.id
        item['type_alias'] = service.service_type.alias
        item['item_alias'] = service.alias
        item['clinic'] = record.provider.userprofile.clinic.name
        item['title'] = service.service_type.name + ': ' + service.name
        item['provider'] = record.provider.username
        item['service_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')

        response.append(item)
    debug.info(service_provided)

    return JsonResponse({'error': False, 'length': len(response), 'list': response})


@csrf_exempt
def record_detail(request):
    response = {}
    record_id = request.POST.get('record_id')
    try:
        record = WorkRecord.objects.get(id=int(record_id))
        service_item = record.service_item
        if service_item.service_group:
            item_alias = record.service_item.service_group.alias
        else:
            item_alias = record.service_item.alias

        if item_alias == 'body_exam_table' or item_alias == 'physical_examination':
            model_obj = apps.get_model(app_label='ehr', model_name=record.model_name)
        else:
            model_obj = apps.get_model(app_label=record.app_label, model_name=record.model_name)

        detail = model_obj.objects.get(id=record.item_id)
        response['error'] = False
        response['detail'] = model_to_dict(detail)
    except WorkRecord.DoesNotExist:
        response['error'] = True
        response['error_msg'] = 'Record does no exist'

    return JsonResponse(response)