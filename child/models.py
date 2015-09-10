# coding=utf-8
from django.db import models

# Create your models here.
from pregnant.models import ChoicesAbstract

GENDER = ((u'未知的性别', '未知的性别'), (u'男', '男'), (u'女', '女'), (u'未说明性别', '未说明性别'))
MOTHER_GESTATIONAL_DISEASE = ((u'糖尿病', '糖尿病'), (u'妊娠期高血压', '妊娠期高血压'), (u'其他', '其他'))
BIRTH_SITUATION = ((u'顺产', '顺产'), (u'抬头吸引', '抬头吸引'), (u'产钳', '产钳'),
                   (u'剖宫', '剖宫'), (u'双多胎', '双多胎'), (u'臀位', '臀位'), (u'其他', '其他'))
YES_OR_NO = ((u'无', '无'), (u'有', '有'))
NEWBORN_ASPHYXIA_YES = ((u'轻', '轻'), (u'中', '中'), (u'重', '重'))
APGAR_SCORE = ((u'1分钟', '1分钟'), (u'5分钟', '5分钟'), (u'不详', '不详'))
FEED_WAY = ((u'纯母乳', '纯母乳'), (u'混合', '混合'), (u'人工', '人工'))
VACCINATE_YES_OR_NO = ((u'已种', '已种'), (u'未种', '未种'))
PASS_NO_NOT = ((u'通过', '通过'), (u'未通过', '未通过'), (u'未筛查', '未筛查'))

GRADE = ((u'上', '上'), (u'中', '中'), (u'下', '下'))
COMPLEXION = ((u'红润', '红润'), (u'黄染', '黄染'), (u'其他', '其他'))
NORMAL_OR_ABNORMAL = ((u'未见异常', '未见异常'), (u'异常', '异常'))
BREGMA = ((u'闭合', '闭合'), (u'未闭', '未闭'))
NECK_ENCLOSED_MASS = ((u'有', '有'), (u'无', '无'))
NAVEL = ((u'未脱落', '未脱落'), (u'脱落', '脱落'), (u'脐部有渗出', '脐部有渗出'), (u'其他', '其他'))
RICKETS_SIGN = ((u'无', '无'), (u'颅骨软化', '颅骨软化'), (u'方颅', '方颅'), (u'枕秃', '枕秃'))
GROWTH_EVALUATE = ((u'通过', '通过'), (u'未过', '未过'))
TWO_VISIT_DISEASE = ((u'未患病', '未患病'), (u'患病', '患病'))
TRANSFER_TREATMENT_SUGGESTION = ((u'无', '无'), (u'有', '有'))
GUIDE = ((u'科学喂养', '科学喂养'), (u'生长发育', '生长发育'), (u'疾病预防', '疾病预防'),
         (u'预防意外伤害', '预防意外伤害'), (u'口腔保健', '口腔保健'))

NEWBORN_HEARING_SCREENING = ((u'通过', '通过'), (u'未通过', '未通过'), (u'未筛查', '未筛查'), (u'不详', '不详'))
NEWBORN_DISEASE_SCREENING = ((u'甲低', '甲低'), (u'苯丙酮尿症', '苯丙酮尿症'), (u'其他遗传代谢病', '其他遗传代谢病'))
SHIT = ((u'糊状', '糊状'), (u'稀', '稀'))
ICTERUS_POSITION = ((u'面部', '面部'), (u'躯干', '躯干'), (u'四肢', '四肢'), (u'手足', '手足'))
BREGMA_1 = ((u'正常', '正常'), (u'膨隆', '膨隆'), (u'凹陷', '凹陷'), (u'其他', '其他'))
NECK_ENCLOSED_MASS = ((u'无', '无'), (u'有', '有'))
SKIN = ((u'未见异常', '未见异常'), (u'湿疹', '湿疹'), (u'糜烂', '糜烂'), (u'其他', '其他'))
GUIDE_3 = ((u'喂养指导', '喂养指导'), (u'发育指导', '发育指导'), (u'防病指导', '防病指导'),
           (u'预防伤害指导', '预防伤害指导'), (u'口腔保健指导', '口腔保健指导'))


class Guide3Choices(ChoicesAbstract):
    pass


class GuideChoices(ChoicesAbstract):
    pass


class BirthSituationChoices(ChoicesAbstract):
    pass


class HealthManual(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='建册日期')
    gender = models.CharField(max_length=30, verbose_name='性别', choices=GENDER)
    birth_date = models.DateField(max_length=10, verbose_name='出生日期')
    id_number = models.CharField(max_length=18, verbose_name='身份证号')
    home_address = models.CharField(max_length=300, verbose_name='家庭住址')
    father_name = models.CharField(max_length=15, verbose_name='姓名')
    father_occupation = models.CharField(max_length=15, verbose_name='职业')
    father_contact_number = models.CharField(max_length=11, verbose_name='联系电话')
    father_birth_date = models.DateField(max_length=10, verbose_name='出生日期')
    mother_name = models.CharField(max_length=15, verbose_name='姓名')
    mother_occupation = models.CharField(max_length=15, verbose_name='职业')
    mother_contact_number = models.CharField(max_length=11, verbose_name='联系电话')
    mother_birth_date = models.DateField(max_length=10, verbose_name='出生日期')
    gestational_weeks = models.PositiveSmallIntegerField(verbose_name='出生孕周')
    mother_gestational_disease = models.CharField(max_length=20, verbose_name='母亲妊娠期患病情况',
                                                  choices=MOTHER_GESTATIONAL_DISEASE)
    mother_gestational_disease_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True)
    deliver_institution = models.CharField(max_length=100, verbose_name='助产机构名称')
    birth_situation = models.ManyToManyField(BirthSituationChoices, verbose_name='出生情况', blank=True, null=True)
    birth_situation_extra = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    newborn_asphyxia = models.CharField(max_length=5, verbose_name='新生儿窒息', choices=YES_OR_NO)
    #newborn_asphyxia_yes = models.CharField(max_length=5, verbose_name='', choices=NEWBORN_ASPHYXIA_YES, blank=True, null=True)
    newborn_asphyxia_yes = models.CharField(max_length=5, choices=NEWBORN_ASPHYXIA_YES, blank=True, null=True)
    apgan_score = models.CharField(max_length=10, verbose_name='Apgar评分', choices=APGAR_SCORE)
    birth_malformation = models.CharField(max_length=5, verbose_name='出生畸形', choices=YES_OR_NO)
    birth_malformation_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True)
    newborn_birth_weight = models.FloatField(verbose_name='新生儿出生体重')
    birth_height = models.FloatField(verbose_name='出生身长')
    feed_way = models.CharField(max_length=15, verbose_name='喂养方式', choices=FEED_WAY)
    drink_milk_volume = models.FloatField(verbose_name='*吃奶量', blank=True, null=True)
    drink_milk_times = models.PositiveSmallIntegerField(verbose_name='*吃奶次数', blank=True, null=True)
    emesis = models.CharField(max_length=5, verbose_name='*呕吐', choices=YES_OR_NO, blank=True, null=True)
    shit_times = models.PositiveSmallIntegerField(verbose_name='*大便次数', blank=True, null=True)
    kajiemiao_vaccinate = models.CharField(max_length=10, verbose_name='卡介苗接种', choices=VACCINATE_YES_OR_NO)
    yigan_vaccinate = models.CharField(max_length=10, verbose_name='乙肝疫苗接种', choices=VACCINATE_YES_OR_NO)
    newborn_hearing_screening = models.CharField(max_length=15, verbose_name='新生儿听力筛查', choices=PASS_NO_NOT)
    pku_screening = models.CharField(max_length=15, verbose_name='苯丙酮尿症筛查', choices=PASS_NO_NOT)
    thyroid_screening = models.CharField(max_length=15, verbose_name='先天性甲状腺功能低下筛查', choices=PASS_NO_NOT)
    extra_disease_screening = models.CharField(max_length=100, verbose_name='其他疾病筛查')
    extra_disease_screening_pass = models.CharField(max_length=15, verbose_name='', choices=PASS_NO_NOT)

    class Meta:
        db_table = 'child_health_manual'


class NewbornFamilyVisit(models.Model):
    visit_date = models.DateField(max_length=10,  verbose_name='随访日期')
    gender = models.CharField(max_length=30,  verbose_name='性别',  choices=GENDER)
    birthday = models.DateField(max_length=10,  verbose_name='出生日期')
    identity = models.CharField(max_length=18,  verbose_name='身份证号', blank=True, null=True)
    address = models.CharField(max_length=300,  verbose_name='家庭住址')
    father_name = models.CharField(max_length=15,  verbose_name='姓名')
    father_occupation = models.CharField(max_length=15,  verbose_name='职业')
    father_contact_number = models.CharField(max_length=11,  verbose_name='联系电话')
    father_birthday = models.DateField(max_length=10,  verbose_name='出生日期')
    mother_name = models.CharField(max_length=15,  verbose_name='姓名')
    mother_occupation = models.CharField(max_length=15,  verbose_name='职业')
    mother_contact_number = models.CharField(max_length=11,  verbose_name='联系电话')
    mother_birthday = models.DateField(max_length=10,  verbose_name='出生日期')
    gestational_weeks = models.PositiveSmallIntegerField(verbose_name='出生孕周')
    mother_gestational_disease = models.CharField(max_length=20,  verbose_name='母亲妊娠期患病情况',
                                                  choices=MOTHER_GESTATIONAL_DISEASE, blank=True, null=True)
    mother_gestational_disease_extra = models.CharField(max_length=100,  verbose_name='', blank=True, null=True)
    deliver_institution = models.CharField(max_length=100,  verbose_name='助产机构名称')
    birth_situation = models.ManyToManyField(BirthSituationChoices, verbose_name='出生情况', blank=True, null=True)
    birth_situation_extra = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    newborn_asphyxia = models.CharField(max_length=5,  verbose_name='新生儿窒息',  choices=YES_OR_NO)
    apgar_score = models.CharField(max_length=10,  verbose_name='Apgar评分',  choices=APGAR_SCORE, blank=True, null=True)
    malformation_or_not = models.CharField(max_length=5,  verbose_name='是否有畸形',  choices=YES_OR_NO)
    malformation_extra = models.CharField(max_length=100,  verbose_name='', blank=True, null=True)
    newborn_hearing_screening = models.CharField(max_length=15,  verbose_name='新生儿听力筛查',
                                                 choices=NEWBORN_HEARING_SCREENING)
    newborn_disease_screening = models.CharField(max_length=15,  verbose_name='新生儿疾病筛查',
                                                 choices=NEWBORN_DISEASE_SCREENING, blank=True, null=True)
    newborn_disease_screening_extra = models.CharField(max_length=100,  verbose_name='', blank=True, null=True)
    newborn_birth_weight = models.FloatField(verbose_name='新生儿出生体重')
    now_weight = models.FloatField(verbose_name='目前体重')
    birth_height = models.FloatField(verbose_name='出生身长')
    feed_way = models.CharField(max_length=15,  verbose_name='喂养方式',  choices=FEED_WAY)
    drink_milk_volume = models.FloatField(verbose_name='*吃奶量', blank=True, null=True)
    drink_milk_times = models.PositiveSmallIntegerField(verbose_name='*吃奶次数', blank=True, null=True)
    emesis = models.CharField(max_length=5,  verbose_name='*呕吐',  choices=YES_OR_NO, blank=True, null=True)
    shit = models.CharField(max_length=10,  verbose_name='*大便',  choices=SHIT, blank=True, null=True)
    shit_times = models.PositiveSmallIntegerField(verbose_name='*大便次数', blank=True, null=True)
    body_temperature = models.FloatField(verbose_name='体温')
    pulse = models.PositiveSmallIntegerField(verbose_name='脉率')
    breath_frequency = models.PositiveSmallIntegerField(verbose_name='呼吸频率')
    complexion = models.CharField(max_length=10,  verbose_name='面色',  choices=COMPLEXION)
    complexion_extra = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    icterus_position = models.CharField(max_length=10,  verbose_name='黄疸部位',  choices=ICTERUS_POSITION)
    bregma_x = models.FloatField(verbose_name='前囟')
    bregma_y = models.FloatField(verbose_name='')
    bregma_1 = models.CharField(max_length=10,  verbose_name='',  choices=BREGMA_1)
    bregma_1_extra = models.CharField(max_length=20,  verbose_name='', blank=True, null=True)
    eye_appearance = models.CharField(max_length=20,  verbose_name='眼外观',  choices=NORMAL_OR_ABNORMAL)
    eye_appearance_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    ear_appearance = models.CharField(max_length=20,  verbose_name='耳外观',  choices=NORMAL_OR_ABNORMAL)
    ear_appearance_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    nose = models.CharField(max_length=20,  verbose_name='鼻',  choices=NORMAL_OR_ABNORMAL)
    nose_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    oral_cavity = models.CharField(max_length=20,  verbose_name='口腔',  choices=NORMAL_OR_ABNORMAL)
    oral_cavity_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    heart_lung_auscultation = models.CharField(max_length=20,  verbose_name='心肺听诊',  choices=NORMAL_OR_ABNORMAL)
    heart_lung_auscultation_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    abdomen_palpation = models.CharField(max_length=20,  verbose_name='腹部触诊',  choices=NORMAL_OR_ABNORMAL)
    abdomen_palpation_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    all_fours_activity = models.CharField(max_length=20,  verbose_name='四肢活动度',  choices=NORMAL_OR_ABNORMAL)
    all_fours_activity_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    neck_enclosed_mass = models.CharField(max_length=5,  verbose_name='颈部包块',  choices=NECK_ENCLOSED_MASS)
    neck_enclosed_mass_yes = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    skin = models.CharField(max_length=20,  verbose_name='皮肤',  choices=SKIN)
    skin_extra = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    anus = models.CharField(max_length=20,  verbose_name='肛门',  choices=NORMAL_OR_ABNORMAL)
    anus_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    externalia = models.CharField(max_length=20,  verbose_name='外生殖器',  choices=NORMAL_OR_ABNORMAL)
    externalia_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    spine = models.CharField(max_length=20,  verbose_name='脊柱',  choices=NORMAL_OR_ABNORMAL)
    spine_abnormal = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    navel = models.CharField(max_length=30,  verbose_name='脐部',  choices=NAVEL)
    navel_extra = models.CharField(max_length=50,  verbose_name='', blank=True, null=True)
    transfer_treatment_suggestion = models.CharField(max_length=5,  verbose_name='转诊建议',
                                                     choices=TRANSFER_TREATMENT_SUGGESTION)
    transfer_treatment_suggestion_reason = models.CharField(max_length=100,  verbose_name='原因', blank=True, null=True)
    transfer_treatment_suggestion_institution = models.CharField(max_length=100,  verbose_name='机构及科室', blank=True, null=True)
    guide = models.ManyToManyField(Guide3Choices,  verbose_name='指导', blank=True, null=True)
    next_visit_date = models.DateField(max_length=10,  verbose_name='下次随访日期')
    next_visit_place = models.CharField(max_length=30,  verbose_name='下次随访地点')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        db_table = 'child_newborn_family_visit'


class Aftercare1To8Month(models.Model):
    visit_date = models.DateField(max_length=10,  verbose_name='随访日期')
    weight = models.FloatField(verbose_name='体重(kg)')
    weight_grade = models.CharField(max_length=5,  verbose_name='', choices=GRADE)
    height = models.FloatField(verbose_name='身长(cm)')
    height_grade = models.CharField(max_length=5,  verbose_name='',  choices=GRADE)
    head_circumference = models.FloatField(verbose_name='头围(cm)')
    skin = models.CharField(max_length=20,  verbose_name='皮肤',  choices=NORMAL_OR_ABNORMAL)
    bregma = models.CharField(max_length=10,  verbose_name='前囟',  choices=BREGMA)
    bregma_length = models.FloatField(verbose_name='', blank=True, null=True)
    bregma_width = models.FloatField(verbose_name='', blank=True, null=True)
    eye_appearance = models.CharField(max_length=20,  verbose_name='眼外观',  choices=NORMAL_OR_ABNORMAL)
    ear_appearance = models.CharField(max_length=20,  verbose_name='耳外观',  choices=NORMAL_OR_ABNORMAL)
    heart_lung = models.CharField(max_length=20,  verbose_name='心肺',  choices=NORMAL_OR_ABNORMAL)
    abdomen = models.CharField(max_length=20,  verbose_name='腹部',  choices=NORMAL_OR_ABNORMAL)
    all_fours = models.CharField(max_length=20,  verbose_name='四肢',  choices=NORMAL_OR_ABNORMAL)
    anus_externalia = models.CharField(max_length=20,  verbose_name='肛门/外生殖器',  choices=NORMAL_OR_ABNORMAL)
    hemoglobin_value = models.FloatField(verbose_name='血红蛋白值')
    outdoor_activities = models.FloatField(verbose_name='户外活动')
    take_vitamin_d = models.FloatField(verbose_name='服用维生素')
    growth_evaluate = models.CharField(max_length=10,  verbose_name='发育评估',  choices=GROWTH_EVALUATE)
    two_visit_disease = models.CharField(max_length=20,  verbose_name='两次随访间患病情况',  choices=TWO_VISIT_DISEASE)
    extra = models.CharField(max_length=50,  verbose_name='其他', blank=True, null=True)
    transfer_treatment_suggestion = models.CharField(max_length=5,  verbose_name='转诊建议',
                                                     choices=TRANSFER_TREATMENT_SUGGESTION)
    transfer_treatment_suggestion_reason = models.CharField(max_length=100,  verbose_name='原因', blank=True, null=True)
    transfer_treatment_suggestion_institution = models.CharField(max_length=100,  verbose_name='机构及科室', blank=True, null=True)
    guide = models.ManyToManyField(GuideChoices,  verbose_name='指导', blank=True, null=True)
    next_visit_date = models.DateField(max_length=10,  verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        abstract = True


class Aftercare1Month(Aftercare1To8Month):
    complexion = models.CharField(max_length=10,  verbose_name='面色',  choices=COMPLEXION)
    neck_enclosed_mass = models.CharField(max_length=5, verbose_name='颈部包块', choices=NECK_ENCLOSED_MASS)
    oral_cavity = models.CharField(max_length=20,  verbose_name='口腔',  choices=NORMAL_OR_ABNORMAL)
    navel = models.CharField(max_length=30,  verbose_name='脐部',  choices=NAVEL)
    rickets_sign = models.CharField(max_length=20,  verbose_name='可疑佝偻病体征',  choices=RICKETS_SIGN)

    class Meta:
        db_table = 'child_aftercare_1_month'


RICKETS_SYMPTOM = ((u'无', '无'), (u'夜惊', '夜惊'), (u'多汗', '多汗'), (u'烦躁', '烦躁'))


class Aftercare3Month(Aftercare1To8Month):
    complexion = models.CharField(max_length=10, verbose_name='面色', choices=COMPLEXION)
    neck_enclosed_mass = models.CharField(max_length=5, verbose_name='颈部包块', choices=NECK_ENCLOSED_MASS)
    oral_cavity = models.CharField(max_length=20, verbose_name='口腔', choices=NORMAL_OR_ABNORMAL)
    navel = models.CharField(max_length=30, verbose_name='脐部', choices=NORMAL_OR_ABNORMAL)
    rickets_symptom = models.CharField(max_length=20, verbose_name='可疑佝偻病症状', choices=RICKETS_SYMPTOM)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN)

    class Meta:
        db_table = 'child_aftercare_3_month'


COMPLEXION_1 = ((u'红润', '红润'), (u'其他', '其他'))
PASS_OR_NO = ((u'通过', '通过'), (u'未通过', '未通过'))
RICKETS_SIGN_1 = ((u'肋串珠', '肋串珠'), (u'肋外翻', '肋外翻'), (u'肋软骨沟', '肋软骨沟'),
                  (u'鸡胸', '鸡胸'), (u'手镯征', '手镯征'))


class Aftercare6Month(Aftercare1To8Month):
    complexion = models.CharField(max_length=10, verbose_name='面色', choices=COMPLEXION_1)
    neck_enclosed_mass = models.CharField(max_length=5, verbose_name='颈部包块', choices=NECK_ENCLOSED_MASS)
    hearing = models.CharField(max_length=20, verbose_name='听力', choices=PASS_OR_NO)
    oral_cavity = models.PositiveSmallIntegerField(verbose_name='口腔')
    rickets_symptom = models.CharField(max_length=20, verbose_name='可疑佝偻病症状', choices=RICKETS_SYMPTOM)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN_1)

    class Meta:
        db_table = 'child_aftercare_6_month'


class Aftercare8Month(Aftercare1To8Month):
    complexion = models.CharField(max_length=10, verbose_name='面色', choices=COMPLEXION_1)
    oral_cavity = models.PositiveSmallIntegerField(verbose_name='口腔')
    rickets_symptom = models.CharField(max_length=20, verbose_name='可疑佝偻病症状', choices=RICKETS_SYMPTOM)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN_1)

    class Meta:
        db_table = 'child_aftercare_8_month'


RICKETS_SIGN_2 = ((u'"o"型腿', '"o"型腿'), (u'"x"型腿', '"x"型腿'))
GUIDE_1 = ((u'科学喂养', '科学喂养'), (u'生长发育', '生长发育'), (u'疾病预防', '疾病预防'),
           (u'预防意外伤害', '预防意外伤害'), (u'口腔保健', '口腔保健'), (u'其他', '其他'))


class Aftercare12To30Month(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期')
    weight = models.FloatField(verbose_name='体重(kg)')
    weight_grade = models.CharField(max_length=5, verbose_name='', choices=GRADE)
    height = models.FloatField(verbose_name='身长(cm)')
    height_grade = models.CharField(max_length=5, verbose_name='', choices=GRADE)
    complexion = models.CharField(max_length=10, verbose_name='面色', choices=COMPLEXION_1)
    skin = models.CharField(max_length=20, verbose_name='皮肤', choices=NORMAL_OR_ABNORMAL)
    eye_appearance = models.CharField(max_length=20, verbose_name='眼外观', choices=NORMAL_OR_ABNORMAL)
    ear_appearance = models.CharField(max_length=20, verbose_name='耳外观', choices=NORMAL_OR_ABNORMAL)
    tooth = models.PositiveSmallIntegerField(verbose_name='出牙/龋齿数（颗）')
    decayed_tooth = models.PositiveSmallIntegerField(verbose_name='')
    heart_lung = models.CharField(max_length=20, verbose_name='心肺', choices=NORMAL_OR_ABNORMAL)
    abdomen = models.CharField(max_length=20, verbose_name='腹部', choices=NORMAL_OR_ABNORMAL)
    all_fours = models.CharField(max_length=20, verbose_name='四肢', choices=NORMAL_OR_ABNORMAL)
    outdoor_activities = models.FloatField(verbose_name='户外活动')
    two_visit_disease = models.CharField(max_length=20, verbose_name='两次随访间患病情况', choices=TWO_VISIT_DISEASE)
    extra = models.CharField(max_length=50, verbose_name='其他', blank=True, null=True)
    transfer_treatment_suggestion = models.CharField(max_length=5, verbose_name='转诊建议', choices=TRANSFER_TREATMENT_SUGGESTION)
    transfer_treatment_suggestion_reason = models.CharField(max_length=100, verbose_name='原因', blank=True, null=True)
    transfer_treatment_suggestion_institution = models.CharField(max_length=100, verbose_name='机构及科室',  blank=True, null=True)
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')
    guide_extra = models.CharField(max_length=30, verbose_name='',blank=True, null=True)

    class Meta:
        abstract = True


class Aftercare12Month(Aftercare12To30Month):
    bregma = models.CharField(max_length=10, verbose_name='前囟', choices=BREGMA)
    bregma_length = models.FloatField(verbose_name='', blank=True, null=True)
    bregma_width = models.FloatField(verbose_name='', blank=True, null=True)
    hearing = models.CharField(max_length=20, verbose_name='听力', choices=PASS_OR_NO)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN_2)
    take_vitamin_d = models.FloatField(verbose_name='服用维生素D')
    growth_evaluate = models.CharField(max_length=10, verbose_name='发育评估', choices=GROWTH_EVALUATE)
    guide = models.ManyToManyField(GuideChoices,  verbose_name='指导', blank=True, null=True)

    class Meta:
        db_table = 'child_aftercare_12_month'


class Aftercare18Month(Aftercare12To30Month):
    bregma = models.CharField(max_length=10, verbose_name='前囟', choices=BREGMA)
    bregma_length = models.FloatField(verbose_name='', blank=True, null=True)
    bregma_width = models.FloatField(verbose_name='', blank=True, null=True)
    step = models.CharField(max_length=20, verbose_name='步态', choices=NORMAL_OR_ABNORMAL)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN_2)
    hemoglobin_value = models.FloatField(verbose_name='血红蛋白值')
    take_vitamin_d = models.FloatField(verbose_name='服用维生素D')
    growth_evaluate = models.CharField(max_length=10, verbose_name='发育评估', choices=GROWTH_EVALUATE)
    guide = models.ManyToManyField(GuideChoices,  verbose_name='指导', blank=True, null=True)

    class Meta:
        db_table = 'child_aftercare_18_month'


GUIDE_2 = ((u'合理膳食', '合理膳食'), (u'生长发育', '生长发育'), (u'疾病预防', '疾病预防'),
           (u'预防意外伤害', '预防意外伤害'), (u'口腔保健', '口腔保健'), (u'其他', '其他'))


class Guide1Choices(ChoicesAbstract):
    pass


class Aftercare24Month(Aftercare12To30Month):
    bregma = models.CharField(max_length=10, verbose_name='前囟', choices=BREGMA)
    bregma_length = models.FloatField(verbose_name='', blank=True, null=True)
    bregma_width = models.FloatField(verbose_name='', blank=True, null=True)
    hearing = models.CharField(max_length=20, verbose_name='听力', choices=PASS_OR_NO)
    step = models.CharField(max_length=20, verbose_name='步态', choices=NORMAL_OR_ABNORMAL)
    rickets_sign = models.CharField(max_length=20, verbose_name='可疑佝偻病体征', choices=RICKETS_SIGN_2)
    take_vitamin_d = models.FloatField(verbose_name='服用维生素D')
    growth_evaluate = models.CharField(max_length=10, verbose_name='发育评估', choices=GROWTH_EVALUATE)
    guide = models.ManyToManyField(Guide1Choices,  verbose_name='指导', blank=True, null=True)

    class Meta:
        db_table = 'child_aftercare_24_month'


class Aftercare30Month(Aftercare12To30Month):
    step = models.CharField(max_length=20, verbose_name='步态', choices=NORMAL_OR_ABNORMAL)
    hemoglobin_value = models.FloatField(verbose_name='血红蛋白值')
    guide = models.ManyToManyField(Guide1Choices,  verbose_name='指导', blank=True, null=True)

    class Meta:
        db_table = 'child_aftercare_30_month'


BODY_GROWTH_EVALUATE = ((u'正常', '正常'), (u'低体重', '低体重'), (u'消瘦', '消瘦'),
                        (u'发育迟缓', '发育迟缓'), (u'超重', '超重'))
TWO_VISIT_DISEASE_1 = ((u'无', '无'), (u'肺炎', '肺炎'), (u'腹泻', '腹泻'), (u'外伤', '外伤'), (u'其他', '其他'))


class Aftercare3To6Year(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期')
    weight = models.FloatField(verbose_name='体重(kg)')
    weight_grade = models.CharField(max_length=5, verbose_name='', choices=GRADE)
    height = models.FloatField(verbose_name='身长(cm)')
    height_grade = models.CharField(max_length=5, verbose_name='', choices=GRADE)
    body_growth_evaluate = models.CharField(max_length=20, verbose_name='体格发育评价', choices=BODY_GROWTH_EVALUATE)
    tooth = models.PositiveSmallIntegerField(verbose_name='牙数（颗）/龋齿数')
    decayed_tooth = models.PositiveSmallIntegerField(verbose_name='')
    heart_lung = models.CharField(max_length=20, verbose_name='心肺', choices=NORMAL_OR_ABNORMAL)
    abdomen = models.CharField(max_length=20, verbose_name='腹部', choices=NORMAL_OR_ABNORMAL)
    hemoglobin_value = models.FloatField(verbose_name='血红蛋白值')
    extra = models.CharField(max_length=50, verbose_name='其他', blank=True, null=True)
    pneumonia = models.PositiveSmallIntegerField(verbose_name='两次随访间患病情况')
    diarrhea = models.PositiveSmallIntegerField(verbose_name='')
    traumatism = models.PositiveSmallIntegerField(verbose_name='')
    two_visit_extra = models.CharField(max_length=20, verbose_name='', blank=True, null=True)
    transfer_treatment_suggestion = models.CharField(max_length=5, verbose_name='转诊建议', choices=TRANSFER_TREATMENT_SUGGESTION)
    transfer_treatment_suggestion_reason = models.CharField(max_length=100, verbose_name='原因', blank=True, null=True)
    transfer_treatment_suggestion_institution = models.CharField(max_length=100, verbose_name='机构及科室', blank=True, null=True)
    guide = models.ManyToManyField(Guide1Choices,  verbose_name='指导', blank=True, null=True)
    guide_extra = models.CharField(max_length=30, verbose_name='', blank=True, null=True)
    doctor_signature = models.CharField(max_length=20, verbose_name='随访医生签名')

    class Meta:
        abstract = True


class Aftercare3Year(Aftercare3To6Year):
    hearing = models.CharField(max_length=20, verbose_name='听力', choices=PASS_OR_NO)
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期')

    class Meta:
        db_table = 'child_aftercare_3_year'


class Aftercare4Year(Aftercare3To6Year):
    eye_sight = models.CharField(max_length=20, verbose_name='视力')
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期')

    class Meta:
        db_table = 'child_aftercare_4_year'


class Aftercare5Year(Aftercare3To6Year):
    eye_sight = models.CharField(max_length=20, verbose_name='视力')
    next_visit_date = models.DateField(max_length=10, verbose_name='下次随访日期')

    class Meta:
        db_table = 'child_aftercare_5_year'


class Aftercare6Year(Aftercare3To6Year):
    eye_sight = models.CharField(max_length=20, verbose_name='视力')

    class Meta:
        db_table = 'child_aftercare_6_year'

