$(function() {

    $.extend($.fn.validatebox.defaults.rules, {
        maxLength: {
            validator: function(value, param){
                return value.length >= param[0];
            },
            message: '身份证号码最多{0}位'
        }
    });

    var datagrid = $('#ehr_resident_list');
    var toolbar = $('#ehr_resident_toolbar');
    var selected_row = undefined;
    var edit_row = undefined;

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_add_body_exam = toolbar.find('#body_exam').linkbutton({ iconCls: 'icon-add', plain: true });

    btn_edit.linkbutton('disable');
    btn_add_body_exam.linkbutton('disable');

    var query_ehr_no = toolbar.find('#query_ehr_no').textbox({ width: 150, options: { validateType: 'maxLength(17)'}});
    var query_age = toolbar.find('#query_age').numberbox({ width: 40 });
    var query_name = toolbar.find('#query_name').textbox({ width: 80 });
    var query_identity = toolbar.find('#query_identity').textbox({ width: 150, options: { validateType: 'maxLength(18)'}});
    var btn_query = toolbar.find('#query').linkbutton({iconCls: 'icon-glyphicons-28-search', plain: true});

    var query_gender = toolbar.find('#query_gender').combobox({
        valueField: 'id', textField: 'text', editable: false, width: 60,
        data: [{'id': 2, 'text': '全部'}, { 'id': 0, 'text': '女'}, { 'id': 1, 'text': '男'}],
        panelHeight: 66
    });
    query_gender.combobox('setValue', 2);

    var query_crowd = toolbar.find('#query_crowd').combobox({
        valueField: 'alias', textField: 'text', editable: false, width: 100, panelHeight: 168,
        data: [{ 'alias': 'all', 'text': '全体'},
               { 'alias': 'hypertension', 'text': '高血压'},
               { 'alias': 'diabetes', 'text': '2型糖尿病'},
               { 'alias': 'psychiatric', 'text': '重性精神疾病'},
               { 'alias': 'pregnant', 'text': '孕产妇'},
               { 'alias': 'old', 'text': '老年人'},
               { 'alias': 'child', 'text': '0-6岁儿童'}]
    });

    btn_query.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('reload');
        }
    });

    btn_add.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            var tabs = datagrid.parents('#ehr_setup_tabs');
            if(!tabs.tabs('exists', '建档：个人基本信息表')){
                tabs.tabs('add', {
                    title: '建档：个人基本信息表', closable: true,
                    href: '/ehr/setup_personal_info_page/'
                });
            }
            else{
                tabs.tabs('select', '建档：个人基本信息表');
            }
        }
    });

    btn_add_body_exam.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            var tabs = datagrid.parents('#ehr_setup_tabs');
            if(!tabs.tabs('exists', '建档：健康体检表')){
                tabs.tabs('add', {
                    title: '建档：健康体检表', closable: true,
                    href: '/ehr/setup_body_exam_page/'
                });
            }
            else{
                var tab = tabs.tabs('getTab', '建档：健康体检表');
                tabs.tabs('update', {
                    tab: tab,
                    options: {
                        href: '/ehr/setup_body_exam_page/'
                    }
                });
                tabs.tabs('select', '建档：健康体检表');
            }
        }
    });

    btn_edit.bind('click', function(){
        if($(this).linkbutton('options').disabled == false){
            var tabs = datagrid.parents('#ehr_setup_tabs');
            if(!tabs.tabs('exists', '修改：个人基本信息表')){
                tabs.tabs('add', {
                    title: '修改：个人基本信息表', closable: true,
                    href: '/ehr/personal_info_edit_tab/',
                    queryParams: {resident_id: selected_row['id']}
                });
            }
            else{
                var tab = tabs.tabs('getTab', '修改：个人基本信息表');
                tabs.tabs('update', {
                    tab: tab,
                    options: {
                        href: '/ehr/personal_info_edit_tab/',
                        queryParams: {resident_id: selected_row['id']}
                    }
                });
                tabs.tabs('select', '修改：个人基本信息表');
            }
        }
    });

    datagrid.datagrid({
        toolbar: '#ehr_resident_toolbar',
        url: '/ehr/ehr_resident_query/',
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
            { field: 'personal_info', title: '个人基本体检表', width: 10 },
            { field: 'body_exam', title: '健康体检表', width: 10 },
            { field: 'gender', title: '性别', width: 6,
                formatter: function(value) {
                    switch (value) {
                        case 0: return '女';
                        case 1: return '男';
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
            { field: 'mobile', title: '电话', width: 12, editor: {
                type: 'textbox', options: { required: true } } }
        ]],
        onBeforeLoad: function (param) {
            param.ehr_no = query_ehr_no.textbox('getValue');
            param.name = query_name.textbox('getValue');
            param.gender = query_gender.combobox('getValue');
            param.age = query_age.numberbox('getValue');
            param.identity = query_identity.textbox('getValue');
            param.crowd = query_crowd.combobox('getValue');
        },
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
                btn_edit.linkbutton('disable');
            } else {
                selected_row = datagrid.datagrid('getSelected');
                if (selected_row['body_exam'] == '否')
                    btn_add_body_exam.linkbutton('enable');
                else
                    btn_add_body_exam.linkbutton('disable');
                btn_edit.linkbutton('enable');
            }
        },
        onAfterEdit: function(index, row) {
            var inserted = datagrid.datagrid('getChanges', 'inserted');
            var updated = datagrid.datagrid('getChanges', 'updated');

            if (inserted.length > 0) {
                $.ajax({
                    url: '/management/resident_add/', method: 'POST',
                    data: row,
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('reload');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 2000, msg: '居民信息记录添加成功！' })
                        }
                    }
                });
            }
            if (updated.length > 0) {
                console.log('update row: ' + edit_row);
                $.ajax({
                    url: '/management/resident_update/', method: 'POST',
                    data: row,
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 2000, msg: '居民信息记录更新成功！' })
                        }
                    }
                });
            }
            edit_row = undefined;
            selected_row = undefined;
            btn_add.linkbutton('enable');
        },
        onDblClickRow: function(index, row){
            var tabs = datagrid.parents('#ehr_setup_tabs');
            if(!tabs.tabs('exists', '个人基本信息表')){
                tabs.tabs('add', {
                    title: '个人基本信息表', closable: true,
                    href: '/ehr/personal_info_review_tab/', method: 'POST',
                    queryParams: {resident_id: row['id']}
                });
            }
            else{
                var tab = tabs.tabs('getTab', '个人基本信息表');
                tabs.tabs('update', {
                    tab: tab,
                    options: {
                        href: '/ehr/personal_info_review_tab/', method: 'POST',
                        queryParams: {resident_id: row['id']}
                    }
                });
                tabs.tabs('select', '个人基本信息表');
            }
        }
    });

    function townOptions(field, index) {
        var current = $(field.target).combobox('getValue');
        $(field.target).combobox({
            url: '/management/get_towns/',
            valueField: 'name',textField: 'name', editable: false,
            onLoadSuccess: function() {
                if (current) {
                    $(this).combobox('setValue', current);
                    var current_village = $(get_edit_field(index, 'village').target).combobox('getValue');
                    $(get_edit_field(index, 'village').target).combobox({
                        url: '/management/get_town_villages_edit/',
                        valueField: 'name', textField: 'name', editable: false,
                        onBeforeLoad: function(param) {
                            param.town_name = current
                        },
                        onLoadSuccess: function() {
                            $(this).combobox('setValue', current_village);
                        }
                    });
                } else {
                    $(this).combobox('setValue', '');
                }
            },
            onSelect: function () {
                syncVillageOptions(get_edit_field(index, 'village'), $(this).combobox('getValue'))
            }
        });
    }

    function syncVillageOptions(field, town_name) {
        $(field.target).combobox({
            url: '/management/get_town_villages_edit/',
            valueField: 'name', textField: 'name', editable: false,
            onBeforeLoad: function(param) {
                param.town_name = town_name;
            },
            onLoadSuccess: function() {
                $(this).combobox('setValue', '');
            }
        });
    }

    function get_edit_field(index, field) {
        return datagrid.datagrid('getEditor', { index: index, field: field })
    }
});