# -*- encoding: utf-8 -*-
import re
import types
from datetime import datetime, date
import simplejson

from django.db.models import Q
from django.db.models.loading import get_model
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import ResidentForm, ChangePwdForm, SmsTimeForm
from .models import Clinic, Region, UserProfile, GroupProfile, Service, Resident, WorkRecord, Sms, SmsTime

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')

import logging
debug = logging.getLogger('debug')


@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return render(request, 'management/admin_base.html')
    else:
        auth.logout(request)
        return render(request, 'login.html')


@login_required
def user_list(request):
    users = User.objects.all().order_by('-is_staff').order_by('-is_superuser')
    return render(request, 'management/user_list.html', {'users': users})


@login_required
def user_add(request):
    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    village_clinics = Clinic.objects.filter(level=Clinic.VILLAGE_CLINIC)
    roles = Group.objects.all()
    return render(request, 'management/user_add.html', {
        'roles': roles,
        'town_clinics': town_clinics,
        'village_clinics': village_clinics
    })


@login_required
def user_new(request):
    user = User()
    #should check if there is existing same name
    username = request.POST.get('name')
    try:
        u = User.objects.get(username=username)
    except User.DoesNotExist:
        user.username = username
        user.set_password(request.POST.get('password'))
        role = Group.objects.get(id=int(request.POST.get('role_id')))
        if role.groupprofile.is_staff:
            user.is_staff = True
        else:
            user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.date_joined = datetime.now()

        user_profile = UserProfile()

        town_clinic_id = int(request.POST.get('town_clinic'))
        if town_clinic_id:
            user_profile.clinic = Clinic.objects.get(id=town_clinic_id)

        village_clinic_id = int(request.POST.get('village_clinic', ''))
        if village_clinic_id:
            user_profile.clinic = Clinic.objects.get(id=village_clinic_id)

        user_profile.department = request.POST.get('department')
        user_profile.position = request.POST.get('position')
        user_profile.create_by = request.user
        user_profile.enabled = 1
        user.save()
        user_profile.user = user
        user_profile.role = role
        user_profile.save()

        for service_item in role.groupprofile.default_services.all():
            user_profile.authorized_services.add(service_item)

        if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
            return HttpResponseRedirect(reverse('management:user_list'))
        else:
            return HttpResponseRedirect(reverse('management:town_staff_user_list'))
    else:
        town_clinic = request.user.userprofile.clinic
        if not town_clinic:
            err_msg = '村卫生室选择错误,该用户未设置卫生院'
            return render(request, 'management/user_add.html', {
                'err_msg': err_msg
            })

        name_err_msg = u"用户名已存在！"
        town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
        village_clinics = Clinic.objects.filter(town_clinic=town_clinic)
        roles = Group.objects.all()
        return render(request, 'management/user_add.html', {
            'name_err_msg': name_err_msg,
            'town_clinic': town_clinic,         #用户是卫生院管理员时
            'town_clinics': town_clinics,       #用户是除了卫生院管理员时
            'village_clinics': village_clinics,     #用户是卫生院管理员时
            'roles': roles,
        })


@login_required
def user_del(request, user_id):
    the_user = User.objects.get(id=int(user_id))
    user_profile = UserProfile.objects.get(user=the_user)
    user_profile.delete()
    the_user.delete()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:user_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_user_list'))


@login_required
def user_edit(request, user_id):
    the_user = User.objects.get(id=int(user_id))
    roles = Group.objects.all()
    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    village_clinics = Clinic.objects.filter(level=Clinic.VILLAGE_CLINIC)
    return render(request, 'management/user_edit.html', {
        'the_user': the_user,
        'roles': roles,
        'town_clinics': town_clinics,
        'village_clinics': village_clinics
    })


@login_required
def user_update(request):
    user_id = request.POST.get('user_id')
    the_user = User.objects.get(id=int(user_id))
    the_user.username = request.POST.get('name')
    if request.POST.get('password') != "":
        the_user.set_password(request.POST.get('password'))

    if request.POST.get('town_clinic'):
        town_clinic_id = int(request.POST.get('town_clinic'))
        if town_clinic_id:
            the_user.userprofile.clinic = Clinic.objects.get(id=int(town_clinic_id))
    if request.POST.get('village_clinic'):
        village_clinic_id = int(request.POST.get('village_clinic'))
        if village_clinic_id:
            the_user.userprofile.clinic = Clinic.objects.get(id=int(village_clinic_id))
    the_user.userprofile.department = request.POST.get('department')
    the_user.userprofile.position = request.POST.get('position')
    the_user.userprofile.update_by = request.user
    the_user.userprofile.update_time = datetime.now()
    # does not support role modification
    #the_user.userprofile.role = Group.objects.get(id=request.POST.get('role_id'))
    if request.POST.get('enabled'):
        the_user.userprofile.enabled = int(request.POST.get('enabled'))
        the_user.is_active = the_user.userprofile.enabled

    the_user.userprofile.save()
    the_user.save()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        users = User.objects.all()

    else:
        town_clinic = request.user.userprofile.clinic
        if not town_clinic:
            err_msg = '村卫生室选择错误,该用户未设置卫生院'
            return render(request, 'management/user_list.html', {
                'err_msg': err_msg
            })
        else:
            users = User.objects.filter(Q(userprofile__clinic=town_clinic) | Q(userprofile__clinic__town_clinic=town_clinic))

    return render(request, 'management/user_list.html', {'users': users})


@login_required
def user_authorize(request, user_id):
    user = User.objects.get(id=int(user_id))
    authorized_services = user.userprofile.authorized_services.all()

    service_types = Service.objects.filter(level=Service.SERVICE_TYPE)
    service_items = Service.objects.filter(level=Service.SERVICE_ITEM)
    return render(request, 'management/user_authorize.html', {
        'service_types': service_types,
        'service_items': service_items,
        'authorized_services': authorized_services,
        'user_id': user.id
    })


@login_required
def user_authorization_update(request):
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=int(user_id))
    user_profile = user.userprofile

    service_item_checked = request.REQUEST.getlist("service_items")
    service_item_origin = []
    for item_id in user_profile.authorized_services.filter(level=Service.SERVICE_ITEM):
        service_item_origin.append(str(item_id.id))

    item_to_add = set(service_item_checked) - set(service_item_origin)
    item_to_del = set(service_item_origin) - set(service_item_checked)

    for item_id in item_to_add:
        service_item = Service.objects.get(id=int(item_id))
        service_type = service_item.service_type
        if service_type not in user_profile.authorized_services.all():
            user_profile.authorized_services.add(service_type)
        user_profile.authorized_services.add(service_item)

    for item_id in item_to_del:
        service = Service.objects.get(id=int(item_id))
        user_profile.authorized_services.remove(service)
        service_type = service.service_type
        if set(service_type.service_items.all()) \
                - set(user_profile.authorized_services.all()):
            pass
        else:
            user_profile.authorized_services.remove(service_type)

    user_profile.save()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:user_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_user_list'))


@login_required
def role_list(request):
    groups = Group.objects.all()
    return render(request, 'management/role_list.html', {
        'groups': groups
    })


@login_required
def role_add(request):
    return render(request, 'management/role_add.html')


@login_required
def role_new(request):
    group = Group()
    group.name = request.POST.get('name')
    group.save()

    profile = GroupProfile()
    if request.POST.get('type') == 'management':
        profile.is_staff = True
    else:
        profile.is_staff = False
    profile.group = group
    profile.enabled = 1
    profile.create_by = request.user

    profile.save()

    return HttpResponseRedirect(reverse('management:role_list'))


@login_required
def role_del(request, group_id):
    group = Group.objects.get(id=int(group_id))
    if group:
        group_profile = group.groupprofile
        group.delete()
        if group_profile:
            group_profile.delete()

    return HttpResponseRedirect(reverse('management:role_list'))


@login_required
def role_edit(request, group_id):
    group = Group.objects.get(id=int(group_id))
    profile = group.groupprofile
    return render(request, 'management/role_edit.html', {
        'group': group,
        'profile': profile
    })


@login_required
def role_update(request):
    group_id = request.POST.get('group_id')
    group_name = request.POST.get('name')
    group = Group.objects.get(id=int(group_id))
    group.name = group_name
    group.save()

    profile = group.groupprofile
    if request.POST.get('type') == 'management':
        profile.is_staff = True
    else:
        profile.is_staff = False
    profile.update_by = request.user
    profile.update_time = datetime.now()
    profile.save()

    return HttpResponseRedirect(reverse('management:role_list'))


@login_required
def role_authorize(request, group_id):
    group = Group.objects.get(id=int(group_id))
    default_services = group.groupprofile.default_services.all()

    service_types = Service.objects.filter(level=Service.SERVICE_TYPE, enabled=1)
    #service_items = Service.objects.filter(level=Service.SERVICE_ITEM, enabled=1)
    return render(request, 'management/role_authorize.html', {
        'service_types': service_types,
        #'service_items': service_items,
        'default_services': default_services,
        'group_id': group.id
    })


@login_required
def role_authorization_update(request):
    group_id = int(request.POST.get('group_id'))
    group_profile = Group.objects.get(id=group_id).groupprofile

    service_item_checked = request.REQUEST.getlist("service_items")
    service_item_origin = []
    for item_id in group_profile.default_services.filter(level=Service.SERVICE_ITEM):
        service_item_origin.append(str(item_id.id))

    item_to_add = set(service_item_checked) - set(service_item_origin)
    item_to_del = set(service_item_origin) - set(service_item_checked)

    for item_id in item_to_add:
        service_item = Service.objects.get(id=int(item_id))
        service_type = service_item.service_type
        if service_type not in group_profile.default_services.all():
            group_profile.default_services.add(service_type)
        group_profile.default_services.add(service_item)

    for item_id in item_to_del:
        service_item = Service.objects.get(id=int(item_id))
        group_profile.default_services.remove(service_item)
        service_type = service_item.service_type
        if set(service_type.service_items.all()) - \
                set(group_profile.default_services.all()):
            pass
        else:
            group_profile.default_services.remove(service_type)

    group_profile.save()

    return HttpResponseRedirect(reverse('management:role_list'))


@login_required
def resident_list(request):
    residents = Resident.objects.all()
    towns = Region.towns.all()
    if request.method == 'GET':
        return render(request, 'management/resident_list.html', {
            'residents': residents,
            'towns': towns
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/resident_list.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


from .forms import Resident2Form


@login_required
def resident_add(request):
    if request.method == 'POST':
        form = Resident2Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('management:resident_list'))
    else:
        form = Resident2Form()

    return render(request, 'management/resident_add.html', {'form': form})


@login_required
def resident_del(request, resident_id):
    Resident.objects.get(id=int(resident_id)).delete()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:resident_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_resident_list'))


@login_required
def resident_edit(request, resident_id):
    resident = Resident.objects.get(id=int(resident_id))
    towns = Region.objects.filter(level=Region.TOWN)
    villages = Region.objects.filter(level=Region.VILLAGE)
    return render(request, 'management/resident_edit.html', {
        'resident': resident,
        'towns': towns,
        'villages': villages
    })


@login_required
def resident_update(request):
    resident_id = request.POST.get('resident_id')
    resident = Resident.objects.get(id=int(resident_id))
    resident.name = request.POST.get('name')
    resident.gender = int(request.POST.get('sex'))
    resident.nation = request.POST.get('nation')
    resident.identity = request.POST.get('identity')
    if request.POST.get('town'):
        town_id = int(request.POST.get('town'))
        if town_id:
            resident.town = Region.objects.get(id=town_id)
    if request.POST.get('village'):
        village_id = int(request.POST.get('village'))
        if village_id:
            resident.village = Region.objects.get(id=village_id)
    resident.address = request.POST.get('address')
    resident.mobile = request.POST.get('mobile')
    resident.email = request.POST.get('email')
    resident.hypertension = int(request.POST.get('hypertension'))
    resident.diabetes = int(request.POST.get('diabetes'))
    resident.psychiatric = int(request.POST.get('psychiatric'))
    resident.pregnant = int(request.POST.get('pregnant'))
    if request.POST.get('enabled'):
        resident.enabled = int(request.POST.get('enabled'))
    resident.save()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:resident_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_resident_list'))


#######################################################################
###############         town clinic operations          ###############

@login_required
def town_clinic_list(request):
    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    return render(request, 'management/town_clinic_list.html',
                  {'town_clinics': town_clinics})


@login_required
def town_clinic_add(request):
    towns = Region.objects.filter(level=Region.TOWN)
    return render(request, 'management/town_clinic_add.html', {
        'towns': towns
    })


@login_required
def town_clinic_new(request):
    try:
        town_clinic_name = request.POST.get('name')
    except KeyError:
        err_msg_name = '请输入卫生院名称'
        towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
        return render(request, 'management/town_clinic_add.html', {
            'towns': towns,
            'err_msg_name': err_msg_name
        })

    if not town_clinic_name.strip():
        err_msg_name = '请输入卫生院名称'
        towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
        return render(request, 'management/town_clinic_add.html', {
            'towns': towns,
            'err_msg_name': err_msg_name
        })

    existed = Clinic.objects.filter(name=town_clinic_name)
    if existed.count() > 0:
        err_msg_name = '该乡镇卫生院已存在'
        towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
        return render(request, 'management/town_clinic_add.html', {
            'towns': towns,
            'err_msg_name': err_msg_name
        })

    town_clinic = Clinic()
    town_clinic.name = town_clinic_name
    town_clinic.level = Clinic.TOWN_CLINIC

    region_id = request.POST.get('region', '')
    if region_id:
        try:
            region = Region.objects.get(id=int(region_id))
        except Region.DoesNotExist:
            err_msg_region = '请选择乡镇卫生院所在乡镇'
            towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
            return render(request, 'management/town_clinic_add.html', {
                'towns': towns,
                'err_msg_region': err_msg_region
            })
        else:
            town_clinic.region = region

    town_clinic.address = request.POST.get('address', '')
    town_clinic.enabled = request.POST.get('enabled', 1)
    town_clinic.create_by = request.user
    town_clinic.save()
    return HttpResponseRedirect(reverse('management:town_clinic_list'))


@login_required
def town_clinic_del(request, town_clinic_id):
    Clinic.objects.get(id=int(town_clinic_id)).delete()
    return HttpResponseRedirect(reverse('management:town_clinic_list'))


@login_required
def town_clinic_edit(request, town_clinic_id):
    town_clinic = Clinic.objects.get(id=int(town_clinic_id))
    towns = Region.objects.filter(level=Region.TOWN)
    return render(request, 'management/town_clinic_edit.html', {
        'town_clinic': town_clinic,
        'towns': towns
    })


@login_required
def town_clinic_update(request):
    try:
        town_clinic_id = int(request.POST.get('town_clinic_id'))
    except (KeyError, ValueError):
        err_msg = '所选择的乡镇卫生院存在错误'
        return render(request, 'management/town_clinic_list.html', {
            'err_msg': err_msg
        })
    town_clinic = Clinic.objects.get(id=town_clinic_id)

    try:
        town_clinic_name = request.POST.get('name')
    except KeyError:
        err_msg_name = '请输入卫生院名称'
        towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
        return render(request, 'management/town_clinic_edit.html', {
            'town_clinic': town_clinic,
            'towns': towns,
            'err_msg_name': err_msg_name
        })

    if town_clinic.name != town_clinic_name:
        existed = Clinic.objects.filter(name=town_clinic_name)
        if existed.count() > 0:
            err_msg_name = '该乡镇卫生院已存在'
            towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
            return render(request, 'management/town_clinic_edit.html', {
                'town_clinic': town_clinic,
                'towns': towns,
                'err_msg_name': err_msg_name
            })

    town_clinic.name = town_clinic_name

    region_id = request.POST.get('region', '')
    if region_id:
        try:
            region = Region.objects.get(id=int(region_id))
        except Region.DoesNotExist:
            err_msg_region = '请选择乡镇卫生院所在乡镇'
            towns = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
            return render(request, 'management/town_clinic_edit.html', {
                'town_clinic': town_clinic,
                'towns': towns,
                'err_msg_region': err_msg_region
            })
        else:
            town_clinic.region = region

    town_clinic.address = request.POST.get('address', '')
    if request.POST.get('enabled') is '1':
        town_clinic.enabled = 1
    else:
        town_clinic.enabled = 0
    town_clinic.update_by = request.user
    town_clinic.update_time = datetime.now()
    town_clinic.save()
    return HttpResponseRedirect(reverse('management:town_clinic_list'))


#######################################################################
###############        village clinic operations        ###############
#######################################################################

@login_required
def village_clinic_list(request):
    town_clinic_id = 0
    vague_name = ''
    enabled_status = 2
    err_msg = ''

    if request.POST.get('town_clinic'):
        town_clinic_id = int(request.POST.get('town_clinic'))
        if town_clinic_id:
            try:
                town_clinic = Clinic.objects.get(id=town_clinic_id)
            except Clinic.DoesNotExist:
                err_msg = '乡镇卫生院选择错误'
                village_clinics = Clinic.objects.filter(level=Clinic.VILLAGE_CLINIC)
                town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
                return render(request, 'management/village_clinic_list.html', {
                    'village_clinics': village_clinics,
                    'town_clinics': town_clinics,
                    'town_clinic_id': town_clinic_id,
                    'err_msg': err_msg
                })
            else:
                village_clinics = town_clinic.village_clinics.all()
        else:
            village_clinics = Clinic.objects.filter(level=Clinic.VILLAGE_CLINIC)
    else:
        village_clinics = Clinic.objects.filter(level=Clinic.VILLAGE_CLINIC)

    if request.POST.get('enabled') in ('1', '0'):
        enabled_status = int(request.POST.get('enabled'))
        village_clinics = village_clinics.filter(enabled=enabled_status)

    if request.POST.get('vague_name'):
        vague_name = request.POST.get('vague_name').strip()
        village_clinics = village_clinics.filter(name__contains=vague_name)

    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    return render(request, 'management/village_clinic_list.html', {
        'village_clinics': village_clinics,
        'town_clinics': town_clinics,
        'town_clinic_id': town_clinic_id,
        'vague_name': vague_name,
        'enabled_status': enabled_status,
        'err_msg': err_msg
    })


@login_required
def village_clinic_add(request):
    towns = Region.objects.filter(level=Region.TOWN)
    villages = Region.objects.filter(level=Region.VILLAGE)
    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    return  render(request, 'management/village_clinic_add.html', {
        'town_clinics': town_clinics,
        'towns': towns,
        'villages': villages
    })


# 1) The clinic name should not be null;
# 2) The clinic name should not be the same as an existing clinic in the
#    same town or under a same town clinic
@login_required
def village_clinic_new(request):
    village_clinic = Clinic()
    village_clinic.name = request.POST.get('name')
    village_clinic.level = Clinic.VILLAGE_CLINIC
    town_clinic_id = request.POST.get('town_clinic')
    village_clinic.town_clinic = Clinic.objects.get(id=int(town_clinic_id))
    village_id = request.POST.get('village')
    village_clinic.region = Region.objects.get(id=int(village_id))
    village_clinic.address = request.POST.get('address')
    village_clinic.enabled = 1  # This field should be worked on.

    village_clinic.save()
    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:village_clinic_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_village_clinic_list'))


@login_required
def village_clinic_del(request, village_clinic_id):
    Clinic.objects.get(id=int(village_clinic_id)).delete()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:village_clinic_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_village_clinic_list'))


@login_required
def village_clinic_edit(request, village_clinic_id):
    village_clinic = Clinic.objects.get(id=int(village_clinic_id))
    town_clinics = Clinic.objects.filter(level=Clinic.TOWN_CLINIC)
    towns = Region.objects.filter(level=Region.TOWN)
    villages = Region.objects.filter(level=Region.VILLAGE)

    return render(request, 'management/village_clinic_edit.html', {
        'village_clinic': village_clinic,
        'town_clinics': town_clinics,
        'towns': towns,
        'villages': villages
    })


@login_required
def village_clinic_update(request):
    village_clinic_id = int(request.POST.get('village_clinic_id'))
    name = request.POST.get('name')
    town_clinic_id = request.POST.get('town_clinic')
    enabled_status = int(request.POST.get('enabled'))
    #village_id = int(request.POST.get('village'))

    village_clinic = Clinic.objects.get(id=int(village_clinic_id))
    village_clinic.name = name
    village_clinic.town_clinic = Clinic.objects.get(id=int(town_clinic_id))
    village_clinic.enabled = enabled_status
    #village_clinic.region = Region.objects.get(id=int(village_id))
    village_clinic.save()

    if request.user.is_superuser or request.user.userprofile.role.name != u"卫生院管理员":
        return HttpResponseRedirect(reverse('management:village_clinic_list'))
    else:
        return HttpResponseRedirect(reverse('management:town_staff_village_clinic_list'))


@login_required
def service_type_list(request):
    service_types = Service.objects.filter(level=Service.SERVICE_TYPE).\
        order_by('-enabled')
    return render(request, 'management/service_type_list.html', {
        'service_types': service_types
    })


@login_required
def service_type_add(request):
    return render(request, 'management/service_type_add.html')


@login_required
def service_type_new(request):
    service_type = Service()
    # there should some check here for the same name
    service_type.name = request.POST.get('name')
    service_type.level = Service.SERVICE_TYPE
    service_type.enabled = 1
    if request.POST.get('should_weight'):
        service_type.should_weight = float(request.POST.get('should_weight'))
    else:
        service_type.should_weight = 0
    if request.POST.get('real_weight'):
        service_type.real_weight = float(request.POST.get('real_weight'))
    else:
        service_type.real_weight = 0
    service_type.create_by = request.user
    service_type.save()

    return HttpResponseRedirect(reverse('management:service_type_list'))


@login_required
def service_type_del(request, service_type_id):
    Service.objects.get(id=int(service_type_id)).delete()
    return HttpResponseRedirect(reverse('management:service_type_list'))


@login_required
def service_type_edit(request, service_type_id):
    service_type = Service.objects.get(id=int(service_type_id))
    return render(request, 'management/service_type_edit.html', {
        'service_type': service_type
    })


@login_required
def service_type_update(request):
    service_type_id = request.POST.get('service_type_id')
    service_type = Service.objects.get(id=int(service_type_id))
    # should check if the same name exists
    service_type.name = request.POST.get('name')
    if request.POST.get('should_weight'):
        service_type.should_weight = float(request.POST.get('should_weight'))
    else:
        service_type.should_weight = 0
    if request.POST.get('real_weight'):
        service_type.real_weight = float(request.POST.get('real_weight'))
    else:
        service_type.real_weight = 0
    service_type.enabled = int(request.POST.get('enabled'))
    service_type.update_by = request.user
    service_type.update_time = datetime.now()
    service_type.save()

    return HttpResponseRedirect(reverse('management:service_type_list'))


@login_required
def service_item_list(request):
    service_items = Service.items.all().order_by('id')
    return render(request, 'management/service_item_list.html', {
        'service_items': service_items
    })


@login_required
def service_item_add(request):
    service_types = Service.types.all()
    return render(request, 'management/service_item_add.html', {
        'service_types': service_types
    })


@login_required
def service_item_new(request):
    service_item = Service()
    service_item.name = request.POST.get('name')
    service_item.unit = request.POST.get('unit')
    if request.POST.get('price'):
        service_item.price = float(request.POST.get('price'))
    else:
        service_item.price = 0
    service_item.level = Service.SERVICE_ITEM
    service_item.enabled = 1
    service_type_id = int(request.POST.get('service_type'))
    service_item.service_type = Service.objects.get(id=service_type_id)
    service_item.create_by = request.user
    service_item.create_time = datetime.now()
    service_item.save()

    return HttpResponseRedirect(reverse('management:service_item_list'))


@login_required
def service_item_del(request, service_item_id):
    Service.objects.get(id=int(service_item_id)).delete()
    return HttpResponseRedirect(reverse('management:service_item_list'))


@login_required
def service_item_edit(request, service_item_id):
    service_item = Service.objects.get(id=int(service_item_id))
    service_types = Service.objects.filter(level=Service.SERVICE_TYPE)
    return render(request, 'management/service_item_edit.html', {
        'service_item': service_item,
        'service_types': service_types
    })


@login_required
def service_item_update(request):
    service_item_id = request.POST.get('service_item_id')
    service_item = Service.objects.get(id=int(service_item_id))
    # should check whether this is the same name
    service_item.name = request.POST.get('name')
    service_item.unit = request.POST.get('unit')
    if request.POST.get('price'):
        try:
            service_item.price = float(request.POST.get('price'))
        except TypeError:
            service_item.price = 0
    else:
        service_item.price = 0
    if request.POST.get('enabled'):
        try:
            service_item.enabled = int(request.POST.get('enabled'))
        except TypeError:
            service_item.enabled = 1
    else:
        service_item.enabled = 1
    service_item.service_type = Service.objects.get(id=int(request.POST.get('service_type')))
    service_item.update_by = request.user
    service_item.update_time = datetime.now()
    service_item.save()

    return HttpResponseRedirect(reverse('management:service_item_list'))


@login_required
def statistics_records(request):
    records = WorkRecord.objects.all()
    town_clinics = Clinic.in_town.all()
    service_types = Service.types.all()
    town_clinic = None
    village_clinic = None
    service_type = None
    service_item = None
    provider = ''

    start_time = datetime(datetime.today().year, 1, 1)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('town_clinic') and int(request.POST.get('town_clinic')) > 0:
            town_clinic = Clinic.in_town.get(id=int(request.POST.get('town_clinic')))
            records = records.filter(provider__userprofile__clinic__town_clinic=town_clinic)
        if request.POST.get('village_clinic') and int(request.POST.get('village_clinic')) > 0:
            village_clinic = Clinic.in_village.get(id=int(request.POST.get('village_clinic')))
            records = records.filter(provider__userprofile__clinic=village_clinic)
        if request.POST.get('provider'):
            provider = request.POST.get('provider').strip()
            records = records.filter(provider__username=provider)
        if request.POST.get('service_type') and int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            records = records.filter(service_item__service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            records = records.filter(service_item=service_item)
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            if start_date.date() <= datetime.today().date():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < datetime.today().date():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)

    return render(request, 'management/statistics_records.html', {
        'town_clinics': town_clinics,
        'town_clinic': town_clinic,
        'village_clinic': village_clinic,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'provider': provider,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'records': records,
    })


@login_required
def statistics_payment(request):

    class Payment:
        def __init__(self, item, amount):
            self.service_item = item
            self.amount = amount

    records = WorkRecord.objects.all()
    town_clinics = Clinic.in_town.all()
    service_types = Service.types.all()
    town_clinic = None
    village_clinic = None
    service_type = None
    service_item = None
    provider = ''

    start_time = datetime(datetime.today().year, 1, 1)
    end_time = datetime.today()

    if request.method == 'POST':
        if int(request.POST.get('town_clinic')) > 0:
            town_clinic = Clinic.in_town.get(id=int(request.POST.get('town_clinic')))
            records = records.filter(provider__userprofile__clinic__town_clinic=town_clinic)
        if request.POST.get('village_clinic') and int(request.POST.get('village_clinic')) > 0:
            village_clinic = Clinic.in_village.get(id=int(request.POST.get('village_clinic')))
            records = records.filter(provider__userprofile__clinic=village_clinic)
        if request.POST.get('provider'):
            provider = request.POST.get('provider').strip()
            records = records.filter(provider__username=provider)
        if int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            records = records.filter(service_item__service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            records = records.filter(service_item=service_item)
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            if start_date.date() <= datetime.today().date():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < datetime.today().date():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)

    payment_dict = {}

    service_items = Service.items.all()

    if service_type:
        service_items = service_items.filter(service_type=service_type)
    if service_item:
        service_items = service_items.filter(id=service_item.id)
    for the_service_item in service_items:
        payment_dict[the_service_item] = 0

    for record in records:
        if record.status == WorkRecord.FINISHED:
            payment_dict[record.service_item] = payment_dict[record.service_item] + \
                                            record.service_item.price

    payment_grid = []

    for the_service_item in service_items:
        payment_grid.append(Payment(the_service_item, payment_dict[the_service_item]))

    return render(request, 'management/statistics_payment.html', {
        'town_clinics': town_clinics,
        'town_clinic': town_clinic,
        'village_clinic': village_clinic,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'provider': provider,
        'payment_grid': payment_grid,
    })


@login_required
def statistics_resident(request):
    if request.method == 'GET':
        return render(request, 'management/statistics_resident.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        if name == '' and identity == '':
            return render(request, 'management/statistics_resident.html')
        if identity == '':
            residents = Resident.objects.filter(name=name)
        elif name == '':
            residents = Resident.objects.filter(identity=identity)
        else:
            residents = Resident.objects.filter(name=name, identity=identity)

        records = []

        for resident in residents:
            records = records + list(WorkRecord.objects.filter(resident=resident))

        return render(request, 'management/statistics_resident.html', {
            'name': name,
            'identity': identity,
            'records': records
        })


# To be finished
@login_required
def statistics_record_detail(request, record_id):
    try:
        record = WorkRecord.objects.get(id=record_id)
    except WorkRecord.DoesNotExist:
        # 返回到哪个页面
        pass
    else:
        from django.apps import apps
        service_model = apps.get_model(record.app_label, record.model_name)
        service_content = service_model.objects.get(id=record.id)
        # 这里将使用响应的模板显示服务结果
        print service_content


@login_required
def special_hypertension(request):
    towns = Region.towns.all()
    residents = Resident.objects.filter(hypertension__gt=0)
    if request.method == 'GET':
        return render(request, 'management/special_hypertension.html', {
            'towns': towns,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_hypertension.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def hypertension_add(request):
    towns = Region.towns.all()
    if request.method == 'GET':
        return render(request, 'management/hypertension_add.html', {
            'towns': towns
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        result_residents = Resident.objects.all()
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            result_residents = result_residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            result_residents = result_residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            result_residents = result_residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            result_residents = result_residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            result_residents = result_residents.filter(identity=identity)
        return render(request, 'management/hypertension_add.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'result_residents': result_residents
        })


@login_required
def special_diabetes(request):
    towns = Region.towns.all()
    b_residents = Resident.objects.filter(diabetes__gt=0)
    if request.method == 'GET':
        return render(request, 'management/special_diabetes.html', {
            'towns': towns,
            'residents': b_residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            b_residents = b_residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            b_residents = b_residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            b_residents = b_residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            b_residents = b_residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            b_residents = b_residents.filter(identity=identity)
        return render(request, 'management/special_diabetes.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': b_residents
        })


@login_required
def special_psychiatric(request):
    towns = Region.towns.all()
    residents = Resident.objects.filter(psychiatric__gt=0)
    if request.method == 'GET':
        return render(request, 'management/special_psychiatric.html', {
            'towns': towns,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_psychiatric.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def special_child(request):
    towns = Region.towns.all()
    residents = Resident.children.all()
    if request.method == 'GET':
        return render(request, 'management/special_child.html', {
            'towns': towns,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_child.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def special_old(request):
    towns = Region.towns.all()
    residents = Resident.old.all()
    if request.method == 'GET':
        return render(request, 'management/special_old.html', {
            'towns': towns,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_old.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def special_pregnant(request):
    towns = Region.towns.all()
    residents = Resident.objects.filter(pregnant__gt=0)
    if request.method == 'GET':
        return render(request, 'management/special_pregnant.html', {
            'towns': towns,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, name, identity = None, None, None, None, None
        if int(request.POST.get('town')):
            town = Region.objects.get(id=int(request.POST.get('town')))
            residents = residents.filter(town=town)
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_pregnant.html', {
            'towns': towns,
            'town': town,
            'village': village,
            'name': name,
            'identity': identity,
            'residents': residents
        })


from django.core import serializers


def get_village_clinics(request, town_clinic_id):
    the_town_clinic = Clinic.objects.get(id=int(town_clinic_id))
    village_clinics = Clinic.objects.filter(town_clinic=the_town_clinic).filter(level=1)
    json_village_clinics = serializers.serialize("json", village_clinics)
    return HttpResponse(json_village_clinics, content_type="application/javascript")


def get_villages(request, town_id):
    the_town = Region.objects.get(id=int(town_id))
    villages = Region.objects.filter(town=the_town).filter(level=1)
    json_villages = serializers.serialize("json", villages)
    return HttpResponse(json_villages, content_type="application/javascript")


def getmodelfield(appname,modelname):
    modelobj = get_model(appname, modelname)
    fielddic={}
    for field in modelobj._meta.fields:
        fielddic[field.name] = field.verbose_name
    return fielddic


#判断是否为字符串 string
def is_string(var_obj):

    return type(var_obj) is types.StringType


#判断是否为日期格式,并且是否符合日历规则 2010-01-31
def is_date(var_obj):

    if len(var_obj) == 10:
        rule = '(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)$/'
        match = re.match(rule, var_obj)
        if match:
            return True
        return False
    return False


#判断是否为邮件地址
def is_email(var_obj):

    rule = '[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$'
    match = re.match(rule, var_obj)

    if match:
        return True
    return False


def is_number(var_obj):

    return type(var_obj) is types.IntType


@login_required
def user_profile(request):
    user = request.user
    userprofile=user.userprofile
    fielduserprofile = getmodelfield('management', 'UserProfile')
    fieldresident = getmodelfield('management', 'Resident')

    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if userprofile.resident is None:
            if form.is_valid():
                #user.userprofile.resident.mobile = request.POST['mobile']
                #user.userprofile.resident.email = request.POST['email']

                #user.userprofile.resident.mobile = form.mobile
                #user.userprofile.resident.email = form.email

                #user.userprofile.resident.name = request.POST['name']
                '''
                resident = Resident()
                #name,gender,nation,identity,birthday为必填项,address,mobile,email为非必填项
                resident.name = request.POST['name']
                resident.gender = request.POST['gender']
                resident.nation = request.POST['nation']
                resident.identity = request.POST['identity']
                resident.birthday = request.POST['birthday']

                resident.address = request.POST['address']
                resident.mobile = request.POST['mobile']
                resident.email = request.POST['email']
                resident.create_by = user
                resident.enabled = 1
                resident.save()

                #以上或不可以替换成
                #form.save()
                #resident=form,有create_by和update_by和enabled要赋值
                userprofile.resident = resident
                userprofile.save()'''
                item = form.save()
                item.create_by = user
                item.enabled = 1
                item.save()
                userprofile.resident = item
                userprofile.save()

                return HttpResponseRedirect(reverse('management:userprofile_index'))

        else:

                #userprofile.resident.full_clean(exclude=['name','sex','nation','identity'])
                #if IsDate(request.POST['birthday']) and IsString(request.POST['address']) and IsString(request.POST['mobile']) and IsEmail(request.POST['email']):
                if request.POST['birthday'] != "" and request.POST['email'] != "":
                    if is_date(request.POST['birthday']) and is_email(request.POST['email']):
                        userprofile.resident.birthday = request.POST['birthday']
                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                        return HttpResponseRedirect(reverse('management:userprofile_index'))
                    elif is_date(request.POST['birthday']):
                        birthday_errors = ""
                        email_errors = "请输入正确邮箱格式"

                        userprofile.resident.birthday = request.POST['birthday']
                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                    elif is_email(request.POST['email']):
                        birthday_errors = "请输入正确日期格式"
                        email_errors = ""

                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                    else:
                        birthday_errors = "请输入正确日期格式"
                        email_errors = "请输入正确邮箱格式"

                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()

                elif request.POST['birthday'] != "":
                    if is_date(request.POST['birthday']):
                        userprofile.resident.birthday = request.POST['birthday']
                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                        return HttpResponseRedirect(reverse('management:userprofile_index'))
                    else:
                        birthday_errors = "请输入正确日期格式"
                        email_errors = ""

                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                elif request.POST['email'] != "":
                    if is_email(request.POST['email']):
                        birthday_errors = "请输入"
                        email_errors = ""

                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()
                    else:
                        birthday_errors = "请输入"
                        email_errors = "请输入正确邮箱格式"

                        userprofile.resident.address = request.POST['address']
                        userprofile.resident.mobile = request.POST['mobile']
                        userprofile.resident.email = request.POST['email']
                        userprofile.resident.update_by = user

                        userprofile.resident.save()
                        userprofile.save()

                else:
                    birthday_errors ="请输入"
                    email_errors = ""

                form = userprofile.resident
                return render(request, 'management/user_profile.html', {
                    'form': form,
                    'userprofile': userprofile,
                    'fielduserprofile': fielduserprofile,
                    'fieldresident': fieldresident,
                    'birthday_errors': birthday_errors,
                    'email_errors': email_errors,
                })

        '''
            if form.is_valid():
                userprofile.resident.birthday = request.POST['birthday']
                userprofile.resident.address = request.POST['address']
                userprofile.resident.mobile = request.POST['mobile']
                userprofile.resident.email = request.POST['email']
                userprofile.resident.update_by = user
                userprofile.resident.enabled = 1
                userprofile.resident.save()
                userprofile.save()

                return HttpResponseRedirect(reverse('management:userprofile_index'))'''

    else:
        #fielduserprofile = getmodelfield('management','UserProfile')
        #fieldresident = getmodelfield('management','Resident')
        if userprofile.resident is None:
            form = ResidentForm()

            #return render(request,'management/user_profile.html',{
            #    'form': form,
            #    'userprofile': userprofile,
            #    'fielduserprofile':fielduserprofile,
            #    })

        else:
            form = userprofile.resident

    return render(request, 'management/user_profile.html', {
        'form': form,
        'userprofile': userprofile,
        'fielduserprofile': fielduserprofile,
        'fieldresident': fieldresident,
    })


@login_required
def userprofile_index(request):
    #return HttpResponseRedirect(reverse('management:user_profile_index'))
    return render(request, 'management/userprofile_index.html', )


@login_required
def user_password(request):
    if request.method == 'POST':
        form = ChangePwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            old_password = request.POST['old_password']
            user = auth.authenticate(username=username, password=old_password)
            if user and user.is_active:
                if request.POST['new_password1'] == request.POST['new_password2']:
                    new_password = request.POST['new_password1']
                    user.set_password(new_password)
                    user.save()
                    auth.login(request, user)
                    return render(request, 'management/userprofile_index.html', )
                else:
                    return render(request,'management/user_password.html', {'form': form, 'two_newpwd_not_match': True})
            else:
                return render(request, 'management/user_password.html', {'form': form, 'oldpassword_is_wrong': True, })

    else:
        form = ChangePwdForm()

    return render(request, 'management/user_password.html', {'form': form, })


def get_items(request, type_id):
    service_type = Service.types.get(id=int(type_id))
    items = Service.items.filter(service_type=service_type)
    json_items = serializers.serialize("json", items)
    return HttpResponse(json_items, content_type="application/javascript")


@login_required
def resident_service_list(request):
    try:
        request.session['resident_id']
    except KeyError:
        return render(request, 'services/read_card.html')
    else:
        resident_id = int(request.session['resident_id'])
        resident = Resident.objects.get(id=resident_id)
        service_types_todo = resident.service_types_todo()
        service_items_todo = resident.service_items_todo()
        #service_items_finished = resident.service_items_finished(datetime(datetime.today().year-1, datetime.today().month, datetime.today().day, 0, 0, 0, 0,))
        service_items_done = resident.service_items_done()

        return render(request, 'management/resident_service_list.html', {
            'resident': resident,
            'service_types_todo': service_types_todo,
            'service_items_todo': service_items_todo,
            #'service_items_finished': service_items_finished,
            'service_items_finished': service_items_done
        })


@login_required
def user_authorized_list(request):
    authorized_services = request.user.userprofile.authorized_services

    return render(request, 'management/user_authorized_list.html', {
        'authorized_services': authorized_services,
    })


@login_required
def user_statistics_records(request):
    records = WorkRecord.objects.all()
    provider = request.user
    service_types = list()
    service_type = None
    service_item = None

    start_time = datetime(datetime.today().year, 1, 1)
    end_time = datetime.today()

    ser_types = provider.userprofile.authorized_services.all()
    for ser_type in ser_types:
        if ser_type.level == 2:
            service_types.append(ser_type)

    if request.method == 'POST':
        if request.POST.get('service_type') and int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            records = records.filter(service_item__service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            records = records.filter(service_item=service_item)
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            if start_date.date() <= datetime.today().date():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < datetime.today().date():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time, provider=provider)

    return render(request, 'management/user_statistics_records.html', {
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'provider': provider,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'records': records,
    })


@login_required
def user_statistics_get_items(request, type_id):
    user = request.user
    service_type = Service.types.get(id=int(type_id))
    service_items = user.userprofile.authorized_services.filter(service_type=service_type)
    json_items = serializers.serialize("json", service_items)
    return HttpResponse(json_items, content_type="application/javascript")

#######################################################################
############### town staff village clinic operations        ###############
#######################################################################


@login_required
def town_staff_village_clinic_list(request):
    vague_name = ''
    enabled_status = 2
    err_msg = ''

    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/village_clinic_list.html', {
            'vague_name': vague_name,
            'enabled_status': enabled_status,
            'err_msg': err_msg
        })
    else:
        village_clinics = Clinic.objects.filter(town_clinic=town_clinic)

    if request.POST.get('enabled') in ('1', '0'):
        enabled_status = int(request.POST.get('enabled'))
        village_clinics = village_clinics.filter(enabled=enabled_status)

    if request.POST.get('vague_name'):
        vague_name = request.POST.get('vague_name').strip()
        village_clinics = village_clinics.filter(name__contains=vague_name)

    return render(request, 'management/village_clinic_list.html', {
        'village_clinics': village_clinics,
        'vague_name': vague_name,
        'enabled_status': enabled_status,
        'err_msg': err_msg
    })


@login_required
def town_staff_village_clinic_edit(request, village_clinic_id):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/village_clinic_edit.html', {
            'err_msg': err_msg
        })

    village_clinic = Clinic.objects.get(id=int(village_clinic_id))
    return render(request, 'management/village_clinic_edit.html', {
        'village_clinic': village_clinic,
        'town_clinic': town_clinic,
    })


@login_required
def town_staff_village_clinic_add(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/village_clinic_add.html', {
            'err_msg': err_msg
        })

    town = town_clinic.region
    villages = Region.objects.filter(town=town)
    return render(request, 'management/village_clinic_add.html', {
        'town_clinic': town_clinic,
        'town': town,
        'villages': villages
    })


@login_required
def town_staff_user_list(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/user_list.html', {
            'err_msg': err_msg
        })
    else:
        users = User.objects.filter(Q(userprofile__clinic=town_clinic) | Q(userprofile__clinic__town_clinic=town_clinic))

    return render(request, 'management/user_list.html', {'users': users})


@login_required
def town_staff_user_add(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/user_add.html', {
            'err_msg': err_msg
        })

    village_clinics = Clinic.objects.filter(town_clinic=town_clinic)
    roles = Group.objects.all()
    return render(request, 'management/user_add.html', {
        'roles': roles,
        'town_clinic': town_clinic,
        'village_clinics': village_clinics
    })


@login_required
def town_staff_user_edit(request, user_id):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '村卫生室选择错误,该用户未设置卫生院'
        return render(request, 'management/user_edit.html', {
            'err_msg': err_msg
        })

    the_user = User.objects.get(id=int(user_id))
    roles = Group.objects.all()
    village_clinics = Clinic.objects.filter(town_clinic=town_clinic)
    return render(request, 'management/user_edit.html', {
        'the_user': the_user,
        'roles': roles,
        'town_clinic': town_clinic,
        'village_clinics': village_clinics
    })


@login_required
def town_staff_resident_list(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/resident_list.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        residents = Resident.objects.filter(town=region)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/resident_list.html', {
            'residents': residents,
            'villages': villages
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/resident_list.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_resident_add(request):
    town_clinic = request.user.userprofile.clinic
    if request.method == 'POST':
        form = Resident2Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('management:town_staff_resident_list'))

    else:

        if not town_clinic:
            err_msg = '该用户未设置卫生院'
            return render(request, 'management/resident_add.html', {
                'err_msg': err_msg,
            })
        else:
            form = Resident2Form()

    town = town_clinic.region
    villages = Region.objects.filter(town=town)
    return render(request, 'management/resident_add.html', {
        'form': form,
        'town': town,
        'villages': villages,
    })


@login_required
def town_staff_resident_edit(request, resident_id):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/resident_edit.html', {
            'err_msg': err_msg,
        })
    else:
        town = town_clinic.region

    resident = Resident.objects.get(id=int(resident_id))
    villages = Region.objects.filter(town=town)
    return render(request, 'management/resident_edit.html', {
        'resident': resident,
        'town': town,
        'villages': villages
    })


@login_required
def town_staff_statistics_records(request):
    start_time = datetime(datetime.today().year, 1, 1)
    end_time = datetime.today()
    service_types = Service.types.all()
    village_clinic = None
    service_type = None
    service_item = None
    provider = ''

    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/statistics_records.html', {
            'err_msg': err_msg,
            'start_date': start_time.date(),
            'end_date': end_time.date(),
        })
    else:
        records = WorkRecord.objects.filter(Q(provider__userprofile__clinic=town_clinic) | Q(provider__userprofile__clinic__town_clinic=town_clinic))
        village_clinics = Clinic.objects.filter(town_clinic=town_clinic)

    if request.method == 'POST':
        if request.POST.get('village_clinic') and int(request.POST.get('village_clinic')) > 0:
            village_clinic = Clinic.in_village.get(id=int(request.POST.get('village_clinic')))
            records = records.filter(provider__userprofile__clinic=village_clinic)
        if request.POST.get('provider'):
            provider = request.POST.get('provider').strip()
            records = records.filter(provider__username=provider)
        if request.POST.get('service_type') and int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            records = records.filter(service_item__service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            records = records.filter(service_item=service_item)
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            if start_date.date() <= datetime.today().date():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < datetime.today().date():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)

    return render(request, 'management/statistics_records.html', {
        'village_clinics': village_clinics,
        'village_clinic': village_clinic,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'provider': provider,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'records': records,
    })


@login_required
def town_staff_statistics_payment(request):

    class Payment:
        def __init__(self, item, amount):
            self.service_item = item
            self.amount = amount

    service_types = Service.types.all()
    village_clinic = None
    service_type = None
    service_item = None
    provider = ''

    start_time = datetime(datetime.today().year, 1, 1)
    end_time = datetime.today()

    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/statistics_payment.html', {
            'err_msg': err_msg,
            'start_date': start_time.date(),
            'end_date': end_time.date(),
        })
    else:
        records = WorkRecord.objects.filter(Q(provider__userprofile__clinic=town_clinic) | Q(provider__userprofile__clinic__town_clinic=town_clinic))
        village_clinics = Clinic.objects.filter(town_clinic=town_clinic)

    if request.method == 'POST':
        if request.POST.get('village_clinic') and int(request.POST.get('village_clinic')) > 0:
            village_clinic = Clinic.in_village.get(id=int(request.POST.get('village_clinic')))
            records = records.filter(provider__userprofile__clinic=village_clinic)
        if request.POST.get('provider'):
            provider = request.POST.get('provider').strip()
            records = records.filter(provider__username=provider)
        if int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            records = records.filter(service_item__service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            records = records.filter(service_item=service_item)
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            if start_date.date() <= datetime.today().date():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < datetime.today().date():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)

    payment_dict = {}

    service_items = Service.items.all()

    if service_type:
        service_items = service_items.filter(service_type=service_type)
    if service_item:
        service_items = service_items.filter(id=service_item.id)
    for the_service_item in service_items:
        payment_dict[the_service_item] = 0

    for record in records:
        if record.status == WorkRecord.FINISHED:
            payment_dict[record.service_item] = payment_dict[record.service_item] + \
                                                record.service_item.price

    payment_grid = []

    for the_service_item in service_items:
        payment_grid.append(Payment(the_service_item, payment_dict[the_service_item]))

    return render(request, 'management/statistics_payment.html', {
        'village_clinics': village_clinics,
        'village_clinic': village_clinic,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'provider': provider,
        'payment_grid': payment_grid,
    })


@login_required
def town_staff_statistics_resident(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/statistics_resident.html', {
            'err_msg': err_msg,
        })
    else:
        work_records = WorkRecord.objects.filter(Q(provider__userprofile__clinic=town_clinic) | Q(provider__userprofile__clinic__town_clinic=town_clinic))

    if request.method == 'GET':
        return render(request, 'management/statistics_resident.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        if name == '' and identity == '':
            return render(request, 'management/statistics_resident.html')
        if identity == '':
            residents = Resident.objects.filter(name=name)
        elif name == '':
            residents = Resident.objects.filter(identity=identity)
        else:
            residents = Resident.objects.filter(name=name, identity=identity)

        records = []

        for resident in residents:
            records = records + list(work_records.filter(resident=resident))

        return render(request, 'management/statistics_resident.html', {
            'name': name,
            'identity': identity,
            'records': records
        })


@login_required
def town_staff_special_hypertension(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_hypertension.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        residents = Resident.objects.filter(town=region, hypertension__gt=0)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_hypertension.html', {
            'villages': villages,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_hypertension.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_special_diabetes(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_diabetes.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        residents = Resident.objects.filter(town=region, diabetes__gt=0)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_diabetes.html', {
            'villages': villages,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_diabetes.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_special_psychiatric(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_psychiatric.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        residents = Resident.objects.filter(town=region, psychiatric__gt=0)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_psychiatric.html', {
            'villages': villages,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_psychiatric.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_special_child(request):
    #residents = list()
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_child.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        #residents_1 = Resident.objects.filter(town=region)
        #for resident in residents_1:
        #    if resident.is_0_3_child or resident.is_0_6_child:
        #        residents.append(resident)
        residents = Resident.children.filter(town=Region)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_child.html', {
            'villages': villages,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_child.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_special_pregnant(request):
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_pregnant.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
        residents = Resident.objects.filter(town=region, pregnant__gt=0)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_pregnant.html', {
            'villages': villages,
            'residents': residents
        })
    elif request.method == 'POST':
        town, village, name, identity = None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_pregnant.html', {
            'villages': villages,
            'village': village,
            'name': name,
            'identity': identity,
            'residents': residents
        })


@login_required
def town_staff_special_old(request):
    #residents = list()
    town_clinic = request.user.userprofile.clinic
    if not town_clinic:
        err_msg = '该用户未设置卫生院'
        return render(request, 'management/special_old.html', {
            'err_msg': err_msg,
        })
    else:
        region = town_clinic.region
       #residents_1 = Resident.objects.filter(town=region)
        #for resident in residents_1:
        #    if resident.is_old_man:
        #        residents.append(resident)
        residents = Resident.old.filter(town=region)
        villages = Region.objects.filter(town=region)

    if request.method == 'GET':
        return render(request, 'management/special_old.html', {
            'villages': villages,
            'residents': set(residents)
        })
    elif request.method == 'POST':
        town, village, gender, name, identity = None, None, None, None, None
        if int(request.POST.get('village')):
            village = Region.objects.get(id=int(request.POST.get('village')))
            residents = residents.filter(village=village)
        if request.POST.get('gender') in {'0', '1'}:
            gender = int(request.POST.get('gender'))
            residents = residents.filter(gender=gender)
        if request.POST.get('name'):
            name = request.POST.get('name')
            residents = residents.filter(name=name)
        if request.POST.get('identity'):
            identity = request.POST.get('identity')
            residents = residents.filter(identity=identity)
        return render(request, 'management/special_child.html', {
            'villages': villages,
            'village': village,
            'gender': gender,
            'name': name,
            'identity': identity,
            'residents': set(residents)
        })


@login_required
def town_staff_role_list(request):
    groups = Group.objects.exclude(name="全局管理员")
    return render(request, 'management/role_list.html', {
        'groups': groups
    })


@login_required
def sms_list(request):
    sms = Sms.objects.all()
    service_types = Service.types.all()
    service_type = None
    service_item = None
    mobile = ''
    name = ''
    status = None
    next_time_date = ''

    if request.method == 'POST':
        if request.POST.get('mobile') != "":
            mobile = request.POST.get('mobile').strip()
            sms = sms.filter(mobile=mobile)
        if request.POST.get('name') != "":
            name = request.POST.get('name').strip()
            sms = sms.filter(name=name)
        if request.POST.get('service_type') and int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            sms = sms.filter(service_type_name=service_type.name)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            sms = sms.filter(service_item_name=service_item.name)
        if request.POST.get('next_time_date') != "":
            next_time_date = datetime.strptime(request.POST.get('next_time_date'), '%Y-%m-%d').date()
            next_time_date = next_time_date.date()
            sms = sms.filter(next_time_date=next_time_date)
        if request.POST.get('status') != "":
            status = int(request.POST.get('status'))
            if status > 0:
                sms = sms.filter(status=status)
            elif status < 0:
                sms = sms.filter(status__lte=status)

    return render(request, 'management/sms_list.html', {
        'sms': sms,
        'mobile': mobile,
        'name': name,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'next_time_date': next_time_date,
        'status': status,
    })


@login_required
def sms_time_list(request):
    user = request.user
    sms_time = SmsTime.objects.filter(create_by=user)
    service_types = Service.types.filter(Q(alias='old') | Q(alias='diabetes') | Q(alias='hypertension') |
                                         Q(alias='psychiatric') | Q(alias='tcm'))
    service_type = None
    service_item = None
    service_time_year = ''
    status = None

    if request.method == 'POST':
        if request.POST.get('service_type') and int(request.POST.get('service_type')) > 0:
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            sms_time = sms_time.filter(service_type=service_type)
        if request.POST.get('service_item') and int(request.POST.get('service_item')) > 0:
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            sms_time = sms_time.filter(service_item=service_item)
        if request.POST.get('service_time_year') != "":
            service_time_year = int(request.POST.get('service_time_year'))
            sms_time = sms_time.filter(service_time__year=service_time_year)
        if request.POST.get('status') != "":
            status = int(request.POST.get('status'))
            sms_time = sms_time.filter()

    return render(request, 'management/sms_time_list.html', {
        'sms_time': sms_time,
        'service_types': service_types,
        'service_type': service_type,
        'service_item': service_item,
        'service_time_year': service_time_year,
        'status': status,
    })


@login_required
def sms_get_items(request, type_id):
    service_type = Service.types.get(id=int(type_id))

    if service_type.alias == "diabetes":
        service_items = Service.items.filter(service_type=service_type, alias='physical_examination')
    if service_type.alias == "hypertension":
        service_items = Service.items.filter(service_type=service_type, alias='physical_examination')
    if service_type.alias == "psychiatric":
        service_items = Service.items.filter(service_type=service_type).exclude(alias__contains='aftercare')
    if service_type.alias == "tcm":
        service_items = Service.items.filter(service_type=service_type, alias='constitution_identification')
    if service_type.alias == "old":
        service_items = Service.items.filter(service_type=service_type)
    json_items = serializers.serialize("json", service_items)
    return HttpResponse(json_items, content_type="application/javascript")


@login_required
def sms_time_add(request):
    if request.method == 'POST':
        form = SmsTimeForm(request.POST)
        if form.is_valid():
            user = request.user
            sms_time_1 = SmsTime.objects.filter(create_by=user)
            service_type = Service.types.get(id=int(request.POST.get('service_type')))
            service_item = Service.items.get(id=int(request.POST.get('service_item')))
            service_time = datetime.strptime(request.POST.get('service_time'), '%Y-%m-%d').date()
            service_time_year = service_time.year
            sms_time_1 = sms_time_1.filter(service_type=service_type, service_item=service_item, service_time__year=service_time_year)
            if sms_time_1.count() != 0:
                err_msg = u"该服务项目已设置今年服务时间！"
                return render(request, 'management/sms_time_add.html', {
                    'form': form,
                    'err_msg': err_msg
                })

            sms_time = SmsTime()
            #sms_time.service_type = Service.types.get(id=int(request.POST.get('service_type')))
            #sms_time.service_item = Service.items.get(id=int(request.POST.get('service_item')))

            #service_time = datetime.strptime(request.POST.get('service_time'), '%Y-%m-%d')
            #sms_time.service_time = date(service_time.year, service_time.month, service_time.day)

            sms_time.service_type = service_type
            sms_time.service_item = service_item
            #service_time = datetime.strptime(request.POST.get('service_time'), '%Y-%m-%d')
            sms_time.service_time = date(service_time.year, service_time.month, service_time.day)

            sms_time.status = SmsTime.UNFINISHED
            sms_time.create_by = request.user
            sms_time.save()

            return HttpResponseRedirect(reverse('management:sms_time_list'))

    else:
        form = SmsTimeForm()

    return render(request, 'management/sms_time_add.html', {'form': form})


@login_required
def sms_time_edit(request, sms_time_id):
    sms_time = SmsTime.objects.get(id=int(sms_time_id))
    #if sms_time.status == 0:
    #    sms_time.message = u"短信已发送，不得再修改！"
    #    sms_time.save()
    #    return HttpResponseRedirect(reverse('management:sms_time_list'))
    return render(request, 'management/sms_time_edit.html', {'sms_time': sms_time})


@login_required
def sms_time_update(request):
    sms_time_id = request.POST.get('sms_time_id')
    sms_time = SmsTime.objects.get(id=int(sms_time_id))

    service_time = datetime.strptime(request.POST.get('service_time'), '%Y-%m-%d').date()
    sms_time.service_time = date(service_time.year, service_time.month, service_time.day)

    sms_time.update_by = request.user
    sms_time.save()

    return HttpResponseRedirect(reverse('management:sms_time_list'))


@login_required
def sms_time_del(request, sms_time_id):
    SmsTime.objects.get(id=int(sms_time_id)).delete()

    return HttpResponseRedirect(reverse('management:sms_time_list'))

import json
log = logging.getLogger('debug')


def graph_workload(request):
    workload = dict()
    for service_type in Service.types.all():
        workload[service_type.name] = dict()
        for town_clinic in Clinic.in_town.all():
            workload[service_type.name][town_clinic.name] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED):
        try:
            town_clinic = record.provider.userprofile.clinic.town_clinic
        except ObjectDoesNotExist:
            pass
        else:
            service_type = record.service_item.service_type
            workload[service_type.name][town_clinic.name] += 1

    clinics = workload.values()[0].keys()
    series = [{"name": key, "data": value.values()} for key, value in workload.items()]
    result = {"clinics": clinics, "series": series}

    #log.debug(result)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")


def graph_payment(request):
    payment = dict()
    for town_clinic in Clinic.in_town.all():
        payment[town_clinic.name] = 0

    total_payment = 0
    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED):
        try:
            town_clinic = record.provider.userprofile.clinic.town_clinic
        except ObjectDoesNotExist:
            pass
        else:
            if record.service_item.price:
                payment[town_clinic.name] += record.service_item.price
                total_payment += record.service_item.price

    total_payment *= 1.0
    percent = [{'name': key, 'y': value/total_payment} for key, value in payment.items()]

    return HttpResponse(simplejson.dumps(percent), content_type='text/html; charset=UTF-8')
    # return JsonResponse(percent, safe=False)


def psychiatric_info_table(request):
    return render(request, 'management/psychiatric_info_table.html')


def psychiatric_info_table_detail(request):
    return render(request, 'management/psychiatric_info_table_detail.html')


#the "item" in this class means town_clinic,service_type,village_clinic,doctor
class RecordPayment:
        def __init__(self, item, records_count, payments):
            self.item = item
            self.records_count = records_count
            self.payments = payments


def town_clinics_statement(request):
    town_clinics = Clinic.in_town.all()

    start_time = datetime(date.today().year, 1, 1, 0, 0, 0)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            if start_date.date() <= date.today():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
                start_time = bj_tz.localize(start_time)
            else:
                start_time = bj_tz.localize(datetime.today())
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            if end_date.date() < date.today():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)

    work_records = WorkRecord.objects.filter(submit_time__gt=start_time, submit_time__lt=end_time)
    payment_dict = {}
    payment_grid = []

    for town_clinic in town_clinics:
        records = work_records.filter(Q(provider__userprofile__clinic=town_clinic) |
                                            Q(provider__userprofile__clinic__town_clinic=town_clinic))
        payment_dict[town_clinic] = 0

        for record in records:
            payment_dict[town_clinic] = payment_dict[town_clinic]+record.service_item.price

        payment_grid.append(RecordPayment(town_clinic, records.count(), payment_dict[town_clinic]))

    return render(request, 'management/town_clinics_statement.html', {
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'payment_grid': payment_grid,
    })


def village_clinics_statement(request, town_clinic_id):
    town_clinic = Clinic.in_town.get(id=town_clinic_id)
    village_clinics = Clinic.in_village.filter(town_clinic=town_clinic)

    start_time = datetime(date.today().year, 1, 1, 0, 0, 0)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            if start_date.date() <= date.today():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
                start_time = bj_tz.localize(start_time)
            else:
                start_time = bj_tz.localize(datetime.today())
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
            if end_date.date() < date.today():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
                end_time = bj_tz.localize(end_time)

    work_records = WorkRecord.objects.filter(submit_time__gt=start_time, submit_time__lt=end_time)

    #The work_record count and the total payment about all the village_clinics of a town_clinic
    payment_dict = {}
    payment_grid = []

    town_records = work_records.filter(provider__userprofile__clinic=town_clinic)
    payment_dict[town_clinic] = 0
    for record in town_records:
        payment_dict[town_clinic] = payment_dict[town_clinic] + record.service_item.price

    payment_grid.append(RecordPayment(town_clinic, town_records.count(), payment_dict[town_clinic]))

    town_records = work_records.filter(provider__userprofile__clinic__town_clinic=town_clinic)

    for village_clinic in village_clinics:
        records = town_records.filter(provider__userprofile__clinic=village_clinic)
        payment_dict[village_clinic] = 0

        for record in records:
            payment_dict[village_clinic] = payment_dict[village_clinic] + record.service_item.price

        payment_grid.append(RecordPayment(village_clinic, records.count, payment_dict[village_clinic]))

    #The work_record count and the total payment about the village_clinics and town_clinic of all the service_type
    payment_service = {}
    payment_list = []
    town_records = work_records.filter(Q(provider__userprofile__clinic=town_clinic) |
                                       Q(provider__userprofile__clinic__town_clinic=town_clinic))

    service_types = Service.types.all()
    for service_type in service_types:
        records = town_records.filter(service_item__service_type=service_type)
        payment_service[service_type] = 0

        for record in records:
            payment_service[service_type] = payment_service[service_type] + record.service_item.price

        payment_list.append(RecordPayment(service_type, records.count(), payment_service[service_type]))

    return render(request, 'management/village_clinics_statement.html', {
        'payment_grid': payment_grid,
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'town_clinic': town_clinic,
        'payment_list': payment_list,
    })


def doctors_statement(request, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    start_time = datetime(datetime.today().year, 1, 1, 0, 0, 0)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            if start_date.date() <= date.today():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
                start_time = bj_tz.localize(start_time)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
            if end_date.date() < date.today():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
                end_time = bj_tz.localize(end_time)

    work_records = WorkRecord.objects.filter(submit_time__gt=start_time, submit_time__lt=end_time)

    records = work_records.filter(provider__userprofile__clinic=clinic)
    doctors = User.objects.filter(userprofile__clinic=clinic)

    payment_doctor = {}
    payment_grid = []
    for doctor in doctors:
        doctor_records = records.filter(provider=doctor)
        payment_doctor[doctor] = 0

        for record in doctor_records:
            payment_doctor[doctor] = payment_doctor[doctor] + record.service_item.price

        payment_grid.append(RecordPayment(doctor, doctor_records.count(), payment_doctor[doctor]))

    return render(request, 'management/doctors_statement.html',{
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'payment_grid': payment_grid,
        'clinic': clinic,
    })


def doctor_work_records(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    start_time = datetime(datetime.today().year, 1, 1, 0, 0, 0)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            if start_date.date() <= date.today():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
                start_time = bj_tz.localize(start_time)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
            if end_date.date() < date.today():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
                end_time = bj_tz.localize(end_time)

    records = WorkRecord.objects.filter(submit_time__gt=start_time, submit_time__lt=end_time, provider=doctor)

    return render(request, 'management/doctor_work_records.html', {
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'doctor': doctor,
        'records': records,
    })


def resident_records(request, doctor_id, resident_id):
    doctor = User.objects.get(id=doctor_id)
    resident = Resident.objects.get(id=resident_id)
    start_time = datetime(datetime.today().year, 1, 1, 0, 0, 0)
    end_time = datetime.today()

    if request.method == 'POST':
        if request.POST.get('start_date'):
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
            if start_date.date() <= date.today():
                start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
                start_time = bj_tz.localize(start_time)
            else:
                start_time = datetime.today()
        if request.POST.get('end_date'):
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
            if end_date.date() < date.today():
                end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
                end_time = bj_tz.localize(end_time)

    records = WorkRecord.objects.filter(submit_time__gt=start_time, submit_time__lt=end_time, resident=resident)

    return render(request, 'management/resident_records.html', {
        'start_date': start_time.date(),
        'end_date': end_time.date(),
        'doctor': doctor,
        'resident': resident,
        'records': records,
    })


'''
def service_details(request, app_label, model_name, service_item_alias, item_id):
    model_obj = get_model(app_label, model_name)
    form = model_obj.objects.get(id=item_id)

    template = '%s/%s.html' % (app_label, 'education_record')

    return render(request, template, {
        'form': form,
    })
'''


def service_details(request, return_name, record_id):
    record = WorkRecord.objects.get(id=record_id)
    model_obj = get_model(record.app_label, record.model_name)
    form = model_obj.objects.get(id=record.item_id)

    if record.app_label == 'psychiatric':
        template = 'psychiatric/psy_visit_review.html'
    elif record.app_label == 'education':
        template = 'education/education_record_review.html'
    else:
        template = '%s/%s_review.html' % (record.app_label, record.service_item_alias)

    debug.info('service_item_alias is {0},template is {1}'.format(record.service_item_alias, template))

    if return_name.isdigit():
        return_name = User.objects.get(id=int(return_name))
    return render(request, template, {
        'form': form,
        'record': record,
        'return_name': return_name,
    })


def resident_records_details(request, doctor_id, record_id):
    record = WorkRecord.objects.get(id=record_id)
    model_obj = get_model(record.app_label, record.model_name)
    form = model_obj.objects.get(id=record.item_id)
    doctor = User.objects.get(id=doctor_id)

    template = '%s/%s.html' % (record.app_label, record.service_item_alias)

    return render(request, template, {
        'form': form,
        'record': record,
        'doctor': doctor,
    })


def excel_temp(request):
    import xlwt
    from django.utils.encoding import smart_unicode

    wb = xlwt.Workbook()
    ws = wb.add_sheet('temp_excel_name')

    records = WorkRecord.objects.all()

    ws.write(0, 0, smart_unicode('服务提供者'))
    ws.write(0, 1, smart_unicode('居民姓名'))
    ws.write(0, 2, smart_unicode('服务项目'))
    ws.write(0, 3, smart_unicode('完成时间'))

    for i, record in enumerate(records):
        ws.write(i + 1, 0, smart_unicode(record.provider.username))
        ws.write(i + 1, 1, smart_unicode(record.resident.name))
        ws.write(i + 1, 2, smart_unicode(record.service_item.name))
        ws.write(i + 1, 3, smart_unicode(record.submit_time))

    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=work_recode.xls'

    wb.save(response)
    return response


from .models import RectificationApply


def rectify_apply(request):
    """
    :param request:
    :return apply record id:
    """
    work_record_id = None
    if request.method == 'GET':
        work_record_id = request.GET['id']

    if work_record_id:
        apply_record = RectificationApply()
        apply_record.work_record = WorkRecord.objects.get(id=int(work_record_id))
        apply_record.finance_opinion = RectificationApply.WAITING
        apply_record.health_opinion = RectificationApply.WAITING
        apply_record.apply_status = RectificationApply.SUBMITTED
        apply_record.save()

    return HttpResponse(apply_record.id)

#from django.http import JsonResponse


def get_towns(request):
    if 'first_text' in request.POST:
        json_data = [{'id': 0, 'name': request.POST.get('first_text')}]
    else:
        json_data = [{'id': 0, 'name': '全部'}]

    towns = Region.towns.all()
    for town in towns:
        json_item = model_to_dict(town, fields=['id', 'name'])
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_towns_edit(request):
    json_data = []
    json_item = {'id': '0', 'name': ''}
    json_data.append(json_item)

    towns = Region.towns.all()
    for town in towns:
        json_item = dict()
        json_item['id'], json_item['name'] = town.id, town.name
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_town_villages(request, town_id):
    json_data = []
    json_item = {'id': '0', 'name': '全部'}
    json_data.append(json_item)

    try:
        town = Region.towns.get(id=town_id)
        villages = Region.villages.filter(town=town)
        for village in villages:
            json_item = dict()
            json_item['id'], json_item['name'] = village.id, village.name
            json_data.append(json_item)
    except Region.DoesNotExist:
        pass

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_town_villages_edit(request):
    town_name = request.POST.get('town_name')
    json_data = []
    json_item = {'id': '0', 'name': ''}
    json_data.append(json_item)

    try:
        town = Region.towns.get(name=town_name)
        villages = Region.villages.filter(town=town)
        for village in villages:
            json_item = dict()
            json_item['id'], json_item['name'] = village.id, village.name
            json_data.append(json_item)
    except Region.DoesNotExist:
        pass

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def resident_add_test(request):
    resident = Resident()
    resident.name = request.POST.get('name')
    resident.gender = request.POST.get('gender')
    resident.identity = request.POST.get('identity')
    resident.address = request.POST.get('address')
    # town_id = request.POST.get('town', '0')
    town_name = request.POST.get('town', '')
    try:
        town = Region.objects.get(name=town_name)
    except Region.DoesNotExist:
        pass
    else:
        resident.town = town
    village_name = request.POST.get('village', '')
    try:
        village = Region.objects.get(name=village_name)
    except Region.DoesNotExist:
        pass
    else:
        resident.village = village
    resident.birthday = request.POST.get('birthday')
    resident.nation = request.POST.get('nation')
    resident.mobile = request.POST.get('mobile')
    resident.email = request.POST.get('email')

    resident.save()
    json_data = {'success': True, 'name': resident.name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data)


def resident_update_test(request):
    resident_id = request.POST.get('id')
    resident = Resident.objects.get(id=int(resident_id))

    resident.name = request.POST.get('name')
    resident.gender = request.POST.get('gender')
    resident.identity = request.POST.get('identity')
    resident.address = request.POST.get('address')
    town_name = request.POST.get('town', '')
    resident.ehr_no = request.POST.get('ehr_no')

    try:
        town = Region.objects.get(name=town_name)
    except Region.DoesNotExist:
        pass
    else:
        resident.town = town
    village_name = request.POST.get('village', '')
    try:
        village = Region.objects.get(name=village_name)
    except Region.DoesNotExist:
        pass
    else:
        resident.village = village
    resident.birthday = request.POST.get('birthday')
    resident.nation = request.POST.get('nation')
    resident.mobile = request.POST.get('mobile')
    resident.email = request.POST.get('email')

    resident.save()
    json_data = {'success': True, 'name': resident.name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data)


def resident_del_test(request):
    resident_id = request.POST.get('resident_id')
    success = True
    resident_name = ''
    try:
        resident = Resident.objects.get(id=int(resident_id))
        resident_name = resident.name
        resident.delete()
    except Resident.DoesNotExist:
        success = False

    json_data = {'success': success, 'name': resident_name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data)

from django.forms.models import model_to_dict


def resident_query_test(request):
    residents = Resident.objects.all()

    town = request.POST.get('town')
    if town and town != "0":
        residents = residents.filter(town=town)
    village = request.POST.get('village')
    if village and village != "0":
        residents = residents.filter(village=village)
    gender = request.POST.get('gender')
    if gender != "2":
        residents = residents.filter(gender=int(gender))
    identity = request.POST.get('identity')
    if identity:
        residents = residents.filter(identity=identity).strip()
    mobile = request.POST.get('mobile')
    if mobile:
        residents = residents.filter(mobile=mobile).strip()
    name = request.POST.get('name')
    if name:
            residents = residents.filter(name=name).strip()

    json_data = []
    for resident in residents:
        item = model_to_dict(resident, exclude=['create_time', 'update_time',
                                                'create_by', 'update_by', 'birthday'])
        item['birthday'] = resident.birthday.strftime('%Y-%m-%d')
        json_data.append(item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def resident_query_list(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_town = request.POST.get('query_town')
    query_village = request.POST.get('query_village')
    query_name = request.POST.get('query_name')
    query_identity = request.POST.get('query_identity')
    query_ehr_no = request.POST.get('query_ehr_no')
    query_crowd = request.POST.get('query_crowd')

    residents = Resident.objects.all().order_by('-id')
    if query_town and query_town != '0':
        residents = residents.filter(town__id=query_town)
    if query_village and query_village != '0':
        residents = residents.filter(village__id=query_village)
    if query_name:
        residents = residents.filter(name=query_name)
    if query_identity:
        residents = residents.filter(identity=query_identity)
    if query_ehr_no:
        if query_ehr_no == '1':
            residents = residents.filter(ehr_no__isnull=False)
        if query_ehr_no == '-1':
            residents = residents.filter(ehr_no__isnull=True)

    if query_crowd and query_crowd != 'all':
        if query_crowd == 'hypertension':
            residents = residents.filter(hypertension=1)
        if query_crowd == 'diabetes':
            residents = residents.filter(diabetes=1)
        if query_crowd == 'psychiatric':
            residents = residents.filter(psychiatric=1)
        if query_crowd == 'pregnant':
            residents = residents.filter(pregnant=1)
        #if query_crowd == 'old':
        #    residents = residents.filter(age__gte=65)
        #if query_crowd == 'child':
            residents = residents.filter(age__lt=7)

    json_items = []
    for resident in residents[first: first + page_size]:
        item = model_to_dict(resident, exclude=['town', 'village', 'birthday',
                                                'create_time', 'create_by',
                                                'update_time', 'update_by'])
        item['birthday'] = resident.birthday.strftime('%Y-%m-%d')
        item['age'] = resident.age
        if resident.town:
            item['town'] = resident.town.name
        else:
            item['town'] = ''
        if resident.village:
            item['village'] = resident.village.name
        else:
            item['village'] = ''
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': residents.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': residents.count(), 'rows': json_items})

from management.models import AdminNav


def admin_nav(request):
    nid = request.POST.get('id', '0')
    nav_items = AdminNav.objects.filter(nid=int(nid))

    json_data = []
    for item in nav_items:
        json_data.append(model_to_dict(item))

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def residents(request):
    return render(request, 'management/residents.html')


def town_clinics(request):
    return render(request, 'management/town_clinics.html')


def town_clinic_list_new(request):
    json_items = []
    for town_clinic in Clinic.in_town.all():
        item = model_to_dict(town_clinic, fields=['id', 'name', 'address'])
        item['village_clinic_num'] = town_clinic.village_clinics.count()
        item['doctor_user_num'] = town_clinic.users.count()
        if town_clinic.region:
            item['town_name'] = town_clinic.region.name
        json_items.append(item)

    json_data = dict()
    json_data['total'] = len(json_items)
    json_data['rows'] = json_items
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data)


def village_clinics(request):
    return render(request, 'management/village_clinics.html')


def village_clinic_list_new(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_town_clinic = request.POST.get('query_town_clinic', '0')
    query_village = request.POST.get('query_village_clinic_name', '')

    village_clinics = Clinic.in_village.all().order_by('id')
    if query_town_clinic and query_town_clinic != '0':
        town_clinic = Clinic.in_town.get(id=int(query_town_clinic))
        village_clinics = village_clinics.filter(town_clinic=town_clinic)
    if query_village:
        village_clinics = village_clinics.filter(name__icontains=query_village)

    json_items = []
    for clinic in village_clinics[first: first + page_size]:
        item = model_to_dict(clinic, fields=['id', 'name', 'address'])
        if clinic.town_clinic:
            item['town_clinic'] = clinic.town_clinic.name

        json_items.append(item)

    #return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    return JsonResponse({'total': village_clinics.count(), 'rows': json_items})


def get_town_clinics(request):
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]

    town_clinics = Clinic.in_town.all()
    for clinic in town_clinics:
        json_items.append(model_to_dict(clinic, fields=['id', 'name']))

    #return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    return JsonResponse(json_items, safe=False)


def get_town_clinic_edit(request):
    json_data = []
    json_item = {'id': '0', 'name': ''}
    json_data.append(json_item)

    town_clinics = Clinic.in_town.all()
    for clinic in town_clinics:
        json_item = dict()
        json_item['id'], json_item['name'] = clinic.id, clinic.name
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def village_clinic_add_test(request):
    name = request.POST.get('name', '')
    town_clinic_name = request.POST.get('town_clinic', '')
    address = request.POST.get('address', '')

    clinic = Clinic()
    clinic.level = Clinic.VILLAGE_CLINIC
    if name:
        clinic.name = name
    if town_clinic_name:
        town_clinic = Clinic.objects.get(name=town_clinic_name)
        clinic.town_clinic = town_clinic
    if address:
        clinic.address = address

    clinic.create_by = request.user
    clinic.save()

    json_data = {'success': True, 'name': clinic.name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data)


def village_clinic_del_test(request):
    log.info(request.POST)
    village_clinic_id = request.POST.get('village_clinic_id')
    success = True
    village_clinic_name = ''
    try:
        village_clinic = Clinic.objects.get(id=int(village_clinic_id))
        village_clinic_name = village_clinic.name
        village_clinic.delete()
    except Resident.DoesNotExist:
        success = False

    json_data = {'success': success, 'name': village_clinic_name}
    # return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    return JsonResponse(json_data)


def village_clinic_update_test(request):
    success = True
    village_clinic_name = ''

    village_clinic_id = request.POST.get('id')
    name = request.POST.get('name')
    address = request.POST.get('address')
    town_clinic_name = request.POST.get('town_clinic')

    try:
        village_clinic = Clinic.in_village.get(id=int(village_clinic_id))
        village_clinic.name = name
        village_clinic.address = address
        village_clinic.town_clinic = Clinic.in_town.get(name=town_clinic_name)
        village_clinic_name = name
        village_clinic.save()
    except Clinic.DoesNotExist:
        success = False

    json_data = {'success': success, 'name': village_clinic_name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')

    # return JsonResponse(json_data)


def users(request):
    return render(request, 'management/users.html')


def user_query_list(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_user_group = request.POST.get('query_user_group', '')
    query_town_clinic = request.POST.get('query_town_clinic', '')
    query_village_clinic = request.POST.get('query_village_clinic', '')
    query_username = request.POST.get('query_username', '')

    users = User.objects.filter(is_superuser=0)
    if query_user_group and query_user_group != '0':
        users = users.filter(userprofile__role__id=query_user_group)
    if query_town_clinic and query_town_clinic != '0':
        users = users.filter(Q(userprofile__clinic__id=query_town_clinic) |
                             Q(userprofile__clinic__town_clinic__id=query_town_clinic))
    if query_village_clinic and query_village_clinic != '0':
        users = users.filter(userprofile__clinic__id=query_village_clinic)
    if query_username:
        users = users.filter(username__icontains=query_username)

    json_items = []
    for user in users[first: first + page_size]:
        item = model_to_dict(user, fields=['id', 'username'])
        if user.is_superuser:
            item['role'] = u'超级管理员'
        elif user.userprofile:
            if user.userprofile.role:
                item['role'] = user.userprofile.role.name
            if user.userprofile.clinic:
                if user.userprofile.clinic.level == Clinic.TOWN_CLINIC:
                    item['town_clinic'] = user.userprofile.clinic.name
                if user.userprofile.clinic.level == Clinic.VILLAGE_CLINIC:
                    item['town_clinic'] = user.userprofile.clinic.town_clinic.name
                    item['village_clinic'] = user.userprofile.clinic.name

            item['department'] = user.userprofile.department
            item['title'] = user.userprofile.position
            if user.userprofile.resident:
                item['name'] = user.userprofile.resident.name
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': users.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': users.count(), 'rows': json_items})


def get_town_village_clinics(request, town_clinic_id):
    first_text = request.POST.get('first_text', '')
    json_data = []
    json_item = {'id': '0', 'name': first_text}
    json_data.append(json_item)

    if (town_clinic_id != '0'):
        town_clinic = Clinic.in_town.get(id=int(town_clinic_id))
        village_clinics = Clinic.in_village.filter(town_clinic=town_clinic)

        for clinic in village_clinics:
            json_item = dict()
            json_item['id'], json_item['name'] = clinic.id, clinic.name
            json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_town_clinics_edit(request):
    json_data = []
    json_item = {'id': '0', 'name': ''}
    json_data.append(json_item)

    town_clinics = Clinic.in_town.all()
    for clinic in town_clinics:
        json_item = dict()
        json_item['id'], json_item['name'] = clinic.id, clinic.name
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_town_village_clinics_edit(request):
    town_clinic_name = request.POST.get('town_clinic_name')

    village_clinics = Clinic.in_village.filter(town_clinic__name=town_clinic_name)
    json_data = []
    json_item = {'id': '0', 'name': ''}
    json_data.append(json_item)

    for clinic in village_clinics:
        json_item = dict()
        json_item['id'], json_item['name'] = clinic.id, clinic.name
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_roles(request):
    first_text = request.POST.get('first_text', '')
    json_data = []
    json_item = {'id': 0, 'name': first_text}
    json_data.append(json_item)

    roles = Group.objects.all()
    for role in roles:
        json_item = dict()
        json_item['id'], json_item['name'] = role.id, role.name
        json_data.append(json_item)

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)

from django.utils import timezone


def user_add_test(request):
    username = request.POST.get('username').strip()
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        user = User(username=username, is_superuser=False, is_active=True, date_joined=timezone.now())
        group = Group.objects.get(id=int(request.POST.get('user_group')))
        user.is_staff = True if group.groupprofile.is_staff else False
        user.set_password(request.POST.get('password'))
        user.save()

        user_profile = UserProfile(user=user, role=group, create_by=request.user,
                                   department=request.POST.get('department', ''),
                                   position=request.POST.get('position', ''))
        town_clinic_id = int(request.POST.get('town_clinic', '0'))
        if town_clinic_id:
            user_profile.clinic = Clinic.objects.get(id=town_clinic_id)
        village_clinic_id = int(request.POST.get('village_clinic', '0'))
        if village_clinic_id:
            user_profile.clinic = Clinic.objects.get(id=village_clinic_id)
        user_profile.save()

        for service_item in group.groupprofile.default_services.all():
            user_profile.authorized_services.add(service_item)

        success, msg = True, u'添加用户【' + username + u'】成功'
    else:
        success, msg = False, u'使用该用户名的用户已存在'

    return HttpResponse(simplejson.dumps({'success': success, 'message': msg}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': msg})


def user_del_test(request):
    success, message = False, ''
    user_id = int(request.POST.get('user_id', '0'))
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            message = u'用户不存在'
        else:
            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                pass
            else:
                user_profile.delete()
            user.delete()
            success, message = True, u'删除用户' + user.username + u'完成'
    else:
        message = u'用户参数错误'

    #return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
    #                    content_type='text/html; charset=UTF-8')
    return JsonResponse({'success': success, 'message': message})


def service_types(request):
    return render(request, 'management/service_types.html')


def service_type_list_new(request):
    json_items = []
    for service_type in Service.types.all():
        item = model_to_dict(service_type, fields=['id', 'name', 'real_weight', 'should_weight'])
        item['item_num'] = service_type.service_items.all().count()
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': len(json_items), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': len(json_items), 'rows': json_items})


def service_type_options(request):
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]

    serivce_types = Service.types.all()
    for service_type in serivce_types:
        item = model_to_dict(service_type, fields=['id', 'name'])
        json_items.append(item)
    # return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    return JsonResponse(json_items, safe=False)


def service_item_list_new(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_service_type = int(request.POST.get('query_service_type', '0'))
    query_service_item_name = request.POST.get('query_service_item_name', '')

    service_items = Service.items.all()

    if query_service_type:
        service_type = Service.types.get(id=query_service_type)
        service_items = service_items.filter(service_type=service_type)
    if query_service_item_name:
        service_items = service_items.filter(name__icontains=query_service_item_name)

    json_items = []
    for service_item in service_items[first: first + page_size]:
        item = model_to_dict(service_item, fields=['id', 'name', 'price', 'unit'])
        item['service_type'] = service_item.service_type.name
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': service_items.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': service_items.count(), 'rows': json_items})


def service_items(request):
    return render(request, 'management/service_items.html')


def service_item_add_test(request):
    serivce_type_name = request.POST.get('service_type', '')
    serivce_item_name = request.POST.get('name')
    service_price = request.POST.get('price', '')
    service_unit = request.POST.get('unit', '')

    service_type = Service.types.get(name=serivce_type_name)
    try:
        service_items = Service.items.filter(service_type=service_type)
        service_item = service_items.get(name=serivce_item_name)
    except Service.DoesNotExist:
        service_item = Service()
        service_item.name = serivce_item_name
        service_item.price = service_price
        service_item.unit = service_unit
        service_item.level = Service.SERVICE_ITEM
        service_item.service_type = service_type
        service_item.create_by = request.user
        service_item.save()
        success = 'true'
        msg = u'服务项目创建完成'
    else:
        success = 'false'
        msg = u'服务项目已经存在'
    return HttpResponse(simplejson.dumps({'success': success, 'message': msg}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': msg})


def service_item_update_test(request):
    service_item_id = int(request.POST.get('id'))
    name = request.POST.get('name')
    unit = request.POST.get('unit')
    price = request.POST.get('price')
    try:
        service_item = Service.items.get(id=service_item_id)
    except Service.DoesNotExist:
        success = False
    else:
        if name != service_item.name:
            service_item.name = name
        if unit:
            service_item.unit = unit
        if price:
            service_item.price = float(price)
        service_item.save()
        success = True

    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success})


def service_item_del_test(request):
    service_item_id = int(request.POST.get('service_item_id'))
    try:
        service_item = Service.items.get(id=service_item_id)
    except Service.DoesNotExist:
        success = 'false'
        msg = u'所要删除的服务记录不存在'
    else:
        service_item.delete()
        success = 'true'
        msg = u'服务记录删除完成'

    return HttpResponse(simplejson.dumps({'success': success, 'message': msg}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': msg})


def records(request):
    return render(request, 'management/records.html')


def record_list_new(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_record_begin = request.POST.get('query_record_begin')
    query_record_end = request.POST.get('query_record_end')
    query_service_type = int(request.POST.get('query_service_type'))
    query_service_item = int(request.POST.get('query_service_item'))
    query_doctor = request.POST.get('query_doctor').strip()
    query_resident = request.POST.get('query_resident').strip()
    query_town_clinic = int(request.POST.get('query_town_clinic'))
    query_village_clinic = int(request.POST.get('query_village_clinic'))

    records = WorkRecord.objects.all()

    if query_town_clinic:
        town_clinic = Clinic.in_town.get(id=int(query_town_clinic))
        records = records.filter(provider__userprofile__clinic__town_clinic=town_clinic)
    if query_village_clinic:
        village_clinic = Clinic.in_village.get(id=int(query_village_clinic))
        records = records.filter(provider__userprofile__clinic=village_clinic)
    if query_service_type:
        service_type = Service.types.get(id=int(query_service_type))
        records = records.filter(service_item__service_type=service_type)
    if query_service_item:
        service_item = Service.items.get(id=int(query_service_item))
        records = records.filter(service_item=service_item)
    if query_doctor:
        records = records.filter(provider__username=query_doctor)
    if query_resident:
        records = records.filter(resident__name=query_resident)

    start_date = datetime.strptime(query_record_begin, '%Y-%m-%d').date()
    start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
    start_time = bj_tz.localize(start_time)
    end_date = datetime.strptime(query_record_end, '%Y-%m-%d')
    if end_date.date() < date.today():
        end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
        end_time = bj_tz.localize(end_time)
    else:
        end_time = bj_tz.localize(datetime.today())

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)
    records = records.filter(service_item__level=Service.SERVICE_ITEM)

    json_items = []
    for record in records[first: first + page_size]:
        item = model_to_dict(record, fields=['id', 'submit_time'])
        item['doctor'] = record.provider.username
        item['resident'] = record.resident.name
        try:
            if record.provider.userprofile.clinic.level == Clinic.TOWN_CLINIC:
                item['town_clinic'] = record.provider.userprofile.clinic.name
                item['village_clinic'] = ''
            else:
                item['village_clinic'] = record.provider.userprofile.clinic.name
                item['town_clinic'] = record.provider.userprofile.clinic.town_clinic.name
        except ObjectDoesNotExist:
            pass
        item['service_type'] = record.service_item.service_type.name
        item['service_item'] = record.service_item.name
        item['submit_time'] = record.submit_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')

        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': records.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': records.count(), 'rows': json_items})


def service_item_options(request):
    first_text = request.POST.get('first_text', '')
    query_service_type = int(request.POST.get('query_service_type', '0'))
    service_type_name = request.POST.get('service_type_name', '')

    json_items = [{'id': 0, 'name': first_text}]

    service_items = Service.items.all()
    if query_service_type:
        service_type = Service.types.get(id=query_service_type)
        service_items = service_items.filter(service_type=service_type)

    for service_item in service_items:
        item = model_to_dict(service_item, fields=['id', 'name'])
        if service_type_name:
            item['service_type_name'] = service_item.service_type.name
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def town_clinic_options(request):
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]

    town_clinics = Clinic.in_town.all()
    for town_clinic in town_clinics:
        json_items.append(model_to_dict(town_clinic, fields=['id', 'name']))

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def village_clinic_options(request):
    first_text = request.POST.get('first_text', '')
    query_town_clinic = int(request.POST.get('query_town_clinic', '0'))
    json_items = [{'id': 0, 'name': first_text}]

    village_clinics = Clinic.in_village.all()
    if query_town_clinic:
        town_clinic = Clinic.in_town.get(id=query_town_clinic)
        village_clinics = village_clinics.filter(town_clinic=town_clinic)

    for village_clinic in village_clinics:
        item = model_to_dict(village_clinic, fields=['id', 'name'])
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def payment(request):
    return render(request, 'management/payment.html')


def payment_list_new(request):
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    query_record_begin = request.POST.get('query_record_begin')
    query_record_end = request.POST.get('query_record_end')
    query_service_type = int(request.POST.get('query_service_type'))
    query_service_item = int(request.POST.get('query_service_item'))
    query_doctor = request.POST.get('query_doctor').strip()
    query_resident = request.POST.get('query_resident').strip()
    query_town_clinic = int(request.POST.get('query_town_clinic'))
    query_village_clinic = int(request.POST.get('query_village_clinic'))

    records = WorkRecord.objects.all()
    service_items = Service.items.all()

    if query_town_clinic:
        town_clinic = Clinic.in_town.get(id=int(query_town_clinic))
        records = records.filter(provider__userprofile__clinic__town_clinic=town_clinic)
    if query_village_clinic:
        village_clinic = Clinic.in_village.get(id=int(query_village_clinic))
        records = records.filter(provider__userprofile__clinic=village_clinic)
    if query_service_type:
        service_type = Service.types.get(id=int(query_service_type))
        records = records.filter(service_item__service_type=service_type)
        service_items = service_items.filter(service_type=service_type)
    if query_service_item:
        service_item = Service.items.get(id=int(query_service_item))
        records = records.filter(service_item=service_item)
        service_items = [service_item]
    if query_doctor:
        records = records.filter(provider__username=query_doctor)
    if query_resident:
        records = records.filter(resident__name=query_resident)

    start_date = datetime.strptime(query_record_begin, '%Y-%m-%d')
    start_time = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
    start_time = bj_tz.localize(start_time)
    end_date = datetime.strptime(query_record_end, '%Y-%m-%d')
    if end_date.date() < date.today():
        end_time = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
        end_time = bj_tz.localize(end_time)
    else:
        end_time = bj_tz.localize(datetime.today())

    records = records.filter(submit_time__lt=end_time, submit_time__gt=start_time)

    workload = {}
    for service_item in service_items:
        workload[service_item] = 0

    for record in records:
        if record.status == WorkRecord.FINISHED and record.service_item.is_service_item:
            workload[record.service_item] += 1

    total_payment = 0
    total_workload = 0
    for service_item in service_items:
        total_workload += workload[service_item]
        total_payment += workload[service_item] * service_item.price
    json_items = [{'service_type': '合计', 'service_item': '',
                   'workload': total_workload, 'payment': total_payment}]

    for service_item in service_items[first: first + page_size]:
        json_items.append({
            'service_type': service_item.service_type.name,
            'service_item': service_item.name,
            'workload': str(workload[service_item]) + service_item.unit,
            'payment': workload[service_item] * service_item.price})

    return HttpResponse(simplejson.dumps({'total': service_items.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': service_items.count(), 'rows': json_items})


def roles(request):
    return render(request, 'management/roles.html')


def role_list_new(request):
    groups = Group.objects.all()
    json_items = []
    for group in groups:
        item = model_to_dict(group, fields=['id', 'name'])
        if group.groupprofile:
            item['is_staff'] = group.groupprofile.is_staff
        item['user_num'] = group.users.all().count()
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def get_role_authorize(request):
    role_id = int(request.POST.get('role_id'))
    role = Group.objects.get(id=role_id)

    json_items = []
    for service in role.groupprofile.default_services.all():
        if service.level == Service.SERVICE_ITEM:
            json_items.append(str(service.id))

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def role_authorize(request):
    role_id = int(request.POST.get('role_id'))
    group_profile = Group.objects.get(id=role_id).groupprofile
    service_item_select = request.POST.getlist('service_item_select')

    service_item_origin = []
    for item_id in group_profile.default_services.filter(level=Service.SERVICE_ITEM):
        service_item_origin.append(str(item_id.id))

    item_to_add = set(service_item_select) - set(service_item_origin)
    item_to_del = set(service_item_origin) - set(service_item_select)

    for item_id in item_to_add:
        service_item = Service.objects.get(id=int(item_id))
        service_type = service_item.service_type
        if service_type not in group_profile.default_services.all():
            group_profile.default_services.add(service_type)
        group_profile.default_services.add(service_item)

    for item_id in item_to_del:
        service_item = Service.objects.get(id=int(item_id))
        group_profile.default_services.remove(service_item)
        service_type = service_item.service_type
        if set(service_type.service_items.all()) - \
                set(group_profile.default_services.all()):
            pass
        else:
            group_profile.default_services.remove(service_type)

    group_profile.save()

    return HttpResponse(simplejson.dumps({'success': True}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': 'true'})


def sms_sent(request):
    return render(request, 'management/sms_sent.html')


def sms_sent_list(request):
    sms_begin = request.POST.get('sms_begin')
    sms_end = request.POST.get('sms_end')
    service_type = int(request.POST.get('service_type'))
    service_item = int(request.POST.get('service_item'))
    resident = request.POST.get('resident').strip()
    mobile = request.POST.get('mobile').strip()
    status = int(request.POST.get('status'))

    sms_list = Sms.objects.all()

    sms_begin = datetime.strptime(sms_begin, '%Y-%m-%d').date()
    sms_list = sms_list.filter(next_time_date__gte=sms_begin)
    sms_end = datetime.strptime(sms_end, '%Y-%m-%d').date()
    sms_list = sms_list.filter(next_time_date__lte=sms_end)

    if service_type:
        service_type = Service.types.get(id=service_type)
        sms_list = sms_list.filter(service_type_name=service_type.name)
    if service_item:
        service_item = Service.items.get(id=service_item)
        sms_list = sms_list.filter(service_item_name=service_item.name)

    if resident:
        sms_list = sms_list.filter(name=resident)
    if mobile:
        sms_list = sms_list.filter(mobile=mobile)
    if status:
        sms_list = sms_list.filter(status=status)

    json_items = []
    for sms in sms_list:
        item = model_to_dict(sms, fields=['id', 'name', 'mobile', 'message', 'status',
                                          'service_type_name', 'service_item_name'])
        item['next_time_date'] = sms.next_time_date.strftime('%Y-%m-%d')
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def sms_setup_page(request):
    return render(request, 'management/sms_setup.html')

from django.core.exceptions import ObjectDoesNotExist


def sms_setup_list(request):
    service_type = int(request.POST.get('service_type'))
    service_item = int(request.POST.get('service_item'))
    sms_begin = request.POST.get('sms_begin')
    sms_end = request.POST.get('sms_end')
    town_clinic = int(request.POST.get('town_clinic'))
    author = request.POST.get('author')
    updater = request.POST.get('updater')
    status = int(request.POST.get('status'))

    sms_setups = SmsTime.objects.all()

    if service_type:
        service_type = Service.types.get(id=service_type)
        sms_setups = sms_setups.filter(service_item__service_type=service_type)
    if service_item:
        service_item = Service.items.get(id=service_item)
        sms_setups = sms_setups.filter(service_item_=service_item)

    sms_begin = datetime.strptime(sms_begin, '%Y-%m-%d').date()
    sms_end = datetime.strptime(sms_end, '%Y-%m-%d').date()
    sms_setups = sms_setups.filter(service_time__gte=sms_begin)
    sms_setups = sms_setups.filter(service_time__lte=sms_end)

    if town_clinic:
        town_clinic = Clinic.in_town.get(id=town_clinic)
        sms_setups = sms_setups.filter(create_by__userprofile__clinic__town_clinic=town_clinic)
    if author:
        author = User.objects.get(username=author)
        sms_setups = sms_setups.filter(create_by=author)
    if updater:
        updater = User.objects.get(username=updater)
        sms_setups = sms_setups.filter(update_by=updater)
    if status:
        sms_setups = sms_setups.filter(status=status)

    json_items = []
    for setup in sms_setups:
        item = model_to_dict(setup, fields=['id', 'status'])
        item['service_type'] = setup.service_type.name
        item['service_type_id'] = setup.service_type.id
        item['service_item'] = setup.service_item.name
        item['service_item_id'] = setup.service_item.id
        item['service_time'] = setup.service_time.strftime('%Y-%m-%d')
        if setup.create_by:
            item['author'] = setup.create_by.username
            try:
                if setup.create_by.userprofile.clinic.is_town_clinic:
                    item['town_clinic'] = setup.create_by.userprofile.clinic.name
                elif setup.create_by.userprofile.clinic.is_village_clinic:
                    item['town_clinic'] = setup.create_by.userprofile.clinic.town_clinic.name
            except ObjectDoesNotExist:
                pass
        if setup.update_by:
            item['updater'] = setup.update_by.username
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


def sms_setup_add(request):
    service_type = int(request.POST.get('service_type'))
    service_item = int(request.POST.get('service_item'))
    service_time = request.POST.get('service_time')

    sms_setup = SmsTime()
    sms_setup.service_type = Service.types.get(id=service_type)
    sms_setup.service_item = Service.items.get(id=service_item)
    sms_setup.service_time = datetime.strptime(service_time, '%Y-%m-%d').date()
    sms_setup.status = SmsTime.UNFINISHED
    sms_setup.create_by = request.user

    sms_setup.save()
    return HttpResponse(simplejson.dumps({'success': True}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': True})


def sms_setup_update(request):
    sms_setup_id = int(request.POST.get('id'))
    service_type = int(request.POST.get('service_type'))
    service_item = int(request.POST.get('service_item'))
    service_time = request.POST.get('service_time')

    sms_setup = SmsTime.objects.get(id=sms_setup_id)
    sms_setup.service_type = Service.types.get(id=service_type)
    sms_setup.service_item = Service.items.get(id=service_item)
    sms_setup.service_time = datetime.strptime(service_time, '%Y-%m-%d').date()
    sms_setup.update_by = request.user

    sms_setup.save()
    return HttpResponse(simplejson.dumps({'success': True}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': True})


def sms_setup_del(request):
    sms_setup_id = int(request.POST.get('id'))
    try:
        sms_setup = SmsTime.objects.get(id=sms_setup_id)
    except SmsTime.DoesNotExist:
        success = False
    else:
        sms_setup.delete()
        success = True
    return HttpResponse(simplejson.dumps({'success': success}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success})


def resident_add_hypertension(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.hypertension == 1:
        success = False
        message = u'已经在高血压人群中'
    else:
        resident.hypertension = 1
        resident.save()
        success = True
        message = u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': message})


def resident_add_diabetes(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.diabetes == 1:
        success = False
        message = u'已经在高血压人群中'
    else:
        resident.diabetes = 1
        resident.save()
        success = True
        message = u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': message})


def resident_add_psychiatric(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.psychiatric == 1:
        success = False
        message = u'已经在高血压人群中'
    else:
        resident.psychiatric = 1
        resident.save()
        success = True
        message = u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': message})


def resident_add_pregnant(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.pregnant == 1:
        success = False
        message = u'已经在高血压人群中'
    else:
        resident.pregnant = 1
        resident.save()
        success = True
        message = u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': message})
