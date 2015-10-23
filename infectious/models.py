#coding=utf-8
from django.db import models

# Create your models here.


class RiskManagement(models.Model):
    risk_inspection = models.TextField(verbose_name='风险排查')
    risk_information = models.TextField(verbose_name='风险信息')
    #risk_information_photo = models.ImageField(updoad_to='')
    risk_evaluation = models.TextField(verbose_name='风险评估')
    contingency_plan = models.TextField(verbose_name='应急预案')
    report_time = models.DateTimeField(verbose_name='报告时间')

    class Meta:
        db_table = 'risk_management'