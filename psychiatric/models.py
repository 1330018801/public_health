#-*- coding=utf-8 -*-
from django.db import models
from ehr.models import ChoicesAbstract, SymptomChoice

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
DANGEROUSNESS = ((u'0级', '0级'), (u'1级', '1级'), (u'2级', '2级'),
                 (u'3级', '3级'), (u'4级', '4级'), (u'5级', '5级'),)
NOW_SYMPTOM = ((u'幻觉', '幻觉'), (u'交流困难', '交流困难'), (u'猜疑', '猜疑'),
              (u'喜怒无常', '喜怒无常'), (u'行为怪异', '行为怪异'), (u'兴奋话多', '兴奋话多'),
              (u'伤人毁物', '伤人毁物'), (u'悲观厌世', '悲观厌世'), (u'无故外走', '无故外走'),
              (u'自语自笑', '自语自笑'), (u'孤僻懒散', '孤僻懒散'), (u'其他', '其他'),)
INSIGHT = ((u'自知力完全', '自知力完全'), (u'自知力不全', '自知力不全'), (u'自知力缺失', '自知力缺失'),)
SITUATION = ((u'良好', '良好'), (u'一般', '一般'), (u'较差', '较差'),)
SITUATION_1 = ((u'良好', '良好'), (u'一般', '一般'), (u'较差', '较差'), (u'此项不适用', '此项不适用'),)
LOCK_SITUATION = ((u'无关锁', '无关锁'), (u'关锁', '关锁'), (u'关锁已解除', '关锁已解除'),)
HOSPITALIZED_SITUATION = ((u'从未住院', '从未住院'), (u'目前正在住院', '目前正在住院'),
                          (u'既往住院，现未住院', '既往住院，现未住院'),)
YES_OR_NO = ((u'无', '无'), (u'有', '有'),)
TAKE_MEDICINE_COMPLIANCE = ((u'规律', '规律'), (u'间断', '间断'), (u'不服药', '不服药'),)
TREATMENT_EFFECT = ((u'痊愈', '痊愈'), (u'好转', '好转'), (u'无变化', '无变化'), (u'加重', '加重'),)
TRANSFER_TREATMENT = ((u'否', '否'), (u'是', '是'),)
RECOVERY_MEASURE = ((u'生活劳动能力', '生活劳动能力'), (u'职业训练', '职业训练'), (u'学习能力', '学习能力'),
                    (u'社会交往', '社会交往'), (u'其他', '其他'),)
VISIT_CLASSIFICATION = ((u'不稳定', '不稳定'), (u'基本稳定', '基本稳定'),
                        (u'稳定', '稳定'), (u'未访到', '未访到'),)
PER = ((u'天', '天'), (u'月', '月'),)


class RecoveryMeasureChoices(ChoicesAbstract):
    pass


class Aftercare(models.Model):
    visit_date = models.DateField(max_length=10, verbose_name='随访日期',)
    dangerousness = models.CharField(max_length=10, verbose_name='危险性', choices=DANGEROUSNESS)
    now_symptom = models.ManyToManyField(SymptomChoice, verbose_name='目前症状', blank=True, null=True,)
    now_symptom_extra = models.CharField(max_length=100, verbose_name='', blank=True, null=True,)
    insight = models.CharField(max_length=30, verbose_name='自知力', choices=INSIGHT)
    sleep_situation = models.CharField(max_length=10, verbose_name='睡眠情况', choices=SITUATION)
    diet_situation = models.CharField(max_length=10, verbose_name='饮食情况', choices=SITUATION)
    society_function_individual_life_care = models.CharField(max_length=10, verbose_name='个人生活料理', choices=SITUATION)
    society_function_housework = models.CharField(max_length=10, verbose_name='家务劳动', choices=SITUATION)
    society_function_productive_work = models.CharField(max_length=10, verbose_name='生产劳动及工作', choices=SITUATION_1)
    society_function_learn_ability = models.CharField(max_length=10, verbose_name='学习能力', choices=SITUATION)
    society_function_social_interpersonal = models.CharField(max_length=10, verbose_name='社会人际交往', choices=SITUATION)
    disease_family_society_effect_mild_disturbance = models.PositiveSmallIntegerField(verbose_name='轻度滋事',)
    disease_family_society_effect_disturbance = models.PositiveSmallIntegerField(verbose_name='肇事',)
    disease_family_society_effect_accident = models.PositiveSmallIntegerField(verbose_name='肇祸',)
    disease_family_society_effect_autolesion = models.PositiveSmallIntegerField(verbose_name='自伤',)
    disease_family_society_effect_attempted_suicide = models.PositiveSmallIntegerField(verbose_name='自杀未遂',)
    #disease_family_society_effect_nothing = models.PositiveSmallIntegerField(verbose_name='',)
    lock_situation = models.CharField(max_length=30, verbose_name='关锁情况', choices=LOCK_SITUATION)
    hospitalized_situation = models.CharField(max_length=30, verbose_name='住院情况', choices=HOSPITALIZED_SITUATION)
    last_hospitalized_date = models.DateField(max_length=10, verbose_name='末次出院时间', blank=True, null=True,)
    laboratory_examination = models.CharField(max_length=10, verbose_name='实验室检查', choices=YES_OR_NO,)
    laboratory_examination_yes = models.CharField(max_length=100, blank=True, null=True)
    take_medicine_compliance = models.CharField(max_length=10, verbose_name='服药依从性', choices=TAKE_MEDICINE_COMPLIANCE)
    medicine_untoward_effect = models.CharField(max_length=10, verbose_name='药物不良反应', choices=YES_OR_NO,)
    medicine_untoward_effect_yes = models.CharField(max_length=100, blank=True, null=True)
    treatment_effect = models.CharField(max_length=10, verbose_name='治疗效果', choices=TREATMENT_EFFECT)
    transfer_treatment = models.CharField(max_length=5, verbose_name='转诊', choices=TRANSFER_TREATMENT,)
    transfer_treatment_reason = models.CharField(max_length=100, verbose_name='转诊原因', blank=True, null=True,)
    transfer_treatment_institution = models.CharField(max_length=100, verbose_name='转诊至机构及科室', blank=True, null=True,)
    take_medicine_1 = models.CharField(max_length=100, verbose_name='药物名称1', blank=True, null=True,)
    take_medicine_1_per = models.CharField(max_length=10, verbose_name='用法用量', choices=PER, default='',
                                           blank=True, null=True,)
    take_medicine_1_time = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True,)
    take_medicine_1_mg = models.FloatField(blank=True, null=True,)
    take_medicine_2 = models.CharField(max_length=100, verbose_name='药物名称2', blank=True, null=True,)
    take_medicine_2_per = models.CharField(max_length=10, verbose_name='用法用量', choices=PER, default='',
                                           blank=True, null=True,)
    take_medicine_2_time = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True,)
    take_medicine_2_mg = models.FloatField(blank=True, null=True,)
    take_medicine_3 = models.CharField(max_length=100, verbose_name='药物名称3', blank=True, null=True,)
    take_medicine_3_per = models.CharField(max_length=10, verbose_name='用法用量', choices=PER, default='',
                                           blank=True, null=True,)
    take_medicine_3_time = models.PositiveSmallIntegerField(verbose_name='', blank=True, null=True,)
    take_medicine_3_mg = models.FloatField(blank=True, null=True,)
    recovery_measure = models.ManyToManyField(RecoveryMeasureChoices, verbose_name='康复措施', blank=True, null=True,)
    recovery_measure_extra = models.CharField(max_length=30, verbose_name='', blank=True, null=True,)
    visit_classification = models.CharField(max_length=100, verbose_name='本次随访分类', choices=VISIT_CLASSIFICATION)
    next_visit_date = models.DateField(verbose_name='下次随访日期')
    doctor_signature = models.CharField(max_length=30, verbose_name='随访医生签名', blank=True, null=True)

    class Meta:
        db_table = 'psychiatric_aftercare'


OUTPATIENT_CHOICES = ((u'未治', u'未治'), (u'间断门诊治疗', u'间断门诊治疗'), (u'连续门诊治疗', u'连续门诊治疗'))
LOCK_CHOICES = ((u'无关锁', u'无关锁'), (u'关锁', u'关锁'), (u'关锁已解除', u'关锁已解除'))
ECONOMY_CHOICES = ((u'贫困，在当地贫困标准以下', u'贫困，在当地贫困标准以下'), (u'非贫困', u'非贫困'), (u'不祥', u'不祥'))
ASSENT_CHOICES = ((u'同意参加管理', u'同意参加管理'), (u'不同意参加管理', u'不同意参加管理'))
CURE_EFFECT_CHOICES = ((u'痊愈', u'痊愈'), (u'好转', u'好转'), (u'无变化', u'无变化'), (u'加重', u'加重'))


class PsychiatricInfo(models.Model):
    guardian_name = models.CharField(max_length=20, verbose_name='监护人姓名')
    guardian_relation = models.CharField(max_length=20, verbose_name='与患者关系')
    guardian_address = models.CharField(max_length=100, verbose_name='监护人地址')
    guardian_phone = models.CharField(max_length=20, verbose_name='监护人电话')
    community_contact_name = models.CharField(max_length=20, verbose_name='辖区村（居）委会联系人')
    community_contact_phone = models.CharField(max_length=20, verbose_name='辖区村（居）委会联系人电话')
    assent = models.CharField(max_length=20, choices=ASSENT_CHOICES)
    signature_date = models.DateField(verbose_name='签字时间')
    disease_begin_date = models.DateField(verbose_name='初次发病时间')
    symptom = models.ManyToManyField(SymptomChoice, verbose_name='既往主要症状', related_name='choices')
    symptom_other = models.CharField(max_length=20, null=True, blank=True)
    cure_outpatient = models.CharField(max_length=20, choices=OUTPATIENT_CHOICES)
    drug_first_date = models.DateField(verbose_name='首次抗精神病药物治疗时间')
    cure_hospital = models.IntegerField(verbose_name='曾住精神专科医院/综合医院精神专科')
    diagnose = models.CharField(max_length=50, verbose_name='诊断')
    diagnose_hospital = models.CharField(max_length=30, verbose_name='诊断医院')
    diagnose_date = models.DateField(verbose_name='诊断日期')
    cure_effect = models.CharField(max_length=10, choices=CURE_EFFECT_CHOICES, verbose_name='最近一次治疗效果')
    social_effect_minor = models.IntegerField(verbose_name='1 轻度滋事', blank=True, null=True)
    social_effect_trouble = models.IntegerField(verbose_name='2 肇事', blank=True, null=True)
    social_effect_disaster = models.IntegerField(verbose_name='3 肇祸', blank=True, null=True)
    social_effect_self_injury = models.IntegerField(verbose_name='4 自伤', blank=True, null=True)
    social_effect_suicide = models.IntegerField(verbose_name='5 自杀', blank=True, null=True)
    lock = models.CharField(max_length=20, choices=LOCK_CHOICES, verbose_name='关锁情况')
    economy = models.CharField(max_length=50, choices=ECONOMY_CHOICES, verbose_name='经济状况')
    doctor_advice = models.CharField(max_length=200, verbose_name='专科医生意见（如果有请记录）', null=True, blank=True)
    fill_table_date = models.DateField(verbose_name='填表日期')
    doctor_signature = models.CharField(max_length=10, verbose_name='医生签字', null=True, blank=True)

    class Meta:
        db_table = 'ehr_psychiatric_info'