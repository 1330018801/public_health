# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from management.models import Resident

from .models import AppUser


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
            response['error'] = False
            response['error_msg'] = 'The mobile has registered'

    return JsonResponse(response)
