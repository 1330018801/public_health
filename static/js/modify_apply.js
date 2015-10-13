$(function() {
    var toolbar = $('#modify_apply_toolbar');
    var datagrid = $('#modify_apply_datagrid');

    var btn_agree = toolbar.find('#btn_agree');
    var btn_disagree = toolbar.find('#btn_disagree');
    btn_agree.linkbutton({ plain: true, iconCls: 'icon-ok'});
    btn_disagree.linkbutton({ plain: true, iconCls: 'icon-cancel'});

    btn_agree.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row != undefined) {
                $.ajax({
                    url: '/management/modify_apply_opinion/', method: 'POST',
                    data: { opinion: 'agree', id: selected_row['id'] },
                    success: function (data) {
                        if (data.success) {
                            $.messager.show({title: '提示', msg: '批准修改申请完成', timeout: 1500});
                            datagrid.datagrid('reload');
                        } else {
                            $.messager.alert('提示', '批准修改申请失败', 'warning');
                        }
                    }
                });
            } else{
                $.messager.alert('提示', '请在列表中选择一项申请', 'info');
            }
        }
    });

    btn_disagree.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row != undefined) {
                $.ajax({
                    url: '/management/modify_apply_opinion/', method: 'POST',
                    data: { opinion: 'disagree', id: selected_row['id'] },
                    success: function (data) {
                        if (data.success) {
                            datagrid.datagrid('reload');
                            $.messager.show({title: '提示', msg: '拒绝修改申请完成', timeout: 1500});
                        } else {
                            $.messager.alert('提示', '拒绝修改申请失败', 'warning');
                        }
                    }
                });
            } else {
                $.messager.alert('提示', '请在列表中选择一项申请', 'info');
            }
        }
    });

    var selected_row = undefined;

    datagrid.datagrid({
        title: '服务结果修改申请', url: '/management/modify_apply_list/',
        toolbar: '#modify_apply_toolbar',
        rownumbers: true, singleSelect: true,  fitColumns: true,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'username', title: '用户名', width: 10 },
            { field: 'role', title: '角色', width: 10 },
            { field: 'resident', title: '居民', width: 10 },
            { field: 'town_clinic', title: '卫生院', width: 10 },
            { field: 'village_clinic', title: '卫生室', width: 10 },
            { field: 'service_type', title: '服务类别', width: 10 },
            { field: 'service_item', title: '服务项目', width: 10 },
            { field: 'apply_time', title: '申请时间', width: 10 },
            { field: 'finance_opinion', title: '财政局意见', width: 10 },
            { field: 'health_opinion', title: '卫生局意见', width: 10 },
            { field: 'status', title: '修改状态', width: 10 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = row;
            }
        },
        onBeforeLoad: function(param) {
        }
    });

});