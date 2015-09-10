$(function() {
    //
    //初始化表格工具中的8个查找条件控件：【开始】
    //
    var toolbar = $('#payment_toolbar');

    var query_begin_date = toolbar.find('#query_begin_date').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    query_begin_date.datebox('setValue', newYearDay(new Date()));

    var query_end_date = toolbar.find('#query_end_date').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    query_end_date.datebox('setValue', myformatter(new Date()));

    var query_service_type = toolbar.find('#query_service_type').combobox({
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

    var query_service_item = toolbar.find('#query_service_item').combobox({
        url: '/management/service_item_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    var query_town_clinic = toolbar.find('#query_town_clinic').combobox({
        url: '/management/town_clinic_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': '全部'}],
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (record) {
            query_village_clinic.combobox({
                onBeforeLoad: function(param) {
                    param.first_text = '全部';
                    param.query_town_clinic = record.id;
                }
            });
            query_village_clinic.combobox('reload', '/management/village_clinic_options/');
            query_village_clinic.combobox('setValue', '0');
        }
    });

    var query_village_clinic = toolbar.find('#query_village_clinic').combobox({
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    var btn_query = toolbar.find('#query').linkbutton({
        iconCls: 'icon-glyphicons-28-search', plain: true
    });

    var query_doctor = toolbar.find('#query_doctor').textbox({ width: 100 });
    var query_resident = toolbar.find('#query_resident').textbox({ width: 100 });

    btn_query.bind('click', function() {
        datagrid.datagrid('reload');
    });

    //
    //初始化表格工具中的8个查找条件控件：【完毕】
    //

    //
    //初始化数据表格：【开始】
    //
    var datagrid = $('#payment');
    datagrid.datagrid({
        title: '工作量和费用统计', url: '/management/payment_list_new/',
        toolbar: '#payment_toolbar',
        rownumbers: true, singleSelect: true, fitColumns: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'service_type', title: '服务类别', width: 10 },
            { field: 'service_item', title: '服务项目', width: 10 },
            { field: 'workload', title: '工作量', width: 6 },
            { field: 'payment', title: '费用', width: 6 }
        ]],
        onBeforeLoad: function(param) {
            param.query_record_begin = query_begin_date.datebox('getValue');
            param.query_record_end = query_end_date.datebox('getValue');
            param.query_town_clinic = query_town_clinic.combobox('getValue');
            param.query_village_clinic = query_village_clinic.combobox('getValue');
            param.query_service_type = query_service_type.combobox('getValue');
            param.query_service_item = query_service_item.combobox('getValue');
            param.query_doctor = query_doctor.textbox('getValue');
            param.query_resident = query_resident.textbox('getValue');
        }
    });
});