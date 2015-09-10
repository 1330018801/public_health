#-*- coding:utf-8 -*-
from django.db import models

SFFS_CHOICES = ((u'门诊', '门诊'), (u'家庭', '家庭'), (u'电话', '电话'),)
ZZ_CHOICES = ((u'无症状', '无症状'), (u'多饮', '多饮'), (u'多食', '多食'),
              (u'多尿', '多尿'), (u'视力模糊', '视力模糊'), (u'感染', '感染'),
              (u'手脚麻木', '手脚麻木'), (u'下肢浮肿', '下肢浮肿'), (u'体重明显下降', '体重明显下降'),)
SHFSZDSYQK_CHOICES = ((u'轻', '轻'), (u'中', '中'), (u'重', '重'),)
SHFSZDXLTZ_CHOICES = ((u'良好', '良好'), (u'一般', '一般'), (u'差', '差'),)
YWBLFY_CHOICES = ((u'无', '无'), (u'有', '有'),)
VISIT_CLASSIFICATION = ((u'控制满意', '控制满意'), (u'控制不满意', '控制不满意'),
                        (u'不良反应', '不良反应'), (u'并发症', '并发症'),)
SIGN_ACROTARSIUM_ARTERY_PULSE = ((u'未触及', '未触及'), (u'触及', '触及'),)
TAKE_MEDICINE_COMPLIANCE = ((u'规律', '规律'), (u'间断', '间断'), (u'不服药', '不服药'),)
HYPOGLYCEMIA_REACTION = ((u'无', '无'), (u'偶尔', '偶尔'), (u'频繁', '频繁'),)


class ChoicesAbstract(models.Model):
    choice = models.CharField(max_length=50, primary_key=True)
    order = models.IntegerField()

    def __unicode__(self):
        return self.choice

    class Meta:
        abstract = True
        ordering = ('order',)


class SymptomChoices(ChoicesAbstract):
    pass


class AftercareAbstract(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期',)
    visit_way = models.CharField(max_length=10, verbose_name='随访方式', choices=SFFS_CHOICES)
    symptom = models.ManyToManyField(SymptomChoices, verbose_name='症状', blank=True, null=True,)
    symptom_extra = models.TextField(verbose_name='其他', blank=True, null=True,)
    sign_blood_pressure = models.FloatField(verbose_name='血压')
    sign_weight = models.FloatField(verbose_name='体重')
    sign_weight_next = models.FloatField(verbose_name='')
    sign_bmi = models.FloatField(verbose_name='体质指数')
    sign_bmi_next = models.FloatField(verbose_name='')
    sign_acrotarsium_artery_pulse = models.CharField(max_length=20, verbose_name='足背动脉搏动', choices=SIGN_ACROTARSIUM_ARTERY_PULSE)
    sign_extra = models.CharField(max_length=100, verbose_name='其他', blank=True, null=True,)
    life_style_guide_smoke = models.PositiveSmallIntegerField(verbose_name='日吸烟量')
    life_style_guide_smoke_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_guide_liquor = models.PositiveSmallIntegerField(verbose_name='日饮酒量')
    life_style_guide_liquor_next = models.PositiveSmallIntegerField(verbose_name='')
    life_style_guide_sport1 = models.PositiveSmallIntegerField(verbose_name='运动')
    life_style_guide_sport2 = models.PositiveSmallIntegerField()
    life_style_guide_sport3 = models.PositiveSmallIntegerField()
    life_style_guide_sport4 = models.PositiveSmallIntegerField()
    life_style_guide_staple = models.FloatField(verbose_name='主食',)
    life_style_guide_staple_next = models.FloatField(verbose_name='',)
    life_style_guide_mentality = models.CharField(max_length=10, verbose_name='心理调整', choices=SHFSZDXLTZ_CHOICES)
    life_style_guide_medical_compliance = models.CharField(max_length=10, verbose_name='遵医行为', choices=SHFSZDXLTZ_CHOICES)
    auxiliary_examination_fbg_value = models.FloatField(verbose_name='空腹血糖值',)
    auxiliary_examination_extra_hemoglobin = models.FloatField(verbose_name='糖化血红蛋白', blank=True, null=True,)
    auxiliary_examination_extra_examination_date = models.DateField(max_length=10 , verbose_name='检查日期', blank=True, null=True,)
    auxiliary_examination_extra_examination = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    take_medicine_compliance = models.CharField(max_length=10, verbose_name='服药依从性', choices=TAKE_MEDICINE_COMPLIANCE)
    medicine_untoward_effect = models.CharField(max_length=10, verbose_name='药物不良反应', choices=YWBLFY_CHOICES)
    hypoglycemia_reaction = models.CharField(max_length=10, verbose_name='低血糖反应', choices=HYPOGLYCEMIA_REACTION,)
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
    take_medicine_insulin = models.CharField(max_length=100, verbose_name='胰岛素', blank=True, null=True,)
    take_medicine_insulin_volume = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    transfer_treatment_reason = models.CharField(max_length=1000, verbose_name='原因', blank=True, null=True,)
    transfer_treatment_institution = models.CharField(max_length=1000, verbose_name='机构及科别', blank=True, null=True,)
    next_visit_date = models.DateField(verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        abstract = True


class Aftercare(AftercareAbstract):
    class Meta:
        db_table = 'diabetes_aftercare'


class Aftercare1(AftercareAbstract):
    class Meta:
        db_table = 'diabetes_aftercare_1'


class Aftercare2(AftercareAbstract):
    class Meta:
        db_table = 'diabetes_aftercare_2'


class Aftercare3(AftercareAbstract):
    class Meta:
        db_table = 'diabetes_aftercare_3'


class Aftercare4(AftercareAbstract):
    class Meta:
        db_table = 'diabetes_aftercare_4'
