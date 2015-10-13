$(function() {
    var selected_row = undefined;
    var edit_row = undefined;

    function get_edit_field(index, field) {
        return datagrid.datagrid('getEditor', { index: index, field: field })
    }

    function service_type_select(field, index) {
        var service_type = selected_row['service_type_id'];
        console.log(service_type);
        $(field.target).combobox({
            url: '/management/service_type_options/',
            valueField: 'id', textField: 'name', editable: false,
            onLoadSuccess: function() {
                if (service_type) {
                    $(this).combobox('setValue', service_type);
                    var service_item = selected_row['service_item_id'];
                    $(get_edit_field(index, 'service_item').target).combobox({
                        url: '/management/service_item_options/',
                        valueField: 'id', textField: 'name',
                        onBeforeLoad: function(param) {
                            param.query_service_type = service_type;
                        },
                        onLoadSuccess: function() {
                            $(this).combobox('setValue', service_item);
                        }
                    });

                } else {
                    $(this).combobox('setValue', 0);
                }
            },
            onSelect: function () {
                sync_service_item_select(get_edit_field(index, 'service_item'), $(this).combobox('getValue'))
            }
        });
    }

    function sync_service_item_select(field, value) {
        $(field.target).combobox({
            url: '/management/service_item_options/',
            valueField: 'id', textField: 'name',
            onBeforeLoad: function(param) {
                param.query_service_type = value
            },
            onLoadSuccess: function() {
                $(this).combobox('setValue', 0);
            }
        });
    }

    var toolbar = $('#sms_setup_toolbar');
    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });

    btn_add.bind('click', function () {
        if (edit_row == undefined) {
            btn_save.show(); btn_undo.show();
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            datagrid.datagrid('insertRow', { index: 0, row: {} });
            datagrid.datagrid('beginEdit', 0);
            edit_row = 0;
            selected_row = datagrid.datagrid('getRows')[0];
            service_type_select(get_edit_field(edit_row, 'service_type'), edit_row);
        }
    });

    btn_edit.bind('click', function () {
        if (selected_row) {
            if (edit_row != undefined) {
                datagrid.datagrid('rejectChanges');
                datagrid.datagrid('endEdit', edit_row);
            } else {
                btn_save.show(); btn_undo.show();
                btn_add.linkbutton('disable');
                btn_edit.linkbutton('disable');
                btn_rm.linkbutton('disable');
            }
            var index = datagrid.datagrid('getRowIndex', selected_row);
            edit_row = index;
            datagrid.datagrid('beginEdit', index);
            service_type_select(get_edit_field(index, 'service_type'), index);
        } else {
            $.messager.alert('警告', '请先选定需要修改的短信设置！', 'warning');
        }
    });

    btn_rm.bind('click', function () {
        if (selected_row) {
            $.messager.confirm('确认操作', '是要删除所选择的短信设置吗？', function(flag) { if (flag) {
                $.ajax({
                    url: '/management/sms_setup_del/', method: 'POST',
                    data: { id: selected_row.id },
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', msg: '短信设置删除成功！' });
                    }
                });
            }});
        } else {
            $.messager.alert('提示', '请选择所要删除的记录', 'info');
        }
    });

    btn_save.bind('click', function () {
        datagrid.datagrid('endEdit', edit_row);
    });

    btn_undo.bind('click', function () {
        btn_save.hide(); btn_undo.hide();
        btn_add.linkbutton('enable');
        btn_edit.linkbutton('enable');
        btn_rm.linkbutton('enable');
        edit_row = undefined;
        selected_row = undefined;
        datagrid.datagrid('rejectChanges');
    });

    toolbar.find('#service_type').combobox({
        url: '/management/service_type_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': '全部'}],
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', 0);
        },
        onSelect: function (record) {
            var service_item = toolbar.find('#service_item');
            service_item.combobox({
                url: '/management/service_item_options/',
                onBeforeLoad: function(param) {
                    param.first_text = '全部';
                    param.query_service_type = record.id;
                }
            });
            service_item.combobox('reload');
            service_item.combobox('setValue', 0);
        }
    });

    toolbar.find('#service_item').combobox({
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': ''}],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    toolbar.find('#sms_begin').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    toolbar.find('#sms_begin').datebox('setValue', newYearDay(new Date()));
    toolbar.find('#sms_end').datebox({
        width: 100, formatter: myformatter, parser :myparser
    });
    toolbar.find('#sms_end').datebox('setValue', endYearDay(new Date()));

    toolbar.find('#town_clinic').combobox({
        url: '/management/town_clinic_options/',
        valueField: 'id', textField: 'name', width: 150, editable: false,
        data: [{'id': 0, 'name': '全部'}],
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    toolbar.find('#author').textbox({ width: 100 });
    toolbar.find('#updater').textbox({ width: 100 });
    toolbar.find('#status').combobox({
        valueField: 'id', textField: 'name', width: 100, editable: false,
        data: [{'id': 0, 'name': "全部"}, {'id': 1, 'name': "已发送"},
               {'id': 2, 'name': "未发送"}, {'id': 3, 'name': "已取消"}],
        onLoadSuccess: function() {
            $(this).combobox('setValue', 0);
        }
    });

    var btn_query = toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        datagrid.datagrid('load');
    });

    var datagrid = $('#sms_setup').datagrid({
        title: '短信发送设置', url: '/management/sms_setup_list/',
        toolbar: '#sms_setup_toolbar',
        rownumbers: true, singleSelect: true, fitColumns: true, pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'service_type_id', title: '服务类别编号', hidden: true },
            { field: 'service_item_id', title: '服务项目编号', hidden: true },
            { field: 'service_type', title: '服务类别', width: 10, editor: {
                type: 'combobox', options: { required: true }
            } },
            { field: 'service_item', title: '服务项目', width: 10, editor: {
                type: 'combobox', options: { required: true }
            } },
            { field: 'service_time', title: '服务时间', width: 6, editor: {
                type: 'datebox', options: { required: true }
            }},
            { field: 'town_clinic', title: '乡镇卫生院', width: 8 },
            { field: 'author', title: '创建者', width: 4 },
            { field: 'updater', title: '最后修改者', width: 4 },
            { field: 'status', title: '短信状态', width: 4, formatter: function(value) {
                switch (value) {
                    case 1: return '已发送';
                    case 2: return '未发送';
                    case 3: return '已取消';
                    default:return '未知';
                }
            } }
        ]],
        onBeforeLoad: function(param) {
            param.service_type = toolbar.find('#service_type').combobox('getValue');
            param.service_item = toolbar.find('#service_item').combobox('getValue');
            param.sms_begin = toolbar.find('#sms_begin').datebox('getValue');
            param.sms_end = toolbar.find('#sms_end').datebox('getValue');
            param.town_clinic = toolbar.find('#town_clinic').combobox('getValue');
            param.author = toolbar.find('#author').val();
            param.updater = toolbar.find('#updater').val();
            param.status = toolbar.find('#status').combobox('getValue');
        },
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = row;
            }
        },
        onAfterEdit: function() {
            btn_save.hide(); btn_undo.hide();
            var inserted_row = $(this).datagrid('getChanges', 'inserted');
            var updated_row = $(this).datagrid('getChanges', 'updated');

            if (inserted_row.length > 0) {
                $.ajax({
                    url: '/management/sms_setup_add/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '短信发生设置添加成功！'});
                    }
                });
            }
            if (updated_row.length > 0) {
                $.ajax({
                    url: '/management/sms_setup_update/', method: 'POST',
                    data: updated_row[0],
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '短信发生设置更新成功！' });
                    }
                });
            }
            edit_row = undefined;
            selected_row = undefined;
            btn_add.linkbutton('enable');
            btn_edit.linkbutton('enable');
            btn_rm.linkbutton('enable');
        }
    });
});
