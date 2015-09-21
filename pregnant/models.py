# -*- coding: utf-8 -*-
from django.db import models

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
                (u'发绀', '发绀'), (u'黄染', '黄染'), (u'色素沉着', '色素沉着'), (u'其他', '其他'),)
LYMPH_NODE_CHOICES = ((u'未触及', '未触及'), (u'锁骨上', '锁骨上'),
                      (u'腋窝', '腋窝'), (u'其他', '其他'),)
NO_YES_CHOICES = ((u'否', '否'), (u'是', '是'),)
LUNG_RALE_CHOICES = ((u'否', '否'), (u'干罗音', '干罗音'), (u'湿罗音', '湿罗音'),
                     (u'其他', '其他'),)
NOTHING_OR_NOT_CHOICES = ((u'无', '无'), (u'有', '有'),)
HEART_RHYTHM = ((u'齐', '齐'), (u'不齐', '不齐'), (u'绝对不齐', '绝对不齐'),)

NORMAL_OR_ABNORMAL = ((u'未见异常', '未见异常'), (u'异常', '异常'),)
TRANSFER_TREATMENT = ((u'无', '无'), (u'有', '有'),)
RECOVERY_OR_NOT = ((u'已恢复', '已恢复'), (u'未恢复', '未恢复'),)
DISPOSE = ((u'结案', '结案'), (u'转诊', '转诊'),)

GYNAECOLOGY_SURGERY = ((u'无', u'无'), (u'有', u'有'))  # for aftercare1
BLOOD_ABO_CHOICES = ((u'A型', u'A型'), (u'B型', u'B型'), (u'O型', u'O型'), (u'AB型', u'AB型'), (u'其他', u'其他'))
BLOOD_RH_CHOICES = ((u'Rh阴性', u'Rh阴性'), (u'Rh阳性', u'Rh阳性'), (u'不祥', u'不祥'))
VAGINAL_SECRETION = ((u'未见异常', u'未见异常'), (u'滴虫', u'滴虫'), (u'假丝酵母菌', u'假丝酵母菌'), (u'其他', u'其他'))
VAGINAL_CLEAN_DEGREE = ((u'I度', u'I度'), (u'II度', u'II度'), (u'III度', u'III度'), (u'IV度', u'IV度'),)


class ChoicesAbstract(models.Model):
    choice = models.CharField(max_length=50, primary_key=True)
    order = models.IntegerField()

    def __unicode__(self):
        return self.choice

    class Meta:
        abstract = True
        ordering = ('order',)


class Guide6Choices(ChoicesAbstract):
    pass


class DiseaseHistoryChoices(ChoicesAbstract):
    pass


class FamilyHistoryChoices(ChoicesAbstract):
    pass


class PersonalHistoryChoices(ChoicesAbstract):
    pass


# 一般体格检查
class PhyExamAbstract(models.Model):
    weeks = models.IntegerField(verbose_name='填表孕周')
    age = models.IntegerField(verbose_name='孕妇年龄')
    husband_name = models.CharField(max_length=20, verbose_name='丈夫姓名')
    husband_age = models.IntegerField(verbose_name='丈夫年龄')
    husband_phone = models.CharField(max_length=20, verbose_name='丈夫电话')
    pregnant_times = models.IntegerField(verbose_name='孕次')
    natural_production = models.IntegerField(verbose_name='阴道分娩')
    surgery_production = models.IntegerField(verbose_name='剖宫产')
    last_menstruation = models.DateField(max_length=10, verbose_name='末次月经')
    not_sure = models.NullBooleanField(verbose_name='不祥', blank=True, null=True)
    due_date = models.DateField(max_length=10, verbose_name='预产期')
    disease_history = models.ManyToManyField(DiseaseHistoryChoices, verbose_name='既往史')
    disease_history_other = models.CharField(max_length=20, verbose_name='其他既往史', blank=True, null=True)
    family_history = models.ManyToManyField(FamilyHistoryChoices, verbose_name='家族史')
    family_history_other = models.CharField(max_length=20, verbose_name='其他家族史', blank=True, null=True)
    personal_history = models.ManyToManyField(PersonalHistoryChoices, verbose_name='个人史')
    personal_history_other = models.CharField(max_length=20, verbose_name='其他个人史', blank=True, null=True)
    gynaecology_surgery_history = models.CharField(max_length=10, choices=GYNAECOLOGY_SURGERY, verbose_name='妇科手术史')
    gynaecology_surgery_name = models.CharField(max_length=20, verbose_name='妇科手术名称', blank=True, null=True)
    miscarriage = models.IntegerField(verbose_name='流产')
    dead_fetus = models.IntegerField(verbose_name='死胎')
    still_birth = models.IntegerField(verbose_name='死产')
    newnatal_death = models.IntegerField(verbose_name='新生儿死亡')
    birth_defect = models.IntegerField(verbose_name='出生缺陷儿')
    height = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
    bmi = models.FloatField(verbose_name='体质指数')
    sbp = models.IntegerField(verbose_name='收缩压')
    dbp = models.IntegerField(verbose_name='舒张压')
    ausculate_heart = models.CharField(max_length=10, choices=NORMAL_OR_ABNORMAL, verbose_name='听诊心脏')
    ausculate_heart_abnormal = models.CharField(max_length=30, verbose_name='听诊心脏异常', blank=True, null=True)
    ausculate_lung = models.CharField(max_length=10, choices=NORMAL_OR_ABNORMAL, verbose_name='听诊肺部')
    ausculate_lung_abnormal = models.CharField(max_length=30, verbose_name='听诊肺部异常', blank=True, null=True)

    class Meta:
        abstract = True


# 妇科检查
class GynaecologicalExamination(models.Model):
    vulva = models.CharField(max_length=20, verbose_name='外阴', choices=NORMAL_OR_ABNORMAL)
    vulva_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    vagina = models.CharField(max_length=20, verbose_name='阴道', choices=NORMAL_OR_ABNORMAL)
    vagina_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    cervix = models.CharField(max_length=20, verbose_name='宫颈', choices=NORMAL_OR_ABNORMAL)
    cervix_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    uteri = models.CharField(max_length=20, verbose_name='宫体', choices=NORMAL_OR_ABNORMAL)
    uteri_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    accessory = models.CharField(max_length=20, verbose_name='附件', choices=NORMAL_OR_ABNORMAL)
    accessory_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    class Meta:
        abstract = True


# 血常规
class BloodRoutineTest(models.Model):
    hemoglobin = models.FloatField(verbose_name='血红蛋白',)
    leukocyte = models.FloatField(verbose_name='白细胞计数值', blank=True, null=True)
    thrombocyte = models.FloatField(verbose_name='血小板',)
    blood_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    class Meta:
        #db_table = 'pregnant_blood_routine_test'
        abstract = True


# 尿常规
class UrineRoutineTest(models.Model):
    urine_protein = models.CharField(max_length=10, verbose_name='尿蛋白')
    urine_glucose = models.CharField(max_length=10, verbose_name='尿糖')
    urine_ket = models.CharField(max_length=10, verbose_name='尿酮体')
    urine_ery = models.CharField(max_length=10, verbose_name='尿潜血')
    urine_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    class Meta:
        #db_table = 'pregnant_urine_routine_test'
        abstract = True


# 血型
class BloodType(models.Model):
    blood_type_abo = models.CharField(max_length=10, verbose_name='血型ABO', choices=BLOOD_ABO_CHOICES)
    blood_type_abo_other = models.CharField(max_length=30, verbose_name='血型其他', blank=True, null=True)
    blood_type_rh = models.CharField(max_length=10, verbose_name='血型Rh', choices=BLOOD_RH_CHOICES, blank=True, null=True)

    class Meta:
        #db_table = 'pregnant_blood_type'
        abstract = True


# 谷丙转氨酶
class AlanineAminotransferase(models.Model):
    sgpt = models.FloatField(verbose_name='血清谷丙转氨酶')

    class Meta:
        #db_table = 'pregnant_alanine_aminotransferase'
        abstract = True


# 谷草转氨酶
class GlutamicOxalaceticTransaminase(models.Model):
    sgot = models.FloatField(verbose_name='血清谷草转氨酶')

    class Meta:
        #db_table = 'pregnant_glutamic_oxalacetic_transaminase'
        abstract = True


# 总胆红素
class TotalBilirubin(models.Model):
    tbil = models.FloatField(verbose_name='总胆红素')

    class Meta:
        #db_table = 'pregnant_total_bilirubin'
        abstract = True


# 血清肌酐
class SerumCreatinine(models.Model):
    scr = models.FloatField(verbose_name='血清肌酐',)

    class Meta:
        # db_table = 'pregnant_serum_creatinine'
        abstract = True


# 血尿素氮
class BloodUreaNitrogen(models.Model):
    bun = models.FloatField(verbose_name='血尿素氮')

    class Meta:
        # db_table = 'pregnant_blood_urea_nitrogen'
        abstract = True

NEGATIVE_OR_POSITIVE = ((u'阴性', '阴性'), (u'阳性', '阳性'),)


# 乙肝五项
class HepatitisBFiveItem(models.Model):
    surface_antigen = models.CharField(max_length=10, verbose_name='乙型肝炎表面抗原', choices=NEGATIVE_OR_POSITIVE)
    surface_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎表面抗体', choices=NEGATIVE_OR_POSITIVE)
    e_antigen = models.CharField(max_length=10, verbose_name='乙型肝炎e抗原', choices=NEGATIVE_OR_POSITIVE)
    e_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎e抗体', choices=NEGATIVE_OR_POSITIVE)
    core_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎核心抗体', choices=NEGATIVE_OR_POSITIVE)

    class Meta:
        #db_table = 'pregnant_hepatitis_b_five_item'
        abstract = True


# 第一次产前随访
class Aftercare1(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='填表日期')
    # 一般体格检查
    weeks = models.IntegerField(verbose_name='填表孕周', blank=True, null=True)
    age = models.IntegerField(verbose_name='孕妇年龄', blank=True, null=True)
    husband_name = models.CharField(max_length=20, verbose_name='丈夫姓名', blank=True, null=True)
    husband_age = models.IntegerField(verbose_name='丈夫年龄')
    husband_phone = models.CharField(max_length=20, verbose_name='丈夫电话', blank=True, null=True)
    pregnant_times = models.IntegerField(verbose_name='孕次', blank=True, null=True)
    natural_production = models.IntegerField(verbose_name='阴道分娩', blank=True, null=True)
    surgery_production = models.IntegerField(verbose_name='剖宫产', blank=True, null=True)
    last_menstruation = models.DateField(max_length=10, verbose_name='末次月经', blank=True, null=True)
    not_sure = models.NullBooleanField(verbose_name='不祥', blank=True, null=True)
    due_date = models.DateField(max_length=10, verbose_name='预产期', blank=True, null=True)
    disease_history = models.ManyToManyField(DiseaseHistoryChoices, verbose_name='既往史', blank=True, null=True)
    disease_history_other = models.CharField(max_length=20, verbose_name='其他既往史', blank=True, null=True)
    family_history = models.ManyToManyField(FamilyHistoryChoices, verbose_name='家族史', blank=True, null=True)
    family_history_other = models.CharField(max_length=20, verbose_name='其他家族史', blank=True, null=True)
    personal_history = models.ManyToManyField(PersonalHistoryChoices, verbose_name='个人史', blank=True, null=True)
    personal_history_other = models.CharField(max_length=20, verbose_name='其他个人史', blank=True, null=True)
    gynaecology_surgery_history = models.CharField(max_length=10, choices=GYNAECOLOGY_SURGERY,
                                                   verbose_name='妇科手术史', blank=True, null=True)
    gynaecology_surgery_name = models.CharField(max_length=20, verbose_name='妇科手术名称', blank=True, null=True)
    miscarriage = models.IntegerField(verbose_name='流产', blank=True, null=True)
    dead_fetus = models.IntegerField(verbose_name='死胎', blank=True, null=True)
    still_birth = models.IntegerField(verbose_name='死产', blank=True, null=True)
    newnatal_death = models.IntegerField(verbose_name='新生儿死亡', blank=True, null=True)
    birth_defect = models.IntegerField(verbose_name='出生缺陷儿', blank=True, null=True)
    height = models.FloatField(verbose_name='身高', blank=True, null=True)
    weight = models.FloatField(verbose_name='体重', blank=True, null=True)
    bmi = models.FloatField(verbose_name='体质指数', blank=True, null=True)
    sbp = models.IntegerField(verbose_name='收缩压', blank=True, null=True)
    dbp = models.IntegerField(verbose_name='舒张压', blank=True, null=True)
    ausculate_heart = models.CharField(max_length=10, choices=NORMAL_OR_ABNORMAL,
                                       verbose_name='听诊心脏', blank=True, null=True)
    ausculate_heart_abnormal = models.CharField(max_length=30, verbose_name='听诊心脏异常', blank=True, null=True)
    ausculate_lung = models.CharField(max_length=10, choices=NORMAL_OR_ABNORMAL,
                                      verbose_name='听诊肺部', blank=True, null=True)
    ausculate_lung_abnormal = models.CharField(max_length=30, verbose_name='听诊肺部异常', blank=True, null=True)

    # 妇科检查
    vulva = models.CharField(max_length=20, verbose_name='外阴', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    vulva_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    vagina = models.CharField(max_length=20, verbose_name='阴道', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    vagina_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    cervix = models.CharField(max_length=20, verbose_name='宫颈', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    cervix_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    uteri = models.CharField(max_length=20, verbose_name='子宫', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    uteri_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    accessory = models.CharField(max_length=20, verbose_name='附件', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    accessory_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    # 血常规计费标准：检测前三项
    hemoglobin = models.FloatField(verbose_name='血红蛋白值', blank=True, null=True)
    leukocyte = models.FloatField(verbose_name='白细胞计数值', blank=True, null=True)
    thrombocyte = models.FloatField(verbose_name='血小板计数值', blank=True, null=True)
    blood_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    # 尿常规计费标准：检测前四项
    urine_protein = models.CharField(max_length=10, verbose_name='尿蛋白', blank=True, null=True)
    urine_glucose = models.CharField(max_length=10, verbose_name='尿糖', blank=True, null=True)
    urine_ket = models.CharField(max_length=10, verbose_name='尿酮体', blank=True, null=True)
    urine_ery = models.CharField(max_length=10, verbose_name='尿潜血', blank=True, null=True)
    urine_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    # 血型
    blood_type_abo = models.CharField(max_length=10, verbose_name='血型ABO',
                                      choices=BLOOD_ABO_CHOICES, blank=True, null=True)
    blood_type_abo_other = models.CharField(max_length=30, verbose_name='血型其他', blank=True, null=True)
    blood_type_rh = models.CharField(max_length=10, verbose_name='血型Rh',
                                     choices=BLOOD_RH_CHOICES, blank=True, null=True)

    blood_glucose = models.FloatField(verbose_name='血糖', blank=True, null=True)
    # 肝功能
    # 谷丙转氨酶
    sgpt = models.FloatField(verbose_name='血清谷丙转氨酶', blank=True, null=True)
    # 谷草转氨酶
    sgot = models.FloatField(verbose_name='血清谷草转氨酶', blank=True, null=True)
    albumin = models.FloatField(verbose_name='白蛋白', blank=True, null=True)
    # 总胆红素
    tbil = models.FloatField(verbose_name='总胆红素', blank=True, null=True)
    dbil = models.FloatField(verbose_name='结合胆红素', blank=True, null=True)
    # 肾功能
    # 血清肌酐
    scr = models.FloatField(verbose_name='血清肌酐', blank=True, null=True)
    # 血尿素氮
    bun = models.FloatField(verbose_name='血尿素氮', blank=True, null=True)
    vaginal_secretion = models.CharField(max_length=20, verbose_name='阴道分泌物',
                                         choices=VAGINAL_SECRETION, blank=True, null=True)
    vaginal_secretion_other = models.CharField(max_length=20, verbose_name='阴道分泌物其他',
                                               blank=True, null=True)
    vaginal_clean_degree = models.CharField(max_length=20, verbose_name='阴道清洁度',
                                            choices=VAGINAL_CLEAN_DEGREE, blank=True, null=True)
    # 乙肝五项
    surface_antigen = models.CharField(max_length=10, verbose_name='乙型肝炎表面抗原',
                                       choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    surface_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎表面抗体',
                                        choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    e_antigen = models.CharField(max_length=10, verbose_name='乙型肝炎e抗原',
                                 choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    e_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎e抗体',
                                  choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    core_antibody = models.CharField(max_length=10, verbose_name='乙型肝炎核心抗体',
                                     choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)

    vdrl = models.CharField(max_length=10, verbose_name='梅毒血清试验',
                            choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    hiv_antibody = models.CharField(max_length=10, verbose_name='HIV抗体检测',
                                    choices=NEGATIVE_OR_POSITIVE, blank=True, null=True)
    b_scan = models.CharField(max_length=50, verbose_name='B超', blank=True, null=True)
    total_evaluation = models.CharField(max_length=20, verbose_name='总体评估指导',
                                        choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    total_evaluation_abnormal = models.CharField(max_length=100, verbose_name='总体评估指导异常',
                                                 blank=True, null=True)
    guide = models.ManyToManyField(Guide6Choices, verbose_name='保健指导', blank=True, null=True)
    guide_other = models.CharField(max_length=100, verbose_name='保健指导其他', blank=True, null=True)
    transfer = models.CharField(max_length=20, verbose_name='转诊', choices=TRANSFER_TREATMENT, blank=True, null=True)
    transfer_reason = models.CharField(max_length=50, verbose_name='转诊原因', blank=True, null=True)
    transfer_hospital = models.CharField(max_length=50, verbose_name='转诊机构及科室', blank=True, null=True)
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')


class GuideChoices(ChoicesAbstract):
    pass


class Guide1Choices(ChoicesAbstract):
    pass


class Guide2Choices(ChoicesAbstract):
    pass


class Guide3Choices(ChoicesAbstract):
    pass


class Guide4Choices(ChoicesAbstract):
    pass


class Aftercare(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期',)
    gestational_weeks = models.PositiveSmallIntegerField(verbose_name='孕周',)
    complaint = models.TextField(max_length=100, verbose_name='主诉',)
    weight = models.FloatField(verbose_name='体重',)
    examination_before_parturition_uteri_bottom_height = models.FloatField(verbose_name='宫底高度',)
    examination_before_parturition_abdomen_circumference = models.FloatField(verbose_name='腹围',)
    examination_before_parturition_fetus_position = models.CharField(max_length=50, verbose_name='胎位',)
    examination_before_parturition_fetal_heart_rate = models.FloatField(verbose_name='胎心率',)
    sbp = models.FloatField(verbose_name='收缩压')
    dbp = models.FloatField(verbose_name='舒张压')
    hemoglobin = models.FloatField(verbose_name='血红蛋白',)
    urine_protein = models.CharField(max_length=10, verbose_name='尿蛋白')
    extra_auxiliary_examination = models.TextField(max_length=1000, verbose_name='其他辅助检查*', blank=True, null=True,)
    classification = models.CharField(max_length=10, verbose_name='分类', choices=NORMAL_OR_ABNORMAL,)
    classification_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    guide_extra = models.CharField(max_length=30, verbose_name='', blank=True, null=True,)
    transfer_treatment = models.CharField(max_length=5, verbose_name='转诊', choices=TRANSFER_TREATMENT,)
    transfer_treatment_reason = models.CharField(max_length=100, verbose_name='原因', blank=True, null=True,)
    transfer_treatment_institution = models.CharField(max_length=100, verbose_name='机构及科室', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名', blank=True, null=True)
    guide = models.ManyToManyField(Guide2Choices, verbose_name='指导', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期', blank=True, null=True)

    class Meta:
        db_table = 'pregnant_aftercare'


class PostpartumRecordAbstract(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期',)
    general_health_situation = models.TextField(max_length=1000, verbose_name='一般健康情况')
    general_mentality_situation = models.TextField(max_length=1000, verbose_name='一般心理状况')
    sbp = models.FloatField(verbose_name='血压')
    dbp = models.FloatField(verbose_name='血压')
    breast = models.CharField(max_length=10, verbose_name='乳房', choices=NORMAL_OR_ABNORMAL,)
    breast_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    lochia = models.CharField(max_length=10, verbose_name='恶露', choices=NORMAL_OR_ABNORMAL,)
    lochia_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    uterus = models.CharField(max_length=10, verbose_name='子宫', choices=NORMAL_OR_ABNORMAL,)
    uterus_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    wound = models.CharField(max_length=10, verbose_name='伤口', choices=NORMAL_OR_ABNORMAL,)
    wound_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    extra = models.TextField(verbose_name='其他', blank=True, null=True)
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        abstract = True


class PostpartumVisit(PostpartumRecordAbstract):
    body_temperature = models.FloatField(verbose_name='体温')
    classification = models.CharField(max_length=10, verbose_name='分类', choices=NORMAL_OR_ABNORMAL,)
    classification_abnormal = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    guide = models.ManyToManyField(Guide3Choices, verbose_name='指导', blank=True, null=True,)
    guide_extra = models.CharField(max_length=30, verbose_name='', blank=True, null=True,)
    transfer_treatment = models.CharField(max_length=5, verbose_name='转诊', choices=TRANSFER_TREATMENT,)
    transfer_treatment_reason = models.CharField(max_length=100, verbose_name='原因', blank=True, null=True,)
    transfer_treatment_institution = models.CharField(max_length=100, verbose_name='机构及科室', blank=True, null=True,)
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期',)

    class Meta:
        db_table = 'pregnant_postpartum_visit'


class Postpartum42Exam(PostpartumRecordAbstract):
    classification = models.CharField(max_length=10, verbose_name='分类', choices=RECOVERY_OR_NOT,)
    classification_not_recovery = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    guide = models.ManyToManyField(Guide4Choices, verbose_name='指导', blank=True, null=True,)
    guide_extra = models.CharField(max_length=30, verbose_name='', blank=True, null=True,)
    dispose = models.CharField(max_length=5, verbose_name='处理', choices=DISPOSE,)
    dispose_transfer_treatment_reason = models.CharField(max_length=100, verbose_name='原因', blank=True, null=True,)
    dispose_transfer_treatment_institution = models.CharField(max_length=100, verbose_name='机构及科室', blank=True, null=True,)

    class Meta:
        db_table = 'pregnant_postpartum42_exam'
