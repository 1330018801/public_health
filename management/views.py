# -*- encoding: utf-8 -*-
from datetime import datetime, date
import simplejson
import xlwt

from django.utils.encoding import smart_unicode
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .models import Clinic, Region, UserProfile, Service, Resident, WorkRecord, Sms, SmsTime, AdminNav, GroupProfile

import pytz
bj_tz = pytz.timezone('Asia/Shanghai')

import logging
debug = logging.getLogger('debug')


@login_required(login_url='/')
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


def excel_sheets(request):
    workbook = xlwt.Workbook()

    # 工作量报表
    sheet_workload = workbook.add_sheet(u'工作量统计')
    sheet_workload.write(0, 0, smart_unicode('医疗机构'))
    sheet_workload.write(0, 1, smart_unicode('健康教育'))
    sheet_workload.write(0, 2, smart_unicode('预防接种'))
    sheet_workload.write(0, 3, smart_unicode('0-6岁儿童'))
    sheet_workload.write(0, 4, smart_unicode('孕产妇'))
    sheet_workload.write(0, 5, smart_unicode('老年人'))
    sheet_workload.write(0, 6, smart_unicode('高血压'))
    sheet_workload.write(0, 7, smart_unicode('2型糖尿病'))
    sheet_workload.write(0, 8, smart_unicode('重性精神病'))
    sheet_workload.write(0, 9, smart_unicode('中医药'))
    sheet_workload.write(0, 10, smart_unicode('传染病报告'))
    sheet_workload.write(0, 11, smart_unicode('卫生监督'))
    sheet_workload.write(0, 12, smart_unicode('合计'))

    # 计算工作量的函数，获取工作量
    clinics = Clinic.in_town.all().order_by('id')
    workload = dict()
    for clinic in Clinic.in_town.all().order_by('id'):
        workload[clinic.name] = dict()
        for service_type in Service.types.all().order_by('id'):
            workload[clinic.name][service_type.name] = 0

    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED, service_item__isnull=False,
                                            provider__userprofile__clinic__in=clinics):
        if record.service_item.is_service_item:
            service_type = record.service_item.service_type
            clinic = record.provider.userprofile.clinic
            workload[clinic.name][service_type.name] += 1

    for i, clinic in enumerate(Service.types.all().order_by('id')):
        sheet_workload.write(i + 1, 0, smart_unicode(clinic.name))

    '''
    records = WorkRecord.objects.all()
    for i, record in enumerate(records):
        sheet_workload.write(i + 1, 0, smart_unicode(record.provider.username))
        sheet_workload.write(i + 1, 1, smart_unicode(record.resident.name))
        sheet_workload.write(i + 1, 2, smart_unicode(record.service_item.name))
        sheet_workload.write(i + 1, 3, smart_unicode(record.submit_time))
    '''

    # 支付费用报表
    sheet_payment = workbook.add_sheet(u'支付金额统计')
    sheet_payment.write(0, 0, smart_unicode('医疗机构'))
    sheet_payment.write(0, 1, smart_unicode('健康教育'))
    sheet_payment.write(0, 2, smart_unicode('预防接种'))
    sheet_payment.write(0, 3, smart_unicode('0-6岁儿童'))
    sheet_payment.write(0, 4, smart_unicode('孕产妇'))
    sheet_payment.write(0, 5, smart_unicode('老年人'))
    sheet_payment.write(0, 6, smart_unicode('高血压'))
    sheet_payment.write(0, 7, smart_unicode('2型糖尿病'))
    sheet_payment.write(0, 8, smart_unicode('重性精神病'))
    sheet_payment.write(0, 9, smart_unicode('中医药'))
    sheet_payment.write(0, 10, smart_unicode('传染病报告'))
    sheet_payment.write(0, 11, smart_unicode('卫生监督'))
    sheet_payment.write(0, 12, smart_unicode('合计'))

    # 计算支付费用的函数，获取支付费用
    '''
    records = WorkRecord.objects.all()
    for i, record in enumerate(records):
        sheet_payment.write(i + 1, 0, smart_unicode(record.provider.username))
        sheet_payment.write(i + 1, 1, smart_unicode(record.resident.name))
        sheet_payment.write(i + 1, 2, smart_unicode(record.service_item.name))
        sheet_payment.write(i + 1, 3, smart_unicode(record.submit_time))
    '''

    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=work_recode.xls'

    workbook.save(response)
    return response


# 某个制定机构下属的医疗机构的各医疗机构的工作量统计
# 如果没有指定机构，则根据用户类型判断，卫生局和财政局管理员，统计所有卫生院
# 卫生院管理员，统计所有下属卫生室


def is_finance_admin(user):
    """
    功能函数：判断用户是否是财政局管理员
    """
    if not user.is_superuser:
        try:
            role = user.userprofile.role
        except ObjectDoesNotExist:
            pass
        else:
            if role.name == u'财政局管理员':
                return True
    return False


def is_health_admin(user):
    """
    功能函数：判断用户是否是财卫生局管理员
    """
    if not user.is_superuser:
        try:
            role = user.userprofile.role
        except ObjectDoesNotExist:
            pass
        else:
            if role.name == u'卫生局管理员':
                return True
    return False


def is_town_clinic_admin(user):
    """
    功能函数：判断用户是否是卫生院管理员
    """
    if user.is_staff:
        if user.is_superuser or is_finance_admin(user) or is_health_admin(user):
            return False
        else:
            return True
    return False


@login_required(login_url='/')
def workload_sheet(request, clinic_id):
    if clinic_id is None:
        user = request.user
        if user.is_superuser or is_finance_admin(user) or is_health_admin(user):
            clinics = Clinic.in_town.all()
        elif user.is_town_clinic_admin(user):
            clinics = user.userprofile.clinic.village_clinics.all()
    else:
        try:
            clinic = Clinic.objects.get(id=int(clinic_id))
        except Clinic.DoesNotExist:
            pass  # 后续处理
        else:
            if clinic.is_town_clinic:
                clinics = clinic.village_clinics.all()
            else:
                pass  # 后续处理

    workload = collections.OrderedDict()
    for clinic in clinics:
        workload[clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = dict()
    for service_type in Service.types.all():
        workload['合计'][service_type.alias] = 0

    records = WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_time())
    for record in records:
        if record.service_item and record.service_item.is_service_item:  # 这是一个计费项目
            try:
                clinic = record.provider.userprofile.clinic
            except ObjectDoesNotExist:
                pass
            else:
                service_type = record.service_item.service_type
                if clinic.is_town_clinic and clinic in clinics:
                    workload[clinic.name][service_type.alias] += 1
                    workload['合计'][service_type.alias] += 1
                elif clinic.is_village_clinic and clinic in clinics:
                    workload[clinic.name][service_type.alias] += 1
                    workload['合计'][service_type.alias] += 1
                elif clinic.is_village_clinic and clinic not in clinics:
                    if clinic.town_clinic in clinics:
                        pass
    '''
    json_data = []
    for key, value in workload.items():
        try:
            village_clinic = Clinic.objects.get(town_clinic=town_clinic, name=key)
        except Clinic.DoesNotExist:
            item = {'id': 0, 'clinic': key}
        else:
            item = {'id': village_clinic.id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    '''


@login_required(login_url='/')
def admin_nav(request):
    """
    函数说明：管理员工作界面中的左侧导航栏内容，
             如果是超级管理员、卫生局管理员、财政局管理员，返回全部菜单项目
             如果是卫生院管理员，则返回符合其权限的菜单项目。
             在AdminNav模型中town_clinic_admin字段不为0，则该菜单项是卫生院管理员的权限
    """
    nid = request.POST.get('id', '0')
    nav_items = AdminNav.objects.filter(nid=int(nid))

    json_data = []
    for item in nav_items:
        user = request.user
        if not user.is_superuser and user.userprofile.role.name == u'卫生院管理员' and item.town_clinic_admin == 0:
            pass
        else:
            json_data.append(model_to_dict(item))

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


#################################################################################

##                       管理员工作界面：居民管理（增删改查）

#################################################################################


@login_required(login_url='/')
def residents_page(request):
    """
    函数说明：管理员工作界面中，居民管理的主页面
    """
    return render(request, 'management/residents.html')


@login_required(login_url='/')
def resident_add(request):
    """
    函数说明：在管理员工作界面，手动增加系统中的居民，区别于读取身份证时，自动增加系统中的居民
    """
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


@login_required(login_url='/')
def resident_update(request):
    """
    函数说明：在管理员工作界面，修改系统中居民的信息
    """
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


@login_required(login_url='/')
def resident_del(request):
    """
    函数说明：在管理员工作界面中，删除系统中的居民
    """
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


@login_required(login_url='/')
def resident_query(request):
    """
    函数说明：在管理员工作界面中，查询居民操作
    返回结果：符合查询条件的居民信息以json形式返回
    """
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


@login_required(login_url='/')
def resident_query_list(request):
    """
    函数说明：在管理员工作界面，查询居民操作
    返回结果：在easyui的datagrid中分页显示查询结果，返回json对象数组
    """
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
        if query_crowd == 'old':
            import datetime
            start_date = datetime.date(1800, 1, 1)
            end_date = datetime.date(datetime.date.today().year-64, 1, 1)
            residents = residents.filter(birthday__range=(start_date, end_date))
        if query_crowd == 'child':
            import datetime
            today = datetime.date.today()
            if today.month == 2 and today.day == 29:
                start_date = datetime.date(today.year-7, 2, 28)
            else:
                start_date = datetime.date(today.year-7, today.month, today.day)
            residents = residents.filter(birthday__range=(start_date, today))

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


@login_required(login_url='/')
def resident_add_hypertension(request):
    """
    函数说明：将指定居民加入高血压人群的操作
    """
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.hypertension == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.hypertension = 1
        resident.save()
        success, message = True, resident.name + u'加入了高血压人群'
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


@login_required(login_url='/')
def resident_add_diabetes(request):
    """
    函数说明：将指定居民加入糖尿病人群的操作
    """
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.diabetes == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.diabetes = 1
        resident.save()
        success, message = True, resident.name + u'加入了糖尿病人群'
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


@login_required(login_url='/')
def resident_add_psychiatric(request):
    """
    函数说明：将指定居民加入重性精神疾病人群的操作
    """
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.psychiatric == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.psychiatric = 1
        resident.save()
        success, message = True, resident.name + u'加入了重性精神疾病人群'
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')


@login_required(login_url='/')
def resident_add_pregnant(request):
    """
    函数说明：将指定居民加入孕产妇人群的操作
    """
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    if resident.pregnant == 1:
        success, message = False, u'已经在高血压人群中'
    else:
        resident.pregnant = 1
        resident.save()
        success, message = True, resident.name + u'加入了孕产妇人群'
    return HttpResponse(simplejson.dumps({'success': success, 'message': message}),
                        content_type='text/html; charset=UTF-8')

#################################################################################

##                       管理员工作界面：乡镇卫生院管理（增删改查）

#################################################################################


@login_required(login_url='/')
def town_clinics(request):
    """
    函数说明：管理员工作界面中，乡镇卫生院管理的主页面
    """
    return render(request, 'management/town_clinics.html')


@login_required(login_url='/')
def town_clinic_list(request):
    """
    函数说明：返回所有乡镇卫生院信息
    返回结果：json对象数组
    """
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

#################################################################################

##                       管理员工作界面：村卫生室管理（增删改查）

#################################################################################


@login_required(login_url='/')
def village_clinics_page(request):
    """
    函数说明：管理员工作界面中，村卫生室管理的主页面
    """
    return render(request, 'management/village_clinics.html')


@login_required(login_url='/')
def village_clinic_list(request):
    """
    函数说明：管理员工作界面中，村卫生室查询列表
    返回结果：在easyui的datagrid中，分页显示的json对象数据组
    """
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


@login_required(login_url='/')
def village_clinic_add(request):
    """
    函数说明：管理员工作界面中，增加村卫生室操作
    现存问题：没有检查该村卫生室是否已经存在！
    """
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


@login_required(login_url='/')
def village_clinic_del(request):
    """
    函数说明：管理员工作界面中，删除村卫生室的操作
    现存问题：没有检查该村卫生室是否存在村医，以及该如何处理存在村医的村卫生室删除问题？
    """
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


@login_required(login_url='/')
def village_clinic_update(request):
    """
    函数说明：管理员工作界面中，更新村卫生室信息的操作
    现存问题：没有检查所属乡镇卫生院的名称是否正确，如果不正确应该提示不存在该卫生院
    """
    success = True
    village_clinic_name = ''

    village_clinic_id = request.POST.get('id')
    name = request.POST.get('name')
    address = request.POST.get('address')
    town_clinic_name = request.POST.get('town_clinic')

    try:
        village_clinic = Clinic.in_village.get(id=int(village_clinic_id))
    except Clinic.DoesNotExist:
        success = False
    else:
        village_clinic.name = name
        village_clinic.address = address
        village_clinic.town_clinic = Clinic.in_town.get(name=town_clinic_name)
        village_clinic.save()

    json_data = {'success': success, 'name': village_clinic_name}
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')

    # return JsonResponse(json_data)

#################################################################################

##                       管理员工作界面：提供下拉列表选项的函数

#################################################################################


@login_required(login_url='/')
def town_options(request):
    """
    参数：request的POST传递参数first_text，作为列表第一项的名称
    返回值：返回所有乡镇的列表，列表的第一项id为0，名称由POST所传递的first_text确定
    """
    first_text = request.POST.get('first_text') if 'first_text' in request.POST else u'全部'
    json_data = [{'id': 0, 'name': first_text}]
    json_data += [model_to_dict(town, fields=['id', 'name']) for town in Region.towns.all()]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


@login_required(login_url='/')
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


@login_required(login_url='/')
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


@login_required(login_url='/')
def town_clinic_options(request):
    """
    参数：request.POST中的first_text指定列表第一项的名称
    返回值：返回所有乡镇卫生院列表，第一项id为0，名称由first_text指定
    """
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]
    json_items += [model_to_dict(clinic, fields=['id', 'name']) for clinic in Clinic.in_town.all()]
    return JsonResponse(json_items, safe=False)


@login_required(login_url='/')
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


@login_required(login_url='/')
def get_town_village_clinics(request, town_clinic_id):
    """
    参数：URL链接中town_clinic_id指定乡镇卫生院id
    返回值：town_clinic_id所指定乡镇卫生院所下属的所有村卫生室列表
    """
    first_text = request.POST.get('first_text', '')
    json_data = [{'id': '0', 'name': first_text}]

    if town_clinic_id != '0':
        town_clinic = Clinic.in_town.get(id=int(town_clinic_id))
        clinics = Clinic.in_village.filter(town_clinic=town_clinic)
        json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in clinics]

    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')


@login_required(login_url='/')
def get_town_clinics_edit(request):
    json_data = [{'id': '0', 'name': ''}]
    json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in Clinic.in_town.all()]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
def get_town_village_clinics_edit(request):
    town_clinic_name = request.POST.get('town_clinic_name')
    clinics = Clinic.in_village.filter(town_clinic__name=town_clinic_name)
    json_data = [{'id': '0', 'name': ''}]
    json_data += [model_to_dict(clinic, fields=['id', 'name']) for clinic in clinics]
    return HttpResponse(simplejson.dumps(json_data), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
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


@login_required(login_url='/')
def service_type_options(request):
    first_text = request.POST.get('first_text', '')
    json_items = [{'id': 0, 'name': first_text}]

    service_types = Service.types.all()
    for service_type in service_types:
        item = model_to_dict(service_type, fields=['id', 'name'])
        json_items.append(item)
    # return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    return JsonResponse(json_items, safe=False)


@login_required(login_url='/')
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


#################################################################################

##                       管理员工作界面：系统用户管理操作（增删改查）

#################################################################################


@login_required(login_url='/')
def users_page(request):
    """
    函数说明：管理员操作界面下，用户管理的主页面
    """
    return render(request, 'management/users.html')


@login_required(login_url='/')
def user_query_list(request):
    """
    函数说明：管理员操作界面下，查询用户并生成列表
    返回结果：easyui中datagrid分页现实所需的json对象数组
    """
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


@login_required(login_url='/')
def user_add(request):
    """
    函数说明：添加用户操作
    """
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


@login_required(login_url='/')
def user_del(request):
    """
    函数说明：删除用户操作
    """
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


#################################################################################

##                       管理员工作界面：服务类别管理操作

#################################################################################


@login_required(login_url='/')
def service_types_page(request):
    """
    函数说明：管理员操作界面下，服务类别管理的主页面
    """
    return render(request, 'management/service_types.html')


@login_required(login_url='/')
def service_type_list(request):
    """
    函数说明：管理员操作界面下，服务类别列表操作，一般不会有服务类别的增删改操作
    """
    json_items = []
    for service_type in Service.types.all():
        item = model_to_dict(service_type, fields=['id', 'name', 'real_weight', 'should_weight'])
        item['item_num'] = service_type.service_items.all().count()
        json_items.append(item)

    return HttpResponse(simplejson.dumps({'total': len(json_items), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': len(json_items), 'rows': json_items})


@login_required(login_url='/')
def service_items_page(request):
    """
    函数说明：管理员操作界面下，服务项目管理的主页面
    """
    return render(request, 'management/service_items.html')


#################################################################################

##                       管理员工作界面：服务项目管理操作

#################################################################################


@login_required(login_url='/')
def service_item_list(request):
    """
    函数说明：管理员操作界面下，服务项目查询列表操作
    返回结果：easyui中datagrid分页显示，所需的json对象数组
    """
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


@login_required(login_url='/')
def service_item_add(request):
    """
    函数说明：增加服务项目操作，此操作不能开放给管理员用户！
    """
    service_type_name = request.POST.get('service_type', '')
    service_item_name = request.POST.get('name')
    service_price = request.POST.get('price', '')
    service_unit = request.POST.get('unit', '')

    service_type = Service.types.get(name=service_type_name)
    service_items = Service.items.filter(service_type=service_type)
    try:
        service_items.get(name=service_item_name)
    except Service.DoesNotExist:
        service_item = Service(name=service_item_name, price=service_price,
                               unit=service_unit, level=Service.SERVICE_ITEM,
                               service_type=service_type, create_by=request.user)
        service_item.save()
        success, msg = 'true', u'服务项目创建完成'
    else:
        success, msg = 'false', u'服务项目已经存在'
    return HttpResponse(simplejson.dumps({'success': success, 'message': msg}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'success': success, 'message': msg})


@login_required(login_url='/')
def service_item_update(request):
    """
    函数说明：更新服务项目信息的操作，包括对服务项目的名称、价格和单位的更新
    """
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


@login_required(login_url='/')
def service_item_del(request):
    """
    函数说明：删除服务项目的操作，此操作不应该开放给管理员用户
    """
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


#################################################################################

##                       管理员工作界面：服务记录管理操作

#################################################################################

@login_required(login_url='/')
def records_page(request):
    """
    函数说明：服务记录列表的主页面
    """
    return render(request, 'management/records_page.html')


@login_required(login_url='/')
def record_list(request):
    """
    函数说明：在easyui的datagrid中显示服务记录列表
    """
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


#################################################################################

##                       管理员工作界面：服务计费管理操作

#################################################################################


@login_required(login_url='/')
def payment_page(request):
    """
    函数说明：服务计费的主页面
    """
    return render(request, 'management/payment_page.html')


@login_required(login_url='/')
def payment_list(request):
    """
    函数说明：在easyui的datagrid中列出各项服务项目的计费情况
    """
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
        service_items = service_items.filter(id=service_item.id)
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
                   'workload': total_workload, 'payment': format(total_payment, '0.2f')}]

    for service_item in service_items[first: first + page_size]:
        json_items.append({
            'service_type': service_item.service_type.name,
            'service_item': service_item.name,
            'workload': str(workload[service_item]) + service_item.unit,
            'payment': format(workload[service_item] * service_item.price, '0.2f')})

    return HttpResponse(simplejson.dumps({'total': service_items.count(), 'rows': json_items}),
                        content_type='text/html; charset=UTF-8')
    # return JsonResponse({'total': service_items.count(), 'rows': json_items})


#################################################################################

##                       管理员工作界面：用户角色管理操作

#################################################################################


@login_required(login_url='/')
def roles_page(request):
    """
    函数说明：角色管理的主页面
    """
    return render(request, 'management/roles.html')


@login_required(login_url='/')
def role_list(request):
    """
    函数说明：列表当前所有角色操作
    """
    json_items = []
    for group in Group.objects.all():
        item = model_to_dict(group, fields=['id', 'name'])
        if group.groupprofile:
            item['is_staff'] = group.groupprofile.is_staff
        item['user_num'] = group.users.all().count()
        json_items.append(item)

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


@login_required(login_url='/')
def get_role_authorize(request):
    """
    函数说明：获取某个指定角色的授权
    """
    role_id = int(request.POST.get('role_id'))
    role = Group.objects.get(id=role_id)

    json_items = []
    for service in role.groupprofile.default_services.all():
        if service.level == Service.SERVICE_ITEM:
            json_items.append(str(service.id))

    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')
    # return JsonResponse(json_items, safe=False)


@login_required(login_url='/')
def role_authorize(request):
    """
    函数说明：对某个指定角色进行授权
    """
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


@login_required(login_url='/')
def role_add(request):
    """
    函数说明：添加角色操作，该功能不开放给管理员用户
    """
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
    """
    函数说明：删除某个指定角色，该功能不开放给管理员用户
    """
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


#################################################################################

##                       管理员工作界面：已发送短信列表操作

#################################################################################


@login_required(login_url='/')
def sms_sent(request):
    """
    函数说明：已发送短信列表主页面
    """
    return render(request, 'management/sms_sent.html')


@login_required(login_url='/')
def sms_sent_list(request):
    """
    函数说明：按照条件查询已发送短信并列表操作
    """
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

#################################################################################

##                       管理员工作界面：已发送短信列表操作

#################################################################################


@login_required(login_url='/')
def sms_setup_page(request):
    """
    函数说明：短信设置主页面
    """
    return render(request, 'management/sms_setup.html')


@login_required(login_url='/')
def sms_setup_list(request):
    """
    函数说明：按照条件查询短信设置并列表操作
    """
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
        sms_setups = sms_setups.filter(service_item=service_item)

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


@login_required(login_url='/')
def sms_setup_add(request):
    """
    函数说明：添加短信设置操作
    """
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


@login_required(login_url='/')
def sms_setup_update(request):
    """
    函数说明：更新短信设置操作
    """
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


@login_required(login_url='/')
def sms_setup_del(request):
    """
    函数说明：删除短信设置操作
    """
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


import json


#################################################################################

##                       管理员工作界面：首页的统计图（工作量和费用统计图）

#################################################################################


@login_required(login_url='/')
def graphs(request):
    """
    函数说明：统计图的主页面
    """
    return render(request, 'management/graphs.html')


@login_required(login_url='/')
def graph_workload(request):
    """
    函数说明：工作量统计图，如果是全局管理员，查看到11个乡镇卫生院的工作量统计图，
            如果是卫生院管理员，查看到该卫生院下属所有村卫生室的工作量统计图。
    """
    user = request.user
    if not user.is_superuser and user.userprofile.role.name == u'卫生院管理员':   # 卫生院管理员
        global_admin = False
        clinics = user.userprofile.clinic.village_clinics.all()
    else:                                                                       # 全局管理员
        global_admin = True
        clinics = Clinic.in_town.all()

    workload = {service_type.name: {clinic.name: 0 for clinic in clinics}
                for service_type in Service.types.all()}

    if global_admin:
        for clinic in clinics:
            for service_type in Service.types.all():
                workload[service_type.name][clinic.name] = WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                    service_item__level=Service.SERVICE_ITEM, service_item__service_type=service_type,
                    provider__userprofile__clinic__town_clinic=clinic).count()
    else:
        for clinic in clinics:
            for service_type in Service.types.all():
                workload[service_type.name][clinic.name] = WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, service_item__level=Service.SERVICE_ITEM,
                    service_item__service_type=service_type, provider__userprofile__clinic=clinic).count()

    clinics = workload.values()[0].keys()
    series = [{"name": key, "data": value.values()} for key, value in workload.items()]
    result = {"clinics": clinics, "series": series}

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")


@login_required(login_url='/')
def graph_payment(request):
    """
    函数说明：支付费用统计图
    """
    user = request.user
    if not user.is_superuser and user.userprofile.role.name == u'卫生院管理员':
        global_admin = False
        clinics = user.userprofile.clinic.village_clinics.all()
    else:
        global_admin = True
        clinics = Clinic.in_town.all()

    payment = dict()

    if global_admin:
        for clinic in clinics:
            payment[clinic.name] = 0
            for service_item in Service.items.all():
                payment[clinic.name] += WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, service_item=service_item,
                    provider__userprofile__clinic__town_clinic=clinic).count() * service_item.price
    else:
        for clinic in clinics:
            payment[clinic.name] = 0
            for service_item in Service.items.all():
                payment[clinic.name] += WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, service_item=service_item,
                    provider__userprofile__clinic=clinic).count() * service_item.price

    total_payment = sum(payment.values()) * 1.0
    percent = [{'name': key, 'y': value/total_payment} for key, value in payment.items()]

    return HttpResponse(simplejson.dumps(percent), content_type='text/html; charset=UTF-8')
    # return JsonResponse(percent, safe=False)

#################################################################################

##                       管理员工作界面：工作量统计查询操作

#################################################################################


@login_required(login_url='/')
def workload_stat_page(request):
    """
    函数说明：工作量统计主页面
    """
    return render(request, 'management/workload_stat_page.html')


@login_required(login_url='/')
def workload_town_clinics_page(request):
    """
    函数说明：乡镇卫生院工作量统计的主页面
    """
    return render(request, 'management/workload_town_clinics_page.html')


from services.utils import new_year_time
import collections


@login_required(login_url='/')
def workload_town_clinics_datagrid(request):
    """
    函数说明：计算各个卫生院各个服务类别的工作量及合计，并在easyui的datagrid中列表显示
    """
    workload = collections.OrderedDict()
    for town_clinic in Clinic.in_town.all():
        workload[town_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = {service_type.alias: 0 for service_type in Service.types.all()}

    sql_count = 0
    t_begin = datetime.now()

    for town_clinic in Clinic.in_town.all():
        for service_type in Service.types.all():

            t0 = datetime.now()

            workload[town_clinic.name][service_type.alias] = WorkRecord.objects.filter(
                status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                service_item__level=Service.SERVICE_ITEM, service_item__service_type=service_type,
                provider__userprofile__clinic__town_clinic=town_clinic).count()

            t1 = datetime.now()
            sql_count += 1
            debug.info("sql_count: {0}; interval: {1}".format(sql_count, t1 - t0))

            workload['合计'][service_type.alias] += workload[town_clinic.name][service_type.alias]

    t_end = datetime.now()
    debug.info("total time: {}".format(t_end - t_begin))

    json_data = []
    for key, value in workload.items():
        try:
            clinic = Clinic.in_town.get(name=key)
        except Clinic.DoesNotExist:
            clinic_id = 0
        else:
            clinic_id = clinic.id
        item = {'id': clinic_id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)

    return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
def workload_village_clinics_page(request, town_clinic_id):
    """
    函数说明：指定乡镇卫生院下属各个村卫生室的工作量统计的主页面
    """
    return render(request, 'management/workload_village_clinics_page.html',
                  {'town_clinic_id': town_clinic_id})


@login_required(login_url='/')
def workload_village_clinics_datagrid(request, town_clinic_id):
    """
    函数说明：计算指定卫生院各个服务类别的工作量及合计，并在datagrid中列表显示
    参数：town_clinic_id，指定卫生院的id
    返回：指定卫生院下属卫生室的各服务类别的工作量及合计
    """
    town_clinic = Clinic.in_town.get(id=int(town_clinic_id))

    workload = collections.OrderedDict()
    for village_clinic in town_clinic.village_clinics.all():
        workload[village_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = {service_type.alias: 0 for service_type in Service.types.all()}

    for village_clinic in town_clinic.village_clinics.all():
        for service_type in Service.types.all():
            workload[village_clinic.name][service_type.alias] = WorkRecord.objects.filter(
                status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                service_item__level=Service.SERVICE_ITEM, service_item__service_type=service_type,
                provider__userprofile__clinic=village_clinic).count()
            workload['合计'][service_type.alias] += workload[village_clinic.name][service_type.alias]

    json_data = []
    for key, value in workload.items():
        try:
            village_clinic = Clinic.objects.get(town_clinic=town_clinic, name=key)
        except Clinic.DoesNotExist:
            item = {'id': 0, 'clinic': key}
        else:
            item = {'id': village_clinic.id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
def workload_doctors_page(request, clinic_id):
    """
    函数说明：医生工作量统计的主页面
    """
    return render(request, 'management/workload_doctors_page.html', {'clinic_id': clinic_id})


@login_required(login_url='/')
def workload_doctors_datagrid(request, clinic_id):
    """
    函数说明：计算指定卫生机构中各位医生的工作量（分类和合计），并在easyui的datagrid中列表显示
    参数：clinic_id，指定卫生机构的id
    返回：指定卫生机构中各位医生的各服务类别的工作量及合计
    """
    clinic = Clinic.objects.get(id=int(clinic_id))

    workload = collections.OrderedDict()
    for doctor in clinic.users.all():
        workload[doctor.user.username] = {service_type.alias: 0 for service_type in Service.types.all()}

    workload['合计'] = {service_type.alias: 0 for service_type in Service.types.all()}

    for doctor in clinic.users.all():
        for service_type in Service.types.all():
            workload[doctor.user.username][service_type.alias] = WorkRecord.objects.filter(
                status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                service_item__level=Service.SERVICE_ITEM, service_item__service_type=service_type,
                provider=doctor.user).count()
            workload['合计'][service_type.alias] += workload[doctor.user.username][service_type.alias]

    json_data = []
    for key, value in workload.items():
        try:
            doctor = User.objects.get(username=key)
        except User.DoesNotExist:
            doctor_id = 0
        else:
            doctor_id = doctor.id
        item = {'id': doctor_id, 'name': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
def workload_list_page(request, provider_id):
    """
    函数说明：某指定医生工作记录列表的主页面
    """
    return render(request, 'management/workload_list_page.html', {'provider_id': provider_id})


@login_required(login_url='/')
def workload_list_datagrid(request, provider_id):
    """
    函数说明：某指定医生工作记录，在easyui的datagrid中列表显示
    """
    provider = User.objects.get(id=int(provider_id))
    records = WorkRecord.objects.filter(provider=provider, status=WorkRecord.FINISHED).order_by('-submit_time')

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
        elif record.status == WorkRecord.SUSPEND_SUBMIT:
            item['status'] = u'暂存/完成'

        json_items.append(item)

    return JsonResponse(json_items, safe=False)


@login_required(login_url='/')
def resident_records_page(request, resident_id):
    """
    函数说明：某指定居民的服务记录列表的主页面
    """
    return render(request, 'management/resident_records_datagrid.html',
                  {'resident_id': resident_id})


@login_required(login_url='/')
def resident_records_datagrid(request, resident_id):
    """
    函数说明：某指定居民的服务记录，并在easyui的datagrid中列表显示
    """
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

#################################################################################

##                       管理员工作界面：支付费用统计查询操作

#################################################################################


@login_required(login_url='/')
def payment_stat_page(request):
    """
    函数说明：支付费用统计的主页面
    """
    return render(request, 'management/payment_stat_page.html')


@login_required(login_url='/')
def payment_town_clinics_page(request):
    """
    函数说明：乡镇卫生院支付费用统计的主页面
    """
    return render(request, 'management/payment_town_clinics_page.html')

import Queue
from multiprocessing import Process, cpu_count


def worker_payment_1(queue, payment):
    queue_full = True
    while queue_full:
        try:
            town_clinic_name, service_type_alias = queue.get()
            debug.info(town_clinic_name, service_type_alias)
            town_clinic = Clinic.objects.get(name=town_clinic_name)
            service_type = Service.objects.get(alias=service_type_alias)
            for service_item in service_type.service_items.filter(level=Service.SERVICE_ITEM):
                payment[town_clinic_name][service_type_alias] += WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                    clinic__town_clinic=town_clinic,
                    service_item=service_item).count() * service_item.price
        except Queue.Empty:
            queue_full = False


@login_required(login_url='/')
def payment_town_clinics_datagrid(request):
    """
    函数说明：计算各个卫生院各个服务类别的工作量及合计，并在easyui的datagrid中列表显示
    """
    payment = collections.OrderedDict()

    for town_clinic in Clinic.in_town.all():
        payment[town_clinic.name] = {service_type.alias: 0 for service_type in Service.types.all()}

    payment['合计'] = {service_type.alias: 0 for service_type in Service.types.all()}

    t_begin = datetime.now()

    q = Queue.Queue()
    jobs = []
    cpu_num = cpu_count()

    debug.info('cpu number: {}'.format(cpu_num))

    for i in range(cpu_num):
        p = Process(target=worker_payment_1, args=(q, payment))
        jobs.append(p)
        p.start()

    for town_clinic in Clinic.in_town.all():
        for service_type in Service.types.all():
            q.put((town_clinic.name, service_type.alias))

    for j in jobs:
        j.join()

    for town_clinic in Clinic.in_town.all():
        for service_type in Service.types.all():
            payment['合计'][service_type.alias] += payment[town_clinic.name][service_type.alias]

    '''
    for town_clinic in Clinic.in_town.all():
        for service_type in Service.types.all():
            for service_item in service_type.service_items.filter(level=Service.SERVICE_ITEM):
                payment[town_clinic.name][service_type.alias] += WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                    clinic__town_clinic=town_clinic,
                    service_item=service_item).count() * service_item.price
            payment['合计'][service_type.alias] += payment[town_clinic.name][service_type.alias]
    '''

    t_end = datetime.now()
    debug.info("total time: {}".format(t_end - t_begin))

    json_data = []
    for key, value in payment.items():
        try:
            clinic = Clinic.in_town.get(name=key)
        except Clinic.DoesNotExist:
            clinic_id = 0
        else:
            clinic_id = clinic.id
        item = {'id': clinic_id, 'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)


@login_required(login_url='/')
def payment_village_clinics_page(request, town_clinic_id):
    """
    函数说明：某指定卫生院下属村卫生室的支付费用的主页面
    """
    return render(request, 'management/payment_village_clinics_page.html',
                  {'town_clinic_id': town_clinic_id})


@login_required(login_url='/')
def payment_village_clinics_datagrid(request, town_clinic_id):
    """
    函数说明：某指定卫生院下属村卫生室的支付费用，在easyui的datagrid中列表显示
    """
    payment = collections.OrderedDict()
    town_clinic = Clinic.in_town.get(id=int(town_clinic_id))

    clinics = town_clinic.village_clinics.all()
    services = Service.types.all()

    for clinic in clinics:
        payment[clinic.name] = {service_type.alias: 0 for service_type in services}

    payment['合计'] = {service_type.alias: 0 for service_type in services}

    # t0 = datetime.now()
    '''
    for record in WorkRecord.objects.filter(status=WorkRecord.FINISHED, submit_time__gte=new_year_time()):
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
    '''
    for clinic in clinics:
        for service_type in services:
            for service_item in service_type.service_items.filter(level=Service.SERVICE_ITEM):
                payment[clinic.name][service_type.alias] += WorkRecord.objects.filter(
                    status=WorkRecord.FINISHED, submit_time__gte=new_year_time(),
                    provider__userprofile__clinic=clinic,
                    service_item=service_item).count() * service_item.price
            payment['合计'][service_type.alias] += payment[clinic.name][service_type.alias]

    # t1 = datetime.now()
    # debug.info("******************************************************{}".format(t1 - t0))

    json_data = []
    for key, value in payment.items():
        item = {'clinic': key}
        item.update(value)
        total = {'total': sum(value.values())}
        item.update(total)
        json_data.append(item)
    return JsonResponse(json_data, safe=False)

#################################################################################

##                       管理员工作界面：修改服务结果申请的管理操作

#################################################################################


@login_required(login_url='/')
def modify_apply_page(request):
    """
    函数说明：修改服务结果申请管理的主页面
    """
    return render(request, 'management/modify_apply_page.html')

from .models import ModifyApply
from datetime import timedelta


@login_required(login_url='/')
def modify_apply_list(request):
    """
    函数说明：修改服务结果申请的列表
    """
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


@login_required(login_url='/')
def modify_apply_opinion(request):
    """
    函数说明：修改服务结果申请的审批意见操作
    """
    opinion = request.POST.get('opinion')
    application = ModifyApply.objects.get(id=int(request.POST.get('id')))

    if request.user.is_superuser:
        if opinion == 'agree':
            application.health_opinion = ModifyApply.AGREE
            application.finance_opinion = ModifyApply.AGREE
        elif opinion == 'disagree':
            application.health_opinion = ModifyApply.DISAGREE
            application.finance_opinion = ModifyApply.DISAGREE
        application.health_opinion_time = timezone.now()
        application.finance_opinion_time = timezone.now()
    elif request.user.userprofile.role.name == u'卫生局管理员':
        if opinion == 'agree':
            application.health_opinion = ModifyApply.AGREE
        elif opinion == 'disagree':
            application.health_opinion = ModifyApply.DISAGREE
        application.health_opinion_time = timezone.now()
    elif request.user.userprofile.role.name == u'财政局管理员':
        if opinion == 'agree':
            application.finance_opinion = ModifyApply.AGREE
        elif opinion == 'disagree':
            application.finance_opinion = ModifyApply.DISAGREE
        application.finance_opinion_time = timezone.now()

    if application.health_opinion == ModifyApply.DISAGREE \
            or application.finance_opinion == ModifyApply.DISAGREE:
        application.apply_status = ModifyApply.REFUSED

    application.save()
    return JsonResponse({'success': True})