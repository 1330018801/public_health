$(function() {
    var accordion = $('#doc_workload');
    var datagrid = $('#doc_workload_table');

    var detail_toolbar = accordion.find('#detail_toolbar');
    var btn_apply = detail_toolbar.find('#modify_apply');
    var btn_modify = detail_toolbar.find('#modify');
    var btn_print = detail_toolbar.find('#print');
    var apply_status = $('#apply_status');

    var form = accordion.find('#form');
    var table = accordion.find('#table');

    btn_apply.linkbutton({iconCls: 'icon-edit', plain: true});
    btn_modify.linkbutton({iconCls: 'icon-edit', plain: true});
    btn_print.linkbutton({iconCls: 'icon-print', plain: true});
    btn_apply.linkbutton('disable');
    btn_modify.linkbutton('disable');

    btn_modify.bind('click', function () {
        $.messager.alert('提示', '修改服务结果的功能有待卫生局确认开通', 'info');
    });

    btn_apply.bind('click', function () {
        $.ajax({
            url: '/services/rectify_apply/', method: 'POST',
            data: {'id': selected_row['id']},
            success: function () {
                selected_row['apply_status'] = 1;
                apply_status.html('申请已提交，等待批准');
                $.messager.show({title: '提示', msg: '修改服务结果的申请提交完成', timeout: 1500});
            }
        })
    });

    btn_print.bind('click', function () {
        table.find('.print_area').printThis();
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
        onBeforeLoad: function (param) {},
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = row;
            }
        },
        onDblClickRow: function (index, row) {
            /*
            var detail = $('#record_detail_review').dialog({
                title: '服务详情', width: 820, height: 500, method: 'POST', modal: true,
                href: '/ehr/record_detail_review/',
                queryParams: {record_id: row['id']},
                buttons: [{
                    text: '打印', iconCls: 'icon-print',
                    handler: function () {
                        detail.find('.print_area').printThis();
                    }
                },{
                    text: '关闭', iconCls: 'icon-cancel',
                    handler: function () {
                        detail.dialog('close');
                    }
                }]
            });
            detail.css('display', 'block');
            detail.dialog('center');
            */
        }
    });

    accordion.accordion({
        onSelect: function (title, index) {
            if (index == 1) {
                if (selected_row) {
                    table.panel({
                        href: '/services/record_detail_review/', method: 'POST',
                        queryParams: {record_id: selected_row['id']}
                    });
                    switch (selected_row['apply_status']) {
                        case 1: apply_status.html('申请已提交，等待批准'); break;
                        case 2: apply_status.html('申请已取消'); break;
                        case 3: apply_status.html('申请已批准'); btn_modify.linkbutton('enable'); break;
                        case 4: apply_status.html('申请未批准'); break;
                        case 5: apply_status.html('修改已完成'); break;
                        case 6: apply_status.html('申请已过期'); break;
                        default : btn_apply.linkbutton('enable');
                    }
                } else {
                    $.messager.alert('提示', '请先选择记录，再查看内容', 'info');
                }
            }
            if (index == 0) {
                apply_status.html('');
                btn_apply.linkbutton('disable');
                btn_modify.linkbutton('disable');
                table.panel('clear');
            }
        }
    })

});
