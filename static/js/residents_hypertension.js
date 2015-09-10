$(function() {
    // 工具栏初始化
    var toolbar = $('#hypertension_toolbar');

    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_query = toolbar.find('#query').linkbutton({
        iconCls: 'icon-glyphicons-28-search', plain: true
    });
    btn_rm.linkbutton('disable');

    var query_town = toolbar.find('#query_town');
    query_town.combobox({
        url: '/management/get_towns/',
        valueField: 'id', textField: 'name', editable: false, width: 120,
        onLoadSuccess: function () { $(this).combobox('setValue', '0'); },
        onSelect: function (rec) {
            var url = '/management/get_town_villages/' + rec.id + '/';
            query_village.combobox('reload', url);
            query_village.combobox('setValue', '0');
        }
    });

    var query_village = toolbar.find('#query_village');
    query_village.combobox({
        valueField: 'id', textField: 'name', editable: false, width: 100,
        data: [{ 'id': '0', 'name': '全部' }],
        onLoadSuccess: function () { $(this).combobox('setValue', '0'); }
    });

    var query_ehr_no = toolbar.find('#query_ehr_no').combobox({
        valueField: 'id', textField: 'status', editable: false, width: 80,
        data: [{ 'id': 0, 'status': '全部'}, { 'id': -1, 'status': '未建档'},
               { 'id': 1, 'status': '已建档'}],
        panelHeight: 72
    });
    var query_name = toolbar.find('#query_name').textbox({ width: 80 });
    var query_identity = toolbar.find('#query_identity').textbox({ width: 150, options: { validateType: 'maxLength(18)'}});

    // 工具栏事件绑定


    btn_query.bind('click', function () {
        datagrid.datagrid('reload');
    });


    // 工具栏上按钮的可用状态以及是否显示，决定于这两个变量的值
    var selected_row = undefined;

    var datagrid = $('#hypertension_list');
    datagrid.datagrid({
        toolbar: '#hypertension_toolbar',
        url: '/management/hypertension_query_list/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'name', title: '姓名', width: 10, editor: {
                type: 'textbox', options: { required: true } } },
            { field: 'ehr_no', title: '健康档案', width:18, formatter: function (value) {
                if (value == null) {
                    return '未建档';
                } else {
                    return value;
                }},
              editor: { type: 'textbox' }
            },
            { field: 'gender', title: '性别', width: 6,
                formatter: function(value) {
                    switch (value) {
                        case '0': return '女';
                        case '1': return '男';
                        default : return '未知';
                    }
                },
                editor: { type: 'combobox', options: { required: true, editable: false, panelHeight: 72,
                        data: [{"value": "1", "text": "男"}, {"value": "0", "text": "女"},
                               {"value": "2", "text": "未知"}] } }
            },
            { field: 'nation', title: '民族', width: 10, editor: {
                type: 'textbox', options: { required: true } } },
            { field: 'age', title: '年龄', width: 6 },
            { field: 'birthday', title: '出生日期', width: 12, editor: {
                type: 'datebox', options: { required: true, editable: false } } },
            { field: 'identity', title: '身份证号码', width: 20, editor: {
                type: 'textbox', options: { required: true, validateType: 'maxLength[18]' } } },
            { field: 'town', title: '乡镇', width: 18, editor: {
                type: 'combobox', options: { editable: false } } },
            { field: 'village', title: '村/街道', width: 10, editor: {
                type: 'combobox', options: { editable: false } } },
            { field: 'address', title: '地址', width: 20, editor: { type: 'textbox' } },
            { field: 'mobile', title: '电话', width: 12, editor: {
                type: 'textbox', options: { required: true } } }
        ]],
        onBeforeLoad: function (param) {
            param.query_town = query_town.combobox('getValue');
            param.query_village = query_village.combobox('getValue');
            param.query_name = query_name.textbox('getValue');
            param.query_identity = query_identity.textbox('getValue');
            param.query_ehr_no = query_ehr_no.combobox('getValue');
        },
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
                btn_rm.linkbutton('disable');
            } else {
                selected_row = datagrid.datagrid('getSelected');
                btn_rm.linkbutton('enable');
            }
        }
    });

});