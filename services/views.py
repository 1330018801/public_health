#-*- coding: utf8 -*-
from datetime import datetime, date
from random import random
import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth.decorators import login_required

from management.models import Service, WorkRecord, Resident
from .utils import get_resident

log = logging.getLogger('debug')


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
        log.info("has family")
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
    #for item in nav_items:
    #    json_data.append(model_to_dict(item))

    return JsonResponse(json_data, safe=False)


def doc_nav(request):
    nid = request.POST.get('id', '0')
    nav_items = DocNav.objects.filter(nid=int(nid))

    json_data = [model_to_dict(item) for item in nav_items]
    #for item in nav_items:
    #    json_data.append(model_to_dict(item))

    return JsonResponse(json_data, safe=False)


def doc_workload_page(request):
    return render(request, 'services/doc_workload_page.html')

from django.contrib.auth.models import User
import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


def doc_workload_list(request):
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=int(user_id))
    records = WorkRecord.objects.filter(provider=user).order_by('-submit_time')

    json_items = []
    for record in records:
        item = dict()
        item['id'] = record.id
        item['ehr_no'] = record.resident.ehr_no
        item['resident_name'] = record.resident.name
        item['doctor_name'] = record.provider.username
        item['service_type'] = record.service_item.service_type.name
        item['service_item'] = record.service_item.name
        item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
        json_items.append(item)

    return JsonResponse(json_items, safe=False)


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


def provide_service(request):
    return render(request, 'test4.html')

