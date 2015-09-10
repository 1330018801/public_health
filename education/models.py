# -*- coding: utf-8 -*-
from django.db import models

WAY = ((u'宣传栏', '宣传栏'), (u'宣传栏更新', '宣传栏更新'), (u'宣传册', '宣传册'), (u'宣传单', '宣传单'), (u'宣传折页', '宣传折页'),
            (u'资料架', '资料架'), (u'宣传栏维护', '宣传栏维护'), (u'音像资料', '音像资料'), (u'公众健康咨询活动', '公众健康咨询活动'),
            (u'健康知识讲座', '健康知识讲座'), (u'健康教育网站', '健康教育网站'))
ATTACHMENT = ((u'书面材料', '书面材料'), (u'图片材料', '图片材料'), (u'印刷材料', '印刷材料'), (u'影音材料', '影音材料'),
              (u'签到表', '签到表'), (u'其他材料', '其他材料'),)


class EducationActivity(models.Model):
    act_time = models.DateTimeField(verbose_name='活动时间')
    scene = models.CharField(max_length=100, verbose_name='活动地点')
    act_type = models.CharField(max_length=100, verbose_name='活动形式')
    subject = models.CharField(max_length=150, verbose_name='活动主题')
    organizer = models.CharField(max_length=50, verbose_name='组织者')
    crowd_type = models.CharField(max_length=50, verbose_name='接受健康教育人员类别')
    crowd_num = models.IntegerField(verbose_name='接受健康教育人数')
    material_type = models.CharField(max_length=50, verbose_name='健康教育资料发放种类')
    material_num = models.IntegerField(verbose_name='健康教育资料发放数量')
    content = models.CharField(max_length=1000, verbose_name='活动内容')
    summary = models.CharField(max_length=1000, verbose_name='活动总结评价')

    class Meta:
        db_table = 'education_activity'


class HealthEducate(models.Model):
    date = models.DateField(verbose_name='')
    place = models.CharField(max_length=100, verbose_name='')
    #way_name = models.CharField(max_length=100, verbose_name='')
    way = models.CharField(max_length=200, verbose_name='', blank=True, null=True)
    topic = models.CharField(max_length=300, verbose_name='')
    principal = models.CharField(max_length=20, verbose_name='')
    audience = models.CharField(max_length=100, verbose_name='')
    people_number = models.PositiveSmallIntegerField(verbose_name='')
    material = models.CharField(max_length=20, verbose_name='')
    count = models.PositiveSmallIntegerField(verbose_name='')
    content = models.TextField(max_length=1000, verbose_name='')
    evaluation = models.TextField(max_length=1000, verbose_name='')
    #attachment = models.CharField(max_length=20, verbose_name='', choices=ATTACHMENT)
    upload = models.ImageField(upload_to='photos/%Y%m%d', max_length=100)

    class Meta:
        db_table = 'education_health_educate'

'''
class Educate(models.Model):
    date = models.DateField(verbose_name='')
    institution = models.CharField(max_length=50, verbose_name='')
    count = models.PositiveSmallIntegerField(verbose_name='')
    principal = models.CharField(max_length=20, verbose_name='')
    content = models.TextField(max_length=1000, verbose_name='')
    load = models.ImageField(upload_to='photos/%Y%m%d', max_length=100)

    class Meta:
        abstract = True
'''


class AdBoard(HealthEducate):
    class Meta:
        db_table = 'education_ad_board'


class AdBoardUpdate(HealthEducate):
    class Meta:
        db_table = 'education_ad_board_update'


class AdBook(HealthEducate):
    class Meta:
        db_table = 'education_ad_book'


class AdPage(HealthEducate):
    class Meta:
        db_table = 'education_ad_page'


class AdBooklet(HealthEducate):
    class Meta:
        db_table = 'education_ad_booklet'


class Shelf(HealthEducate):
    class Meta:
        db_table = 'education_shelf'


class AdBoardMaintenance(HealthEducate):
    class Meta:
        db_table = 'education_ad_board_maintenance'


class Video(HealthEducate):
    class Meta:
        db_table = 'education_video'


class PublicHealthConsultation(HealthEducate):
    class Meta:
        db_table = 'education_public_health_consultation'


class HealthKnowledgeLecture(HealthEducate):
    class Meta:
        db_table = 'education_health_knowledge_lecture'


class HealthEducationWebsite(HealthEducate):
    class Meta:
        db_table = 'education_health_education_website'
