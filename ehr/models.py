# -*- coding: utf-8 -*-
from django.db import models

from pregnant.models import ChoicesAbstract

GENDER = ((u'未知的性别', '未知的性别'), (u'男', '男'), (u'女', '女'), (u'未说明的性别', '未说明的性别'),)
RESIDENCE_TYPE = ((u'户籍', '户籍'), (u'非户籍', '非户籍'))
NATION_CHOICE = ((u'汉族', '汉族'), (u'少数民族', '少数民族'))
BLOOD_TYPE = ((u'A型', 'A型'), (u'B型', 'B型'), (u'O型', 'O型'), (u'AB型', 'AB型'), (u'不详', '不详'))
BLOOD_RH = ((u'否', '否'), (u'是', '是'), (u'不详', '不详'))
EDUCATION = ((u'文盲及半文盲', '文盲及半文盲'), (u'小学', '小学'), (u'初中', '初中'),
             (u'高中/技校/中专', '高中/技校/中专'), (u'大学专科及以上', '大学专科及以上'), (u'不详', '不详'))
OCCUPATION = ((u'国家机关、党群组织、企业、事业单位负责人', '国家机关、党群组织、企业、事业单位负责人'),
              (u'专业技术人员', '专业技术人员'), (u'办事人员和有关人员', '办事人员和有关人员'),
              (u'商业、服务业人员', '商业、服务业人员'), (u'农、林、牧、渔、水利业生产人员', '农、林、牧、渔、水利业生产人员'),
              (u'生产、运输设备操作人员及有关人员', '生产、运输设备操作人员及有关人员'),
              (u'军人', '军人'), (u'不便分类的其他从业人员', '不便分类的其他从业人员'))
MARRIAGE = ((u'未婚', '未婚'), (u'已婚', '已婚'), (u'丧偶', '丧偶'), (u'离婚', '离婚'),
            (u'未说明的婚姻状况', '未说明的婚姻状况'))
YES_NO = ((u'无', '无'), (u'有', '有'))
KITCHEN_FAN = ((u'无', '无'), (u'油烟机', '油烟机'), (u'换气扇', '换气扇'), (u'烟囱', '烟囱'))
FUEL_TYPE = ((u'液化气', '液化气'), (u'煤', '煤'), (u'天然气', '天然气'), (u'沼气', '沼气'),
             (u'柴火', '柴火'), (u'其他', '其他'))
WATER = ((u'自来水', '自来水'), (u'经净化过滤的水', '经净化过滤的水'), (u'井水', '井水'), (u'河湖水', '河湖水'),
         (u'塘水', '塘水'), (u'其他', '其他'))
TOILET = ((u'卫生厕所', '卫生厕所'), (u'一格或二格粪池式', '一格或二格粪池式'), (u'马桶', '马桶'),
          (u'露天粪坑', '露天粪坑'), (u'简易棚厕', '简易棚厕'))
LIVESTOCK_FENCE = ((u'单设', '单设'), (u'室内', '室内'), (u'室外', '室外'))


class PaymentWayChoices(ChoicesAbstract):
    pass


class AllergyHistoryYesChoices(ChoicesAbstract):
    pass


class ExposeHistoryYesChoices(ChoicesAbstract):
    pass


class DiseaseHistoryChoices(ChoicesAbstract):
    pass


class FamilyHistoryChoices(ChoicesAbstract):
    pass


class DisabilityChoices(ChoicesAbstract):
    pass


class PersonalInfo(models.Model):
    gender = models.CharField(max_length=30, verbose_name='性别', choices=GENDER)
    birthday = models.DateField(max_length=10, verbose_name='出生日期')
    identity = models.CharField(max_length=30, blank=True, null=True, verbose_name='身份证号')
    work_company = models.CharField(max_length=50, null=True, blank=True, verbose_name='工作单位')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='本人电话')
    contact_name = models.CharField(max_length=20, verbose_name='联系人姓名', blank=True, null=True)
    contact_phone = models.CharField(max_length=11, verbose_name='联系人电话', blank=True, null=True)
    residence_type = models.CharField(max_length=20, verbose_name='常住类型', choices=RESIDENCE_TYPE, blank=True, null=True)
    nation = models.CharField(max_length=20, verbose_name='民族', blank=True, null=True, choices=NATION_CHOICE)
    nation_extra = models.CharField(max_length=20, verbose_name='', blank=True, null=True)
    blood_type = models.CharField(max_length=10, verbose_name='血型', blank=True, null=True, choices=BLOOD_TYPE)
    blood_rh = models.CharField(max_length=10, verbose_name='RH阴性', blank=True, null=True, choices=BLOOD_RH)
    education = models.CharField(max_length=50, verbose_name='文化程度', blank=True, null=True, choices=EDUCATION)
    occupation = models.CharField(max_length=200, verbose_name='职业', blank=True, null=True, choices=OCCUPATION)
    marriage = models.CharField(max_length=100, verbose_name='婚姻状况', blank=True, null=True, choices=MARRIAGE)
    payment_way = models.ManyToManyField(PaymentWayChoices, verbose_name='医疗费用支付方式', blank=True, null=True)
    payment_way_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True)
    allergy_history = models.ManyToManyField(AllergyHistoryYesChoices, verbose_name='药物过敏史', blank=True, null=True)
    allergy_history_yes_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True)
    expose_history = models.ManyToManyField(ExposeHistoryYesChoices, verbose_name='暴露史', blank=True, null=True)

    disease_history = models.ManyToManyField(DiseaseHistoryChoices, verbose_name='疾病', blank=True, null=True)
    disease_history_cancer = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    disease_history_occupational = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    disease_history_extra = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    diagnose_date_2 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_3 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_4 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_5 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_6 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_7 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_8 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_9 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_10 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_11 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_12 = models.DateField(verbose_name='确诊时间', blank=True, null=True)
    diagnose_date_13 = models.DateField(verbose_name='确诊时间', blank=True, null=True)

    surgery_history = models.CharField(max_length=10, verbose_name='手术', blank=True, null=True, choices=YES_NO)
    surgery_1_name = models.CharField(max_length=20, verbose_name='名称1', blank=True, null=True)
    surgery_1_date = models.DateField(blank=True, null=True)
    surgery_2_name = models.CharField(max_length=20, verbose_name='名称2', blank=True, null=True)
    surgery_2_date = models.DateField(blank=True, null=True)

    injury_history = models.CharField(max_length=10, verbose_name='外伤', choices=YES_NO, blank=True, null=True)
    injury_1_name = models.CharField(max_length=20, verbose_name='名称1', blank=True, null=True)
    injury_1_date = models.DateField(blank=True, null=True)
    injury_2_name = models.CharField(max_length=20, verbose_name='名称2', blank=True, null=True)
    injury_2_date = models.DateField(blank=True, null=True)

    transfusion_history = models.CharField(max_length=10, blank=True, null=True, verbose_name='输血', choices=YES_NO)
    transfusion_1_reason = models.CharField(max_length=20, verbose_name='原因1', blank=True, null=True)
    transfusion_1_date = models.DateField(blank=True, null=True)
    transfusion_2_reason = models.CharField(max_length=20, verbose_name='原因2', blank=True, null=True)
    transfusion_2_date = models.DateField(blank=True, null=True)

    family_history_father = models.ManyToManyField(FamilyHistoryChoices, blank=True, null=True,
                                                   related_name='father_disease')
    family_history_father_extra = models.CharField(max_length=30, blank=True, null=True)
    family_history_mother = models.ManyToManyField(FamilyHistoryChoices, blank=True, null=True,
                                                   related_name='mother_disease')
    family_history_mother_extra = models.CharField(max_length=30, blank=True, null=True)
    family_history_sibling = models.ManyToManyField(FamilyHistoryChoices, blank=True, null=True,
                                                    related_name='sibling_disease')
    family_history_sibling_extra = models.CharField(max_length=30, blank=True, null=True)
    family_history_children = models.ManyToManyField(FamilyHistoryChoices, blank=True, null=True,
                                                     related_name='children_disease')
    family_history_children_extra = models.CharField(max_length=30, blank=True, null=True)

    genetic_disease = models.CharField(max_length=10, blank=True, null=True, verbose_name='遗传病史', choices=YES_NO)
    genetic_disease_yes = models.CharField(max_length=100, verbose_name='疾病名称', blank=True, null=True)
    disability = models.ManyToManyField(DisabilityChoices, verbose_name='残疾情况', blank=True, null=True)
    disability_extra = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    surroundings_kitchen_exhaust = models.CharField(max_length=20, verbose_name='厨房排风设备',
                                                    blank=True, null=True, choices=KITCHEN_FAN)
    surroundings_fuel_type = models.CharField(max_length=20, verbose_name='燃料类型',
                                              blank=True, null=True, choices=FUEL_TYPE)
    surroundings_water = models.CharField(max_length=50, verbose_name='饮水', blank=True, null=True, choices=WATER)
    surroundings_toilet = models.CharField(max_length=50, verbose_name='厕所', blank=True, null=True, choices=TOILET)
    surrounding_livestock_fence = models.CharField(max_length=20, verbose_name='禽畜栏',
                                                   blank=True, null=True, choices=LIVESTOCK_FENCE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'ehr_personal_info'


class SymptomChoice(ChoicesAbstract):
    pass


MOUTH_LIP_CHOICES = ((u'红润', '红润'), (u'苍白', '苍白'), (u'发绀', '发绀'), (u'皲裂', '皲裂'), (u'疱疹', '疱疹'))
MOUTH_TOOTH_CHOICES = ((u'正常', '正常'), (u'缺齿', '缺齿'), (u'龋齿', '龋齿'), (u'义齿（假牙）', '义齿（假牙）'))
MOUTH_THROAT_CHOICES = ((u'无充血', '无充血'), (u'充血', '充血'), (u'淋巴滤泡增生', '淋巴滤泡增生'))
HEARING_CHOICES = ((u'听见', '听见'), (u'听不清或无法听见', '听不清或无法听见'))
MOVEMENT_FUNCTION_CHOICES = ((u'可顺利完成', '可顺利完成'), (u'无法独立完成其中任何一个动作', '无法独立完成其中任何一个动作'))
SKIN_CHOICES = ((u'正常', '正常'), (u'潮红', '潮红'), (u'苍白', '苍白'), (u'发绀', '发绀'), (u'黄染', '黄染'),
                (u'色素沉着', '色素沉着'), (u'其他', '其他'))
LYMPH_NODE_CHOICES = ((u'未触及', '未触及'), (u'锁骨上', '锁骨上'), (u'腋窝', '腋窝'), (u'其他', '其他'))
NO_YES_CHOICES = ((u'否', '否'), (u'是', '是'))
LUNG_RALE_CHOICES = ((u'否', '否'), (u'干罗音', '干罗音'), (u'湿罗音', '湿罗音'), (u'其他', '其他'))
NOTHING_OR_NOT_CHOICES = ((u'无', '无'), (u'有', '有'))
HEART_RHYTHM = ((u'齐', u'齐'), (u'不齐', u'不齐'), (u'绝对不齐', u'绝对不齐'))


# 一般体格检查
class PhysicalExamination(models.Model):
    body_temperature = models.FloatField(verbose_name='体温')
    pulse = models.PositiveSmallIntegerField(verbose_name='脉率')
    breath_frequency = models.PositiveSmallIntegerField(verbose_name='呼吸频率')
    blood_pressure_left_sbp = models.FloatField(verbose_name='左侧收缩压')
    blood_pressure_left_dbp = models.FloatField(verbose_name='左侧舒张压')
    blood_pressure_right_sbp = models.FloatField(verbose_name='右侧收缩压')
    blood_pressure_right_dbp = models.FloatField(verbose_name='右侧舒张压')
    height = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
    waistline = models.FloatField(verbose_name='腰围')
    body_mass_index = models.FloatField(verbose_name='体质指数')
    mouth_lip = models.CharField(verbose_name='口唇',
                                 max_length=10, choices=MOUTH_LIP_CHOICES)
    mouth_tooth = models.CharField(verbose_name='齿列',
                                   max_length=10, choices=MOUTH_TOOTH_CHOICES)
    mouth_tooth_missing_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_throat = models.CharField(verbose_name='咽部', max_length=10, choices=MOUTH_THROAT_CHOICES)
    eyesight_left = models.FloatField(verbose_name='左眼')
    eyesight_right = models.FloatField(verbose_name='右眼')
    eyesight_left_rectified = models.FloatField(verbose_name='矫正视力左眼', blank=True, null=True)
    eyesight_right_rectified = models.FloatField(verbose_name='矫正视力右眼', blank=True, null=True)
    hearing = models.CharField(verbose_name='听力', max_length=60, choices=HEARING_CHOICES)
    movement_function = models.CharField(verbose_name='运动功能', max_length=100, choices=MOVEMENT_FUNCTION_CHOICES)
    skin = models.CharField(verbose_name='皮肤', max_length=20, choices=SKIN_CHOICES)
    skin_extra = models.CharField(max_length=100, blank=True, null=True)
    lymph_node = models.CharField(verbose_name='淋巴结', max_length=20, choices=LYMPH_NODE_CHOICES)
    lymph_node_extra = models.CharField(max_length=100, blank=True, null=True)
    lung_barrel_chested = models.CharField(verbose_name='桶状胸', max_length=10, choices=NO_YES_CHOICES)
    lung_breath_sound = models.CharField(verbose_name='呼吸音', max_length=10, choices=NO_YES_CHOICES)
    lung_breath_sound_extra = models.CharField(max_length=100, blank=True, null=True)
    lung_rale = models.CharField(verbose_name='罗音', max_length=10, choices=LUNG_RALE_CHOICES)
    lung_rale_extra = models.CharField(max_length=100, blank=True, null=True)
    heart_rate = models.IntegerField(verbose_name='心率')
    heart_rhythm = models.CharField(verbose_name='心律', max_length=10, choices=HEART_RHYTHM)
    heart_noise = models.CharField(verbose_name='杂音', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    heart_noise_extra = models.CharField(max_length=100, blank=True, null=True)
    stomach_tenderness = models.CharField(verbose_name='压痛', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    stomach_tenderness_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_enclosed_mass = models.CharField(verbose_name='包块', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    stomach_enclosed_mass_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_hepatomegaly = models.CharField(verbose_name='肝大', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    stomach_hepatomegaly_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_slenauxe = models.CharField(verbose_name='脾大', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    stomach_slenauxe_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_shifting_dullness = models.CharField(verbose_name='移动性浊音', max_length=10, choices=NOTHING_OR_NOT_CHOICES)
    stomach_shifting_dullness_extra = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        #db_table = 'body_physical_examination'
        abstract = True


# 血常规
class BloodRoutineTest(models.Model):
    hemoglobin = models.FloatField(verbose_name='血红蛋白')
    leucocyte = models.FloatField(verbose_name='白细胞')
    blood_platelets = models.FloatField(verbose_name='血小板')
    blood_routine_test_extra = models.CharField(max_length=20, blank=True, null=True, verbose_name='其他',)

    class Meta:
        #db_table = 'body_blood_routine_test'
        abstract = True


# 尿常规
class UrineRoutineTest(models.Model):
    urine_protein = models.CharField(max_length=10, verbose_name='尿蛋白')
    urine_glucose = models.CharField(max_length=10, verbose_name='尿糖')
    ketone_bodies = models.CharField(max_length=10, verbose_name='尿酮体')
    occult_blood = models.CharField(max_length=10, verbose_name='尿潜血')
    routine_urine_test_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    class Meta:
        #db_table = 'body_urine_routine_test'
        abstract = True


# 血糖
class BloodGlucose(models.Model):
    blood_glucose_mmol = models.FloatField(blank=True, null=True)
    blood_glucose_mg = models.FloatField(blank=True, null=True)

    class Meta:
        #db_table = 'body_blood_glucose'
        abstract = True

NORMAL_OR_ABNORMAL = ((u'正常', '正常'), (u'异常', '异常'),)


# 心电图
class Electrocardiogram(models.Model):
    electr_gram = models.CharField(max_length=10, verbose_name='', choices=NORMAL_OR_ABNORMAL)
    electr_gram_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    class Meta:
        #db_table = 'body_electrocardiogram'
        abstract = True


# 血清谷丙转氨酶
class AlanineAminotransferase(models.Model):
    alt = models.FloatField(verbose_name='血清谷丙转氨酶')

    class Meta:
        #db_table = 'body_alanine_aminotransferase'
        abstract = True


# 血清谷草转氨酶
class GlutamicOxalaceticTransaminase(models.Model):
    ast = models.FloatField(verbose_name='血清谷草转氨酶')

    class Meta:
        #db_table = 'body_glutamic_oxalacetic_transaminase'
        abstract = True


# 血清肌酐
class SerumCreatinine(models.Model):
    scr = models.FloatField(verbose_name='血清肌酐')

    class Meta:
        #db_table = 'body_serum_creatinine'
        abstract = True


# 血尿素氮
class BloodUreaNitrogen(models.Model):
    bun = models.FloatField(verbose_name='血尿素氮')

    class Meta:
        abstract = True
        #db_table = 'body_blood_urea_nitrogen'


# 总胆红素
class TotalBilirubin(models.Model):
    tbil = models.FloatField(verbose_name='总胆红素')

    class Meta:
        abstract = True
        #db_table = 'body_total_bilirubin'


# 血脂
class BloodFat(models.Model):
    tc = models.FloatField(verbose_name='总胆固醇')  # Total Cholesterol
    tg = models.FloatField(verbose_name='甘油三脂')  # Triglycerides
    ldl_c = models.FloatField(verbose_name='血清低密度脂蛋白胆固醇')
    hdl_c = models.FloatField(verbose_name='血清高密度脂蛋白胆固醇')

    class Meta:
        #db_table = 'body_blood_fat'
        abstract = True


MOST = ((u'是', '是'), (u'基本是', '基本是'),)
TEND = ((u'是', '是'), (u'倾向是', '倾向是'),)


# 彩超
class BUltrasonic(models.Model):
    b_ultrasonic = models.CharField(max_length=200, verbose_name='彩超')

    class Meta:
        abstract = True


# 中医体质辨识
class ConstitutionIdentification(models.Model):
    pinghe = models.CharField(max_length=15, verbose_name='平和质', choices=MOST)
    qixu = models.CharField(max_length=15, verbose_name='气虚质', choices=TEND)
    yangxu = models.CharField(max_length=15, verbose_name='阳虚质', choices=TEND)
    yinxu = models.CharField(max_length=15, verbose_name='阴虚质', choices=TEND)
    tanshi = models.CharField(max_length=15, verbose_name='痰湿质', choices=TEND)
    shire = models.CharField(max_length=15, verbose_name='湿热质', choices=TEND)
    xueyu = models.CharField(max_length=15, verbose_name='血瘀质', choices=TEND)
    qiyu = models.CharField(max_length=15, verbose_name='气郁质', choices=TEND)
    tebing = models.CharField(max_length=15, verbose_name='特禀质', choices=TEND)

    class Meta:
        #db_table = 'body_constitution_identification'
        abstract = True


class BodyExam(models.Model):
    visit_date = models.DateField(verbose_name='体检日期', blank=True, null=True)
    doctor = models.CharField(max_length=10, verbose_name='责任医生', blank=True, null=True)

    # 一般体格检查
    body_temperature = models.FloatField(verbose_name='体温', blank=True, null=True)
    pulse = models.PositiveSmallIntegerField(verbose_name='脉率', blank=True, null=True)
    breath_frequency = models.PositiveSmallIntegerField(verbose_name='呼吸频率', blank=True, null=True)
    blood_pressure_left_sbp = models.FloatField(verbose_name='左侧收缩压', blank=True, null=True)
    blood_pressure_left_dbp = models.FloatField(verbose_name='左侧舒张压', blank=True, null=True)
    blood_pressure_right_sbp = models.FloatField(verbose_name='右侧收缩压', blank=True, null=True)
    blood_pressure_right_dbp = models.FloatField(verbose_name='右侧舒张压', blank=True, null=True)
    height = models.FloatField(verbose_name='身高', blank=True, null=True)
    weight = models.FloatField(verbose_name='体重', blank=True, null=True)
    waistline = models.FloatField(verbose_name='腰围', blank=True, null=True)
    body_mass_index = models.FloatField(verbose_name='体质指数', blank=True, null=True)
    mouth_lip = models.CharField(verbose_name='口唇',
                                 max_length=10, choices=MOUTH_LIP_CHOICES, blank=True, null=True)
    mouth_tooth = models.CharField(verbose_name='齿列',
                                   max_length=10, choices=MOUTH_TOOTH_CHOICES, blank=True, null=True)
    mouth_tooth_missing_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_missing_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_decayed_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_upleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_bottomleft = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_upright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_tooth_denture_bottomright = models.CharField(max_length=10, verbose_name='', blank=True, null=True,)
    mouth_throat = models.CharField(verbose_name='咽部', max_length=10,
                                    choices=MOUTH_THROAT_CHOICES, blank=True, null=True)
    eyesight_left = models.FloatField(verbose_name='左眼', blank=True, null=True)
    eyesight_right = models.FloatField(verbose_name='右眼', blank=True, null=True)
    eyesight_left_rectified = models.FloatField(verbose_name='矫正视力左眼', blank=True, null=True)
    eyesight_right_rectified = models.FloatField(verbose_name='矫正视力右眼', blank=True, null=True)
    hearing = models.CharField(verbose_name='听力', max_length=60,
                               choices=HEARING_CHOICES, blank=True, null=True)
    movement_function = models.CharField(verbose_name='运动功能', max_length=100,
                                         choices=MOVEMENT_FUNCTION_CHOICES, blank=True, null=True)
    skin = models.CharField(verbose_name='皮肤', max_length=20, choices=SKIN_CHOICES, blank=True, null=True)
    skin_extra = models.CharField(max_length=100, blank=True, null=True)
    lymph_node = models.CharField(verbose_name='淋巴结', max_length=20,
                                  choices=LYMPH_NODE_CHOICES, blank=True, null=True)
    lymph_node_extra = models.CharField(max_length=100, blank=True, null=True)
    lung_barrel_chested = models.CharField(verbose_name='桶状胸', max_length=10,
                                           choices=NO_YES_CHOICES, blank=True, null=True)
    lung_breath_sound = models.CharField(verbose_name='呼吸音', max_length=10,
                                         choices=NO_YES_CHOICES, blank=True, null=True)
    lung_breath_sound_extra = models.CharField(max_length=100, blank=True, null=True)
    lung_rale = models.CharField(verbose_name='罗音', max_length=10,
                                 choices=LUNG_RALE_CHOICES, blank=True, null=True)
    lung_rale_extra = models.CharField(max_length=100, blank=True, null=True)
    heart_rate = models.IntegerField(verbose_name='心率', blank=True, null=True)
    heart_rhythm = models.CharField(verbose_name='心律', max_length=10,
                                    choices=HEART_RHYTHM, blank=True, null=True)
    heart_noise = models.CharField(verbose_name='杂音', max_length=10,
                                   choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    heart_noise_extra = models.CharField(max_length=100, blank=True, null=True)
    stomach_tenderness = models.CharField(verbose_name='压痛', max_length=10,
                                          choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    stomach_tenderness_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_enclosed_mass = models.CharField(verbose_name='包块', max_length=10,
                                             choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    stomach_enclosed_mass_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_hepatomegaly = models.CharField(verbose_name='肝大', max_length=10,
                                            choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    stomach_hepatomegaly_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_slenauxe = models.CharField(verbose_name='脾大', max_length=10,
                                        choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    stomach_slenauxe_extra = models.CharField(max_length=100, null=True, blank=True)
    stomach_shifting_dullness = models.CharField(verbose_name='移动性浊音',
                                                 max_length=10, choices=NOTHING_OR_NOT_CHOICES, blank=True, null=True)
    stomach_shifting_dullness_extra = models.CharField(max_length=100, null=True, blank=True)

    # 血常规（老年人、精神病）
    hemoglobin = models.FloatField(verbose_name='血红蛋白', blank=True, null=True)
    leucocyte = models.FloatField(verbose_name='白细胞', blank=True, null=True)
    blood_platelets = models.FloatField(verbose_name='血小板', blank=True, null=True)
    blood_routine_test_extra = models.CharField(max_length=20, blank=True, null=True, verbose_name='其他',)

    # 尿常规（老年人）
    urine_protein = models.CharField(max_length=10, verbose_name='尿蛋白', blank=True, null=True)
    urine_glucose = models.CharField(max_length=10, verbose_name='尿糖', blank=True, null=True)
    ketone_bodies = models.CharField(max_length=10, verbose_name='尿酮体', blank=True, null=True)
    occult_blood = models.CharField(max_length=10, verbose_name='尿潜血', blank=True, null=True)
    routine_urine_test_extra = models.CharField(max_length=20, verbose_name='其他', blank=True, null=True)

    # 血糖（老年人、精神病）
    blood_glucose_mmol = models.FloatField(blank=True, null=True)
    blood_glucose_mg = models.FloatField(blank=True, null=True)

    # 心电图（老年人、精神病）
    electr_gram = models.CharField(max_length=10, verbose_name='', choices=NORMAL_OR_ABNORMAL, blank=True, null=True)
    electr_gram_abnormal = models.CharField(max_length=50, verbose_name='', blank=True, null=True)

    # 谷丙转氨酶（老年人、精神病）
    alt = models.FloatField(verbose_name='血清谷丙转氨酶', blank=True, null=True)

    # 谷草转氨酶（老年人、精神病）
    ast = models.FloatField(verbose_name='血清谷草转氨酶', blank=True, null=True)

    # 总胆红素（老年人）
    tbil = models.FloatField(verbose_name='总胆红素', blank=True, null=True)

    # 血清肌酐（老年人）
    scr = models.FloatField(verbose_name='血清肌酐', blank=True, null=True)

    # 血尿素氮（老年人）
    bun = models.FloatField(verbose_name='血尿素氮', blank=True, null=True)

    # 血脂（老年人）
    tc = models.FloatField(verbose_name='总胆固醇', blank=True, null=True)
    tg = models.FloatField(verbose_name='甘油三脂', blank=True, null=True)
    ldl_c = models.FloatField(verbose_name='血清低密度脂蛋白胆固醇', blank=True, null=True)
    hdl_c = models.FloatField(verbose_name='血清高密度脂蛋白胆固醇', blank=True, null=True)

    # 彩超
    b_ultrasonic = models.CharField(max_length=200, verbose_name='彩超', blank=True, null=True)

    # 中医体质辨识（中医药）
    pinghe = models.CharField(max_length=15, verbose_name='平和质', choices=MOST, blank=True, null=True)
    qixu = models.CharField(max_length=15, verbose_name='气虚质', choices=TEND, blank=True, null=True)
    yangxu = models.CharField(max_length=15, verbose_name='阳虚质', choices=TEND, blank=True, null=True)
    yinxu = models.CharField(max_length=15, verbose_name='阴虚质', choices=TEND, blank=True, null=True)
    tanshi = models.CharField(max_length=15, verbose_name='痰湿质', choices=TEND, blank=True, null=True)
    shire = models.CharField(max_length=15, verbose_name='湿热质', choices=TEND, blank=True, null=True)
    xueyu = models.CharField(max_length=15, verbose_name='血瘀质', choices=TEND, blank=True, null=True)
    qiyu = models.CharField(max_length=15, verbose_name='气郁质', choices=TEND, blank=True, null=True)
    tebing = models.CharField(max_length=15, verbose_name='特禀质', choices=TEND, blank=True, null=True)