# coding=utf-8
from django.db import models

__author__ = 'Xie Zhiqing'

VISIT_WAY = ((u'门诊', '门诊'), (u'家庭', '家庭'))
PATIENT_TYPE = ((u'初治', '初治'), (u'复治', '复治'))
PHLEGM_SITUATION = ((u'阳性', '阳性'), (u'阴性', '阴性'), (u'未查痰', '未查痰'))
DRUG_FAST_SITUATION = ((u'耐药', '耐药'), (u'非耐药', '非耐药'), (u'未检测', '未检测'))
USAGE = ((u'每日', '每日'), (u'间歇', '间歇'))
SUPERVISOR = ((u'医生', '医生'), (u'家属', '家属'), (u'自服药', '自服药'), (u'其他', '其他'))
SOLE_ROOM = ((u'有', '有'), (u'无', '无'))
VENTILATE_SITUATION = ((u'良好', '良好'), (u'一般', '一般'), (u'差', '差'))
MASTER_OR_NOT = ((u'掌握', '掌握'), (u'未掌握', '未掌握'))


class ChoicesAbstract(models.Model):
    choice = models.CharField(max_length=50, primary_key=True)
    order = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.choice

    class Meta:
        abstract = True
        ordering = 'order'


class SymptomSignChoices(ChoicesAbstract):
    pass


class DosageFormChoices(ChoicesAbstract):
    pass


class SymptomSign1Choices(ChoicesAbstract):
    pass


class DoHouse(models.Model):
    visit_date = models.DateField(verbose_name='随访时间')
    visit_way = models.CharField(verbose_name='随访方式', max_length=10, choices=VISIT_WAY)
    patient_type = models.CharField(verbose_name='患者类型', max_length=10, choices=PATIENT_TYPE)
    phlegm_situation = models.CharField(verbose_name='痰菌情况', max_length=20, choices=PHLEGM_SITUATION)
    drug_fast_situation = models.CharField(verbose_name='耐药情况', max_length=20, choices=DRUG_FAST_SITUATION)
    symptom_sign = models.ManyToManyField(SymptomSignChoices, verbose_name='症状及体征', blank=True, null=True)
    symptom_sign_extra = models.TextField(verbose_name='', blank=True, null=True)
    take_medicine_chemotherapy = models.CharField(verbose_name='化疗方案', max_length=500, blank=True, null=True)
    take_medicine_usage = models.CharField(verbose_name='用法', max_length=10, choices=USAGE, blank=True, null=True)
    take_medicine_dosage_form = models.ManyToManyField(DosageFormChoices, verbose_name='药品剂型', blank=True, null=True)
    supervisor = models.CharField(verbose_name='督导人员选择', max_length=20, choices=SUPERVISOR)
    residence_environment_sole_room = models.CharField(verbose_name='单独的居室', max_length=5, choices=SOLE_ROOM)
    resident_environment_ventilate_situation = models.CharField(verbose_name='通风情况', max_length=10, choices=VENTILATE_SITUATION)
    life_style_evaluate_smoke = models.PositiveSmallIntegerField(verbose_name='吸烟')
    life_style_evaluate_smoke_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_evaluate_liquor = models.PositiveSmallIntegerField(verbose_name='饮酒')
    life_style_evaluate_liquor_next = models.PositiveSmallIntegerField(verbose_name='')
    education_train_receive_medicine_place = models.CharField(verbose_name='取药地点、时间', max_length=50)
    education_train_receive_medicine_date = models.DateField(verbose_name='')
    education_train_1 = models.CharField(verbose_name='服药记录卡的填写', max_length=20, choices=MASTER_OR_NOT)
    education_train_2 = models.CharField(verbose_name='服药方法及药品存放', max_length=20, choices=MASTER_OR_NOT)
    education_train_3 = models.CharField(verbose_name='肺结核治疗疗程', max_length=20, choices=MASTER_OR_NOT)
    education_train_4 = models.CharField(verbose_name='不规律服药危害', max_length=20, choices=MASTER_OR_NOT)
    education_train_5 = models.CharField(verbose_name='服药后不良反应及处理', max_length=20, choices=MASTER_OR_NOT)
    education_train_6 = models.CharField(verbose_name='治疗期间复诊查痰', max_length=20, choices=MASTER_OR_NOT)
    education_train_7 = models.CharField(verbose_name='外出期间如何坚持服药', max_length=20, choices=MASTER_OR_NOT)
    education_train_8 = models.CharField(verbose_name='生活习惯及注意事项', max_length=20, choices=MASTER_OR_NOT)
    education_train_9 = models.CharField(verbose_name='密切接触者检查', max_length=20, choices=MASTER_OR_NOT)
    next_visit_date = models.DateField(verbose_name='下次随访时间')
    doctor_signature = models.CharField(verbose_name='评估医生签名', max_length=20)

    class Meta:
        db_table = 'phthisis_do_house'


VISIT_WAY_1 = ((u'门诊', '门诊'), (u'家庭', '家庭'), (u'电话', ''))
YES_OR_NO = ((u'无', '无'), (u'有', '有'))
STOP_CURE_REASON = ((u'完成疗程', '完成疗程'), (u'死亡', '死亡'), (u'丢失', '丢失'), (u'转入耐多药治疗', '转入耐多药治疗'))


class Aftercare(models.Model):
    visit_date = models.DateField(verbose_name='随访时间')
    month_order = models.PositiveSmallIntegerField(verbose_name='治疗月序')
    supervisor = models.CharField(verbose_name='督导人员', max_length=20, choices=SUPERVISOR)
    visit_way = models.CharField(verbose_name='随访方式', max_length=10, choices=VISIT_WAY_1)
    symptom_sign = models.ManyToManyField(SymptomSign1Choices, verbose_name='症状及体征', blank=True, null=True)
    symptom_sign_extra = models.TextField(verbose_name='', blank=True, null=True)
    life_style_guide_smoke = models.PositiveSmallIntegerField(verbose_name='吸烟')
    life_style_guide_smoke_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_guide_liquor = models.PositiveSmallIntegerField(verbose_name='饮酒')
    life_style_guide_liquor_next = models.PositiveSmallIntegerField(verbose_name='')
    take_medicine_chemotherapy = models.CharField(verbose_name='化疗方案', max_length=500, blank=True, null=True)
    take_medicine_usage = models.CharField(verbose_name='用法', max_length=10, choices=USAGE, blank=True, null=True)
    take_medicine_dosage_form = models.ManyToManyField(DosageFormChoices, verbose_name='药品剂型', blank=True, null=True)
    take_medicine_missing_times = models.PositiveSmallIntegerField(verbose_name='漏服药次数', blank=True, null=True)
    medicine_untoward_effect = models.CharField(max_length=10, verbose_name='药物不良反应', choices=YES_OR_NO)
    medicine_untoward_effect_yes = models.CharField(max_length=1000, verbose_name='', blank=True, null=True)
    complication = models.CharField(max_length=10, verbose_name='并发症或合并症', choices=YES_OR_NO)
    complication_yes = models.CharField(max_length=1000, verbose_name='', blank=True, null=True)
    transfer_treatment_department = models.CharField(max_length=1000, verbose_name='科别', blank=True, null=True,)
    transfer_treatment_reason = models.CharField(max_length=1000, verbose_name='原因', blank=True, null=True,)
    transfer_treatment_2_weeks_aftercare = models.TextField(verbose_name='2周内随访，随访结果', blank=True, null=True)
    dispose_opinion = models.CharField(max_length=1000, verbose_name='处理意见')
    next_visit_date = models.DateField(verbose_name='下次随访时间')
    doctor_signature = models.CharField(verbose_name='随访医生签字', max_length=20)
    stop_cure_date = models.DateField(verbose_name='出现停止治疗时间', blank=True, null=True)
    stop_cure_reason = models.CharField(verbose_name='停止治疗原因', max_length=50, choices=STOP_CURE_REASON, blank=True, null=True)
    whole_management_due_aftercare_times = models.PositiveSmallIntegerField(verbose_name='应访视患者', blank=True, null=True)
    whole_management_actual_aftercare_times = models.PositiveSmallIntegerField(verbose_name='实际访视', blank=True, null=True)
    whole_management_due_medicine_times = models.PositiveSmallIntegerField(verbose_name='患者在疗程中，应服药', blank=True, null=True)
    whole_management_actual_medicine_times = models.PositiveSmallIntegerField(verbose_name='实际服药', blank=True, null=True)
    whole_management_medicine_rate = models.FloatField(verbose_name='服药率', blank=True, null=True)
    whole_management_doctor_signature = models.CharField(verbose_name='评估医生签名', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'phthisis_aftercare'
