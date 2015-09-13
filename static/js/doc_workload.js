$(function() {
    var accordion = $('#doc_workload');
    var datagrid = $('#doc_workload_table');

    var detail_toolbar = accordion.find('#detail_toolbar');
    var btn_edit = detail_toolbar.find('#edit');
    var btn_submit = detail_toolbar.find('#submit');
    var btn_print = detail_toolbar.find('#print');

    var form = accordion.find('#form');
    var table = accordion.find('#table');

    btn_edit.linkbutton({iconCls: 'icon-edit', plain: true});
    btn_edit.linkbutton('disable');
    btn_submit.linkbutton({iconCls: 'icon-save', plain: true});
    btn_submit.linkbutton('disable');
    btn_print.linkbutton({iconCls: 'icon-print', plain: true});

    btn_submit.bind('click', function () {
        form.form('submit', {
            url: '/services/suspend_submit/', method: 'POST',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                param.record_id = selected_row['id'];
            },
            success: function (json_data) {
                var data = eval('(' + json_data + ')');
                if (data.success) {
                    table.panel({
                        href: '/services/record_detail_review/', method: 'POST',
                        queryParams: {record_id: selected_row['id']}
                    });
                    $.messager.show({title: '提示', msg: '暂存记录保存完成', timeout: 1000});
                } else {
                    $.messager.alert('提示', '暂存记录保存失败', 'info');
                }
            }
        })
    });

    var selected_row = undefined;
    datagrid.datagrid({
        url: '/services/doc_workload_list/', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
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
                btn_submit.linkbutton('disable');
            } else {
                selected_row = row;
                if (row['status'] == '完成') {
                    btn_submit.linkbutton('disable');
                } else if (row['status'] == '暂存') {
                    btn_submit.linkbutton('enable');
                }
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
                    })
                } else {
                    $.messager.alert('提示', '请先选择记录，再查看内容', 'info');
                }
            }
            if (index == 0) { table.panel('clear'); }
        }
    })

});
