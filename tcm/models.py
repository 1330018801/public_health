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


class AftercareAbstract(models.Model):
    visit_date = models.DateField(max_length=15, verbose_name='随访日期',)
    guide_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=30, verbose_name='随访医生签名')

    class Meta:
        abstract = True


class Aftercare(models.Model):
    visit_date = models.DateField(max_length=15, verbose_name='随访日期',)
    guide = models.ManyToManyField(TcmChildGuideChoices1, verbose_name='指导', blank=True, null=True,)
    guide_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=30, verbose_name='随访医生签名')
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期', blank=True, null=True)

    class Meta:
        db_table = 'tcm_child_aftercare'


class Aftercare6Month(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices1, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期',)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_6_month'))


class Aftercare12Month(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices1, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期',)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_12_month'))


class Aftercare18Month(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices2, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期',)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_18_month'))


class Aftercare24Month(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices2, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期',)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_24_month'))


class Aftercare30Month(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices3, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=15, verbose_name='下次随访日期',)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_30_month'))


class Aftercare3Year(AftercareAbstract):
    guide = models.ManyToManyField(TcmChildGuideChoices3, verbose_name='指导', blank=True, null=True,)

    class Meta:
        db_table = '_'.join(('tcm', 'aftercare_3_year'))