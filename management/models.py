# -*- encoding: utf-8 -*-
from datetime import date

from django.db import models
from django.contrib.auth.models import User, Group
from ehr.models import PersonalInfo
from psychiatric.models import PsychiatricInfo
from vaccine.models import VaccineCard


GENDER_CHOICES = ((0, '女'), (1, '男'), (2, '未知'),)
EVALUATION_CHOICES = ((0, '未评价'), (1, '不满意'), (2, '一般'), (3, '满意'), )
RECORD_STATUS_CHOICES = ((1, '已开始'), (2, '暂停'), (3, '完成'), (4, '已支付'), (5, '取消'),)
NATION_CHOICES = ((1, '汉族'), (2, '蒙古族'), (3, '回族'), (4, '藏族'), (5, '维吾尔族'),
                  (6, '苗族'), (7, '彝族'), (8, '壮族'), (9, '布依族'), (10, '朝鲜族'),
                  (11, '满族'), (12, '侗族'), (13, '瑶族'), (14, '白族'), (15, '土家族'),
                  (16, '哈尼族'), (17, '哈萨克族'), (18, '傣族'), (19, '黎族'), (20, '僳僳族'),
                  (21, '佤族'), (22, '畲族'), (23, '高山族'), (24, '拉祜族'), (25, '水族'),
                  (26, '东乡族'), (27, '纳西族'), (28, '景颇族'), (29, '柯尔克孜族'), (30, '土族'),
                  (31, '达斡尔族'), (32, '仫佬族'), (33, '羌族'), (34, '布朗族'), (35, '撒拉族'),
                  (36, '毛难族'), (37, '仡佬族'), (38, '锡伯族'), (39, '阿昌族'), (40, '普米族'),
                  (41, '塔吉克族'), (42, '怒族'), (43, '乌孜别克族'), (44, '俄罗斯族'), (45, '鄂温克族'),
                  (46, '崩龙族'), (47, '保安族'), (48, '裕固族'), (49, '京族'), (50, '塔塔尔族'),
                  (51, '独龙族'), (52, '鄂伦春族'), (53, '赫哲族'), (54, '门巴族'), (55, '珞巴族'),
                  (56, '基诺族'),)


class ChangeLogModel(models.Model):
    """
    An abstract base model that provides self-change logging fields
    such as create_by, create_time, update_by and update_time and the
    current enabled status: False for disabled and True for enabled
    """
    DISABLED, ENABLED = 0, 1
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=True)
    enabled = models.IntegerField(default=1)

    class Meta:
        abstract = True


class TownManager(models.Manager):
    def get_queryset(self):
        return super(TownManager, self).get_queryset().filter(level=Region.TOWN)


class VillageManager(models.Manager):
    def get_queryset(self):
        return super(VillageManager, self).get_queryset().filter(level=Region.VILLAGE)


class Region(ChangeLogModel):
    """
    A model describes the locations in Sanhe city including towns and
    villages. The administration hierarchy is described by 'level' and
    'town' field.
    """
    VILLAGE, TOWN = (1, 2)

    # 131082 xxx for towns; 131082 xxx xxx for villages
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=60)
    level = models.IntegerField(null=False)
    # 乡镇及乡镇所属的村，该字段都指向该乡镇
    town = models.ForeignKey('self', null=True)
    # 本村或社区内当前健康档案数量，此字段只对level=1有效
    # 健康档案编号17位，no = id + '%05d' % (ehr_no + 1)
    ehr_no = models.IntegerField(default=0)
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_regions',
                                  related_query_name='created_region')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_regions',
                                  related_query_name='updated_region')

    objects = models.Manager()
    towns = TownManager()
    villages = VillageManager()

    def _is_town(self):
        if self.level == self.TOWN:
            return True
        else:
            return False

    is_town = property(_is_town)

    def _is_village(self):
        if self.level == self.VILLAGE:
            return True
        else:
            return False

    is_village = property(_is_village)

    def __unicode__(self):
        if self.is_town:
            return self.name
        else:
            return self.town.name + self.name


class TownClinicManager(models.Manager):
    def get_queryset(self):
        return super(TownClinicManager, self).get_queryset().filter(level=Clinic.TOWN_CLINIC)


class VillageClinicManager(models.Manager):
    def get_queryset(self):
        return super(VillageClinicManager, self).get_queryset().filter(level=Clinic.VILLAGE_CLINIC)


class Clinic(ChangeLogModel):
    """
    A model describes the clinics in Sanhe city including
    town clinics and village clinics. The administration hierarchy
    is described by 'level' and 'town' field.
    """
    VILLAGE_CLINIC, TOWN_CLINIC = (1, 2)

    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, null=True)
    region = models.ForeignKey(Region, related_name='clinics',
                               related_query_name='clinic', null=True)
    level = models.IntegerField(null=False)
    # if is_town_clinic, town_clinic is itself,but the field in database is None
    # otherwise town_clinic points to a town clinic
    town_clinic = models.ForeignKey('self', null=True,
                                    related_name='village_clinics',
                                    related_query_name='village_clinic')
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_clinics',
                                  related_query_name='created_clinic')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_clinics',
                                  related_query_name='updated_clinic', )

    objects = models.Manager()
    in_town = TownClinicManager()
    in_village = VillageClinicManager()

    def __unicode__(self):
        if self.is_town_clinic:
            return self.name
        else:
            return self.name + '(' + self.town_clinic.name + ')'

    def _is_town_clinic(self):
        if self.level == Clinic.TOWN_CLINIC:
            return True
        else:
            return False

    is_town_clinic = property(_is_town_clinic)

    def _is_village_clinic(self):
        if self.level == Clinic.VILLAGE_CLINIC:
            return True
        else:
            return False

    is_village_clinic = property(_is_village_clinic)


class ChildrenManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        critical_day = date(today.year-7, today.month, today.day)
        return super(ChildrenManager, self).get_queryset().filter(birthday__gt=critical_day)


class OldManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        critical_day = date(today.year-65, today.month, today.day)
        return super(OldManager, self).get_queryset().filter(birthday__lt=critical_day)


class Family(models.Model):
    pass


class OldManManager(models.Manager):
    """
    检索出老年人：出生年到今年达到65年
    """
    def get_queryset(self):
        import datetime
        start_date = datetime.date(1800, 1, 1)
        end_date = datetime.date(datetime.date.today().year-64, 1, 1)
        return super(VillageClinicManager, self).get_queryset().filter(birthday__range=(start_date, end_date))


class OldManManager(models.Manager):
    """
    检索出0-6岁儿童：到今天不满7周岁
    """
    def get_queryset(self):

        return super(VillageClinicManager, self).get_queryset().filter(level=Clinic.VILLAGE_CLINIC)


class Resident(ChangeLogModel):
    """
    描述居民基本信息的类
    """
    CHILD_4_YEAR, CHILD_7_YEAR, OLD_MAN_AGE = 4, 7, 65
    FEMALE, MALE, UNKNOWN = 0, 1, 2
    JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICES)
    nation = models.CharField(max_length=10, verbose_name='民族')
    birthday = models.DateField(verbose_name='出生日期')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='家庭地址')
    # 6位区县编码 + 3位乡镇编码 + 3位村（社区）编码 + 5位顺序编码 = 17位唯一健康档案编码
    # 因此，乡镇和村（社区）信息是居民信息中必须有的内容
    ehr_no = models.CharField(max_length=17, null=True, verbose_name='健康档案编号')
    personal_info_table = models.OneToOneField(PersonalInfo, null=True, verbose_name='个人基本信息表')
    psychiatric_info_table = models.OneToOneField(PsychiatricInfo, null=True, verbose_name='重性精神疾病患者信息表')
    vaccine_card = models.OneToOneField(VaccineCard, null=True, verbose_name='预防接种卡')
    # 身份证号码无法作为居民的ID，有些居民例如婴幼儿没有身份证号码
    identity = models.CharField(max_length=30, null=True, unique=True, verbose_name='身份证号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号码')
    email = models.EmailField(null=True, blank=True, verbose_name='电子邮箱')
    family = models.ForeignKey(Family, related_name='members', related_query_name='members',
                               null=True, blank=True)
    town = models.ForeignKey(Region, related_name='town_residents', null=True,
                             related_query_name='town_resident', verbose_name='所在乡镇')
    village = models.ForeignKey(Region, related_name='village_residents', null=True,
                                related_query_name='village_resident', verbose_name='所在村庄/街道')
    diabetes = models.IntegerField(default=0, verbose_name='糖尿病患者')
    hypertension = models.IntegerField(default=0, verbose_name='高血压患者')
    psychiatric = models.IntegerField(default=0, verbose_name='重症精神病患者')
    pregnant = models.IntegerField(default=0, verbose_name='孕产妇')
    #photo = models.ImageField()
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_residents',
                                  related_query_name='created_resident')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_residents',
                                  related_query_name='updated_resident')
    objects = models.Manager()
    children = ChildrenManager()
    old = OldManager()

    def __unicode__(self):
        return self.name

    def suffering_pregnant(self):
        if self.pregnant_courses:
            for course in self.pregnant_courses.all():
                if course.recover_date is None:
                    return True
        return False

    def _get_age(self):
        today = date.today()
        try:
            the_day = self.birthday.replace(year=today.year)
        except ValueError:
            the_day = self.birthday.replace(year=today.year, day=today.day-1)

        if the_day > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year

    age = property(_get_age)

    def _is_old_man(self):
        if self.age > self.OLD_MAN_AGE:
            return True
        else:
            return False

    is_old_man = property(_is_old_man)

    def _is_0_6_child(self):
        if self.age < self.CHILD_7_YEAR:
            return True
        else:
            return False

    is_0_6_child = property(_is_0_6_child)

    def _is_0_3_child(self):
        if self.age < self.CHILD_4_YEAR:
            return True
        else:
            return False

    is_0_3_child = property(_is_0_3_child)

    def service_items_todo(self):
        items = set()
        # whether the resident is a hypertension patient
        if self.hypertension:
            items = items | set(Service.items.filter(
                service_type__alias='hypertension', alias='physical_examination'))
            if date.today().month < self.APR:
                items = items | set(Service.items.filter(
                    service_type__alias='hypertension', alias='aftercare_1'))
            elif date.today().month < self.JUL:
                items = items | set(Service.items.filter(
                    service_type__alias='hypertension', alias='aftercare_2'))
            elif date.today().month < self.OCT:
                items = items | set(Service.items.filter(
                    service_type__alias='hypertension', alias='aftercare_3'))
            else:
                items = items | set(Service.items.filter(
                    service_type__alias='hypertension', alias='aftercare_4'))
        # whether the resident is a diabetes patient
        if self.diabetes:
            items = items | set(Service.items.filter(
                service_type__alias='diabetes', alias='physical_examination'))
            if date.today().month < self.APR:
                items = items | set(Service.items.filter(
                    service_type__alias='diabetes', alias='aftercare_1'))
            elif date.today().month < self.JUL:
                items = items | set(Service.items.filter(
                    service_type__alias='diabetes', alias='aftercare_2'))
            elif date.today().month < self.OCT:
                items = items | set(Service.items.filter(
                    service_type__alias='diabetes', alias='aftercare_3'))
            else:
                items = items | set(Service.items.filter(
                    service_type__alias='diabetes', alias='aftercare_4'))
        # whether the resident is a pregnant
        if self.pregnant:
            items = items | set(Service.items.filter(service_type__alias='pregnant'))
        # whether the resident is a psychiatric patient
        if self.psychiatric:
            items = items | set(Service.items.filter(
                service_type__alias='psychiatric', alias='physical_examination'))
            items = items | set(Service.items.filter(
                service_type__alias='psychiatric', alias='blood_routine_test'))
            items = items | set(Service.items.filter(
                service_type__alias='psychiatric', alias='transaminase'))
            items = items | set(Service.items.filter(
                service_type__alias='psychiatric', alias='blood_glucose'))
            items = items | set(Service.items.filter(
                service_type__alias='psychiatric', alias='electrocardiogram'))
            if date.today() < date(date.today().year, self.FEB, 16):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_1'))
            elif date.today() < date(date.today().year, self.APR, 1):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_2'))
            elif date.today() < date(date.today().year, self.MAY, 16):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_3'))
            elif date.today() < date(date.today().year, self.JUL, 1):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_4'))
            elif date.today() < date(date.today().year, self.AUG, 16):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_5'))
            elif date.today() < date(date.today().year, self.OCT, 1):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_6'))
            elif date.today() < date(date.today().year, self.NOV, 15):
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_7'))
            else:
                items = items | set(Service.items.filter(
                    service_type__alias='psychiatric', alias='aftercare_8'))
        # whether the resident is a person older than 65
        if self.is_old_man:
            items = items | set(Service.items.filter(service_type__alias='old'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='constitution_identification'))
        # whether the resident is parent of a child 0-6 years old
        if self.is_0_6_child:
            items = items | set(Service.items.filter(service_type__alias='child'))
            items = items | set(Service.items.filter(service_type__alias='vaccine'))
        # whether the resident is parent of a child 0-3 years old
        if self.is_0_3_child:
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_6_month'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_12_month'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_18_month'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_24_month'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_30_month'))
            items = items | set(Service.items.filter(
                service_type__alias='tcm', alias='aftercare_3_year'))
        return items

    def service_items_finished_of_type(self, from_the_day, service_type):
        items = [record.service_item for record in WorkRecord.objects.filter(
            resident=self, submit_time__gt=from_the_day, service_item__service_type=service_type)]
        return set(items)

    def service_items_finished(self, from_the_day):
        items = [record.service_item for record in WorkRecord.objects.filter(
            resident=self, submit_time__gt=from_the_day)]
        return set(items)

    def service_items_done(self):
        items = set()
        today = date.today()
        new_year_day = date(today.year, 1, 1)
        if self.diabetes:
            diabetes = Service.types.get(alias='diabetes')
            items = items | self.service_items_finished_of_type(new_year_day, diabetes)
        if self.hypertension:
            hypertension = Service.types.get(alias='hypertension')
            items = items | self.service_items_finished_of_type(new_year_day, hypertension)
        if self.psychiatric:
            psychiatric = Service.types.get(alias='psychiatric')
            items = items | self.service_items_finished_of_type(new_year_day, psychiatric)
        if self.is_old_man:
            old = Service.types.get(alias='old')
            items = items | self.service_items_finished_of_type(new_year_day, old)
            tcm = Service.types.get(alias='tcm')
            items = items | self.service_items_finished_of_type(new_year_day, tcm)
        if self.pregnant:
            pregnant = Service.types.get(alias='pregnant')
            one_year_ago = date(today.year-1, today.month, today.day)
            diagnose_date = one_year_ago
            #if self.pregnant_courses:
            #    for course in self.pregnant_courses:
            #        if course.recover_date is None:
            #            diagnose_date = course.diagnose_date
            #            break
            items = items | self.service_items_finished_of_type(diagnose_date, pregnant)
        if self.is_0_6_child:
            child = Service.types.get(alias='child')
            items = items | self.service_items_finished_of_type(self.birthday, child)
            vaccine = Service.types.get(alias='vaccine')
            items = items | self.service_items_finished_of_type(self.birthday, vaccine)
            tcm = Service.types.get(alias='tcm')
            items = items | self.service_items_finished_of_type(self.birthday, tcm)
        return items

    def service_types_todo(self):
        types = [item.service_type for item in self.service_items_todo()]
        return set(types)


class CourseOfIllness(models.Manager):
    diagnose_date = models.DateField(verbose_name='确诊日期')
    diagnose_clinic = models.ForeignKey(Clinic, verbose_name='确诊医疗机构')
    recover_date = models.DateField(verbose_name='康复日期', null=True)
    recover_clinic = models.ForeignKey(Clinic, verbose_name='确诊医疗机构', null=True)

    class Meta:
        abstract = True


'''
class CourseOfDiabetes(CourseOfIllness):
    patient = models.ForeignKey(Resident, verbose_name='糖尿病患者',
                                related_name='diabetes_courses',
                                related_query_name='diabetes_course')


class CourseOfHypertension(CourseOfIllness):
    patient = models.ForeignKey(Resident, verbose_name='高血压患者',
                                related_name='hypertension_courses',
                                related_query_name='hypertension_course')


class CourseOfPsychiatric(CourseOfIllness):
    patient = models.ForeignKey(Resident, verbose_name='重症精神病患者',
                                related_name='psychiatric_courses',
                                related_query_name='diabetes_course')
'''


class CourseOfPregnant(CourseOfIllness):
    patient = models.ForeignKey(Resident, verbose_name='孕产妇',
                                related_name='pregnant_courses',
                                related_query_name='pregnant_course')


class ServiceTypeManager(models.Manager):
    def get_queryset(self):
        return super(ServiceTypeManager, self).get_queryset().filter(level=Service.SERVICE_TYPE)


class ServiceItemManager(models.Manager):
    def get_queryset(self):
        return super(ServiceItemManager, self).get_queryset().filter(level=Service.SERVICE_ITEM)


class Service(ChangeLogModel):
    """
    A model describe the fundamental public health services including
    11 service types and 119 service items. The service hierarchy is
    described by the 'level' and 'type' field.
    """
    # for level
    SERVICE_ITEM, SERVICE_TYPE, SERVICE_GROUP = 1, 2, 3

    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10, null=True)
    price = models.FloatField(null=True)
    real_weight = models.FloatField(null=True)
    should_weight = models.FloatField(null=True)
    level = models.IntegerField(null=False)
    alias = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=6, null=True)
    # 如果本身是服务类别，那么此字段为null
    service_type = models.ForeignKey('self', null=True,
                                     related_name='service_items',
                                     related_query_name='service_item')
    # 服务组，服务类别>服务组>服务项目（计费项目）
    # 服务组是一般是位于一张表格中的服务项目组成
    # 服务类别、服务组和不属于服务组的服务项目，此字段为null
    service_group = models.ForeignKey('self', null=True,
                                      related_name='group_items',
                                      related_query_name='group_item')
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_services',
                                  related_query_name='created_service')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_services',
                                  related_query_name='updated_service')

    objects = models.Manager()
    types = ServiceTypeManager()
    items = ServiceItemManager()

    def service_groups(self):
        groups = list()
        if self.level != self.SERVICE_TYPE:
            return groups
        else:
            for item in self.service_items.all():
                if item.is_service_group():
                    groups.append(item)
            return groups

    def is_service_group(self):
        if self.level == self.SERVICE_TYPE:
            return False
        elif self.level == self.SERVICE_GROUP:
            return True
        elif self.level == self.SERVICE_ITEM and self.service_group is None:
            return True
        else:
            return False

    def _is_service_type(self):
        if self.level == self.SERVICE_TYPE:
            return True
        else:
            return False

    is_service_type = property(_is_service_type)

    def _is_service_item(self):
        if self.level == self.SERVICE_ITEM:
            return True
        else:
            return False

    is_service_item = property(_is_service_item)

    def __unicode__(self):
        if self.is_service_type:
            return self.name
        else:
            return self.service_type.name + '-' + self.name

    class Meta:
        ordering = ['code']


class GroupProfile(ChangeLogModel):
    """
    A model extends the django.contrib.auth.models.Group with
    such fields as 'is_staff' and 'default_services'. Town_clinic
    doctor and village_clinic doctor are the two main groups with
    different default service authorization.
    """
    group = models.OneToOneField(Group)
    is_staff = models.BooleanField(null=False, default=None)
    default_services = models.ManyToManyField(Service, null=True,
                                              related_name='authorized_groups',
                                              related_query_name='authorized_group')
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_group_profiles',
                                  related_query_name='created_group_profile')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_group_profiles',
                                  related_query_name='updated_group_profile')

    def __unicode__(self):
        if self.is_staff:
            return self.group.name + '(Administrator)'
        else:
            return self.group.name + '(Common user)'


class UserProfile(ChangeLogModel):
    """
    A model extends the django.contrib.auth.models.User with such
    describing fields as 'clinic', 'resident', 'authorized_services',
    etc. The model also provides the mechanism for service
    authorization to individual user.
    """
    user = models.OneToOneField(User)
    role = models.ForeignKey(Group, related_name='users',
                             related_query_name='user', verbose_name="角色")
    resident = models.OneToOneField(Resident, null=True)
    clinic = models.ForeignKey(Clinic, null=True,
                               related_name='users',
                               related_query_name='user', verbose_name="卫生院/卫生室")
    department = models.CharField(max_length=20, null=True, verbose_name="科室")
    position = models.CharField(max_length=20, null=True, verbose_name="岗位")
    authorized_services = models.ManyToManyField(Service, null=True,
                                                 related_name='authorized_users',
                                                 related_query_name='authorized_user')
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_user_profiles',
                                  related_query_name='created_user_profile')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_user_profiles',
                                  related_query_name='updated_user_profile')

    def __unicode__(self):
        if self.user.is_superuser:
            return self.user.username + '(Superuser)'
        elif self.user.is_staff:
            return self.user.username + '(Administrator)'
        else:
            return self.user.username + '(' + self.clinic.name + ')'


class WorkRecord(models.Model):
    # for evaluation
    NO_EVALUATION, UNSATISFIED, NORMAL, SATISFIED = (0, 1, 2, 3)
    # for status
    BEGAN, SUSPEND, FINISHED, PAID, CANCELLED, ERROR = (1, 2, 3, 4, 5, 6)

    provider = models.ForeignKey(User)
    resident = models.ForeignKey(Resident)
    service_item = models.ForeignKey(Service, null=True)
    # 应用的名称与服务类别的别称（alias）一致
    app_label = models.CharField(max_length=50, null=True)
    # 服务项目模型的名称
    model_name = models.CharField(max_length=50, null=True)
    # 该服务项目所在服务组的item_id
    group_item_id = models.IntegerField(null=True)
    # 该次服务的结果在对应数据库表中的主键
    item_id = models.IntegerField(null=True)
    # 该次服务的服务项目的别称（alias）
    service_item_alias = models.CharField(max_length=50, null=True)
    evaluation = models.IntegerField(default=SATISFIED)
    status = models.IntegerField(default=FINISHED)
    begin_time = models.DateTimeField(auto_now_add=True)
    submit_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)
    update_by = models.FloatField(User, null=True)

    class Meta:
        ordering = ['-submit_time']


class ModifyApply(models.Model):
    # 卫生局和财政局的意见
    WAITING, AGREE, DISAGREE = 1, 2, 3
    # 申请的状态
    SUBMITTED, CANCELED, AGREED, REFUSED, RECTIFIED, OVERDUE = 1, 2, 3, 4, 5, 6

    work_record = models.OneToOneField(WorkRecord, related_name='modify_apply')             # 申请修改的服务内容
    apply_time = models.DateTimeField(auto_now_add=True)    # 提交申请的时间
    finance_opinion = models.IntegerField(default=WAITING)  # 财政局的意见
    finance_opinion_time = models.DateTimeField(null=True)  # 财政局给出意见的时间
    health_opinion = models.IntegerField(default=WAITING)   # 卫生局的意见
    health_opinion_time = models.DateTimeField(null=True)    # 卫生局给出意见的时间
    apply_status = models.IntegerField()                    # 申请的状态
    finish_time = models.DateTimeField(null=True)           # 申请处理完成的时间


class Sms(models.Model):
    READY, SENT, ERROR = 1, 2, -1
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    name = models.CharField(max_length=20, verbose_name='姓名')
    next_time_date = models.DateField(verbose_name='下次服务时间')
    service_type_name = models.CharField(max_length=100, verbose_name='服务类别')
    service_item_name = models.CharField(max_length=100, verbose_name='服务项目')
    template_id = models.CharField(max_length=30, verbose_name='模板ID')
    status = models.IntegerField(verbose_name='短信状态')
    message = models.CharField(max_length=300, verbose_name='消息内容/错误提示', null=True)


class SmsTime(models.Model):
    FINISHED, UNFINISHED, CANCELED = 1, 2, 3
    service_type = models.ForeignKey(Service, related_name='sms_service_items',
                                     related_query_name='sms_service_item', verbose_name='服务类别')
    service_item = models.ForeignKey(Service, verbose_name='服务项目')
    service_time = models.DateField(verbose_name='下次服务时间')
    status = models.IntegerField(verbose_name='状态')
    message = models.CharField(max_length=300, null=True)
    create_by = models.ForeignKey(User, null=True,
                                  related_name='created_sms_times',
                                  related_query_name='created_sms_time')
    update_by = models.ForeignKey(User, null=True,
                                  related_name='updated_sms_times',
                                  related_query_name='updated_sms_time')


class Nav(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=50)
    state = models.CharField(max_length=20, null=True)
    iconCls = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=50, null=True)
    nid = models.IntegerField(default=0)

    class Meta:
        abstract = True


class AdminNav(Nav):
    town_clinic_admin = models.IntegerField(default=1)
    pass


class SvcNav(Nav):
    classification = models.CharField(max_length=20)
    pass


class DocNav(Nav):
    pass