# -*- coding: utf-8 -*-
import logging
import pytz
import simplejson
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.apps import apps

from management.models import Resident, WorkRecord, Family

from .forms import PersonalInfoForm

debug = logging.getLogger('debug')
bj_tz = pytz.timezone('Asia/Shanghai')


def family_list(request):
    try:
        request.session['resident_id']
    except KeyError:
        return render(request, 'services/service_grid.html')
    else:
        resident = Resident.objects.get(id=int(request.session['resident_id']))

    if resident.family is None:
        family = Family()
        family.save()
        resident.family = family
        resident.save()

    json_items = []
    for each in resident.family.members.all():
        item = model_to_dict(each, fields=['id', 'name', 'nation', 'ehr_no',
                                           'identity', 'address', 'mobile'])
        if each.gender == Resident.MALE:
            item['gender'] = u'男'
        elif each.gender == Resident.FEMALE:
            item['gender'] = u'女'
        else:
            item['gender'] = u'未知'
        item['age'] = each.age
        item['birthday'] = each.birthday.strftime('%Y-%m-%d')
        json_items.append(item)
    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')


def child_add_new(request):
    child = Resident()
    child.name = request.POST.get('name')
    child.gender = int(request.POST.get('gender'))
    child.nation = request.POST.get('nation')
    birthday = request.POST.get('birthday')
    child.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    resident_id = request.session['resident_id']
    resident = Resident.objects.get(id=int(resident_id))

    child.family = resident.family
    child.save()
    return HttpResponse(simplejson.dumps({'success': True, 'message': 'OK'}),
                        content_type='text/html; charset=UTF-8')


def family_add_adult_query(request):
    name = request.POST.get('name', '').strip()
    gender = request.POST.get('gender')
    identity = request.POST.get('identity', '').strip()

    json_items = []
    if name == '' and identity == '':
        return HttpResponse(simplejson.dumps({'total': 0, 'rows': json_items}),
                            content_type='text/html; charset=UTF-8')
    adults = Resident.objects.all()
    if name:
        adults = adults.filter(name=name)
    if identity:
        adults = adults.filter(identity=identity)
    if gender:
        gender = int(gender)
        if gender == Resident.MALE:
            adults = adults.filter(gender=int(gender))
        if gender == Resident.FEMALE:
            adults = adults.filter(gender=int(gender))

    for adult in adults:
        item = model_to_dict(adult, fields=['id', 'name', 'gender', 'nation',
                                            'identity', 'address', 'mobile'])
        item['age'] = adult.age
        item['birthday'] = adult.birthday.strftime('%Y-%m-%d')
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': len(json_items), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')


def family_add_adult(request):
    adult = Resident.objects.get(id=int(request.POST.get('id')))
    resident = Resident.objects.get(id=int(request.session['resident_id']))

    adult.family = resident.family
    adult.save()

    return HttpResponse(simplejson.dumps({'success': True, 'message': 'OK'}),
                        content_type='text/html; charset=UTF-8')


def family_member_rm(request):
    resident = Resident.objects.get(id=int(request.POST.get('id')))
    resident.family = None
    resident.save()

    return HttpResponse(simplejson.dumps({'success': True, 'message': 'OK'}),
                        content_type='text/html; charset=UTF-8')


def personal_info_submit(request):
    form = PersonalInfoForm(request.POST)
    if form.is_valid():
        personal_info = form.save()
        resident = Resident.objects.get(id=int(request.POST.get('resident_id')))
        resident.personal_info_table = personal_info
        '''
        以下是自动生成健康档案编号的方法，但是需求手动设置健康档案编号
        if resident.village:
            village = resident.village
            village.ehr_no += 1
            resident.ehr_no = village.id + '%05d' % village.ehr_no
            village.save()
        else:
            resident.ehr_no = '13108200000000000'
        '''
        if resident.ehr_no is None:
            ehr_village_no = int(request.POST.get('ehr_village_no'))    # 由于是必填项，而且是数字类型，所以在此不必检查类型
            ehr_unique_no = int(request.POST.get('ehr_unique_no'))      # 由于是必填项，而且是数字类型，所以在此不必检查类型
            town_no = request.user.userprofile.clinic.region.town.id
            resident.ehr_no = town_no + '%03d' % ehr_village_no + '%05d' % ehr_unique_no
            resident.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def personal_info_table_new(request):
    form = PersonalInfoForm()
    content = render(request, 'ehr/personal_info_form_content.html', {'form': form}).content
    return HttpResponse(content)


def personal_info_review_new(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    personal_info = resident.personal_info_table
    if personal_info:
        form = PersonalInfoForm(instance=personal_info)
        return render(request, 'ehr/personal_info_review_content.html',
                      {'form': form, 'resident': resident})
    else:
        form = PersonalInfoForm()
        return render(request, 'ehr/personal_info_form_content.html',
                      {'form': form, 'resident': resident})


def record_list(request):
    resident_id = request.POST.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))
    records = WorkRecord.objects.filter(resident=resident).order_by('-submit_time')

    json_items = []
    for record in records:
        item = model_to_dict(resident, fields=['ehr_no', 'name'])
        item['id'] = record.id
        item['resident_name'] = record.resident.name
        item['doctor_name'] = record.provider.username
        item['service_type'] = record.service_item.service_type.name
        item['service_item'] = record.service_item.name
        item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
        json_items.append(item)
    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')


def record_detail_review(request):
    record_id = int(request.POST.get('record_id'))
    record = WorkRecord.objects.get(id=record_id)
    resident = record.resident

    service_item = record.service_item
    if service_item.service_group:
        item_alias = record.service_item.service_group.alias
    else:
        item_alias = record.service_item.alias

    if item_alias == 'body_exam_table' or item_alias == 'constitution_identification':
        model_obj = apps.get_model(app_label='ehr', model_name=record.model_name)
    else:
        model_obj = apps.get_model(app_label=record.app_label, model_name=record.model_name)

    form = model_obj.objects.get(id=record.item_id)
    if item_alias == 'body_exam_table' or item_alias == 'constitution_identification':
        template = 'ehr/body_exam_review.html'
    elif record.app_label == 'vaccine' and record.service_item.alias != 'vaccine_card':
        template = 'vaccine/vaccine_review.html'
    elif record.app_label == 'psychiatric':
        template = 'psychiatric/psy_visit_review_content.html'
    else:
        template = '%s/%s_review_content.html' % (record.app_label, item_alias)

    return render(request, template, {'form': form, 'resident': resident})


def ehr_page(request):
    return render(request, 'ehr/family_ehr.html')


def change_resident(request):
    resident_id = request.POST.get('id')
    try:
        resident = Resident.objects.get(id=int(resident_id))
        request.session['resident_id'] = resident.id
        request.session['resident_name'] = resident.name
        # 这里应该也将允许服务的列表也更新一下
    except Resident.DoesNotExist:
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True, 'message': resident.name})