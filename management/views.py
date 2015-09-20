# -*- encoding: utf-8 -*-
from datetime import datetime, date
import simplejson

from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from .models import Clinic, Region, UserProfile, Service, Resident, WorkRecord, Sms, SmsTime

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')

import logging
debug = logging.getLogger('debug')


def excel_file(request):
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


def residents_page(request):
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


def village_clinics_page(request):
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

# 乡镇卫生院和村卫生室列表，用于页面上下拉列表的选项
# 乡镇和村庄（街道）列表，用于页面上下拉列表的选项
# 服务类别和服务项目列表，用于页面上下拉列表的选项


def town_options(request):
    """
    参数：request的POST传递参数first_text，作为列表第一项的名称
    返回值：返回所有乡镇的列表，列表的第一项id为0，名称由POST所传递的first_text确定
    """
    first_text = request.POST.get('first_text') if 'first_text' in request.POST else u'全部'
    json_data = [{'id': 0, 'name': first_text}]
    json_data += [model_to_dict(town, fields=['id', 'name']) for town in Region.towns.all()]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


def town_village_options(request, town_id):
    """
    参数：URL链接中town_id指定乡镇id
    返回值：town_id所指定乡镇所下属的所有村庄（街道）列表
    """
    json_data = [{'id': '0', 'name': '全部'}]
    try:
        villages = Region.villages.filter(town=Region.towns.get(id=town_id))
    except Region.DoesNotExist:
        pass
    else:
        json_data += [model_to_dict(village, fields=['id', 'name']) for village in villages]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


def town_name_village_options(request):
    """
    参数：request.POST中的town_name指定乡镇名称
    返回值：town_name所指定乡镇下属的所有村庄（街道）列表
    """
    json_data = [{'id': '0', 'name': ''}]
    town_name = request.POST.get('town_name')
    try:
        villages = Region.villages.filter(town=Region.towns.get(name=town_name))
    except Region.DoesNotExist:
        pass
    else:
        json_data += [model_to_dict(village, fields=['id', 'name']) for village in villages]

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


def town_clinic_options(request):
    """
    参数：request.POST中的first_text指定列表第一项的名称
    返回值：返回所有乡镇卫生院列表，第一项id为0，名称由first_text指定
    """
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]
    json_items += [model_to_dict(clinic, fields=['id', 'name']) for clinic in Clinic.in_town.all()]
    return JsonResponse(json_items, safe=False)


def village_clinic_options(request):
    """
    参数：request.POST中的first_text指定列表第一项的名称
    参数：request.POST中的query_town_clinic指定筛选该乡镇卫生院下属的村卫生室
    返回值：返回指定乡镇卫生院下属的村卫生室列表，第一项id为0，名称由first_text指定
    """
    first_text = request.POST.get('first_text', '')
    query_town_clinic = int(request.POST.get('query_town_clinic', 0))
    json_items = [{'id': 0, 'name': first_text}]
    options = Clinic.in_village.all()
    if query_town_clinic:
        town_clinic = Clinic.in_town.get(id=query_town_clinic)
        options = options.filter(town_clinic=town_clinic)
    json_items += [model_to_dict(clinic, fields=['id', 'name']) for clinic in options]
    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')


def get_town_village_clinics(request, town_clinic_id):
    first_text = request.POST.get('first_text', '')
    json_data = [{'id': '0', 'name': first_text}]

    if town_clinic_id != '0':
        town_clinic = Clinic.in_town.get(id=int(town_clinic_id))
        clinics = Clinic.in_village.filter(town_clinic=town_clinic)
        json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in clinics]

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


def get_town_clinics_edit(request):
    json_data = [{'id': '0', 'name': ''}]
    json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in Clinic.in_town.all()]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


def get_town_village_clinics_edit(request):
    town_clinic_name = request.POST.get('town_clinic_name')
    clinics = Clinic.in_village.filter(town_clinic__name=town_clinic_name)
    json_data = [{'id': '0', 'name': ''}]
    json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in clinics]
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


def users_page(request):
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


def service_types_page(request):
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


def service_items_page(request):
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


def records_page(request):
    return render(request, 'management/records_page.html')


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


def payment_page(request):
    return render(request, 'management/payment_page.html')


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
        if record.service_item:
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


def roles_page(request):
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

from management.models import GroupProfile


def role_add(request):
    name = request.POST.get('name')
    group = Group(name=name)
    group.save()

    is_staff = int(request.POST.get('is_staff'))
    profile = GroupProfile(is_staff=is_staff)
    profile.group = group
    profile.create_by = request.user
    profile.save()

    return JsonResponse({'success': True})


def role_del(request):
    try:
        group = Group.objects.get(id=int(request.POST.get('id')))
    except Group.DoesNotExist:
        success = False
    else:
        try:
            group_profile = group.groupprofile
        except ObjectDoesNotExist:
            pass
        else:
            group_profile.delete()
        group.delete()
        success = True

    return JsonResponse({'success': success})

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
        success, message = False, u'已经在高血压人群中'
    else:
        resident.hypertension = 1
        resident.save()
        success, message = True, u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


def resident_add_diabetes(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.diabetes == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.diabetes = 1
        resident.save()
        success, message = True, u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


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


def resident_add_pregnant(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.pregnant == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.pregnant = 1
        resident.save()
        success, message = True, u''
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')

import json


def graphs(request):
    return render(request, 'management/graphs.html')


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
            if record.service_item and record.service_item.is_service_item:
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
            if record.service_item and record.service_item.is_service_item:
                if record.service_item.price:
                    payment[town_clinic.name] += record.service_item.price
                    total_payment += record.service_item.price

    total_payment *= 1.0
    percent = [{'name': key, 'y': value/total_payment} for key, value in payment.items()]

    return HttpResponse(simplejson.dumps(percent), content_type='text/html; charset=UTF-8')
    # return JsonResponse(percent, safe=False)

"""
工作量统计及相关功能页面
"""


def workload_stat_page(request):
    return render(request, 'management/workload_stat_page.html')


def workload_town_clinics_page(request):
    return render(request, 'management/workload_town_clinics_page.html')


from services.utils import new_year_day
import collections


def workload_town_clinics_datagrid(request):
    """
    函数说明：计算各个卫生院各个服务类别的工作量及合计
    """
    workload = collections.OrderedDict()

    for town_clinic in Clinic.in_town.all():
        workload[town_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = dict()
    for service_type in Service.types.all():
        workload['合计'][service_type.alias] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_day()):
        try:
            town_clinic = record.provider.userprofile.clinic.town_clinic
        except ObjectDoesNotExist:
            pass
        else:
            if record.service_item and record.service_item.is_service_item:  # 这是一个计费项目
                service_type = record.service_item.service_type
                workload[town_clinic.name][service_type.alias] += 1
                workload['合计'][service_type.alias] += 1

    json_data = []
    for key, value in workload.items():
        try:
            clinic = Clinic.in_town.get(name=key)
        except Clinic.DoesNotExist:
            id = 0
        else:
            id = clinic.id
        item = {'id': id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    debug.info(len(json_data))
    return JsonResponse(json_data, safe=False)


def workload_village_clinics_page(request, town_clinic_id):
    return render(request, 'management/workload_village_clinics_page.html',
                  {'town_clinic_id': town_clinic_id})


def workload_village_clinics_datagrid(request, town_clinic_id):
    """
    函数说明：计算指定卫生院各个服务类别的工作量及合计
    参数：town_clinic_id，指定卫生院的id
    返回：指定卫生院下属卫生室的各服务类别的工作量及合计
    """
    town_clinic = Clinic.in_town.get(id=int(town_clinic_id))

    workload = collections.OrderedDict()
    for village_clinic in town_clinic.village_clinics.all():
        workload[village_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = dict()
    for service_type in Service.types.all():
        workload['合计'][service_type.alias] = 0

    records = WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_day())
    for record in records:
        if record.service_item and record.service_item.is_service_item: # 这是一个计费项目
            try:
                clinic = record.provider.userprofile.clinic
            except ObjectDoesNotExist:
                pass
            else:
                service_type = record.service_item.service_type
                if clinic.town_clinic == town_clinic:
                    workload[clinic.name][service_type.alias] += 1
                    workload['合计'][service_type.alias] += 1

    json_data = []
    for key, value in workload.items():
        try:
            village_clinic = Clinic.objects.get(town_clinic=town_clinic, name=key)
        except Clinic.DoesNotExist:
            id = 0
        else:
            id = village_clinic.id
        item = {'id': id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


def workload_doctors_page(request, clinic_id):
    return render(request, 'management/workload_doctors_page.html', {'clinic_id': clinic_id})


def workload_doctors_datagrid(request, clinic_id):
    """
    函数说明：计算指定卫生机构中各位医生的工作量（分类和合计）
    参数：clinic_id，指定卫生机构的id
    返回：指定卫生机构中各位医生的各服务类别的工作量及合计
    """
    clinic = Clinic.objects.get(id=int(clinic_id))

    workload = collections.OrderedDict()
    for doctor in clinic.users.all():
        workload[doctor.user.username] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = dict()
    for service_type in Service.types.all():
        workload['合计'][service_type.alias] = 0

    records = WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_day())
    for record in records:
        if record.service_item and record.service_item.is_service_item:  # 这是一个计费项目
            try:
                provider_clinic = record.provider.userprofile.clinic
            except ObjectDoesNotExist:
                pass
            else:
                if provider_clinic == clinic:  # 指定医疗机构的服务记录被累加
                    service_type = record.service_item.service_type
                    workload[record.provider.username][service_type.alias] += 1
                    workload['合计'][service_type.alias] += 1

    json_data = []
    for key, value in workload.items():
        try:
            doctor = User.objects.get(username=key)
        except User.DoesNotExist:
            id = 0
        else:
            id = doctor.id
        item = {'id': id, 'name': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


def workload_list_page(request, provider_id):
    return render(request, 'management/workload_list_page.html', {'provider_id': provider_id})


def workload_list_datagrid(request, provider_id):
    provider = User.objects.get(id=int(provider_id))
    records = WorkRecord.objects.filter(provider=provider).order_by('-submit_time')

    json_items = []
    for record in records:
        item = dict()
        item['id'] = record.id
        item['ehr_no'] = record.resident.ehr_no
        item['resident_id'] = record.resident.id
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
        json_items.append(item)

    return JsonResponse(json_items, safe=False)


def resident_records_page(request, resident_id):
    return render(request, 'management/resident_records_datagrid.html',
                  {'resident_id': resident_id})


def resident_records_datagrid(request, resident_id):
    resident = Resident.objects.get(id=int(resident_id))
    records = WorkRecord.objects.filter(resident=resident).order_by('-submit_time')

    json_items = []
    for record in records:
        if record.service_item:
            item = model_to_dict(resident, fields=['ehr_no', 'name'])
            item['id'] = record.id
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
            json_items.append(item)
    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')

"""
支付金额相关的统计页面和功能
"""


def payment_stat_page(request):
    return render(request, 'management/payment_stat_page.html')


def payment_town_clinics_page(request):
    return render(request, 'management/payment_town_clinics_page.html')


def payment_town_clinics_datagrid(request):
    """
    函数说明：计算各个卫生院各个服务类别的工作量及合计
    """
    payment = collections.OrderedDict()

    for town_clinic in Clinic.in_town.all():
        payment[town_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    payment['合计'] = dict()
    for service_type in Service.types.all():
        payment['合计'][service_type.alias] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_day()):
        try:
            town_clinic = record.provider.userprofile.clinic.town_clinic
        except ObjectDoesNotExist:
            pass
        else:
            if record.service_item and record.service_item.is_service_item:  # 这是一个计费项目
                service_type = record.service_item.service_type
                payment[town_clinic.name][service_type.alias] += record.service_item.price
                payment['合计'][service_type.alias] += record.service_item.price

    json_data = []
    for key, value in payment.items():
        try:
            clinic = Clinic.in_town.get(name=key)
        except Clinic.DoesNotExist:
            id = 0
        else:
            id = clinic.id
        item = {'id': id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


def payment_village_clinics_page(request, town_clinic_id):
    return render(request, 'management/payment_village_clinics_page.html', {'town_clinic_id': town_clinic_id})


def payment_village_clinics_datagrid(request, town_clinic_id):
    payment = collections.OrderedDict()
    town_clinic = Clinic.in_town.get(id=int(town_clinic_id))

    for village_clinic in town_clinic.village_clinics.all():
        payment[village_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    payment['合计'] = dict()
    for service_type in Service.types.all():
        payment['合计'][service_type.alias] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_day()):
        if record.service_item and record.service_item.is_service_item:  # 这是一个计费项目
            try:
                clinic = record.provider.userprofile.clinic
            except ObjectDoesNotExist:
                pass
            else:
                if clinic.town_clinic == town_clinic:
                    service_type = record.service_item.service_type
                    payment[clinic.name][service_type.alias] += record.service_item.price
                    payment['合计'][service_type.alias] += record.service_item.price

    json_data = []
    for key, value in payment.items():
        item = {'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


def modify_apply_page(request):
    return render(request, 'management/modify_apply_page.html')

from .models import ModifyApply
from datetime import timedelta


def modify_apply_list(request):
    applications = ModifyApply.objects.all()
    json_data = []
    for each in applications:
        json_item = model_to_dict(each, fields=['id'])
        json_item['apply_time'] = each.apply_time.astimezone(bj_tz).strftime('%Y-%m-%d %H:%M:%S')
        record = each.work_record
        json_item['username'] = record.provider.username
        json_item['role'] = record.provider.userprofile.role.name
        json_item['resident'] = record.resident.name

        if record.provider.userprofile.clinic.is_town_clinic:
            json_item['town_clinic'] = record.provider.userprofile.clinic.name
        else:
            json_item['town_clinic'] = record.provider.userprofile.clinic.town_clinic.name
            json_item['village_clinic'] = record.provider.userprofile.clinic.name
        if record.service_item.is_service_item:
            json_item['service_type'] = record.service_item.service_type.name
            json_item['service_item'] = record.service_item.name

        if each.finance_opinion:
            if each.finance_opinion == ModifyApply.WAITING:
                json_item['finance_opinion'] = u'等待审批'
            elif each.finance_opinion == ModifyApply.AGREE:
                json_item['finance_opinion'] = u'同意'
            elif each.finance_opinion == ModifyApply.DISAGREE:
                json_item['finance_opinion'] = u'不同意'
        if each.health_opinion:
            if each.health_opinion == ModifyApply.WAITING:
                json_item['health_opinion'] = u'等待审批'
            elif each.health_opinion == ModifyApply.AGREE:
                json_item['health_opinion'] = u'同意'
            elif each.health_opinion == ModifyApply.DISAGREE:
                json_item['health_opinion'] = u'不同意'

        if each.apply_status != ModifyApply.OVERDUE \
                and timezone.now() > each.apply_time + timedelta(days=2):
            each.apply_status = ModifyApply.OVERDUE
            each.save()

        if each.apply_status == ModifyApply.SUBMITTED:
            json_item['status'] = u'已提交'
        elif each.apply_status == ModifyApply.CANCELED:
            json_item['status'] = u'已取消'
        elif each.apply_status == ModifyApply.AGREED:
            json_item['status'] = u'已批准'
        elif each.apply_status == ModifyApply.REFUSED:
            json_item['status'] = u'未批准'
        elif each.apply_status == ModifyApply.RECTIFIED:
            json_item['status'] = u'已修改'
        elif each.apply_status == ModifyApply.OVERDUE:
            json_item['status'] = u'已过期'

        json_data.append(json_item)

    return JsonResponse(json_data, safe=False)


def modify_apply_opinion(request):
    opinion = request.POST.get('opinion')
    application = ModifyApply.objects.get(id=int(request.POST.get('id')))
    if opinion == 'agree':
        application.health_opinion = ModifyApply.AGREE
        application.finance_opinion = ModifyApply.AGREE
        application.apply_status = ModifyApply.AGREED
    elif opinion == 'disagree':
        application.health_opinion = ModifyApply.DISAGREE
        application.finance_opinion = ModifyApply.DISAGREE
        application.apply_status = ModifyApply.REFUSED
    application.health_opinion_time = timezone.now()
    application.financial_opinion_time = timezone.now()
    application.save()
    return JsonResponse({'success': True})