# -*- coding=utf-8 -*-
import psycopg2
import requests
import json
import sys
import logging

debug = True
DB_PARA = "dbname=sh_health_dev user=postgres password=6yhn7ujm,./ host=202.112.52.20 port=5432"

GET_READY_MSG = """SELECT id, mobile, name, next_time_date, service_type_name, service_item_name,
                   template_id FROM management_sms WHERE status=1"""
MARK_SEND_SUCCESS = "UPDATE management_sms SET status=2, message='发送成功' WHERE id={0}"
MARK_SEND_FAILURE = "UPDATE management_sms SET status={0}, message='{1}' WHERE id={2}"


class Message(object):
    def __init__(self, row):
        self.id = row[0]
        self.mobile = row[1]
        self.name = row[2]
        self.next_time_date = row[3]
        self.service_type_name = row[4]
        self.service_item_name = row[5]
        self.template_id = row[6]


def get_logger():
    logger = logging.getLogger('sms_preparing')
    logger.setLevel(logging.DEBUG)
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


def send_msg_weimi(msg):
    response = requests.post("http://api.weimi.cc/2/sms/send.html",
                             data={
                                 "uid": "RDJXMWZjud06",
                                 "pas": "fkjk9x35",
                                 "mob": msg.mobile,
                                 "cid": msg.template_id,
                                 "p1": msg.name,
                                 "p2": msg.next_time_date.strftime('%Y年%m月%d日'),
                                 "p3": msg.service_type_name,
                                 "p4": msg.service_item_name,
                                 "type": "json"
                             }, timeout=3, verify=False);
    result = json.loads(response.content)
    if result['code'] == 0:
        cur.execute(MARK_SEND_SUCCESS.format(msg.id))
        conn.commit()
        log.info("Message sent success(mobile:{0}, name:{1}, service_type:{2}, service_item:{3}, date:{4})"
                 .format(msg.mobile, msg.name, msg.service_type_name, msg.service_item_name, msg.next_time_date))
    else:
        cur.execute(MARK_SEND_FAILURE.format(int(result['code']), result['msg'].encode('utf8'), msg.id))
        conn.commit()
        log.info("Message sent failure(mobile:{0}, name:{1}, service_type:{2}, service_item:{3}, date:{4})"
                 .format(msg.mobile, msg.name, msg.service_type_name, msg.service_item_name, msg.next_time_date))


if __name__ == '__main__':
    log = get_logger()
    conn = psycopg2.connect(DB_PARA)
    cur = conn.cursor()

    cur.execute(GET_READY_MSG)
    for row in cur.fetchall():
        send_msg_weimi(Message(row))

    cur.close()
    conn.close()
