# -*- coding=utf-8 -*-
from django.db import models


VACCINATE_POSITION_CHOICES = (
    (u'请选择', '请选择'),
    (u'上臂三角肌', '上臂三角肌'),
    (u'上臂三角肌中部略下处', '上臂三角肌中部略下处'),
    (u'上臂外侧三角肌', '上臂外侧三角肌'),
    (u'上臂外侧三角肌附着处', '上臂外侧三角肌附着处'),
    (u'上臂外侧三角肌下缘附着处', '上臂外侧三角肌下缘附着处'),
    (u'其他', '其他'),)


class Vaccination(models.Model):
    vaccine = models.ForeignKey('management.Service', verbose_name='疫苗与剂次')
    visit_date = models.DateField(max_length=10,  verbose_name='接种日期')
    vaccinate_position = models.CharField(max_length=100, verbose_name='接种部位')
    batch_number = models.CharField(max_length=100, verbose_name='疫苗批号',)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=20, verbose_name='医生签名')
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期', blank=True, null=True)


GENDER = ((u'男', u'男'), (u'女', u'女'),)
CENSUS_REGISTER_ADDRESS = ((u'同家庭地址', u'同家庭地址'),)


class VaccineCard(models.Model):
    ehr_village_no = models.CharField(max_length=3, verbose_name='健康档案编码中村（社区）对应的3位编码')
    ehr_unique_no = models.CharField(max_length=5, verbose_name='健康档案编码中最后5位编码')

    gender = models.CharField(max_length=20, verbose_name='性别', choices=GENDER)
    birth_date = models.DateField(max_length=10, verbose_name='出生日期')
    guardian_name = models.CharField(max_length=20, verbose_name='监护人姓名')
    relation_to_child = models.CharField(max_length=10, verbose_name='与儿童关系')
    contact_number = models.CharField(max_length=11, verbose_name='联系电话')
    home_county = models.CharField(max_length=20, verbose_name='户籍地址/县（区）', default='三河市')
    home_town = models.ForeignKey('management.Region', related_name='town_vaccine_card',
                                  verbose_name='家庭地址/乡镇（街道）')
    register_local = models.BooleanField(verbose_name='本地户籍', default=False)
    register_province = models.CharField(max_length=20, verbose_name='户籍地址/省（市、自治区）', null=True)
    register_city = models.CharField(max_length=20, verbose_name='户籍地址/市', null=True)
    register_county = models.CharField(max_length=20, verbose_name='户籍地址/县（区）', null=True)
    register_town = models.CharField(max_length=20, verbose_name='户籍地址/乡镇（街道）', null=True)

    immigrate_time = models.DateField(max_length=10, verbose_name='迁入时间', blank=True, null=True)
    emigrate_time = models.DateField(max_length=10, verbose_name='迁出时间', blank=True, null=True)
    emigrate_reason = models.CharField(max_length=300, verbose_name='迁出原因', blank=True, null=True)
    vaccine_abnormal_reaction_history = models.CharField(max_length=300, verbose_name='疫苗异常反应史')
    vaccinate_taboo = models.CharField(max_length=300, verbose_name='接种禁忌')
    infection_history = models.CharField(max_length=300, verbose_name='传染病史')
    found_card_date = models.DateField(max_length=10, verbose_name='建卡日期')
    found_card_person = models.CharField(max_length=20, verbose_name='建卡人')

    class Meta:
        db_table = 'vaccine_card'