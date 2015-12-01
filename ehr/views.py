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
from services.utils import get_resident

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
        item['speciality'] = ''
        if each.diabetes:
            item['speciality'] = '孕'
        if each.hypertension:
            if item['speciality']:
                item['speciality'] += ' /高血压'
            else:
                item['speciality'] += '高血压'
        if each.diabetes:
            if item['speciality']:
                item['speciality'] += ' /糖尿病'
            else:
                item['speciality'] += '糖尿病'
        if each.psychiatric:
            if item['speciality']:
                item['speciality'] += ' /精神病'
            else:
                item['speciality'] += '精神病'
        if each.is_old_man:
            if item['speciality']:
                item['speciality'] += ' /老年人'
            else:
                item['speciality'] += '老年人'
        if each.is_0_6_child:
            if item['speciality']:
                item['speciality'] += ' /0-6岁儿童'
            else:
                item['speciality'] += '0-6岁儿童'
        json_items.append(item)
    return HttpResponse(simplejson.dumps(json_items), content_type='text/html; charset=UTF-8')


def child_add(request):
    child = Resident()
    child.name = request.POST.get('name')
    child.gender = int(request.POST.get('gender'))
    child.nation = request.POST.get('nation')

    birthday = request.POST.get('birthday')
    child.birthday = datetime.strptime(birthday, '%Y-%m-%d')
    if request.user.userprofile.clinic.region.is_town:
        town = request.user.userprofile.clinic.region
        village = None
    else:
        village = request.user.userprofile.clinic.region
        town = village.town
    child.town = town
    child.village = village

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
    resident_id = request.POST.get('resident_id')
    if resident_id:
        resident_id = int(resident_id)
        resident = Resident.objects.get(id=resident_id)
        if resident.town is None:
            if request.user.userprofile.clinic.region.is_town:
                town = request.user.userprofile.clinic.region
                village = None
            else:
                village = request.user.userprofile.clinic.region
                town = village.town
            resident.town = town
            resident.village = village
            resident.save()

    else:  # 创建一个新的居民对象
        from services.utils import gender_map

        gender = gender_map().index(request.POST.get('gender'))
        nation = request.POST.get('nation')
        if nation == u'少数民族' and request.POST.get('nation_extra'):
            nation = request.POST.get('nation_extra')
        if request.user.userprofile.clinic.region.is_town:
            town = request.user.userprofile.clinic.region
            village = None
        else:
            village = request.user.userprofile.clinic.region
            town = village.town

        resident = Resident(name=request.POST.get('resident_name'),
                            gender=gender, nation=nation,
                            town=town, village=village,
                            birthday=request.POST.get('birthday'),
                            address=request.POST.get('address'),
                            identity=request.POST.get('identity'),
                            mobile=request.POST.get('phone'),
                            create_by=request.user)
        resident.save()

    form = PersonalInfoForm(request.POST)
    if form.is_valid():
        personal_info = form.save()
        resident.personal_info_table = personal_info
        record = WorkRecord(resident=resident, provider=request.user,
                            service_item_alias='personal_info_table',
                            item_id=personal_info.id)
        record.save()
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
            ehr_village_no = int(request.POST.get('ehr_village_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
            ehr_unique_no = int(request.POST.get('ehr_unique_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
            town_no = request.user.userprofile.clinic.town_clinic.region.id
            resident.ehr_no = town_no + '%03d' % ehr_village_no + '%05d' % ehr_unique_no
        resident.save()
        success = True
    else:
        debug.info(form.errors.as_data())
        success = False
    return json_result({'success': success, 'resident_id': resident.id})


def personal_info_review(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    personal_info = resident.personal_info_table
    if personal_info:
        form = PersonalInfoForm(instance=personal_info)
        return render(request, 'ehr/personal_info_review_content.html',
                      {'form': form, 'resident': resident})
    else:
        initial = {'identity': resident.identity, 'birthday': resident.birthday}
        form = PersonalInfoForm(initial=initial)
        return render(request, 'ehr/personal_info_form_content.html',
                      {'form': form, 'resident': resident})


def personal_info_review_tab(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    personal_info = resident.personal_info_table
    if personal_info:
        form = PersonalInfoForm(instance=personal_info)
        return render(request, 'ehr/personal_info_review_tab.html',
                      {'form': form, 'resident': resident})


from .forms import BodyExamForm
from .models import BodyExam, PersonalInfo


def body_exam_table(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    record = WorkRecord.objects.filter(resident=resident,
                                       service_item_alias='body_exam_table').first()
    if record:
        table = BodyExam.objects.get(id=record.item_id)
        form = BodyExamForm(instance=table)
    else:
        form = BodyExamForm()
    return render(request, 'ehr/body_exam_form.html', {'form': form, 'resident': resident})


def body_exam_submit(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    form = BodyExamForm(request.POST)
    success = False
    if form.is_valid():
        result = form.save()
        # 建档体检因为不是付费项目，这里没有把service_item记录在WorkRecord中
        # 在后续的筛选中只需要使用service_item_alias或者model_name
        record = WorkRecord(resident=resident, provider=request.user, model_name='BodyExam',
                            service_item_alias='body_exam_table', item_id=result.id)
        record.save()
        success = True
    else:
        debug.info(form.errors.as_data())

    return json_result({'success': success})


def record_list(request):
    resident_id = request.POST.get('resident_id')
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


def record_detail_review(request):
    record_id = int(request.POST.get('record_id'))
    record = WorkRecord.objects.get(id=record_id)
    resident = record.resident

    service_item = record.service_item
    if service_item.service_group:
        item_alias = record.service_item.service_group.alias
    else:
        item_alias = record.service_item.alias

    if item_alias == 'body_exam_table' or item_alias == 'physical_examination':
        model_obj = apps.get_model(app_label='ehr', model_name=record.model_name)
    else:
        model_obj = apps.get_model(app_label=record.app_label, model_name=record.model_name)

    form = model_obj.objects.get(id=record.item_id)
    if item_alias == 'body_exam_table' \
            or item_alias == 'physical_examination':
        template = 'ehr/body_exam_review.html'
    elif item_alias == 'constitution_identification':
        template = 'tcm/old_identify_review.html'
    elif record.app_label == 'vaccine' and record.service_item.alias != 'vaccine_card':
        template = 'vaccine/vaccine_review.html'
    elif record.app_label == 'psychiatric':
        template = 'psychiatric/psy_visit_review_content.html'
    elif record.app_label == 'education':
        template = 'education/activity_table_review.html'
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


def ehr_setup(request):
    return render(request, 'ehr/ehr_setup.html')


def ehr_resident_list(request):
    return render(request, 'ehr/ehr_resident_list.html')


from services.utils import json_result


def ehr_resident_query(request):
    """
    函数说明：在卫生院医生、村医工作界面，查询列表辖区内所有建档居民
    返回结果：在easyui的datagrid中分页显示查询结果，返回json对象数组
    """
    page = int(request.POST.get('page'))
    page_size = int(request.POST.get('rows'))
    first = page_size * (page - 1)

    user = request.user
    region = user.userprofile.clinic.region

    if region is None:
        return json_result({'total': 0, 'rows': []})

    residents = Resident.objects.filter(town=region.town) if region.is_town \
        else Resident.objects.filter(town=region.town, village=region)

    ehr_no = request.POST.get('ehr_no', '').strip()
    name = request.POST.get('name', '').strip()
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    identity = request.POST.get('identity', '').strip()
    crowd = request.POST.get('crowd', '').strip()

    if ehr_no:
        residents = residents.filter(ehr_no=ehr_no)
    if name:
        residents = residents.filter(name=name)
    if gender:
        gender = int(gender)
        if gender == Resident.FEMALE:
            residents = residents.filter(gender=gender)
        if gender == Resident.MALE:
            residents = residents.filter(gender=gender)
    if age:
        age = int(age)
        import datetime

        today = datetime.date.today()
        birth_date = datetime.date(today.year - age, today.month, today.day)
        residents = residents.filter(birthday__lte=birth_date, birthday__year=today.year - age)
    if identity:
        residents = residents.filter(identity=identity)

    if crowd and crowd != 'all':
        if crowd == 'hypertension':
            residents = residents.filter(hypertension=1)
        if crowd == 'diabetes':
            residents = residents.filter(diabetes=1)
        if crowd == 'psychiatric':
            residents = residents.filter(psychiatric=1)
        if crowd == 'pregnant':
            residents = residents.filter(pregnant=1)
        if crowd == 'old':
            import datetime

            today = datetime.date.today()
            end_date = datetime.date(today.year - 64, 1, 1)
            residents = residents.filter(birthday__lt=end_date)
        if crowd == 'child':
            import datetime

            today = datetime.date.today()
            if today.month == 2 and today.day == 29:
                start_date = datetime.date(today.year - 7, 2, 28)
            else:
                start_date = datetime.date(today.year - 7, today.month, today.day)
            residents = residents.filter(birthday__gt=start_date)

    json_items = []

    for resident in residents[first: first + page_size]:
        item = model_to_dict(resident, exclude=['town', 'village', 'birthday',
                                                'create_time', 'create_by',
                                                'update_time', 'update_by'])
        item['birthday'] = resident.birthday.strftime('%Y-%m-%d')
        item['age'] = resident.age
        item['town'] = resident.town.name if resident.town else ''
        item['village'] = resident.village.name if resident.village else ''
        item['personal_info'] = u'是' if resident.personal_info_table is not None else u'否'
        item['body_exam'] = u'是' \
            if WorkRecord.objects.filter(resident=resident,
                                         service_item_alias='body_exam_table').count() else u'否'
        json_items.append(item)

    return json_result({'total': residents.count(), 'rows': json_items})


def setup_personal_info_page(request):
    return render(request, 'ehr/setup_personal_info_page.html')


def personal_info_setup(request):
    form = PersonalInfoForm()
    return render(request, 'ehr/personal_info_form_content.html', {'form': form})


def setup_body_exam_page(request):
    return render(request, 'ehr/setup_body_exam_page.html')


def body_exam_setup(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    form = BodyExamForm()
    return render(request, 'ehr/body_exam_form.html', {'form': form, 'resident': resident})


def personal_info_edit_tab(request):
    return render(request, 'ehr/personal_info_edit_tab.html')


def personal_info_edit(request):
    resident_id = int(request.POST.get('resident_id'))
    resident = Resident.objects.get(id=resident_id)
    form = PersonalInfoForm(instance=resident.personal_info_table)
    return render(request, 'ehr/personal_info_form_content.html',
                  {'form': form,
                   'resident': resident,
                   'ehr_village_no': int(resident.ehr_no[9:12]),
                   'ehr_unique_no': int(resident.ehr_no[12:17])
                  })


def personal_info_edit_submit(request):
    resident_id = request.POST.get('resident_id')
    if resident_id:
        resident_id = int(resident_id)
        resident = Resident.objects.get(id=resident_id)
        from services.utils import gender_map

        gender = gender_map().index(request.POST.get('gender'))
        nation = request.POST.get('nation')
        if nation == u'少数民族' and request.POST.get('nation_extra'):
            nation = request.POST.get('nation_extra')
        resident.name = request.POST.get('resident_name')
        resident.gender = gender
        resident.nation = nation
        resident.birthday = request.POST.get('birthday')
        resident.address = request.POST.get('address')
        resident.identity = request.POST.get('identity')
        resident.mobile = request.POST.get('phone')
        resident.update_by = request.user

        ehr_village_no = int(request.POST.get('ehr_village_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
        ehr_unique_no = int(request.POST.get('ehr_unique_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
        town_no = request.user.userprofile.clinic.town_clinic.region.id
        resident.ehr_no = town_no + '%03d' % ehr_village_no + '%05d' % ehr_unique_no
        resident.save()

        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            debug.info(resident.personal_info_table.id)
            debug.info(form.is_valid())
            debug.info(form.cleaned_data)
            submit_data = {field: value for field, value in form.cleaned_data.items() if value}
            result, created = PersonalInfo.objects.update_or_create(id=resident.personal_info_table.id,
                                                                    defaults=submit_data)
            resident.save()
            record = WorkRecord.objects.get(resident=resident, service_item_alias='personal_info_table')
            record.update_by = request.user
            record.save()
            success = True
        else:
            debug.info(form.errors.as_data())
            success = False
    else:
        success = False

    return json_result({'success': success, 'resident_id': resident_id})


def personal_info_submit(request):
    resident_id = request.POST.get('resident_id')
    if resident_id:
        resident_id = int(resident_id)
        resident = Resident.objects.get(id=resident_id)
    else:  # 创建一个新的居民对象
        from services.utils import gender_map

        gender = gender_map().index(request.POST.get('gender'))
        nation = request.POST.get('nation')
        if nation == u'少数民族' and request.POST.get('nation_extra'):
            nation = request.POST.get('nation_extra')
        if request.user.userprofile.clinic.region.is_town:
            town = request.user.userprofile.clinic.region
            village = None
        else:
            village = request.user.userprofile.clinic.region
            town = village.town
        resident = Resident(name=request.POST.get('resident_name'),
                            gender=gender, nation=nation,
                            town=town, village=village,
                            birthday=request.POST.get('birthday'),
                            address=request.POST.get('address'),
                            identity=request.POST.get('identity'),
                            mobile=request.POST.get('phone'),
                            create_by=request.user)
        resident.save()

    form = PersonalInfoForm(request.POST)
    if form.is_valid():
        personal_info = form.save()
        resident.personal_info_table = personal_info
        record = WorkRecord(resident=resident, provider=request.user,
                            service_item_alias='personal_info_table',
                            item_id=personal_info.id)
        record.save()
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
            ehr_village_no = int(request.POST.get('ehr_village_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
            ehr_unique_no = int(request.POST.get('ehr_unique_no'))  # 由于是必填项，而且是数字类型，所以在此不必检查类型
            town_no = request.user.userprofile.clinic.town_clinic.region.id
            resident.ehr_no = town_no + '%03d' % ehr_village_no + '%05d' % ehr_unique_no
            resident.save()

        if resident.identity is None and personal_info.identity is not None:
            resident.identity = personal_info.identity
            resident.save()
        elif resident.identity is not None and personal_info.identity is not None:
            if resident.identity != personal_info.identity:
                resident.identity = personal_info.identity
                resident.save()

        if resident.mobile is None and personal_info.phone is not None:
            resident.mobile = personal_info.phone
            resident.save()
        elif resident.mobile is not None and personal_info.phone is not None:
            if resident.mobile != personal_info.phone:
                resident.mobile = personal_info.phone
                resident.save()

        success = True
    else:
        success = False
    return json_result({'success': success, 'resident_id': resident.id})
