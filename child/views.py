# coding=utf-8
import logging
import simplejson

# from django.http import JsonResponse
from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse

from management.models import WorkRecord, Resident, Service
from services.utils import get_model_name, new_year_day

from .forms import *
from .models import NewbornFamilyVisit

debug = logging.getLogger('debug')


def get_resident(request):
    resident_id = request.session.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))
    return resident


def newborn_visit_page(request):
    return render(request, 'child/newborn_visit_page.html')


def newborn_visit_submit(request):
    form = NewbornFamilyVisitForm(request.POST)
    if form.is_valid():
        result = form.save()
        resident = get_resident(request)
        service_item = Service.items.get(alias='newborn_family_visit')
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='child', model_name='NewbornFamilyVisit',
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        debug.info(form.errors.as_data())
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')


def newborn_visit_table(request):
    resident = get_resident(request)
    service_item = Service.items.get(alias='newborn_family_visit')
    try:
        record = WorkRecord.objects.get(resident=resident, service_item=service_item)
    except WorkRecord.DoesNotExist:
        form = NewbornFamilyVisitForm()
        return render(request, 'child/newborn_family_visit_form_content.html',
                      {'form': form, 'resident': resident})
    else:
        form = NewbornFamilyVisit.objects.get(id=record.item_id)
        return render(request, 'child/newborn_family_visit_review_content.html',
                      {'form': form, 'resident': resident})


def health_0_1_page(request):
    return render(request, 'child/health_0_1_page.html')


def health_0_1_review(request):
    global model
    resident = get_resident(request)
    context = {'aftercare_1_month': None, 'aftercare_3_month': None,
               'aftercare_6_month': None, 'aftercare_8_month': None}
    for item_alias in context:
        service_item = Service.items.get(alias=item_alias, service_type__alias='child')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            try:
                model_name = get_model_name(item_alias)
                model = apps.get_model(app_label='child', model_name=model_name)
                context[item_alias] = model.objects.get(id=record.item_id)
            except model.DoesNotExist:
                pass
    context['resident'] = resident
    return render(request, 'child/health_0_1_review.html', context)


def health_0_1_form(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name]()
    template = 'child/' + item_alias + '_form_content.html'

    #因为要根据性别判断儿童的身高和体重等级，所以要把新生儿家庭访视里的性别取得
    record = WorkRecord.objects.filter(resident=resident, model_name='NewbornFamilyVisit').first()
    if record:
        newborn_family = NewbornFamilyVisit.objects.get(id=record.item_id)
        gender = newborn_family.gender
    else:
        gender = u'男'
    return render(request, template, {'form': form, 'resident': resident,
                                      'item_alias': item_alias, 'gender': gender})


def health_0_1_submit(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    service_item = Service.items.get(alias=item_alias, service_type__alias='child')
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name](request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='child', model_name=get_model_name(item_alias),
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')

    # return JsonResponse({'success': success})


def health_1_2_page(request):
    return render(request, 'child/health_1_2_page.html')


def health_1_2_review(request):
    global model
    resident = get_resident(request)
    context = {'aftercare_12_month': None, 'aftercare_18_month': None,
               'aftercare_24_month': None, 'aftercare_30_month': None}
    for item_alias in context:
        service_item = Service.items.get(alias=item_alias, service_type__alias='child')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            try:
                model_name = get_model_name(item_alias)
                model = apps.get_model(app_label='child', model_name=model_name)
                context[item_alias] = model.objects.get(id=record.item_id)
            except model.DoesNotExist:
                pass
    context['resident'] = resident
    return render(request, 'child/health_1_2_review.html', context)


def health_1_2_form(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name]()
    template = 'child/' + item_alias + '_form_content.html'

    #因为要根据性别判断儿童的身高和体重等级，所以要把新生儿家庭访视里的性别取得
    record = WorkRecord.objects.filter(resident=resident, model_name='NewbornFamilyVisit').first()
    if record:
        newborn_family = NewbornFamilyVisit.objects.get(id=record.item_id)
        gender = newborn_family.gender
    else:
        gender = u'男'
    return render(request, template, {'form': form, 'resident': resident,
                                      'item_alias': item_alias, 'gender': gender})


def health_1_2_submit(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    service_item = Service.items.get(alias=item_alias, service_type__alias='child')
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name](request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='child', model_name=get_model_name(item_alias),
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')

    # return JsonResponse({'success': success})


def health_3_6_page(request):
    return render(request, 'child/health_3_6_page.html')


def health_3_6_review(request):
    global model
    resident = get_resident(request)
    context = {'aftercare_3_year': None, 'aftercare_4_year': None,
               'aftercare_5_year': None, 'aftercare_6_year': None}
    for item_alias in context:
        service_item = Service.items.get(alias=item_alias, service_type__alias='child')
        try:
            record = WorkRecord.objects.get(resident=resident, service_item=service_item)
        except WorkRecord.DoesNotExist:
            pass
        else:
            try:
                model_name = get_model_name(item_alias)
                model = apps.get_model(app_label='child', model_name=model_name)
                context[item_alias] = model.objects.get(id=record.item_id)
            except model.DoesNotExist:
                pass
    context['resident'] = resident
    return render(request, 'child/health_3_6_review.html', context)


def health_3_6_form(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name]()
    template = 'child/' + item_alias + '_form_content.html'

    #因为要根据性别判断儿童的身高和体重等级，所以要把新生儿家庭访视里的性别取得
    record = WorkRecord.objects.filter(resident=resident, model_name='NewbornFamilyVisit').first()
    if record:
        newborn_family = NewbornFamilyVisit.objects.get(id=record.item_id)
        gender = newborn_family.gender
    else:
        gender = u'男'
    return render(request, template, {'form': form, 'resident': resident,
                                      'item_alias': item_alias, 'gender': gender})


def health_3_6_submit(request):
    item_alias = request.POST.get('item_alias')
    resident = get_resident(request)
    service_item = Service.items.get(alias=item_alias, service_type__alias='child')
    form_name = get_model_name(item_alias) + 'Form'
    form = globals()[form_name](request.POST)
    if form.is_valid():
        result = form.save()
        record = WorkRecord(provider=request.user, resident=resident, service_item=service_item,
                            app_label='child', model_name=get_model_name(item_alias),
                            item_id=result.id, service_item_alias=service_item.alias)
        record.save()
        success = True
    else:
        success = False

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')

    # return JsonResponse({'success': success})