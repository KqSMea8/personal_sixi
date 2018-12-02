# -*- coding: UTF-8 -*-
import logging
import urllib2
import json
import datetime

from dataCalculate import redis_rw2
from MaterielMonitor import models

#hhhh
logger = logging.getLogger('django')


def get_speed_material_tag_static():
    delete_old_tag_data()
    rw = redis_rw2.redis_rw()
    rw.Init_redis("rm20562.eos.grid.sina.com.cn", 20562, "rm20562.eos.grid.sina.com.cn", 20562, 86400)
    today = datetime.date.today()
    key = (today - datetime.timedelta(days=2)).strftime("%Y%m%d")+'by_tag_all'
    tag_list = rw.hgetall(key)
    if tag_list:
        for tag in tag_list:
            dt = key[0:8]
            tag_id = tag
            tag_str = rw.hget(key, tag)
            if time.time() < 1543596087:
                exposure_clac, exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter = tag_str.split(
                    '@')
            else:
                exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter, exposure_clac = tag_str.split(
                    '@')
            models.speed_material_tag_static.objects.using('cron_db').create(dt=dt,
                                                                         tag_id=tag_id,
                                                                         exposure_clac=exposure_clac,
                                                                         exposure_num=exposure_num,
                                                                         click_num=click_num,
                                                                         forward=forward,
                                                                         comment=comment,
                                                                         commend=commend,
                                                                         k_exposure_click=k_exposure_click,
                                                                         k_exposure_inter=k_exposure_inter)

    update_time = datetime.datetime.utcnow()
    models.blog_update_time.objects.create(update_type='speed_material_tag_static', update_time=update_time)


def get_speed_material_recall_static():
    delete_old_recall_data()
    rw = redis_rw2.redis_rw()
    rw.Init_redis("rm20562.eos.grid.sina.com.cn", 20562, "rm20562.eos.grid.sina.com.cn", 20562, 86400)
    today = datetime.date.today()
    key = (today - datetime.timedelta(days=2)).strftime("%Y%m%d")+'by_recall_all'
    recall_list = rw.hgetall(key)
    print(recall_list)
    if recall_list:
        for recall in recall_list:
            dt = key[0:8]
            recall_id = recall
            recall_str = rw.hget(key, recall)
            if time.time() < 1543596087:
                exposure_clac, exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter = recall_str.split(
                    '@')
            else:
                exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter, exposure_clac = recall_str.split(
                    '@')
            models.speed_material_recall_static.objects.using('cron_db').create(dt=dt,
                                                                         recall_id=recall_id,
                                                                         exposure_clac=exposure_clac,
                                                                         exposure_num=exposure_num,
                                                                         click_num=click_num,
                                                                         forward=forward,
                                                                         comment=comment,
                                                                         commend=commend,
                                                                         k_exposure_click=k_exposure_click,
                                                                         k_exposure_inter=k_exposure_inter)

    update_time = datetime.datetime.utcnow()
    models.blog_update_time.objects.create(update_type='speed_material_recall_static', update_time=update_time)


def get_speed_material_newvsold_static():
    delete_old_newvsold_data()
    rw = redis_rw2.redis_rw()
    rw.Init_redis("rm20562.eos.grid.sina.com.cn", 20562, "rm20562.eos.grid.sina.com.cn", 20562, 86400)
    today = datetime.date.today()
    key = (today - datetime.timedelta(days=2)).strftime("%Y%m%d")+'by_tag_newvsold'
    newvsold_list = rw.hgetall(key)
    if newvsold_list:
        for newvsold in newvsold_list:
            dt = key[0:8]
            tag_id = newvsold
            mid_str = rw.hget(key, newvsold)
            mid_str=mid_str.strip('{')
            mid_str = mid_str.strip('}')
            mid_str = mid_str.replace('\'', '')
            tag_str_div =mid_str.split(',')
            for tag_str_list in tag_str_div:
                is_newuser=tag_str_list.split(':')[0]
                tag_str =tag_str_list.split(':')[1]
                if time.time() < 1543596087:
                exposure_clac, exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter = tag_str.split(
                    '@')
                else:
                exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter, exposure_clac = tag_str.split(
                    '@')
                models.speed_material_newvsold_static.objects.using('cron_db').create(dt=dt,
                                                                             tag_id=tag_id,
                                                                             is_newuser=is_newuser,
                                                                             exposure_clac=exposure_clac,
                                                                             exposure_num=exposure_num,
                                                                             click_num=click_num,
                                                                             forward=forward,
                                                                             comment=comment,
                                                                             commend=commend,
                                                                             k_exposure_click=k_exposure_click,
                                                                             k_exposure_inter=k_exposure_inter)

    update_time = datetime.datetime.utcnow()
    models.blog_update_time.objects.create(update_type='speed_material_newvsold_static', update_time=update_time)


def get_speed_material_uservsvisitor_static():
    delete_old_uservsvisitor_data()
    rw = redis_rw2.redis_rw()
    rw.Init_redis("rm20562.eos.grid.sina.com.cn", 20562, "rm20562.eos.grid.sina.com.cn", 20562, 86400)
    today = datetime.date.today()
    key = (today - datetime.timedelta(days=2)).strftime("%Y%m%d")+'by_tag_uservsvisitor'
    uservsvisitor_list = rw.hgetall(key)
    if uservsvisitor_list:
        for servsvisitor in uservsvisitor_list:
            dt = key[0:8]
            tag_id = servsvisitor
            mid_str = rw.hget(key, servsvisitor)
            mid_str = mid_str.strip('{')
            mid_str = mid_str.strip('}')
            mid_str =mid_str.replace('\'','')
            tag_str_div =mid_str.split(',')
            for tag_str_list in tag_str_div:
                is_user = tag_str_list.split(':')[0]
                tag_str = tag_str_list.split(':')[1]
                if time.time() < 1543596087: 1543636856
                exposure_clac, exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter = tag_str.split(
                    '@')
                else:
                exposure_num, click_num, forward, comment, commend, k_exposure_click, k_exposure_inter, exposure_clac = tag_str.split(
                    '@')
                models.speed_material_uservsvisitor_static.objects.using('cron_db').create(dt=dt,
                                                                             tag_id=tag_id,
                                                                             is_user=is_user,
                                                                             exposure_clac=exposure_clac,
                                                                             exposure_num=exposure_num,
                                                                             click_num=click_num,
                                                                             forward=forward,
                                                                             comment=comment,
                                                                             commend=commend,
                                                                             k_exposure_click=k_exposure_click,
                                                                             k_exposure_inter=k_exposure_inter)

    update_time = datetime.datetime.utcnow()
    models.blog_update_time.objects.create(update_type='speed_material_uservsvisitor_static', update_time=update_time)



def delete_old_tag_data():
    mobile_expiration_date = (datetime.date.today() - datetime.timedelta(days=31)).strftime("%Y%m%d")
    logger.info('delete speed_material_tag_static where date < ' + str(mobile_expiration_date))
    models.speed_material_tag_static.objects.using('cron_db').filter(dt__lt=mobile_expiration_date).delete()


def delete_old_recall_data():
    mobile_expiration_date = (datetime.date.today() - datetime.timedelta(days=31)).strftime("%Y%m%d")
    logger.info('delete speed_material_recall_static where date < ' + str(mobile_expiration_date))
    models.speed_material_recall_static.objects.using('cron_db').filter(dt__lt=mobile_expiration_date).delete()


def delete_old_newvsold_data():
    mobile_expiration_date = (datetime.date.today() - datetime.timedelta(days=31)).strftime("%Y%m%d")
    logger.info('delete speed_material_newvsold_static where date < ' + str(mobile_expiration_date))
    models.speed_material_newvsold_static.objects.using('cron_db').filter(dt__lt=mobile_expiration_date).delete()


def delete_old_uservsvisitor_data():
    mobile_expiration_date = (datetime.date.today() - datetime.timedelta(days=31)).strftime("%Y%m%d")
    logger.info('delete speed_material_uservsvisitor_static where date < ' + str(mobile_expiration_date))
    models.speed_material_uservsvisitor_static.objects.using('cron_db').filter(dt__lt=mobile_expiration_date).delete()

