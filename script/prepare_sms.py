# -*- coding=utf-8 -*-

import psycopg2
import logging
import sys
from datetime import date, timedelta

debug = True
interval = 200  # 提前发送短信通知的天数
DB_PARA = "dbname=sh_health_dev user=postgres password=6yhn7ujm,./ host=202.112.52.20 port=5432"

birth_based_items = {'1_month': ['child_aftercare_1_month'],
                     '2_month': ['vaccine_poliomyelitis_vaccine_1'],
                     '3_month': ['vaccine_diphtheria_pertussis_tetanus_1',
                                 'child_aftercare_3_month'],
                     '6_month': ['vaccine_meningitis_a_1',
                                 'child_aftercare_6_month',
                                 'tcm_aftercare_6_month'],
                     '8_month': ['vaccine_measles_rubella',
                                 'vaccine_japanese_encephalitis_attenuated_1',
                                 'vaccine_japanese_encephalitis_inactivated_1',
                                 'child_aftercare_12_month'],
                     '12_month': ['child_aftercare_12_month',
                                  'tcm_aftercare_12_month'],
                     '18_month': ['vaccine_hepatitis_a_attenuated',
                                  'vaccine_hepatitis_a_inactivated_1',
                                  'vaccine_meales_mumps_rubella',
                                  'child_aftercare_18_month',
                                  'tcm_aftercare_18_month'],
                     '24_month': ['child_aftercare_24_month',
                                  'tcm_aftercare_24_month'],
                     '30_month': ['child_aftercare_30_month',
                                  'tcm_aftercare_30_month'],
                     '3_year': ['child_aftercare_3_year',
                                'tcm_aftercare_3_year'],
                     '4_year': ['child_aftercare_4_year'],
                     '5_year': ['child_aftercare_5_year'],
                     '6_year': ['vaccine_diphtheria_tetanus_vaccine',
                                'child_aftercare_6_year']}

INSERT_READY_MSG = """INSERT INTO management_sms (mobile, name, next_time_date,
                      service_type_name, service_item_name, template_id, status)
                      values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', 1)"""
FIND_PARENTS = """SELECT father_id, mother_id FROM family_family
                  inner join family_family_children ON
                  family_family.id=family_family_children.family_id AND
                  family_family_children.resident_id={0}"""
GET_MOBILE = "SELECT mobile, name FROM management_resident WHERE id={0}"
GET_ALL_RESIDENT = """SELECT id, name, identity, birthday
                      FROM management_resident WHERE enabled=1"""

GET_ALL_SERVICE = """SELECT id, name, alias, level, service_type_id
                     FROM management_service WHERE enabled=1"""
IF_NEXT_DATE = """SELECT exists (SELECT column_name FROM information_schema.columns
                  WHERE table_name='{0}' AND column_name='{1}')"""
GET_RESIDENT = """SELECT management_resident.id FROM management_resident INNER JOIN management_workrecord
                  ON management_resident.id=management_workrecord.resident_id
                  AND management_workrecord.app_label='{0}'
                  AND management_workrecord.service_item_alias='{1}'
                  AND management_workrecord.item_id={2}"""


# 日志功能初始化和配置
def get_logger():
    logger = logging.getLogger('sms_preparing')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s]%(levelname)s(%(name)s):%(message)s')
    file_handler = logging.FileHandler('../log/sms.log')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    if debug:
        logger.addHandler(stream_handler)
    else:
        logger.addHandler(file_handler)
    return logger


class Service(object):
    services = []

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.alias = row[2]
        self.level = row[3]
        self.type_id = row[4]

    @classmethod
    def get_all_types(cls):
        return [ss for ss in cls.services if ss.is_service_type]

    @classmethod
    def items_of(cls, s):
        if s.is_service_type:
            return [ss for ss in cls.services if ss.type_id == s.id]
        return []

    @classmethod
    def next_service_item_of(cls, s):
        return cls.services[cls.services.index(s) + 1]

    @classmethod
    def get_by_alias(cls, alias):
        for s in cls.services:
            if s.alias == alias:
                return s
        return None

    @property
    def is_service_type(self):
        if self.level == 2:
            return True
        else:
            return False


class Resident(object):
    def __init__(self, c):
        self.id = c[0]
        self.name = c[1]
        self.identity = c[2]
        self.birthday = c[3]

    def get_birthday(self):
        if self.birthday is not None:
            return self.birthday
        elif self.identity is not None and len(self.identity) == 18:
            try:
                year = int(self.identity[0:4])
                month = int(self.identity[4:6])
                day = int(self.identity[6:8])
            except (ValueError, IndexError):
                return None
            else:
                return date(year, month, day)
        return None

    def is_age_of(self, age):
        birthday = self.get_birthday()
        if birthday is not None:
            if birthday == date.today() - timedelta(days=age_days(age)):
                return True
        return False


# 获取所有服务类别和服务项目，方便程序内部使用
def get_all_service():
    cur.execute(GET_ALL_SERVICE)
    Service.services = [Service(s) for s in cur.fetchall()]


# 计算某年龄的孩子从出生到今天的天数，每月30天，每年365天
def age_days(age):
    count, period = age.split('_')
    if period == 'year':
        return int(count) * 365
    elif period == 'month':
        return int(count) / 12 * 365 + int(count) % 12 * 30


# 计算提供服务的实际时间，一般为当日之后interval天
def visit_date(d):
    d = date.today() + timedelta(days=d)
    while d.weekday() < 1 or d.weekday() > 5:
        d = d + timedelta(days=1)
    return d


# 根据服务类别获取短信模板id
def get_template(service_type, table_name=None, service_item=None):
    templates = {'vaccine': 'UyMdACLsTGS5', 'others': 'VqHxWu3Hq6xd'}
    if table_name is not None:
        service_type, service_item = service_item.split('_', 1)
    if service_type == 'vaccine':
        return templates['vaccine']
    else:
        return templates['others']


# 将所要发送短信的主要内容记录在数据库中，待合适时间发送
def insert_ready_msg2(name, mobile, service_type, service_item):
    template = get_template(service_type=service_type.alias)
    cur.execute(INSERT_READY_MSG.format(mobile, name, visit_date(interval),
                                        service_type.name, service_item.name, template))
    conn.commit()
    log.info("""Insert msg to database success(mobile:{0}, name:{1},
                next_time_date:{2}, service_type:{3}, service_item:{4}"""
             .format(mobile, name, visit_date(interval), service_type.name, service_item.name))


# 搜索所有服务项目中有下一次服务时间
# 判断表中是否存在所指定的下一次日期，以及该日期是否应该提醒，
# 如果是则计算所应发送短信的主要内容，并记录到数据库中
def next_date_based_process():
    for service_type in Service.get_all_types():
        for service_item in Service.items_of(service_type):
            tbl_name = '_'.join((service_type.alias, service_item.alias))
            for next_time_date_label in ['next_visit_date', 'next_vaccinate_date']:
                cur.execute(IF_NEXT_DATE.format(tbl_name, next_time_date_label))
                next_time_date_exist = cur.fetchone()[0]
                if next_time_date_exist:
                    cur.execute("SELECT id, {0} FROM {1}".format(next_time_date_label, tbl_name))
                    for row in cur.fetchall():
                        item_id, the_date = row[0], row[1]
                        #if the_date == date.today() + timedelta(days=interval):
                        if the_date <= date.today() + timedelta(days=interval):
                            cur.execute(GET_RESIDENT.format(service_type.alias, service_item.alias, item_id))
                            resident_id = cur.fetchone()[0]
                            cur.execute("SELECT name FROM management_resident WHERE id={0}".format(resident_id))
                            resident_name = cur.fetchone()[0]
                            mobile = get_valid_contact(resident_id)
                            if mobile is None:
                                log.error("Error: can not find any contact for {0}".format(resident_name))
                                break
                            insert_ready_msg2(resident_name, mobile, service_type,
                                              Service.next_service_item_of(service_item))


def get_valid_contact(resident_id):
    cur.execute("SELECT mobile FROM management_resident WHERE id={0}".format(resident_id))
    mobile = cur.fetchone()[0]
    if mobile is not None:
        return mobile
    else:
        cur.execute(FIND_PARENTS.format(resident_id))
        parent = cur.fetchone()
        if parent is not None:
            for each in [adult for adult in parent if adult is not None]:
                cur.execute("SELECT mobile FROM management_resident WHERE id={0}".format(each))
                mobile = cur.fetchone()[0]
                if mobile is not None:
                    return mobile
        else:
            log.info("Can not find parent for {0}".format(resident_id))
    return None


# 相对于出生日期的服务项目，计算所应发送的所有短信内容，并记录在数据库中
def birth_based_process():
    cur.execute(GET_ALL_RESIDENT)
    for row in cur.fetchall():
        child = Resident(row)
        birthday = child.get_birthday()
        if birthday is None:
            log.warn("Resident {0} has no birthday information".format(child.name))
            continue
        if birthday >= date.today() - timedelta(days=365 * 7):
            for age in birth_based_items.keys():
                if child.is_age_of(age):
                    tables = birth_based_items[age]
                    for tbl_name in tables:
                        service_type_label, service_item_label = tbl_name.split('_', 1)
                        service_type = Service.get_by_alias(service_type_label)
                        service_item = Service.get_by_alias(service_item_label)
                        mobile = get_valid_contact(child.id)
                        if mobile is None:
                            log.error("Error: can not find any contact for {0}".format(child.name))
                            break
                        insert_ready_msg2(child.name, mobile, service_type, service_item)

if __name__ == '__main__':
    log = get_logger()

    conn = psycopg2.connect(DB_PARA)
    cur = conn.cursor()

    get_all_service()

    next_date_based_process()
    birth_based_process()

    cur.close()
    conn.close()
