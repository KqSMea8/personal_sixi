# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class blog_materiel_static(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    static_num = models.IntegerField(default=0)
    static_category = models.CharField(max_length=100, default='')
    send_num = models.IntegerField(default=0)
    not_send_num = models.IntegerField(default=0)
    low_zpz_num = models.IntegerField(default=0)
    weed_out_num = models.IntegerField(default=0)
    contribute_num = models.IntegerField(default=0)
    usable_object_num = models.IntegerField(default=0)
    level_num = models.IntegerField(default=0)


class blog_tagCategory(models.Model):
    tag_category = models.CharField(max_length=100, default='')
    tag_content = models.CharField(max_length=20, default='')
    tag_lfid = models.CharField(max_length=20, default='')


class blog_ability_tagCategory(models.Model):
    ability_tag = models.CharField(max_length=100, default='')
    ability_content = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
    category_content = models.CharField(max_length=100, default='')


class blog_rank(models.Model):
    rank_time = models.IntegerField(default=0)
    rank_category = models.CharField(default='', max_length=100)
    rank_type = models.CharField(default='', max_length=20)
    ranking = models.IntegerField(default=0)
    last_ranking = models.IntegerField(default=0)
    blog_mid = models.CharField(max_length=50, default='')
    content = models.CharField(max_length=50, default='')
    gender_static = models.CharField(max_length=200, default='')
    freq_static = models.CharField(max_length=200, default='')
    age_static = models.CharField(max_length=200, default='')
    city_static = models.CharField(max_length=200, default='')
    relay_num = models.CharField(max_length=200, default='')
    comment_num = models.CharField(max_length=200, default='')
    favour_num = models.CharField(max_length=200, default='')
    expose_num = models.CharField(max_length=200, default='')


class blog_materiels(models.Model):
    blog_mid = models.CharField(max_length=50, default='', db_index=True, primary_key=True)
    blog_summary = models.TextField()
    blog_status = models.BooleanField(default=False)
    send_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    click_send_rate = models.DecimalField(default=0.0, max_digits=5, decimal_places=3)
    content_tag = models.CharField(default='', max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    usable_object_name = models.TextField(default='')
    location_filter = models.CharField(default='', max_length=50)
    relay_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    favour_num = models.IntegerField(default=0)
    expose_num = models.IntegerField(default=0)
    is_checked = models.IntegerField(default=0)  # push_model物料是否下线 1：下线 0：在线


class black_relation():
    from_uid = ''
    to_uid = ''


class similarity_user():
    uid = ''
    nick = ''
    similarity = ''


class blog_interaction(models.Model):
    blog_mid = models.CharField(max_length=50, default='')
    relay_num = models.CharField(max_length=200, default='')
    comment_num = models.CharField(max_length=200, default='')
    favour_num = models.CharField(max_length=200, default='')
    expose_num = models.CharField(max_length=200, default='')
    create_time = models.DateTimeField(auto_now_add=True)


class permission(models.Model):
    class Meta:
        permissions = (
            ('view_keyword', 'can see keyword blacklist'),
            ('view_black_user', 'can see user blacklist'),
            ('view_black_relation', 'can see relation blacklist'),
            ('view_relation_blog_remove', 'can see remove_blog_relation'),
            ('view_interest_blog_remove', 'can see remove_blog_interest'),
            ('view_dashboard', 'can see materiel and rank static'),
            ('remove_keyword', 'can remove keyword blacklist'),
            ('remove_black_user', 'can remove user blacklist'),
            ('remove_black_relation', 'can remove relation blacklist'),
            ('push_blog', 'can push blog'),
            ('view_potential_info', 'can see potential info'),
            ('view_collaborative_user_static', 'can see collaborative_user'),
            ('view_collaborative_monitor_static', 'can see collaborative_monitor'),
            ('view_contribute_static', 'can see contribute_static'),
            ('view_materiel_static', 'can see materiel_static'),
            ('view_recall_static', 'can see recall_static'),
            ('view_push_accept_total', 'can see push_accept_total'),
            ('view_rank_ability_static', 'can see rank_ability_static'),
            ('view_material_feature_static', 'can see material_feature_static'),
            ('view_user_feature_static', 'can see user_feature_static'),
            ('view_add_gold_v_user_tag', 'can see add_gold_v_user_tag_audit'),
            ('view_push_strategy_static', 'can see push_strategy_static'),
            ('view_push_click_tag_static', 'can see push_click_tag_static'),
            ('view_mobile_click_static', 'can see mobile_click_static'),

        )


class blog_contribute_static(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    static_category = models.CharField(max_length=100, default='')
    contribute_num = models.IntegerField(default=0)
    classA_num = models.IntegerField(default=0)
    classB_num = models.IntegerField(default=0)
    classC_num = models.IntegerField(default=0)
    classD_num = models.IntegerField(default=0)


class blog_recall_static(models.Model):
    static_time = models.DateTimeField(auto_now_add=False)
    static_group = models.CharField(max_length=100, default='')
    select_number_of_mblog = models.IntegerField(default=0)
    calc_number_of_people = models.IntegerField(default=0)
    select_number_of_people = models.IntegerField(default=0)
    calc_number_of_message = models.IntegerField(default=0)
    select_number_of_message = models.IntegerField(default=0)


class blog_category_rank(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    rank_type = models.CharField(max_length=100, default='')
    ranking = models.IntegerField(default=0)
    blog_mid = models.CharField(max_length=50, default='')
    send_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    rate_num = models.CharField(max_length=50, default='')


class blog_relation_rank(models.Model):
    ranking = models.IntegerField(default=0)
    uid = models.CharField(max_length=50, default='')
    uname = models.CharField(max_length=50, default='')
    blog_mid = models.CharField(max_length=50, default='')
    blog_summary = models.TextField(default='None')
    send_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    click_send_rate = models.CharField(max_length=50, default='')


class blog_mbloger_ability_static(models.Model):
    rank_type = models.CharField(max_length=100, default='')
    uid = models.CharField(max_length=50, default='')
    uname = models.CharField(max_length=50, default='')
    weight = models.CharField(max_length=50, default='')
    weight_r = models.CharField(max_length=50, default='')
    weight_c = models.CharField(max_length=50, default='')
    score = models.CharField(max_length=50, default='')
    reason = models.CharField(max_length=50, default='')
    zpz_count = models.IntegerField(default=0)
    fans_count = models.IntegerField(default=0)
    hot_score = models.IntegerField(default=0)
    is_checked = models.IntegerField(default=0)


class blog_collaborative_user(models.Model):
    user_date = models.TextField(max_length=50, default='')
    push_num = models.IntegerField(default=0)
    send_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    click_send_rate = models.CharField(max_length=50, default='')


class blog_collaborative_monitor(models.Model):
    monitor_date = models.TextField(max_length=50, default='')
    rank_type = models.CharField(max_length=100, default='')
    push_num = models.IntegerField(default=0)
    send_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    click_send_rate = models.CharField(max_length=50, default='')


class blog_push_accept_total(models.Model):
    push_date = models.TextField(max_length=50, default='')
    user_num = models.CharField(max_length=100, default='')
    supply_user_num = models.IntegerField(default=0)
    model_user_num = models.IntegerField(default=0)
    calc_num = models.IntegerField(default=0)
    score_user_num = models.IntegerField(default=0)
    real_push_num = models.IntegerField(default=0)
    freq_aver_score = models.CharField(max_length=100, default='')
    model_push_aver_score = models.CharField(max_length=100, default='')


class tag_recommend(models.Model):
    tag = models.CharField(max_length=50, default='')
    uid = models.CharField(max_length=50, default='')
    nick = models.CharField(max_length=50, default='')
    state = models.IntegerField(default=1)


class blog_update_time(models.Model):
    update_type = models.CharField(max_length=100, default='')
    update_time = models.DateTimeField(auto_now_add=True)


class blog_user_feature(models.Model):
    feature_date = models.TextField(max_length=50, default='')
    push_uid = models.CharField(max_length=50, default='')
    push_user_freq = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    reg_prov_code = models.CharField(max_length=50, default='')
    interest_cat = models.CharField(max_length=50, default='')
    interest_tag = models.CharField(max_length=50, default='')
    interest_obj = models.CharField(max_length=50, default='')
    reg_city_code = models.CharField(max_length=50, default='')
    lbs_prov_code = models.CharField(max_length=50, default='')
    lbs_city_code = models.CharField(max_length=50, default='')
    short_interest_cat = models.CharField(max_length=50, default='')
    short_interest_tag = models.CharField(max_length=50, default='')
    short_interest_obj = models.CharField(max_length=50, default='')


class blog_material_feature(models.Model):
    feature_time = models.DateTimeField(auto_now_add=True)
    mid = models.CharField(max_length=50, default='')
    uid = models.CharField(max_length=50, default='')
    expose_num = models.CharField(max_length=50, default='')
    like_num = models.CharField(max_length=50, default='')
    ret_num = models.CharField(max_length=50, default='')
    cmt_num = models.CharField(max_length=50, default='')
    mbloger_avg_click_ratio = models.CharField(max_length=50, default='')
    push_rate = models.CharField(max_length=50, default='')
    like_rate = models.CharField(max_length=50, default='')
    freq_click_ratio = models.CharField(max_length=50, default='')
    update_time = models.CharField(max_length=50, default='')
    segment = models.CharField(max_length=50, default='')
    ruku_time = models.CharField(max_length=50, default='')
    push_send_num = models.CharField(max_length=50, default='')
    ret_num_weight = models.CharField(max_length=50, default='')
    cmt_num_weight = models.CharField(max_length=50, default='')
    mblog_hot_weight = models.CharField(max_length=50, default='')
    time_weight = models.CharField(max_length=50, default='')
    like_num_weight = models.CharField(max_length=50, default='')
    has_topic = models.CharField(max_length=50, default='')
    main_feed_act_rate = models.CharField(max_length=50, default='')
    hot_like_num_1h = models.CharField(max_length=50, default='')
    hot_ret_num_1h = models.CharField(max_length=50, default='')
    hot_cmt_num_1h = models.CharField(max_length=50, default='')
    hot_cmt_num = models.CharField(max_length=50, default='')
    hot_like_num = models.CharField(max_length=50, default='')
    hot_ret_num = models.CharField(max_length=50, default='')
    is_weekend = models.CharField(max_length=50, default='')
    mblog_cate_vector = models.CharField(max_length=50, default='')
    to_ids = models.CharField(max_length=50, default='')
    user_ctype = models.CharField(max_length=50, default='')
    user_vtype = models.CharField(max_length=50, default='')
    act_num = models.CharField(max_length=50, default='')
    user_hot = models.CharField(max_length=50, default='')
    pic_num = models.CharField(max_length=50, default='')
    push_type_rate = models.CharField(max_length=50, default='')
    level_id = models.CharField(max_length=50, default='')
    summary = models.CharField(max_length=50, default='')
    cmt_rate = models.CharField(max_length=50, default='')
    age_click_ratio = models.CharField(max_length=50, default='')
    ret_num_1h = models.CharField(max_length=50, default='')
    act_rate_1h = models.CharField(max_length=50, default='')
    expose_num_1h = models.CharField(max_length=50, default='')
    like_num_1h = models.CharField(max_length=50, default='')
    ret_rate_1h = models.CharField(max_length=50, default='')
    cmt_num_1h = models.CharField(max_length=50, default='')
    like_rate_1h = models.CharField(max_length=50, default='')
    act_num_1h = models.CharField(max_length=50, default='')
    cmt_rate_1h = models.CharField(max_length=50, default='')
    mblog_city_vector = models.CharField(max_length=50, default='')
    has_title = models.CharField(max_length=50, default='')
    pro_id = models.CharField(max_length=50, default='')
    has_article = models.CharField(max_length=50, default='')
    pid_click_ratio = models.CharField(max_length=50, default='')
    push_group_click_num = models.CharField(max_length=50, default='')
    hot_feed_act_rate = models.CharField(max_length=50, default='')
    create_time = models.CharField(max_length=50, default='')
    is_long_pic = models.CharField(max_length=50, default='')
    push_tag_rate = models.CharField(max_length=50, default='')
    lbs_info = models.CharField(max_length=50, default='')
    is_gif = models.CharField(max_length=50, default='')
    has_video = models.CharField(max_length=50, default='')
    ret_rate = models.CharField(max_length=50, default='')
    push_group_rate = models.CharField(max_length=50, default='')
    class_level1 = models.CharField(max_length=50, default='')
    summary_segment = models.CharField(max_length=50, default='')
    act_rate = models.CharField(max_length=50, default='')
    push_group_send_num = models.CharField(max_length=50, default='')
    city_id = models.CharField(max_length=50, default='')
    text_length = models.CharField(max_length=50, default='')
    conf_act_rate = models.CharField(max_length=50, default='')
    has_link = models.CharField(max_length=50, default='')
    user_reg_pro = models.CharField(max_length=50, default='')
    source = models.CharField(max_length=50, default='')
    cid_click_ratio = models.CharField(max_length=50, default='')
    mblog_user_C1_vector = models.CharField(max_length=50, default='')
    user_reg_city = models.CharField(max_length=50, default='')
    push_click_num = models.CharField(max_length=50, default='')
    gender_click_ratio = models.CharField(max_length=50, default='')


class gold_v_user(models.Model):
    uid = models.CharField(max_length=50, default='')
    tag = models.CharField(max_length=50, default='')
    weight = models.FloatField(default=0.0)
    is_checked = models.IntegerField(default=0)


class blog_mbloger_tag_category(models.Model):
    category_content = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
    tag_content = models.CharField(max_length=100, default='')
    tag = models.CharField(max_length=100, default='')


class gold_v_user_tag_audit(models.Model):
    uid = models.CharField(max_length=50, default='')
    nick = models.CharField(max_length=50, default='')
    cat = models.CharField(max_length=50, default='')
    tag = models.CharField(max_length=50, default='')
    cat_weight = models.FloatField(default=0.0)
    tag_weight = models.FloatField(default=0.0)
    is_checked = models.IntegerField(default=0)  # 0:未审核，1:已通过，2:已拒绝


class push_strategy_static(models.Model):
    team = models.CharField(max_length=50, default='')
    push_type = models.CharField(max_length=50, default='')
    push_date = models.TextField(max_length=50, default='')
    interest_num = models.TextField(max_length=50, default='')
    relate_num = models.TextField(max_length=50, default='')
    contrast_interest_num = models.TextField(max_length=50, default='')
    contrast_relate_num = models.TextField(max_length=50, default='')


class f_user_audit(models.Model):
    uid = models.CharField(max_length=50, default='')
    nick = models.CharField(max_length=50, default='')
    cat = models.CharField(max_length=50, default='')
    tag = models.CharField(max_length=50, default='')
    cat_weight = models.FloatField(default=0.0)
    tag_weight = models.FloatField(default=0.0)
    tag_checked = models.IntegerField(default=0)  # 0:未审核，1:已通过，2:已拒绝，3:线上淘汰
    source = models.CharField(max_length=50, default='')
    audit_description = models.CharField(max_length=100, default='')


class push_click_tag_static(models.Model):
    category = models.CharField(max_length=50, default='')
    category_name = models.TextField(max_length=50, default='')
    push_date = models.TextField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    push_num = models.CharField(max_length=50, default='')
    accept_push_user = models.CharField(max_length=50, default='')
    material_num = models.CharField(max_length=50, default='')
    aver_push = models.CharField(max_length=50, default='')
    click_rate_now = models.CharField(max_length=50, default='')
    click_rate_forecast = models.CharField(max_length=50, default='')


class interest_timely_push_data(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='')
    category_name = models.TextField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    push_num = models.CharField(max_length=50, default='')
    accept_push_user = models.CharField(max_length=50, default='')
    material_num = models.CharField(max_length=50, default='')
    aver_push = models.CharField(max_length=50, default='')
    click_rate_now = models.CharField(max_length=50, default='')
    click_rate_forecast = models.CharField(max_length=50, default='')


class mobile_click_static(models.Model):
    push_date = models.TextField(max_length=50, default='')
    luicode = models.CharField(max_length=50, default='')
    not_immidiate = models.CharField(max_length=50, default='')
    push_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    click_rate = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')  # version:机型、factory:厂商、system:系统
    system = models.CharField(max_length=50, default='')
    factory = models.CharField(max_length=50, default='')
    version = models.CharField(max_length=50, default='')


class interest_timely_push_each_data(models.Model):
    push_date = models.TextField(max_length=50, default='')
    mid = models.CharField(max_length=50, default='')
    start_time = models.CharField(max_length=50, default='')
    paperwork = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=50, default='')
    mater_type = models.CharField(max_length=50, default='')
    timely_click = models.CharField(max_length=50, default='')
    timely_push = models.CharField(max_length=50, default='')
    timely_click_rate = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    push_round = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')


class mobile_user_portrait_static(models.Model):
    push_date = models.TextField(max_length=50, default='')
    portrait_type = models.CharField(max_length=50, default='')  # age; gender; category; province
    type = models.CharField(max_length=50, default='')  # version:机型、factory:厂商、system:系统
    system = models.CharField(max_length=50, default='')
    factory = models.CharField(max_length=50, default='')
    version = models.CharField(max_length=50, default='')
    system_account = models.CharField(max_length=500, default='')
    factory_account = models.CharField(max_length=500, default='')
    version_account = models.CharField(max_length=500, default='')


class strategy_recommend(models.Model):
    strategy_type = models.CharField(max_length=50, default='')
    strategy_date = models.TextField(max_length=100, default='')
    recommend_num = models.CharField(max_length=50, default='')
    follow_people = models.CharField(max_length=50, default='0')
    follow_num = models.CharField(max_length=50, default='')
    follow_ratio = models.CharField(max_length=50, default='0.0')
    unfollow_num = models.CharField(max_length=50, default='')
    unfollow_ratio = models.CharField(max_length=50, default='0.0')


class relation_interest_category(models.Model):
    update_date = models.TextField(max_length=50, default='')
    data_type = models.CharField(max_length=50, default='')
    all_user_num = models.CharField(max_length=50, default='')
    interest_cat_select_num = models.CharField(max_length=50, default='')
    cat_select_user_num = models.CharField(max_length=50, default='')
    all_cat_select_num = models.CharField(max_length=50, default='')
    aver_user_select_cat_num = models.CharField(max_length=50, default='')
    mbloger_expose_num = models.CharField(max_length=50, default='')
    aver_mbloger_expose_num = models.CharField(max_length=50, default='')
    aver_interest_mbloger_expose_num = models.CharField(max_length=50, default='')
    interest_cat_mbloger_atten_num = models.CharField(max_length=50, default='')
    interest_mbloger_atten_num = models.CharField(max_length=50, default='')
    aver_interest_cat_mbloger_atten = models.CharField(max_length=50, default='')
    aver_interest_mbloger_atten_num = models.CharField(max_length=50, default='')
    interest_mbloger_cancel_atten_pair = models.CharField(max_length=50, default='')
    interest_user_mbloger_cancel_atten_pair = models.CharField(max_length=50, default='')
    aver_interest_mbloger_cancel_atten = models.CharField(max_length=50, default='')
    aver_interest_user_mbloger_cancel_atten = models.CharField(max_length=50, default='')
    untag_user_expose = models.CharField(max_length=50, default='')
    untag_user_follow = models.CharField(max_length=50, default='')


class speed_tag_category_dict(models.Model):
    category_id = models.CharField(max_length=100, default='')
    category_name = models.CharField(max_length=100, default='')


class speed_material_static(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='')
    category_mid_num = models.IntegerField(default=0)
    recall = models.CharField(max_length=100, default='')
    recall_mid_num = models.IntegerField(default=0)
    feature = models.CharField(max_length=100, default='')
    feature_mid_num = models.IntegerField(default=0)


class speed_material_change(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='')
    category_add_num = models.IntegerField(default=0)
    category_offline_num = models.IntegerField(default=0)
    recall = models.CharField(max_length=100, default='')
    recall_add_num = models.IntegerField(default=0)
    recall_offline_num = models.IntegerField(default=0)
    feature = models.CharField(max_length=100, default='')
    feature_add_num = models.IntegerField(default=0)
    feature_offline_num = models.IntegerField(default=0)


class day_mobile_click_static(models.Model):
    calc_date = models.TextField(max_length=50, default='')
    push_date = models.TextField(max_length=50, default='')
    luicode = models.CharField(max_length=50, default='')
    not_immidiate = models.CharField(max_length=50, default='')
    push_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    click_rate = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')  # version:机型、factory:厂商、system:系统
    system = models.CharField(max_length=50, default='')
    factory = models.CharField(max_length=50, default='')
    version = models.CharField(max_length=50, default='')


class mobile_weibo_version(models.Model):
    push_date = models.TextField(max_length=50, default='')
    dt = models.TextField(max_length=50, default='')
    version = models.CharField(max_length=50, default='')  # 版本
    is_vivo = models.CharField(max_length=50, default='')
    push_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    click_rate = models.CharField(max_length=50, default='')


class total_push_click(models.Model):
    static_time = models.DateTimeField(auto_now_add=True)
    push_date = models.TextField(max_length=50, default='')
    click_num = models.IntegerField(default=0)


class blog_to_id_category(models.Model):
    to_id = models.CharField(max_length=100, default='')
    category_name = models.CharField(max_length=100, default='')


class team_push_static(models.Model):
    uid = models.CharField(max_length=50, default='')
    push_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    interest_push_num = models.IntegerField(default=0)
    interest_click_num = models.IntegerField(default=0)
    relation_push_num = models.IntegerField(default=0)
    relation_click_num = models.IntegerField(default=0)
    date = models.TextField(max_length=20, default='')
    type = models.TextField(max_length=10, default='')  # online,offline


class team_push_info(models.Model):
    uid = models.CharField(max_length=50, default='')
    mid = models.CharField(max_length=50, default='')
    luicode = models.CharField(max_length=20, default='')
    content = models.CharField(max_length=200, default='')
    send_time = models.CharField(max_length=20, default='')
    click_time = models.CharField(max_length=20, default='0')
    date = models.TextField(max_length=20, default='')
    type = models.TextField(max_length=10, default='')  # online,offline


class team_info(models.Model):
    uid = models.CharField(max_length=50, default='')
    nick = models.CharField(max_length=50, default='')
    dept = models.CharField(max_length=50, default='')


class team_feed_info(models.Model):
    uid = models.CharField(max_length=50, default='')
    mid = models.CharField(max_length=50, default='')
    content = models.CharField(max_length=200, default='')
    time = models.CharField(max_length=50, default='')
    order = models.IntegerField(default=0)
    is_click = models.IntegerField(default=0)
    is_repost = models.IntegerField(default=0)
    is_comment = models.IntegerField(default=0)
    is_like = models.IntegerField(default=0)
    date = models.TextField(max_length=20, default='')


class team_feed_static(models.Model):
    uid = models.CharField(max_length=50, default='')
    time = models.CharField(max_length=50, default='')
    mid_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)
    interactive_num = models.IntegerField(default=0)
    repost_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    like_num = models.IntegerField(default=0)
    date = models.TextField(max_length=20, default='')


class speed_material_tag_static(models.Model):
    dt = models.CharField(max_length=50, default='')
    tag_id = models.CharField(max_length=50, default='')
    exposure_clac = models.CharField(max_length=50, default='') #新增曝光个数
    exposure_num = models.CharField(max_length=50, default='0.0')
    click_num = models.CharField(max_length=50, default='0.0')
    forward = models.CharField(max_length=50, default='0.0')
    comment = models.CharField(max_length=50, default='0.0')
    commend = models.CharField(max_length=50, default='0.0')
    k_exposure_click = models.CharField(max_length=50, default='0.0')
    k_exposure_inter = models.CharField(max_length=50, default='0.0')
    

class speed_material_recall_static(models.Model):
    dt = models.CharField(max_length=50, default='')
    recall_id = models.CharField(max_length=50, default='')
    exposure_clac = models.CharField(max_length=50, default='') #新增曝光个数
    exposure_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    forward = models.CharField(max_length=50, default='')
    comment = models.CharField(max_length=50, default='')
    commend = models.CharField(max_length=50, default='')
    k_exposure_click = models.CharField(max_length=50, default='')
    k_exposure_inter = models.CharField(max_length=50, default='')


class speed_material_newvsold_static(models.Model):
    dt = models.CharField(max_length=50, default='')
    tag_id = models.CharField(max_length=50, default='')
    is_newuser = models.CharField(max_length=50, default='')
    exposure_clac = models.CharField(max_length=50, default='')  # 新增曝光个数
    exposure_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    forward = models.CharField(max_length=50, default='')
    comment = models.CharField(max_length=50, default='')
    commend = models.CharField(max_length=50, default='')
    k_exposure_click = models.CharField(max_length=50, default='')
    k_exposure_inter = models.CharField(max_length=50, default='')


class speed_material_uservsvisitor_static(models.Model):
    dt = models.CharField(max_length=50, default='')
    tag_id = models.CharField(max_length=50, default='')
    is_user = models.CharField(max_length=50, default='')
    exposure_clac = models.CharField(max_length=50, default='')  # 新增曝光个数
    exposure_num = models.CharField(max_length=50, default='')
    click_num = models.CharField(max_length=50, default='')
    forward = models.CharField(max_length=50, default='')
    comment = models.CharField(max_length=50, default='')
    commend = models.CharField(max_length=50, default='')
    k_exposure_click = models.CharField(max_length=50, default='')
    k_exposure_inter = models.CharField(max_length=50, default='')


