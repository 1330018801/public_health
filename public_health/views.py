# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from management.models import WorkRecord, Service, Clinic

import logging
debug = logging.getLogger('debug')


def login(request):
    err_msg = ''
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if user.is_staff or user.is_superuser:
                # return HttpResponseRedirect(reverse('management:index'))
                return HttpResponseRedirect(reverse('admin_new'))
            else:
                #return HttpResponseRedirect(reverse('services:service_grid'))
                return HttpResponseRedirect(reverse('services:provide_service'))
        else:
            err_msg = '用户不存在或者密码错误'
    return render(request, 'login.html', {'err_msg': err_msg})


def new_login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return render(request, 'test2.html', {'role': u'超级管理员'})
            if user.is_staff:
                role = user.userprofile.role.name
                debug.info(role)
                return render(request, 'test2.html', {'role': role})
            else:
                return render(request, 'test4.html')
        else:
            message = u'用户不存在或者密码错误'

    return render(request, 'new_login.html', {'message': message})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def logout_new(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('new_login'))


def admin_new(request):
    return render(request, 'test2.html')
################################### For Test ###################################


def test2(request):
    return render(request, 'test2.html')


def test3(request):
    return render(request, 'test3.html')


def test4(request):
    return render(request, 'test4.html')


from django.core import serializers
from django.http import HttpResponse
from management.models import Resident


def xhr_test(request):
    user_id = request.GET.get('id')
    users = Resident.objects.filter(id__gt=int(user_id))
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/javascript')


def graph_clinics(request):
    clinics = list()
    for town_clinic in Clinic.in_town.all():
        clinics.append(town_clinic.name)

    workload = dict()
    for service_type in Service.types.all():
        workload[service_type.name] = dict()
        for town_clinic in Clinic.in_town.all():
            workload[service_type.name][town_clinic.name] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED):
        town_clinic = record.provider.userprofile.clinic.town_clinic
        service_type = record.service_item.service_type
        workload[service_type.name][town_clinic.name] += 1

    data = list()
    for key, value in workload.items():
        item = dict()
        item["name"] = key
        item['data'] = value.values()
        data.append(item)

    result = dict()
    result["clinics"] = clinics
    result["series"] = data

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")


def graphs(request):
    return render(request, 'graphs.html')


def graph_types(request):
    pass