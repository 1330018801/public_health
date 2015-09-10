$(function() {
    //
    //初始化表格工具中的8个查找条件控件：【开始】
    //
    var records_tb = $('#records_tb');
    function newYearDay(date) {
        var y = date.getFullYear();
        return y+'-01-01'
    }

    var curr_date = new Date();
    records_tb.find('#query_record_begin').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    records_tb.find('#query_record_begin').datebox('setValue', newYearDay(curr_date));

    records_tb.find('#query_record_end').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    records_tb.find('#query_record_end').datebox('setValue', myformatter(curr_date));
    records_tb.find('#query_service_type').combobox({
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
            var query_service_item = records_tb.find('#query_service_item');
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

    records_tb.find('#query_service_item').combobox({
        url: '/management/service_item_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    records_tb.find('#query_town_clinic').combobox({
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
            var query_village_clinic = records_tb.find('#query_village_clinic');
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

    records_tb.find('#query_village_clinic').combobox({
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    records_tb.find('#btn_query').bind('click', function() {
        $('#records').datagrid('load');
    });
    //
    //初始化表格工具中的8个查找条件控件：【完毕】
    //

    //
    //初始化数据表格：【开始】
    //

    $('#records').datagrid({
        title: '服务记录列表', toolbar: '#records_tb',
        url: '/management/record_list_new/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'town_clinic', title: '乡镇卫生院', width: 10 },
            { field: 'village_clinic', title: '村卫生室', width: 10 },
            { field: 'doctor', title: '医生用户', width: 6 },
            { field: 'resident', title: '居民姓名', width: 6 },
            { field: 'service_type', title: '服务类别', width: 10 },
            { field: 'service_item', title: '服务项目', width: 10 },
            { field: 'submit_time', title: '完成时间', width: 10 }
        ]],
        onBeforeLoad: function(param) {
            param.query_record_begin = records_tb.find('#query_record_begin').datebox('getValue');
            param.query_record_end = records_tb.find('#query_record_end').datebox('getValue');
            param.query_town_clinic = records_tb.find('#query_town_clinic').combobox('getValue');
            param.query_village_clinic = records_tb.find('#query_village_clinic').combobox('getValue');
            param.query_service_type = records_tb.find('#query_service_type').combobox('getValue');
            param.query_service_item = records_tb.find('#query_service_item').combobox('getValue');
            param.query_doctor = records_tb.find('#query_doctor').val();
            param.query_resident = records_tb.find('#query_resident').val();
        }
    });

});