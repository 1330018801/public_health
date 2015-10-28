# -*- coding: utf-8 -*-
from django.db import models
from pregnant.models import ChoicesAbstract

GUIDE_1 = (
    (u'中医饮食调养指导', '中医饮食调养指导'),
    (u'中医起居调摄指导', '中医起居调摄指导'),
    (u'传授摩腹、捏脊方法', '传授摩腹、捏脊方法'),
    (u'其他', '其他'),)


GUIDE_2 = (
    (u'中医饮食调养指导', '中医饮食调养指导'),
    (u'中医起居调摄指导', '中医起居调摄指导'),
    (u'传授迎香穴、足三里穴方法', '传授迎香穴、足三里穴方法'),
    (u'其他', '其他'),)


GUIDE_3 = (
    (u'中医饮食调养指导', '中医饮食调养指导'),
    (u'中医起居调摄指导', '中医起居调摄指导'),
    (u'传授按揉四神聪穴方法', '传授按揉四神聪穴方法'),
    (u'其他', '其他'),)


class TcmChildGuideChoices1(ChoicesAbstract):
    pass

    class Meta:
        db_table = 'tcm_child_guide_choice_1'


class TcmChildGuideChoices2(ChoicesAbstract):
    pass

    class Meta:
        db_table = 'tcm_child_guide_choice_2'


class TcmChildGuideChoices3(ChoicesAbstract):
    pass

    class Meta:
        db_table = 'tcm_child_guide_choice_3'


class Aftercare(models.Model):
    visit_date = models.DateField(max_length=15, verbose_name='随访日期',)
    guide = models.ManyToManyField(TcmChildGuideChoices1, verbose_name='指导', blank=True, null=True,)
    guide_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=30, verbose_name='随访医生签名')
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期', blank=True, null=True)

    class Meta:
        db_table = 'tcm_child_aftercare'


CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
YES_TREND = ((u'是', '是'), (u'倾向是', '倾向是'))
YES_MAINLY = ((u'是', '是'), (u'基本是', '基本是'))

class TcmOldIdentifyChoicesAbstract(models.Model):
    choice = models.CharField(max_length=50, primary_key=True)
    order = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.choice

    class Meta:
        abstract = True
        ordering = ('order',)


class TcmOldIdentifyChoicesQixu(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesYangxu(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesYinxu(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesTanshi(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesShire(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesXueyu(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesQiyu(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesTebing(TcmOldIdentifyChoicesAbstract):
    pass


class TcmOldIdentifyChoicesPinghe(TcmOldIdentifyChoicesAbstract):
    pass


class OldIdentify(models.Model):
    q1 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q2 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q3 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q4 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q5 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q6 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q7 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q8 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q9 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q10 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q11 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q12 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q13 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q14 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q15 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q16 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q17 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q18 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q19 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q20 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q21 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q22 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q23 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q24 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q25 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q26 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q27 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q28 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q29 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q30 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q31 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q32 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    q33 = models.PositiveSmallIntegerField(verbose_name='', choices=CHOICES, blank=True, null=True)
    points_qixu = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_yangxu = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_yinxu = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_tanshi = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_shire = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_xueyu = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_qiyu = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_tebing = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    points_pinghe = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True)
    yes_trend_qixu = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_yangxu = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_yinxu = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_tanshi = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_shire = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_xueyu = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_qiyu = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_tebing = models.CharField(choices=YES_TREND, max_length=20, blank=True, null=True)
    yes_trend_pinghe = models.CharField(choices=YES_MAINLY, max_length=20, blank=True, null=True)
    health_care_guide_qixu = models.ManyToManyField(TcmOldIdentifyChoicesQixu, verbose_name='', blank=True, null=True)
    health_care_guide_yangxu = models.ManyToManyField(TcmOldIdentifyChoicesYangxu, verbose_name='', blank=True, null=True)
    health_care_guide_yinxu = models.ManyToManyField(TcmOldIdentifyChoicesYinxu, verbose_name='', blank=True, null=True)
    health_care_guide_tanshi = models.ManyToManyField(TcmOldIdentifyChoicesTanshi, verbose_name='', blank=True, null=True)
    health_care_guide_shire = models.ManyToManyField(TcmOldIdentifyChoicesShire, verbose_name='', blank=True, null=True)
    health_care_guide_xueyu = models.ManyToManyField(TcmOldIdentifyChoicesXueyu, verbose_name='', blank=True, null=True)
    health_care_guide_qiyu = models.ManyToManyField(TcmOldIdentifyChoicesQiyu, verbose_name='', blank=True, null=True)
    health_care_guide_tebing = models.ManyToManyField(TcmOldIdentifyChoicesTebing, verbose_name='', blank=True, null=True)
    health_care_guide_pinghe = models.ManyToManyField(TcmOldIdentifyChoicesPinghe, verbose_name='', blank=True, null=True)
    health_care_guide_extra_qixu = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_yangxu = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_yinxu = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_tanshi = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_shire = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_xueyu = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_qiyu = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_tebing = models.CharField(max_length=200, blank=True, null=True)
    health_care_guide_extra_pinghe = models.CharField(max_length=200, blank=True, null=True)
    fill_table_date = models.DateField(blank=True, null=True)
    doctor_signature = models.CharField(max_length=50, blank=True, null=True)