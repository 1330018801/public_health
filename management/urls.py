# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from management import views


urlpatterns = patterns('',
    url(r'^admin_nav/$', views.admin_nav, name='admin_nav'),

    # 下拉列表选项
    url(r'^town_clinic_options/$', views.town_clinic_options, name='town_clinic_options'),
    url(r'^village_clinic_options/$', views.village_clinic_options, name='village_clinic_options'),
    url(r'^village_clinic_list/$', views.village_clinic_list, name='village_clinic_list'),
    url(r'^get_town_clinics_edit/$', views.town_clinic_options, name='town_clinic_options'),
    url(r'^get_town_village_clinics_edit/$', views.get_town_village_clinics_edit, name='get_town_village_clinics_edit'),
    url(r'^get_town_village_clinics/(?P<town_clinic_id>\d+)/$', views.get_town_village_clinics, name='get_town_village_clinics'),
    url(r'^get_towns/$', views.town_options, name='town_options'),
    url(r'^get_town_villages/(?P<town_id>\d+)/$', views.town_village_options, name='town_village_options'),
    url(r'^get_town_villages_edit/$', views.town_name_village_options, name='town_village_options'),
    url(r'^get_town_clinics/$', views.town_clinic_options, name='town_clinic_options'),
    url(r'^get_town_clinic_edit/$', views.town_clinic_options, name='get_town_clinic_edit'),

    url(r'^service_type_options/$', views.service_type_options, name='service_type_options'),
    url(r'^service_item_options/$', views.service_item_options, name='service_item_options'),

    url(r'^get_roles/$', views.get_roles, name='get_roles'),


    # 管理员工作界面中，对系统中居民的操作
    url(r'^residents/$', views.residents_page, name='residents_page'),
    url(r'^resident_add/$', views.resident_add, name='resident_add'),
    url(r'^resident_update/$', views.resident_update, name='resident_update'),
    url(r'^resident_del/$', views.resident_del, name='resident_del'),
    url(r'^resident_query/$', views.resident_query, name='resident_query'),
    url(r'^resident_query_list/$', views.resident_query_list, name='resident_query_list'),
    url(r'^resident_add_hypertension/$', views.resident_add_hypertension, name='resident_add_hypertension'),
    url(r'^resident_add_diabetes/$', views.resident_add_diabetes, name='resident_add_diabetes'),
    url(r'^resident_add_psychiatric/$', views.resident_add_psychiatric, name='resident_add_psychiatric'),
    url(r'^resident_add_pregnant/$', views.resident_add_pregnant, name='resident_add_pregnant'),


    # 管理员工作界面中，乡镇卫生院管理操作
    url(r'^town_clinics/$', views.town_clinics, name='town_clinics'),
    url(r'^town_clinic_list_new/$', views.town_clinic_list, name='town_clinic_list'),

    # 管理员工作界面中，村卫生室管理操作
    url(r'^village_clinics/$', views.village_clinics_page, name='village_clinics_page'),
    url(r'^village_clinic_add/$', views.village_clinic_add, name='village_clinic_add'),
    url(r'^village_clinic_del/$', views.village_clinic_del, name='village_clinic_del'),
    url(r'^village_clinic_update/$', views.village_clinic_update, name='village_clinic_update'),

    # 管理员工作界面中，系统用户管理操作
    url(r'^users/$', views.users_page, name='users_page'),
    url(r'^user_query_list/$', views.user_query_list, name='user_query_list'),
    url(r'^user_add/$', views.user_add, name='user_add'),
    url(r'^user_del/$', views.user_del, name='user_del'),

    # 管理员工作界面中，服务类别管理操作
    url(r'^service_types/$', views.service_types_page, name='service_types_page'),
    url(r'^service_type_list_new/$', views.service_type_list, name='service_type_list'),

    # 管理员工作界面中，服务项目管理操作
    url(r'^service_item_list_new/$', views.service_item_list, name='service_item_list'),
    url(r'^service_items/$', views.service_items_page, name='service_items_page'),
    url(r'^service_item_add/$', views.service_item_add, name='service_item_add'),
    url(r'^service_item_update/$', views.service_item_update, name='service_item_update'),
    url(r'^service_item_del/$', views.service_item_del, name='service_item_del'),

    # 管理员工作界面中，服务记录明细管理操作
    url(r'^records/$', views.records_page, name='records_page'),
    url(r'^record_list/$', views.record_list, name='record_list'),

    # 管理员工作界面中，服务计费管理操作
    url(r'^payment/$', views.payment_page, name='payment_page'),
    url(r'^payment_list/$', views.payment_list, name='payment_list'),

    # 管理员工作界面中，用户角色管理操作
    url(r'^roles/$', views.roles_page, name='roles_page'),
    url(r'^role_list/$', views.role_list, name='role_list'),
    url(r'^get_role_authorize/$', views.get_role_authorize, name='get_role_authorize'),
    url(r'^role_authorize/$', views.role_authorize, name='role_authorize'),
    url(r'^role_add/$', views.role_add, name='role_add'),
    url(r'^role_del/$', views.role_del, name='role_del'),

    # 管理员工作界面中，已发送短信管理操作
    url(r'^sms_sent/$', views.sms_sent, name='sms_sent'),
    url(r'^sms_sent_list/$', views.sms_sent_list, name='sms_sent_list'),

    # 管理员工作界面中，短信设置管理操作
    url(r'^sms_setup_page/$', views.sms_setup_page, name='sms_setup_page'),
    url(r'^sms_setup_list/$', views.sms_setup_list, name='sms_setup_list'),
    url(r'^sms_setup_add/$', views.sms_setup_add, name='sms_setup_add'),
    url(r'^sms_setup_update/$', views.sms_setup_update, name='sms_setup_update'),
    url(r'^sms_setup_del/$', views.sms_setup_del, name='sms_setup_del'),

    # 管理员工作界面中，生成excel统计表格的操作
    url(r'^excel_file/$', views.excel_file, name='excel_file'),

    # 管理员工作界面中，生成统计图的操作
    url(r'^graphs/$', views.graphs, name='graphs'),
    url(r'^graph_workload/$', views.graph_workload, name='graph_workload'),
    url(r'^graph_payment/$', views.graph_payment, name='graph_payment'),

    # 生成二维统计报表所需要的函数
    url(r'^workload_stat_page/$', views.workload_stat_page, name='workload_stat_page'),  # 统计首页

    url(r'^workload_town_clinics_page/$', views.workload_town_clinics_page, name='workload_town_clinics_page'),
    url(r'^workload_town_clinics_datagrid/$', views.workload_town_clinics_datagrid,
        name='workload_town_clinics_datagrid'),  # 各卫生院各服务类别工作量二维表
    url(r'^workload_town_excel/$', views.workload_town_excel, name='workload_town_excel'),

    url(r'^workload_village_clinics_page/$', views.workload_village_clinics_page,
        name='workload_village_clinics_page'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表的页面
    url(r'^workload_village_clinics_datagrid/$', views.workload_village_clinics_datagrid,
        name='workload_village_clinics_datagrid'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表

    url(r'^workload_doctors_page/(?P<clinic_id>\d+)/$', views.workload_doctors_page,
        name='workload_doctors_page'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表的页面
    url(r'^workload_doctors_datagrid/(?P<clinic_id>\d+)/$', views.workload_doctors_datagrid,
        name='workload_doctors_datagrid'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表
    # 获取指定卫生机构的所有服务记录列表的页面
    url(r'^workload_list_page/(?P<provider_id>\d+)/$', views.workload_list_page, name='workload_list_page'),
    # 获取指定卫生机构的所有服务记录列表
    url(r'^workload_list_datagrid/(?P<provider_id>\d+)/$', views.workload_list_datagrid, name='workload_list_datagrid'),

    url(r'^resident_records_page/(?P<resident_id>\d+)/$', views.resident_records_page, name='resident_records_page'),
    url(r'^resident_records_datagrid/(?P<resident_id>\d+)/$', views.resident_records_datagrid,
        name='resident_records_datagrid'),

    url(r'^payment_stat_page/$', views.payment_stat_page, name='payment_stat_page'),  # 统计首页
    url(r'^payment_town_clinics_page/$', views.payment_town_clinics_page,
        name='payment_town_clinics_page'),  # 各卫生院各服务类别支付金额二维表
    url(r'^payment_town_clinics_datagrid/$', views.payment_town_clinics_datagrid,
        name='payment_town_clinics_datagrid'),  # 各卫生院各服务类别支付金额二维表
    url(r'^payment_town_excel/$', views.payment_town_excel, name='payment_town_excel'),


    url(r'^payment_village_clinics_page/$', views.payment_village_clinics_page,
        name='payment_village_clinics_page'),  # 各卫生院各服务类别支付金额二维表
    url(r'^payment_village_clinics_datagrid/$', views.payment_village_clinics_datagrid,
        name='payment_village_clinics_datagrid'),  # 各卫生院各服务类别支付金额二维表

    # 管理员工作界面中，修改服务记录结果申请的管理操作
    url(r'^modify_apply_page/$', views.modify_apply_page, name='modify_apply_page'),
    url(r'^modify_apply_list/$', views.modify_apply_list, name='modify_apply_list'),
    url(r'^modify_apply_opinion/$', views.modify_apply_opinion, name='modify_apply_opinion'),


)