#-*- coding=utf-8 -*-
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
NORMAL_OR_ABNORMAL = ((u'正常', '正常'), (u'异常', '异常'),)


EAT = ((0, '独立完成（0分）'), (3, '需要协助，如切碎、搅拌食物等（3分）'), (5, '完全需要帮助（5分）'),)
WASH = ((0, '独立完成（0分）'), (1, '独立完成能独立地洗头、梳头、洗脸、刷牙、剃须等；洗澡需要协助（1分）'), (3, '在协助下和适当的时间内，能完成部分梳洗活动（3分）'), (7, '完全需要帮助（7分）'),)
DRESS = ((0, '独立完成（0分）'), (3, '需要协助，在适当的时间内完成部分穿衣（3分）'), (5, '完全需要帮助（5分）'),)
TOILET = ((0, '不需要协助，可自控（0分）'), (1, '偶尔失禁，但基本上能如厕或使用便具（1分）'),
          (5, '经常失禁，在很多提示和协助下尚能如厕或使用便具（5分）'), (10, '完全失禁，完全需要帮助（10分）'),)
ACTIVITY = ((0, '独立完成所有活动（0分）'), (1, '借助较小的外力或辅助装置能完成站立、行走、上下楼梯等（1分）'),
            (5, '借助较大的外力才能完成站立、行走，不能上下楼梯（5分）'), (10, '卧床不起，活动完全需要帮助住（10分）'),)
GRADE = ((u'可自理', '可自理（0～3分）'), (u'轻度依赖', '轻度依赖（4～8分）'),
         (u'中度依赖', '中度依赖（9～18分）'),(u'重度依赖', '重度依赖（≥19分）'),)


class LivingSelfcareAppraisal(models.Model):
    eat = models.PositiveSmallIntegerField(verbose_name='（一）进食：使用餐具将饭菜送入口、咀嚼、吞咽等活动')
    wash = models.PositiveSmallIntegerField(verbose_name='（二）梳洗：梳头、洗脸、刷牙、剃须、洗澡等活动')
    dress = models.PositiveSmallIntegerField(verbose_name='（三）穿衣：穿衣裤、袜子、鞋子等活动')
    toilet = models.PositiveSmallIntegerField(verbose_name='（四）如厕：小便、大便等活动及自控')
    activity = models.PositiveSmallIntegerField(verbose_name='（五）活动：站立、室内行走、上下楼梯、户外活动')
    total = models.PositiveSmallIntegerField(verbose_name='总分')
    #grade = models.CharField(max_length=20,verbose_name='等级程度', choices=GRADE)

    class Meta:
        db_table = 'old_living_selfcare_appraisal'