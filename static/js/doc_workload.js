$(function() {
    var accordion = $('#doc_workload');
    var datagrid = $('#doc_workload_table');

    var detail_toolbar = accordion.find('#detail_toolbar');
    var btn_apply = detail_toolbar.find('#modify_apply').linkbutton({iconCls: 'icon-edit', plain: true});
    var btn_modify = detail_toolbar.find('#modify').linkbutton({iconCls: 'icon-edit', plain: true});
    var btn_save = detail_toolbar.find('#save').linkbutton({iconCls: 'icon-save', plain: true});
    var btn_print = detail_toolbar.find('#print').linkbutton({iconCls: 'icon-print', plain: true});
    var apply_status = $('#apply_status');

    var form = accordion.find('#form');
    var table = accordion.find('#table');

    btn_modify.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            $.messager.alert('提示', '修改服务结果的功能有待卫生局确认开通', 'info');
        }
    });

    btn_apply.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            $.ajax({
                url: '/services/rectify_apply/', method: 'POST',
                data: {'id': selected_row['id']},
                success: function () {
                    selected_row['apply_status'] = 1;
                    apply_status.html('申请已提交，等待批准');
                    $.messager.show({title: '提示', msg: '修改服务结果的申请提交完成', timeout: 1500});
                }
            })
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row['service_item'] == '第一次产前随访') {
                form.form('submit', {
                    url: '/services/suspend_submit/', method: 'POST',
                    onSubmit: function (param) {
                        param.record_id = selected_row['id'];
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    },
                    success: function (json_data) {
                        var data = eval('(' + json_data + ')');
                        if (data.success) {
                            table.panel('refresh');
                            datagrid.datagrid('reload');
                            $.messager.show({title: '提示', msg: '第一次产前随访记录保存成功', timeout: 1000});
                        } else {
                            $.messager.alert('提示', '第一次产前随访记录保存失败', 'info');
                        }
                    }
                });
            }
            if (selected_row['service_item'] == '精神病患者健康体检') {
                form.form('submit', {
                    url: '/services/suspend_submit/', method: 'POST',
                    onSubmit: function (param) {
                        param.record_id = selected_row['id'];
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    },
                    success: function (json_data) {
                        var data = eval('(' + json_data + ')');
                        if (data.success) {
                            table.panel('refresh');
                            datagrid.datagrid('reload');
                            $.messager.show({title: '提示', msg: '重性精神疾病患者健康体检保存成功', timeout: 1000});
                        } else {
                            $.messager.alert('提示', '重性精神疾病患者健康体检保存失败', 'info');
                        }
                    }
                })
            }
            if (selected_row['service_item'] == '老年人健康体检') {
                form.form('submit', {
                    url: '/services/suspend_submit/', method: 'POST',
                    onSubmit: function (param) {
                        param.record_id = selected_row['id'];
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    },
                    success: function (json_data) {
                        var data = eval('(' + json_data + ')');
                        if (data.success) {
                            table.panel('refresh');
                            datagrid.datagrid('reload');
                            $.messager.show({title: '提示', msg: '老年人健康体检保存成功', timeout: 1000});
                        } else {
                            $.messager.alert('提示', '老年人健康体检保存失败', 'info');
                        }
                    }
                })
            }
        }
    });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            table.find('.print_area').printThis();
        }
    });

    var selected_row = undefined;
    datagrid.datagrid({
        url: '/services/doc_workload_list/', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'apply_status', title: '修改申请', hidden: true},
            { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                switch (value) {
                    case null: return '未建档';
                    case '13108200000000000': return '未编号';
                    default : return value;
                }
            } },
            { field: 'resident_name', title: '居民', width: 4 },
            { field: 'doctor_name', title: '医生', width: 4 },
            { field: 'service_type', title: '类别', width: 10 },
            { field: 'service_item', title: '项目', width: 10 },
            { field: 'submit_time', title: '服务时间', width: 8 },
            { field: 'status', title: '状态', width: 4 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = row;
            }
        }
    });

    accordion.accordion({
        onSelect: function (title, index) {
            if (index == 1) {
                if (selected_row) {
                    table.panel({
                        href: '/services/record_detail_review/', method: 'POST',
                        queryParams: {record_id: selected_row['id']},
                        onLoad: function () {
                            if (form.find('input').length > 0) {
                                btn_save.show();
                                btn_apply.hide();
                                btn_modify.hide();
                                btn_print.linkbutton('disable');
                            } else {
                                btn_save.hide();
                                btn_apply.show();
                                switch (selected_row['apply_status']) {
                                    case 1: apply_status.html('申请已提交，等待批准'); break;
                                    case 2: apply_status.html('申请已取消'); break;
                                    case 3: apply_status.html('申请已批准'); btn_modify.linkbutton('enable'); break;
                                    case 4: apply_status.html('申请未批准'); break;
                                    case 5: apply_status.html('修改已完成'); break;
                                    case 6: apply_status.html('申请已过期'); break;
                                    default : btn_apply.linkbutton('enable');
                                }
                                btn_print.linkbutton('enable');
                            }
                        }
                    });
                } else {
                    $.messager.alert('提示', '请先选择记录，再查看内容', 'info');
                }
            }
            if (index == 0) {
                apply_status.html('');
                table.panel('clear');
            }
        }
    })

});
