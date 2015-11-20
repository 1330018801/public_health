#-*- coding: utf8 -*-
from datetime import datetime, date
from random import random
import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from management.models import Service, WorkRecord, Resident
from management.models import ModifyApply

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


debug = logging.getLogger('debug')


@login_required
def service_grid(request):
    service_types_highlight = []
    try:
        request.session['resident_id']
    except KeyError:
        break_service = Service()
        break_service.name = u'模拟读卡'
        break_service.alias = u'reading_card'
        break_service.level = Service.SERVICE_TYPE

        test_card = Service()
        test_card.name = u'读取身份证'
        test_card.alias = u'test_card'
        test_card.level = Service.SERVICE_TYPE
    else:
        resident = Resident.objects.get(id=int(request.session['resident_id']))
        service_items_id_highlight = request.session['service_items_id_highlight']
        for item_id in service_items_id_highlight:
            item = Service.items.get(id=item_id)
            service_types_highlight.append(item.service_type)
        service_types_highlight = set(service_types_highlight)

        break_service = Service()
        break_service.name = u'结束{0}的服务'.format(resident.name)
        break_service.alias = u'break_service'
        break_service.level = Service.SERVICE_TYPE

        test_card = Service()
        test_card.name = u'结束{0}的服务'.format(resident.name)
        test_card.alias = u'test_quit'
        test_card.level = Service.SERVICE_TYPE

    ehr_service = Service()
    ehr_service.name = u'家庭健康档案管理'
    ehr_service.alias = u'ehr'
    ehr_service.level = Service.SERVICE_TYPE

    service_types = Service.types.filter(enabled=1)
    for service_type in [service_type for service_type in service_types
                         if service_type.alias in ('diabetes', 'hypertension', 'psychiatric')]:
        service_type.name = service_type.name.replace(u'健康管理', '')
    service_types = list(service_types)
    service_types.append(ehr_service)
    service_types.append(break_service)
    service_types.append(test_card)

    return render(request, 'services/service_grid.html', {
        'service_types': service_types,
        'service_types_highlight': service_types_highlight
    })


# 模拟读卡器读取身份证的函数
# 读卡器驱动等相关程序替换掉
@login_required
def reading_card(request):
    # 在有身份证的居民中随机选择一名
    adults = Resident.objects.filter(identity__isnull=False)
    count = adults.count()
    adults = list(adults)
    resident = adults[int(random()*count)]
    #candidates = list()
    #candidates.append(resident)

    #try:
    #    if resident.gender == Resident.MALE:
    #        family = resident.is_father_in
    #    if resident.gender == Resident.FEMALE:
    #        family = resident.is_mother_in
    #except ObjectDoesNotExist:
    #    pass
    #else:
    #    for child in family.children.all():
    #        if child.is_0_6_child:
    #            candidates.append(child)
    if resident.family:
        candidates = [everyone for everyone in resident.family.members.all()]
    else:
        candidates = [resident]

    json_candidates = serializers.serialize("json", candidates)
    return HttpResponse(json_candidates, content_type="application/javascript")


@login_required
def resident_chosen(request):
    resident_id = request.GET.get('id')
    resident = Resident.objects.get(id=int(resident_id))
    request.session['resident_id'] = resident.id
    request.session['resident_name'] = resident.name

    service_items_authorized = set(request.user.userprofile.authorized_services.filter(level=Service.SERVICE_ITEM))
    #service_items_highlight = service_items_authorized & resident.service_items_todo() - resident.service_items_done()

    # 记得这里要改回来哦
    service_items_highlight = service_items_authorized

    service_items_id_highlight = []
    for item in service_items_highlight:
        service_items_id_highlight.append(item.id)

    service_types_highlight = []
    for item_id in service_items_id_highlight:
        item = Service.items.get(id=item_id)
        service_types_highlight.append(item.service_type)

    vaccine_card = Service.items.get(alias='vaccine_card')
    if vaccine_card.service_type in service_types_highlight:
        service_items_id_highlight.append(vaccine_card.id)

    request.session['service_items_id_highlight'] = service_items_id_highlight

    json_highlight = serializers.serialize("json", service_types_highlight)
    return HttpResponse(json_highlight, content_type="application/javascript")


@login_required
def break_the_service(request):
    for session_para in ['resident_id', 'resident_name',
                         'service_items_id_highlight']:
        try:
            request.session[session_para]
        except KeyError:
            pass
        else:
            del request.session[session_para]
    return HttpResponseRedirect(reverse('services:service_grid'))


@login_required
def test_card(request):
    name = request.GET.get('name')
    birthday = request.GET.get('birthday')
    gender = request.GET.get('gender')
    nation = request.GET.get('nation')
    address = request.GET.get('address')
    identity = request.GET.get('identity')

    try:
        resident = Resident.objects.get(identity=identity)
    except Resident.DoesNotExist:
        resident = Resident()
        resident.name = name
        resident.gender = gender
        try:
            year, month, day = int(birthday[:4]), int(birthday[4:6]), int(birthday[6:8])
        except Exception:
            pass
        else:
            resident.birthday = date(year, month, day)
        resident.nation = nation
        resident.address = address
        resident.identity = identity
        resident.save()
    finally:
        candidates = list()
        candidates.append(resident)
        if resident.family:
            for member in resident.family.members.all():
                if member is not resident and member.identity is None:
                    candidates.append(member)

        json_candidates = serializers.serialize("json", candidates)
        return HttpResponse(json_candidates, content_type="application/javascript")


@login_required
def mobile_submit(request):
    resident_id = request.GET.get('id')
    mobile = request.GET.get('mobile')

    try:
        resident = Resident.objects.get(id=resident_id)
    except Resident.DoesNotExist:
        pass
    else:
        resident.mobile = mobile
        resident.save()


@login_required
def service_index(request, type_label):
    service_type = Service.objects.get(alias=type_label)
    service_items = Service.items.filter(service_type__alias=type_label)
    service_items_id = []
    for item in service_items:
        service_items_id.append(item.id)
    service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)
    return render(request, 'services/index.html', {
        'service_type': service_type,
        'service_items_id_highlight': service_items_id_highlight
    })


@login_required
def service_disposal(request, content_form, type_label, item_label):
    if request.method == 'GET':
        return service_disposal_get(request, content_form, type_label, item_label)
    elif request.method == 'POST':
        return service_disposal_post(request, content_form, type_label, item_label)


@login_required
def service_disposal_post(request, content_form, type_label, item_label):
    form = content_form(request.POST)
    if form.is_valid():
        service_result = form.save()
        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.service_item = Service.objects.filter(service_type__alias=type_label).\
            get(alias=item_label)
        record.app_label = type_label
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item_alias = item_label
        record.item_id = service_result.id
        record.evaluation = WorkRecord.SATISFIED  # this should be some para from request
        record.submit_time = datetime.now()
        record.status = WorkRecord.FINISHED
        record.save()

        for session_para in ['resident_id', 'resident_name',
                             'service_items_id_highlight']:
            try:
                request.session[session_para]
            except KeyError:
                pass
            else:
                del request.session[session_para]
        return HttpResponseRedirect(reverse('services:service_grid'))
    else:
        return service_render(request, form, type_label, item_label)


@login_required
def service_disposal_get(request, content_form, type_label, item_label):
    form = content_form()
    # 当前不支持服务项目过程中的暂存功能
    '''
    record = WorkRecord()
    record.provider = request.user
    record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
    record.app_label = type_label
    record.model_name = form.Meta.model.__name__  # Test
    record.service_item = Service.objects.filter(service_type__alias=type_label).\
        get(alias=item_label)
    record.status = WorkRecord.BEGAN
    record.save()
    request.session['record_id'] = record.id
    '''
    return service_render(request, form, type_label, item_label)


@login_required
def service_render(request, form, type_label, item_label):
    service_type = Service.objects.get(alias=type_label)
    service_item = service_type.service_items.get(alias=item_label)
    visit_date = date.today().strftime("%Y-%m-%d")

    service_items = Service.items.filter(service_type__alias=type_label)
    service_items_id = []

    try:
        request.session['service_items_id_highlight']
    except KeyError:
        service_items_id_highlight = []
    else:
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

    template = '%s/%s.html' % (type_label, item_label)
    return render(request, template, {
        'visit_date': visit_date,
        'service_type': service_type,
        'service_item': service_item,
        'service_items_id_highlight': service_items_id_highlight,
        'form': form
    })

from management.models import SvcNav, DocNav
from django.forms.models import model_to_dict
from django.http import JsonResponse


def svc_nav(request):
    nid = request.POST.get('id', '0')
    nav_items = SvcNav.objects.filter(nid=int(nid))
    json_data = [model_to_dict(item) for item in nav_items]

    return JsonResponse(json_data, safe=False)


def doc_nav(request):
    nid = request.POST.get('id', '0')
    nav_items = DocNav.objects.filter(nid=int(nid))
    json_data = [model_to_dict(item) for item in nav_items]

    return JsonResponse(json_data, safe=False)


def doc_workload_page(request):
    return render(request, 'services/doc_workload_page.html')


def doc_workload_list(request):
    begin_date = datetime.strptime(request.POST.get('begin_date'), '%Y-%m-%d')
    begin_date = bj_tz.localize(begin_date)
    end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
    end_date = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
    end_date = bj_tz.localize(end_date)

    resident_name = request.POST.get('resident', None)
    service_type = request.POST.get('service_type', None)
    service_item = request.POST.get('service_item', None)

    user = request.user
    records = WorkRecord.objects.filter(provider=user, service_item__isnull=False,
                                        submit_time__range=(begin_date, end_date)).order_by('-submit_time')
    if resident_name is not None:
        records = records.filter(resident__name=resident_name)
    if service_item is not None:
        service_item = Service.items.get(id=service_item)
        records = records.filter(service_item=service_item)
    elif service_type is not None:
        service_type = Service.types.get(id=service_type)
        records = records.filter(service_item__service_type=service_type)

    json_items = []
    for record in records:
        item = dict()
        item['id'] = record.id
        item['ehr_no'] = record.resident.ehr_no
        item['resident_name'] = record.resident.name
        item['doctor_name'] = record.provider.username
        if record.service_item:
            item['service_type'] = record.service_item.service_type.name
            item['service_item'] = record.service_item.name
        elif record.service_item_alias == 'body_exam_table':
            item['service_type'] = u'健康档案建档'
            item['service_item'] = u'健康体检表（建档）'
        elif record.service_item_alias == 'personal_info_table':
                item['service_type'] = u'健康档案建档'
                item['service_item'] = u'个人基本信息表（建档）'
        item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
        if record.status == WorkRecord.FINISHED:
            item['status'] = u'完成'
        elif record.status == WorkRecord.SUSPEND:
            item['status'] = u'暂存'
        elif record.status == WorkRecord.SUSPEND_SUBMIT:
            item['status'] = u'暂存/完成'
        try:
            record.modify_apply
        except ObjectDoesNotExist:
            pass
        else:
            if timezone.now() > record.modify_apply.apply_time + timedelta(days=2):
                record.modify_apply.apply_status = ModifyApply.OVERDUE
                record.modify_apply.save()
            item['apply_status'] = record.modify_apply.apply_status
        json_items.append(item)

    return JsonResponse(json_items, safe=False)

from django.utils import timezone
from datetime import timedelta
from ehr.models import BodyExam
from ehr.forms import BodyExamForm
from ehr.views import record_detail_review as ehr_record_review

from old.views import body_exam_suspend_submit as old_body_exam_suspend_submit
from psychiatric.views import body_exam_suspend_submit as psy_body_exam_suspend_submit
from pregnant.views import aftercare_1_suspend_submit as preg_aftercare_1_suspend_submit
from pregnant.models import Aftercare1 as PregnantAftercare1
from pregnant.forms import Aftercare1Form as PregnantAftercare1Form


def record_detail_review(request):
    record_id = int(request.POST.get('record_id'))
    record = WorkRecord.objects.get(id=record_id)
    if record.status == WorkRecord.SUSPEND:
        if record.app_label == 'old' and record.service_item.alias == 'body_exam_table':
            result = BodyExam.objects.get(id=record.item_id)
            form = BodyExamForm(instance=result)
            return render(request, 'ehr/body_exam_form.html',
                          {'form': form, 'resident': record.resident, 'type_alias': record.app_label})
        elif record.app_label == 'psychiatric' and record.service_item.alias == 'body_exam_table':
            result = BodyExam.objects.get(id=record.item_id)
            form = BodyExamForm(instance=result)
            return render(request, 'ehr/body_exam_form.html',
                          {'form': form, 'resident': record.resident, 'type_alias': record.app_label})
        elif record.app_label == 'pregnant' and record.service_item.alias == 'aftercare_1':
            result = PregnantAftercare1.objects.get(id=record.item_id)
            form = PregnantAftercare1Form(instance=result)
            return render(request, 'pregnant/antenatal_1_form_content.html',
                          {'form': form, 'resident': record.resident})

    elif record.status == WorkRecord.FINISHED or record.status == WorkRecord.SUSPEND_SUBMIT:
        return ehr_record_review(request)


def suspend_submit(request):
    record_id = int(request.POST.get('record_id'))
    record = WorkRecord.objects.get(id=record_id)
    if record.service_item.alias == 'body_exam_table' and record.app_label == 'old':
        return old_body_exam_suspend_submit(request, record)
    if record.service_item.alias == 'body_exam_table' and record.app_label == 'psychiatric':
        return psy_body_exam_suspend_submit(request, record)
    if record.service_item.alias == 'aftercare_1' and record.app_label == 'pregnant':
        return preg_aftercare_1_suspend_submit(request, record)


def reading_card_new(request):
    """
    返回准备读取身份证的页面，上面有两个按钮：“读取身份证”，“退出本次服务”，
    医生点击“读取身份证”后，该居民即成为后续服务的对象，直到点击“退出本次服务”
    """
    return render(request, 'services/reading_card.html')


def quit_card(request):
    for session_para in ['resident_id', 'resident_name']:
        if session_para in request.session:
            del request.session[session_para]
    return JsonResponse({'success': True})


def read_card(request):
    """
    用户点击“读取身份证”触发读卡事件，本函数模拟读卡，从后台数据库随机选择一人
    由于，现在在家庭电子健康档案中能够切换家庭成员作为服务对象，因袭现在没有必要
    提示选择家庭成员。
    """
    adults = Resident.objects.filter(identity__isnull=False)
    resident = adults[int(random() * adults.count())]
    request.session['resident_id'] = resident.id
    request.session['resident_name'] = resident.name
    request.session['resident_ehr_no'] = resident.ehr_no
    json_data = model_to_dict(resident, fields=['id', 'name', 'ehr_no'])

    return JsonResponse(json_data)


def real_read_card(request):
    resident_name = request.POST.get('name')
    birthday = request.POST.get('birthday')
    gender = request.POST.get('gender')
    nation = request.POST.get('nation')
    address = request.POST.get('address')
    identity = request.POST.get('identity')
    try:
        resident = Resident.objects.get(identity=identity)
    except Resident.DoesNotExist:
        resident = Resident()
        resident.name = resident_name
        resident.gender = gender
        if len(birthday) != 8:
            resident.birthday = '1900-01-01'
        else:
            resident.birthday = birthday[0:4] + '-' + birthday[4:6] + '-' + birthday[6:8]
        resident.nation = nation
        resident.address = address
        resident.identity = identity
        resident.save()

    request.session['resident_id'] = resident.id
    request.session['resident_name'] = resident.name
    request.session['resident_ehr_no'] = resident.ehr_no
    json_data = model_to_dict(resident, fields=['id', 'name', 'ehr_no'])

    return JsonResponse(json_data)


def doc_info_page(request):
    return render(request, 'services/doc_info_page.html')


def get_doc_info(request):
    """
    返回当前医生用户的信息
    """
    user = request.user
    json_data = model_to_dict(user, fields=['id', 'username'])
    if user.is_staff:   # 管理员用户
        pass
    else:               # 医生用户
        profile = user.userprofile
        json_data['role'] = profile.role.name
        if profile.clinic:
            if profile.clinic.is_town_clinic:
                json_data['town_clinic'] = profile.clinic.name
                json_data['department'] = profile.department
                json_data['position'] = profile.position
            else:
                json_data['town_clinic'] = profile.clinic.town_clinic.name
                json_data['village_clinic'] = profile.clinic.name
                json_data['position'] = u'村医'
    return JsonResponse([json_data], safe=False)

from django.contrib import auth


def update_password(request):
    request.user.set_password(request.POST.get('password'))
    request.user.save()
    auth.logout(request)

    return JsonResponse({'success': True})


def rectify_apply(request):
    record = WorkRecord.objects.get(id=request.POST.get('id'))
    application = ModifyApply(work_record=record, apply_status=ModifyApply.SUBMITTED)
    application.save()
    return HttpResponse({'success': True})


def doc_statistics(request):
    return render(request, 'services/doc_statistics_page.html')


def get_doc_stat(request):
    begin_date = datetime.strptime(request.POST.get('begin_date'), '%Y-%m-%d')
    begin_date = bj_tz.localize(begin_date)
    end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
    end_date = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
    end_date = bj_tz.localize(end_date)

    provider = request.user
    json_data = []

    total = 0
    for service_type in Service.types.all():
        service_type_count = 0
        for service_item in service_type.service_items.all():
            count = WorkRecord.objects.filter(provider=provider, service_item=service_item,
                                              submit_time__range=(begin_date, end_date)).count()
            service_type_count += count
            json_data.append({'service': service_type.name + ':' + service_item.name, 'count': count})
        json_data.append({'service': service_type.name + ':' + u'合计', 'count': service_type_count})
        total += service_type_count
    json_data.append({'service': u'全部合计', 'count': total})

    return JsonResponse(json_data, safe=False)

from django.contrib.auth.models import User


def change_password(request):
    user_id = request.POST.get('id')
    user = User.objects.get(id=int(user_id))

    if user == request.user:
        user.set_password(request.POST.get('password'))
        user.save()
        return JsonResponse({'success': True, 'message': '修改自己的密码后应马上重新登录'})
    elif user.is_staff:
        return JsonResponse({'success': False, 'message': '不能修改其他管理员的密码'})
    else:
        user.set_password(request.POST.get('password'))
        user.save()
        return JsonResponse({'success': True})