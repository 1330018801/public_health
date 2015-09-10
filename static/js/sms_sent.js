$(function() {
    var toolbar = $('#sms_sent_toolbar');

    toolbar.find('#sms_begin').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    toolbar.find('#sms_begin').datebox('setValue', newYearDay(new Date()));
    toolbar.find('#sms_end').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    toolbar.find('#sms_end').datebox('setValue', myformatter(new Date()));
    toolbar.find('#service_type').combobox({
        url: '/management/service_type_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': '全部'}],
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (record) {
            var query_service_item = toolbar.find('#service_item');
            query_service_item.combobox({
                onBeforeLoad: function(param) {
                    param.first_text = '全部';
                    param.query_service_type = record.id;
                }
            });
            query_service_item.combobox('reload');
            query_service_item.combobox('setValue', '0');
        }
    });
    toolbar.find('#service_item').combobox({
        url: '/management/service_item_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });
    toolbar.find('#resident').textbox({ width: 100 });
    toolbar.find('#mobile').textbox({ width: 100 });
    toolbar.find('#status').combobox({
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': "全部"}, {'id': 1, 'name': "准备发送"},
               {'id': 2, 'name': "发送完成"}, {'id': -1, 'name': "发送错误"}],
        onLoadSuccess: function() {
            $(this).combobox('setValue', '0');
        }
    });
    toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    toolbar.find('#btn_query').bind('click', function() {
        $('#sms_list').datagrid('load');
    });

    $('#sms_list').datagrid({
        title: '发送短信列表', url: '/management/sms_sent_list/',
        toolbar: '#sms_sent_toolbar',
        rownumbers: true, singleSelect: true,  fitColumns: true, pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'mobile', title: '手机号码', width: 10 },
            { field: 'name', title: '居民姓名', width: 10 },
            { field: 'next_time_date', title: '服务时间', width: 10 },
            { field: 'service_type_name', title: '服务类别', width: 10 },
            { field: 'service_item_name', title: '服务项目', width: 10 },
            { field: 'status', title: '短信状态', width: 10, formatter: function(value) {
                switch (value ) {
                    case 1: return "准备发送";
                    case 2: return "发送完成";
                    case -1:return "发送错误";
                    default:return "未知";
                }
            } },
            { field: 'message', title: '返回信息', width: 10 }
        ]],
        onBeforeLoad: function(param) {
            param.sms_begin = toolbar.find('#sms_begin').datebox('getValue');
            param.sms_end = toolbar.find('#sms_end').datebox('getValue');
            param.service_type = toolbar.find('#service_type').combobox('getValue');
            param.service_item = toolbar.find('#service_item').combobox('getValue');
            param.resident = toolbar.find('#resident').val();
            param.mobile = toolbar.find('#mobile').val();
            param.status = toolbar.find('#status').combobox('getValue');
        }
    });

});