#-*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from management.models import Clinic
from django.contrib.auth.models import User


class Patrol(models.Model):
    institution = models.CharField(max_length=50, verbose_name="")
    place_content = models.TextField(max_length=1000, verbose_name="")
    main_problem = models.TextField(max_length=2000, verbose_name="")
    patrol_date = models.DateField(verbose_name="")
    patrolman = models.CharField(max_length=50, verbose_name="")
    remarks = models.TextField(max_length=1000, verbose_name="", blank=True, null=True)


class InformationReport(models.Model):
    institution = models.CharField(max_length=50, verbose_name="")
    discover_date = models.DateTimeField(verbose_name="")
    information_type = models.CharField(max_length=50, verbose_name="")
    information_content = models.TextField(max_length=1000, verbose_name="")
    report_date = models.DateTimeField(verbose_name="")
    reporter = models.CharField(max_length=50, verbose_name="")


class Inspection(models.Model):
    institution = models.ForeignKey(Clinic, verbose_name='机构')
    place_content = models.TextField(max_length=1000, verbose_name='巡查地点与内容')
    main_problem = models.TextField(max_length=2000, verbose_name='发现的主要问题')
    inspection_date = models.DateField(verbose_name='巡查日期')
    inspector = models.CharField(max_length=50, verbose_name='巡查人')
    remarks = models.TextField(max_length=1000, verbose_name='备注', blank=True, null=True)
    create_by = models.ForeignKey(User, verbose_name='登记人')
    create_time = models.DateTimeField(verbose_name='登记时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

REPORT_TYPE = ((1, '食品安全'), (2, '饮用水卫生'), (3, '职业病危害'), (4, '学校卫生'), (5, '非法行医（采供血）'))


class InfoReport(models.Model):
    institution = models.ForeignKey(Clinic, verbose_name='机构')
    discover_time = models.DateTimeField(verbose_name='发现时间')
    info_type = models.CharField(max_length=50, verbose_name='信息类别')
    info_content = models.TextField(max_length=1000, verbose_name='信息内容')
    report_time = models.DateTimeField(verbose_name='报告时间', auto_now_add=True)
    reporter = models.CharField(max_length=50, verbose_name='报告人')