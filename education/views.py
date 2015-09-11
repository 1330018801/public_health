# -*- coding: utf-8 -*-
from datetime import datetime, date
import os
import simplejson

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

from django.utils import timezone
from education.forms import *
from management.models import WorkRecord, Resident, Service

import logging
debug = logging.getLogger('debug')

'''
def ad_board(request):
    if request.method == 'POST':
        form = AdBoardForm(request.POST)
        if form.is_valid():
            item = form.save()
            record = WorkRecord.objects.get(id=int(request.session.get('record_id')))
            record.evaluation = 2  # satisfied, should be some para from request
            record.item_id = item.id
            record.submit_time = timezone.now()
            record.status = 3
            record.save()
            #This two lines should put in the service_grid view
            if request.session['record_id']:
                del request.session['record_id']
            if request.session['resident_id']:
                del request.session['resident_id']
            return HttpResponseRedirect(reverse('service:service_grid'))
    else:
        form = AdBoardForm()
        record = WorkRecord()
        record.provider = request.user
        record.resident = Resident.objects.get(id=int(request.session.get('resident_id')))
        record.app_label = 'child'
        record.model_name = form.Meta.model.__name__  # Test
        record.service_item = Service.objects.filter(service_type__alias='child').\
            get(alias='child_health_manual')
        record.status = 1  # began
        record.save()
        request.session['record_id'] = record.id

    service_type = Service.objects.get(alias='education')
    service_item = service_type.service_items.get(alias='ad_board')
    found_date = time.strftime("%Y-%m-%d")
    return render(request, 'child/child_health_manual.html', {
        'service_type': service_type,
        'service_item': service_item,
        'found_date': found_date,
        'form': form
    })
    '''


@login_required
def service_disposal(request, content_form, type_label, item_label):
    if request.method == 'GET':
        return service_disposal_get(request, content_form, type_label, item_label)
    elif request.method == 'POST':
        return service_disposal_post(request, content_form, type_label, item_label)


@login_required
def service_disposal_post(request, content_form, type_label, item_label):
    form = content_form(request.POST, request.FILES)
    debug.info('The filename of {0} is {1}'.format('upload', request.FILES.get('upload')))
    if form.is_valid():
        service_result = form.save()
        debug.info('The filename of {0} is {1}'.format('upload', service_result.upload))
        record = WorkRecord()
        record.provider = request.user
        try:
            resident = Resident.objects.get(name='没有人')
        except Resident.DoesNotExist:
            resident = Resident(name='没有人', gender=2, nation='汉族', birthday=date(1900, 1, 1))
            resident.save()
        else:
            pass
        record.resident = resident
        record.service_item = Service.objects.filter(service_type__alias=type_label). \
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
        return HttpResponseRedirect(reverse('management:index'))
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

    # ad_boards = AdBoard.objects.all()
    debug.info('os.path.abspath(os.path.dirname(__file__)) is {0}'.format(os.path.abspath(os.path.dirname(__file__))))

    try:
        request.session['service_items_id_highlight']
    except KeyError:
        service_items_id_highlight = []
    else:
        for item in service_items:
            service_items_id.append(item.id)
        service_items_id_highlight = set(request.session['service_items_id_highlight']) & set(service_items_id)

    #template = '%s/%s.html' % (type_label, item_label)
    return render(request, 'education/education_record.html', {
        #'ad_boards': ad_boards,
        'visit_date': visit_date,
        'service_type': service_type,
        'service_item': service_item,
        'service_items_id_highlight': service_items_id_highlight,
        'form': form
    })


def activity_page(request):
    return render(request, 'education/activity.html')


from django.forms.models import model_to_dict
import pytz
bj_tz = pytz.timezone('Asia/Shanghai')


def activity_list(request):
    activities = EducationActivity.objects.all()

    json_items = []
    for act in activities:
        item = model_to_dict(act, fields=['id', 'scene', 'act_type', 'subject'])
        try:
            record = WorkRecord.objects.get(app_label='education', item_id=act.id)
        except WorkRecord.DoesNotExist:
            pass
        else:
            item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
            item['act_time'] = act.act_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M')
            json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')

    # return JsonResponse(json_items, safe=False)


def activity_table(request):
    form = EducationActivityForm(request.POST)
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
        success = True
        message = u'健康教育活动记录保存完成'
    else:
        success = False
        message = u'健康教育活动数据验证失败'

    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')

    # return JsonResponse({'success': success, 'message': message})


def activity_review(request):
    act_id = int(request.POST.get('id'))
    activity = EducationActivity.objects.get(id=act_id)
    form = EducationActivityForm(instance=activity)

    response = render(request, 'education/activity_table_review.html', {'form': form}).content
    return HttpResponse(simplejson.dumps(response), content_type='text/html; charset=UTF-8')

    # return JsonResponse(response, safe=False)