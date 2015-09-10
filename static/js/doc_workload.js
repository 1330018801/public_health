$(function() {
    var btn_edit = $('#edit');
    var query_name = $('#query_name');
    var query_identity = $('#query_identity');
    var btn_query = $('#query');
    var datagrid = $('#doc_workload_table');
    var toolbar = $('#doc_workload_toolbar');
    var user_id = toolbar.find('input[name=user_id]').val();

    btn_edit.linkbutton({plain: true, iconCls: 'icon-edit'});
    btn_edit.linkbutton('disable');

    btn_query.linkbutton({plain: true, iconCls: 'icon-search'});

    query_name.textbox();
    query_identity.textbox();

    var selected_row = undefined;

    datagrid.datagrid({
        url: '/services/doc_workload_list/', rownumbers: true, singleSelect: true, fitColumns: true,
        toolbar: '#doc_workload_toolbar',
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                switch (value) {
                    case null: return '未建档';
                    case '13108200000000000': return '未编号';
                    default : return value;
                }
            } },
            { field: 'resident_name', title: '居民姓名', width: 4 },
            { field: 'doctor_name', title: '服务提供者', width: 4 },
            { field: 'service_type', title: '服务类别', width: 10 },
            { field: 'service_item', title: '服务项目', width: 10 },
            { field: 'submit_time', title: '服务时间', width: 8 }
        ]],
        onBeforeLoad: function (param) {
            param.user_id = user_id;
        },
        onClickRow: function (index, row) {
            //selected_row = (selected_row == row) ? undefined : row;
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
                btn_edit.linkbutton('disable');
            } else {
                selected_row = row;
                btn_edit.linkbutton('enable');
            }
        },
        onDblClickRow: function (index, row) {
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
        }
    });

});
