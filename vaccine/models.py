# -*- coding=utf-8 -*-
from django.db import models


VACCINATE_POSITION_CHOICES = (
    (u'请选择', '请选择'),
    (u'上臂三角肌', '上臂三角肌'),
    (u'上臂三角肌中部略下处', '上臂三角肌中部略下处'),
    (u'上臂外侧三角肌', '上臂外侧三角肌'),
    (u'上臂外侧三角肌附着处', '上臂外侧三角肌附着处'),
    (u'上臂外侧三角肌下缘附着处', '上臂外侧三角肌下缘附着处'),
    (u'其他', '其他'),)


class Vaccination(models.Model):
    vaccine = models.ForeignKey('management.Service', verbose_name='疫苗与剂次')
    visit_date = models.DateField(max_length=10,  verbose_name='接种日期')
    vaccinate_position = models.CharField(max_length=100, verbose_name='接种部位')
    batch_number = models.CharField(max_length=100, verbose_name='疫苗批号',)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=20, verbose_name='医生签名')
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期', blank=True, null=True)


class VaccineAbstract(models.Model):
    visit_date = models.DateField(max_length=10,  verbose_name='接种日期')
    vaccinate_position = models.CharField(max_length=200, verbose_name='接种部位', choices=VACCINATE_POSITION_CHOICES, default='请选择')
    batch_number = models.CharField(max_length=300, verbose_name='疫苗批号',)
    remarks = models.CharField(max_length=500, verbose_name='备注', blank=True, null=True,)
    doctor_signature = models.CharField(max_length=30, verbose_name='医生签名', blank=True)

    class Meta:
        abstract = True


# 乙肝疫苗-1
class HepatitisBVaccine1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_b_vaccine_1'))


# 乙肝疫苗-2
class HepatitisBVaccine2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_b_vaccine_2'))


# 乙肝疫苗-3
class HepatitisBVaccine3(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_b_vaccine_3'))


# 卡介苗
class BcgVaccine(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'bcg_vaccine'))


# 脊灰疫苗①
class PoliomyelitisVaccine1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'poliomyelitis_vaccine_1'))


# 脊灰疫苗②
class PoliomyelitisVaccine2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'poliomyelitis_vaccine_2'))


# 脊灰疫苗③
class PoliomyelitisVaccine3(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'poliomyelitis_vaccine_3'))


# 脊灰疫苗④
class PoliomyelitisVaccine4(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'poliomyelitis_vaccine_4'))


# 百白破疫苗①
class DiphtheriaPertussisTetanus1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'diphtheria_pertussis_tetanus_1'))


# 百白破疫苗②
class DiphtheriaPertussisTetanus2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'diphtheria_pertussis_tetanus_2'))


# 百白破疫苗③
class DiphtheriaPertussisTetanus3(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'diphtheria_pertussis_tetanus_3'))


# 百白破疫苗④
class DiphtheriaPertussisTetanus4(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'diphtheria_pertussis_tetanus_4'))


# 白破疫苗
class DiphtheriaTetanusVaccine(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'diphtheria_tetanus_vaccine'))


# 麻风疫苗
class MeaslesRubella(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_rubella'))


# 麻腮风疫苗①
class MeaslesMumpsRubella1(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_mumps_rubella_1'))


# 麻腮风疫苗②
class MeaslesMumpsRubella2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_mumps_rubella_2'))


# 麻腮疫苗
class MeaslesMumps(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_mumps'))


# 麻疹疫苗①
class Measles1(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_1'))


# 麻疹疫苗②
class Measles2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'measles_2'))


# A群流脑疫苗①
class MeningitisA1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'meningitis_a_1'))


# A群流脑疫苗②
class MeningitisA2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'meningitis_a_2'))


# A+C群流脑疫苗①
class MeningitisAc1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'meningitis_ac_1'))


# A+C群流脑疫苗②
class MeningitisAc2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'meningitis_ac_2'))


# 乙脑减毒活疫苗①
class JapaneseEncephalitisAttenuated1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_attenuated_1'))


# 乙脑减毒活疫苗②
class JapaneseEncephalitisAttenuated2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_attenuated_2'))


# 乙脑灭活疫苗①
class JapaneseEncephalitisInactivated1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_inactivated_1'))


# 乙脑灭活疫苗②
class JapaneseEncephalitisInactivated2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_inactivated_2'))


# 乙脑灭活疫苗③
class JapaneseEncephalitisInactivated3(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_inactivated_3'))


# 乙脑灭活疫苗④
class JapaneseEncephalitisInactivated4(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'japanese_encephalitis_inactivated_4'))


# 甲肝减毒活疫苗
class HepatitisAAttenuated(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_a_attenuated'))


# 甲肝灭活疫苗①
class HepatitisAInactivated1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_a_inactivated_1'))


# 甲肝灭活疫苗②
class HepatitisAInactivated2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'hepatitis_a_inactivated_2'))


# 炭疽疫苗
class AnthraxVaccine(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'anthrax_vaccine'))


# 钩体疫苗①
class LeptospiraVaccine1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'leptospira_vaccine_1'))


# 钩体疫苗②
class LeptospiraVaccine2(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'leptospira_vaccine_2'))


# 出血热疫苗（双价）①
class HemorrhagicIII1(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'hemorrhagic_i_ii_1'))


# 出血热疫苗（双价）②
class HemorrhagicIII2(VaccineAbstract):
    next_vaccinate_date = models.DateField(max_length=15, verbose_name='下次接种日期')

    class Meta:
        db_table = '_'.join(('vaccine', 'hemorrhagic_i_ii_2'))


# 出血热疫苗（双价）③
class HemorrhagicIII3(VaccineAbstract):

    class Meta:
        db_table = '_'.join(('vaccine', 'hemorrhagic_i_ii_3'))


GENDER = ((u'男', u'男'), (u'女', u'女'),)
CENSUS_REGISTER_ADDRESS = ((u'同家庭地址', u'同家庭地址'),)


class VaccineCard(models.Model):
    ehr_village_no = models.CharField(max_length=3, verbose_name='健康档案编码中村（社区）对应的3位编码')
    ehr_unique_no = models.CharField(max_length=5, verbose_name='健康档案编码中最后5位编码')

    gender = models.CharField(max_length=20, verbose_name='性别', choices=GENDER)
    birth_date = models.DateField(max_length=10, verbose_name='出生日期')
    guardian_name = models.CharField(max_length=20, verbose_name='监护人姓名')
    relation_to_child = models.CharField(max_length=10, verbose_name='与儿童关系')
    contact_number = models.CharField(max_length=11, verbose_name='联系电话')
    home_county = models.CharField(max_length=20, verbose_name='户籍地址/县（区）', default='三河市')
    home_town = models.ForeignKey('management.Region', related_name='town_vaccine_card',
                                  verbose_name='家庭地址/乡镇（街道）')
    register_local = models.BooleanField(verbose_name='本地户籍', default=False)
    register_province = models.CharField(max_length=20, verbose_name='户籍地址/省（市、自治区）', null=True)
    register_city = models.CharField(max_length=20, verbose_name='户籍地址/市', null=True)
    register_county = models.CharField(max_length=20, verbose_name='户籍地址/县（区）', null=True)
    register_town = models.CharField(max_length=20, verbose_name='户籍地址/乡镇（街道）', null=True)

    immigrate_time = models.DateField(max_length=10, verbose_name='迁入时间', blank=True, null=True)
    emigrate_time = models.DateField(max_length=10, verbose_name='迁出时间', blank=True, null=True)
    emigrate_reason = models.CharField(max_length=300, verbose_name='迁出原因', blank=True, null=True)
    vaccine_abnormal_reaction_history = models.CharField(max_length=300, verbose_name='疫苗异常反应史')
    vaccinate_taboo = models.CharField(max_length=300, verbose_name='接种禁忌')
    infection_history = models.CharField(max_length=300, verbose_name='传染病史')
    found_card_date = models.DateField(max_length=10, verbose_name='建卡日期')
    found_card_person = models.CharField(max_length=20, verbose_name='建卡人')

    class Meta:
        db_table = 'vaccine_card'