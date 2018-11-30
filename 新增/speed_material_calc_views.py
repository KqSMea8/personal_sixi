# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
import logging

from dataCalculate.storage import *
from django.http import JsonResponse
from django.shortcuts import render


logger = logging.getLogger('django')


@login_required(login_url='/login')
def speed_materiel_calc_view(request):
    return render(request, 'pages/speed_materiel_calc_static.html')


def show_speed_material_tag_static_date(request):
    if request.method == 'GET':
        date_dict = models.speed_material_tag_static.objects.using('cron_db').values('dt').distinct().order_by(
            '-dt')
        max_date = int(date_dict[0]['dt']) - 7
        date_week = models.speed_material_tag_static.objects.using('cron_db').filter(dt__gt=max_date).values(
            'dt').distinct().order_by(
            '-dt')
        dts = []
        for date in date_week:
            dts.append(date['dt'])
        result = {'dts': json.dumps(dts)}
        return JsonResponse(result)


def show_speed_material_tag_static(request):
    if request.method == 'GET':
        dt = request.GET.get('dt')
        tag_id = []
        exposure_clac = []
        exposure_num = []
        click_num = []
        forwards = []
        comment = []
        commend = []
        k_exposure_click = []
        k_exposure_inter = []
        tag_list = models.speed_material_tag_static.objects.using('cron_db').filter(dt=dt).order_by('-exposure_num')
        for tag in tag_list:
            tag_id.append(tag.tag_id)
            exposure_clac.append(tag.exposure_clac)
            exposure_num.append(tag.exposure_num)
            click_num.append(tag.click_num)
            forwards.append(tag.forward)
            comment.append(tag.comment)
            commend.append(tag.commend)
            k_exposure_click.append(tag.k_exposure_click)
            k_exposure_inter.append(tag.k_exposure_inter)

        result = {'tag_id': json.dumps(tag_id),
                  'exposure_clac': json.dumps(exposure_clac),
                  'exposure_num':json.dumps(exposure_num),
                  'click_num':json.dumps(click_num),
                  'forwards': json.dumps(forwards),
                  'comment': json.dumps(comment),
                  'commend':json.dumps(commend),
                  'k_exposure_click':json.dumps(k_exposure_click),
                  'k_exposure_inter':json.dumps(k_exposure_inter)}
        return JsonResponse(result)


def show_speed_material_recall_static_date(request):
    if request.method == 'GET':
        date_dict = models.speed_material_recall_static.objects.using('cron_db').values('dt').distinct().order_by(
            '-dt')
        max_date = int(date_dict[0]['dt']) - 7
        date_week = models.speed_material_recall_static.objects.using('cron_db').filter(dt__gt=max_date).values(
            'dt').distinct().order_by(
            '-dt')
        dts = []
        for date in date_week:
            dts.append(date['dt'])
        result = {'dts': json.dumps(dts)}
        return JsonResponse(result)


def show_speed_material_recall_static(request):
    if request.method == 'GET':
        dt = request.GET.get('dt')
        recall_id = []
        exposure_clac =[]
        exposure_num = []
        click_num = []
        forwards = []
        comment = []
        commend = []
        k_exposure_click = []
        k_exposure_inter = []
        recall_list = models.speed_material_recall_static.objects.using('cron_db').filter(dt=dt)
        for recall in recall_list:
            recall_id.append(recall.recall_id)
            exposure_clac.append(recall.exposure_clac)
            exposure_num.append(recall.exposure_num)
            click_num.append(recall.click_num)
            forwards.append(recall.forward)
            comment.append(recall.comment)
            commend.append(recall.commend)
            k_exposure_click.append(recall.k_exposure_click)
            k_exposure_inter.append(recall.k_exposure_inter)

        result = {'recall_id': json.dumps(recall_id),
                  'exposure_clac': json.dumps(exposure_clac),
                  'exposure_num':json.dumps(exposure_num),
                  'click_num':json.dumps(click_num),
                  'forwards': json.dumps(forwards),
                  'comment': json.dumps(comment),
                  'commend':json.dumps(commend),
                  'k_exposure_click':json.dumps(k_exposure_click),
                  'k_exposure_inter':json.dumps(k_exposure_inter)}
        return JsonResponse(result)


@login_required(login_url='/login')
def speed_materiel_calc1_view(request):
    return render(request, 'pages/speed_materiel_calc1_static.html')
def show_speed_material_newvsold_static_date(request):
    if request.method == 'GET':
        date_dict = models.speed_material_newvsold_static.objects.using('cron_db').values('dt').distinct().order_by(
            '-dt')
        max_date = int(date_dict[0]['dt']) - 7
        date_week = models.speed_material_newvsold_static.objects.using('cron_db').filter(dt__gt=max_date).values(
            'dt').distinct().order_by(
            '-dt')
        dts = []
        for date in date_week:
            dts.append(date['dt'])
        result = {'dts': json.dumps(dts)}
        return JsonResponse(result)


def show_speed_material_newvsold_static(request):
    if request.method == 'GET':
        dt = request.GET.get('dt')
        is_newuser = request.GET.get('is_newuser')
        tag_id = []
        exposure_clac = []
        exposure_num = []
        click_num = []
        forwards = []
        comment = []
        commend = []
        k_exposure_click = []
        k_exposure_inter = []

        tag_list = models.speed_material_newvsold_static.objects.using('cron_db').filter(is_newuser=is_newuser, dt=dt)
        for tag in tag_list:
            tag_id.append(tag.tag_id)
            exposure_num.append(tag.exposure_num)
            exposure_clac.append(tag.exposure_clac)
            click_num.append(tag.click_num)
            forwards.append(tag.forward)
            comment.append(tag.comment)
            commend.append(tag.commend)
            k_exposure_click.append(tag.k_exposure_click)
            k_exposure_inter.append(tag.k_exposure_inter)

        result = {'tag_id': json.dumps(tag_id),
                  'exposure_clac':json.dumps(exposure_clac),
                  'exposure_num': json.dumps(exposure_num),
                  'click_num': json.dumps(click_num),
                  'forwards': json.dumps(forwards),
                  'comment': json.dumps(comment),
                  'commend': json.dumps(commend),
                  'k_exposure_click': json.dumps(k_exposure_click),
                  'k_exposure_inter': json.dumps(k_exposure_inter)}
        return JsonResponse(result)


@login_required(login_url='/login')
def speed_materiel_calc2_view(request):
    return render(request, 'pages/speed_materiel_calc2_static.html')


def show_speed_material_uservsvisitor_static_date(request):
    if request.method == 'GET':
        date_dict = models.speed_material_uservsvisitor_static.objects.using('cron_db').values('dt').distinct().order_by(
            '-dt')
        max_date = int(date_dict[0]['dt']) - 7
        date_week = models.speed_material_uservsvisitor_static.objects.using('cron_db').filter(dt__gt=max_date).values(
            'dt').distinct().order_by(
            '-dt')
        dts = []
        for date in date_week:
            dts.append(date['dt'])
        result = {'dts': json.dumps(dts)}
        return JsonResponse(result)


def show_speed_material_uservsvisitor_static(request):
    if request.method == 'GET':
        dt = request.GET.get('dt')
        is_user = request.GET.get('is_user')
        tag_id = []
        exposure_clac = []
        exposure_num = []
        click_num = []
        forwards = []
        comment = []
        commend = []
        k_exposure_click = []
        k_exposure_inter = []

        tag_list = models.speed_material_uservsvisitor_static.objects.using('cron_db').filter(is_user=is_user,
                                                                                              dt=dt)
        for tag in tag_list:
            tag_id.append(tag.tag_id)
            exposure_clac.append(tag.exposure_clac)
            exposure_num.append(tag.exposure_num)
            click_num.append(tag.click_num)
            forwards.append(tag.forward)
            comment.append(tag.comment)
            commend.append(tag.commend)
            k_exposure_click.append(tag.k_exposure_click)
            k_exposure_inter.append(tag.k_exposure_inter)

        result = {'tag_id': json.dumps(tag_id),
                  'exposure_clac':json.dumps(exposure_clac),
                  'exposure_num':json.dumps(exposure_num),
                  'click_num':json.dumps(click_num),
                  'forwards': json.dumps(forwards),
                  'comment': json.dumps(comment),
                  'commend':json.dumps(commend),
                  'k_exposure_click':json.dumps(k_exposure_click),
                  'k_exposure_inter':json.dumps(k_exposure_inter)}
        return JsonResponse(result)

