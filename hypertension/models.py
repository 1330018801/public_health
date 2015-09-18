# -*- coding: utf-8 -*-
from django.db import models

from pregnant.models import ChoicesAbstract

MOUTH_LIP_CHOICES = ((u'红润', '红润'), (u'苍白', '苍白'), (u'发绀', '发绀'),
                     (u'皲裂', '皲裂'), (u'疱疹', '疱疹'),)
MOUTH_TOOTH_CHOICES = ((u'正常', '正常'), (u'缺齿', '缺齿'), (u'龋齿', '龋齿'),
                       (u'义齿（假牙）', '义齿（假牙）'),)
MOUTH_THROAT_CHOICES = ((u'无充血', '无充血'), (u'充血', '充血'),
                        (u'淋巴滤泡增生', '淋巴滤泡增生'),)
HEARING_CHOICES = ((u'听见', '听见'), (u'听不清或无法听见', '听不清或无法听见'),)
MOVEMENT_FUNCTION_CHOICES = ((u'可顺利完成', '可顺利完成'),
                             (u'无法独立完成其中任何一个动作', '无法独立完成其中任何一个动作'))
SKIN_CHOICES = ((u'正常', '正常'), (u'潮红', '潮红'), (u'苍白', '苍白'),
                (u'发绀', '发绀'), (u'黄染', '苍白'), (u'色素沉着', '色素沉着'), (u'其他', '其他'),)
LYMPH_NODE_CHOICES = ((u'未触及', '未触及'), (u'锁骨上', '锁骨上'),
                      (u'腋窝', '腋窝'), (u'其他', '其他'),)
NO_YES_CHOICES = ((u'否', '否'), (u'是', '是'),)
LUNG_RALE_CHOICES = ((u'否', '否'), (u'干罗音', '干罗音'), (u'湿罗音', '湿罗音'),
                     (u'其他', '其他'),)
NOTHING_OR_NOT_CHOICES = ((u'无', '无'), (u'有', '有'),)
HEART_RHYTHM = ((u'齐', '齐'), (u'不齐', '不齐'), (u'绝对不齐', '绝对不齐'),)

SFFS_CHOICES = ((u'门诊', '门诊'), (u'家庭', '家庭'), (u'电话', '电话'),)
ZZ_CHOICES = ((u'无症状', '无症状'), (u'头痛头晕', '头痛头晕'), (u'恶心呕吐', '恶心呕吐'),
              (u'眼花耳鸣', '眼花耳鸣'), (u'呼吸困难', '呼吸困难'), (u'心悸胸闷', '心悸胸闷'),
              (u'鼻衄出血不止', '鼻衄出血不止'), (u'四肢发麻', '四肢发麻'), (u'下肢浮肿', '下肢浮肿'),)
SHFSZDSYQK_CHOICES = ((u'轻', '轻'), (u'中', '中'), (u'重', '重'),)
SHFSZDXLTZ_CHOICES = ((u'良好', '良好'), (u'一般', '一般'), (u'差', '差'),)
TAKE_MEDICINE_COMPLIANCE = ((u'规律', '规律'), (u'间断', '间断'), (u'不服药', '不服药'),)
YWBLFY_CHOICES = ((u'无', '无'), (u'有', '有'),)
VISIT_CLASSIFICATION = ((u'控制满意', '控制满意'), (u'控制不满意', '控制不满意'),
                        (u'不良反应', '不良反应'), (u'并发症', '并发症'),)


class SymptomChoices(ChoicesAbstract):
    pass


class Aftercare(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期',)
    visit_way = models.CharField(max_length=10, verbose_name='随访方式', choices=SFFS_CHOICES)
    symptom = models.ManyToManyField(SymptomChoices, verbose_name='症状', blank=True, null=True,)
    symptom_extra = models.TextField(verbose_name='其他', blank=True, null=True,)
    sign_sbp = models.FloatField(verbose_name='血压-收缩压')
    sign_dbp = models.FloatField(verbose_name='血压-舒张压')
    sign_weight = models.FloatField(verbose_name='体重')
    sign_weight_next = models.FloatField(verbose_name='')
    sign_bmi = models.FloatField(verbose_name='体质指数')
    sign_bmi_next = models.FloatField(verbose_name='')
    sign_heart_rhythm = models.FloatField(verbose_name='心率')
    sign_extra = models.CharField(max_length=100, verbose_name='其他')
    life_style_guide_smoke = models.PositiveSmallIntegerField(verbose_name='日吸烟量')
    life_style_guide_smoke_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_guide_liquor = models.PositiveSmallIntegerField(verbose_name='日饮酒量')
    life_style_guide_liquor_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_guide_sport1 = models.PositiveSmallIntegerField(verbose_name='运动')
    life_style_guide_sport2 = models.PositiveSmallIntegerField()
    life_style_guide_sport3 = models.PositiveSmallIntegerField()
    life_style_guide_sport4 = models.PositiveSmallIntegerField()
    life_style_guide_salt = models.CharField(max_length=10, verbose_name='摄盐情况', choices=SHFSZDSYQK_CHOICES)
    life_style_guide_salt_next = models.CharField(max_length=10, choices=SHFSZDSYQK_CHOICES)
    life_style_guide_mentality = models.CharField(max_length=10, verbose_name='心理调整', choices=SHFSZDXLTZ_CHOICES)
    life_style_guide_medical_compliance = models.CharField(max_length=10, verbose_name='遵医行为', choices=SHFSZDXLTZ_CHOICES)
    auxiliary_examination = models.TextField(verbose_name='辅助检查*', blank=True, null=True,)
    take_medicine_compliance = models.CharField(max_length=10, verbose_name='服药依从性', choices=TAKE_MEDICINE_COMPLIANCE)
    medicine_untoward_effect = models.CharField(max_length=10, verbose_name='药物不良反应', choices=YWBLFY_CHOICES)
    medicine_untoward_effect_yes = models.CharField(max_length=100, blank=True, null=True)
    visit_classification = models.CharField(max_length=100, verbose_name='此次随访分类', choices=VISIT_CLASSIFICATION)
    take_medicine_1 = models.CharField(max_length=100, verbose_name='药物名称1', blank=True, null=True,)
    take_medicine_1_day = models.PositiveSmallIntegerField(verbose_name='用法用量', blank=True, null=True,)
    take_medicine_1_time = models.FloatField(blank=True, null=True,)
    take_medicine_2 = models.CharField(max_length=100, verbose_name='药物名称2', blank=True, null=True,)
    take_medicine_2_day = models.PositiveSmallIntegerField(verbose_name='用法用量', blank=True, null=True,)
    take_medicine_2_time = models.FloatField(blank=True, null=True,)
    take_medicine_3 = models.CharField(max_length=100, verbose_name='药物名称3', blank=True, null=True,)
    take_medicine_3_day = models.PositiveSmallIntegerField(verbose_name='用法用量', blank=True, null=True,)
    take_medicine_3_time = models.FloatField(blank=True, null=True,)
    take_medicine_qt = models.CharField(max_length=100, verbose_name='其他药物', blank=True, null=True,)
    take_medicine_qt_day = models.PositiveSmallIntegerField(verbose_name='用法用量', blank=True, null=True,)
    take_medicine_qt_time = models.FloatField(blank=True, null=True,)
    transfer_treatment_reason = models.CharField(max_length=1000, verbose_name='原因', blank=True, null=True,)
    transfer_treatment_institution = models.CharField(max_length=1000, verbose_name='机构及科室', blank=True, null=True,)
    next_visit_date = models.DateField(verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        db_table = 'hypertension_aftercare'
