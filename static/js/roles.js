$(function() {
    var datagrid = $('#roles');
    var dialog = $('#role_authorize');
    var toolbar = $('#roles_toolbar');
    var btn_add = toolbar.find('#btn_add');
    var btn_del = toolbar.find('#btn_del');
    var btn_save = toolbar.find('#btn_save');
    var btn_undo = toolbar.find('#btn_undo');
    var btn_authorize = toolbar.find('#btn_authorize');
    var select = $('#service_item_select');

    select.multiSelect({
        keepOrder: true,
        selectableOptgroup: true,
        selectableHeader: '<div align="center" style="font-size: 14px;">未授权的服务项目</div>',
        selectionHeader: '<div align="center" style="font-size: 14px;">授权的服务项目</div>',
        afterInit: function () {
        }
    });

    //初始化角色授权对话框
    dialog.dialog({
        title: '设置角色权限', width: 600, height: 400, closed: true, cache: false, modal: true,
        buttons: [
            { text: '确定', iconCls: 'icon-ok', handler: function() {
                $('#role_authorize_form').form('submit', {
                    url: '/management/role_authorize/',
                    onSubmit: function(param) {
                        param.role_id = selected_row.id;
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    },
                    success: function() { $.messager.show({ title: '提示', msg: '角色权限更新成功！' }); }
                });
                $('#role_authorize').dialog('close');
            }},
            { text: '取消', iconCls: 'icon-cancel', handler: function() { $('#role_authorize').dialog('close'); } }
        ],
        onOpen: function() {
            dialog.css('display', 'block');
            dialog.dialog('center');
        },
        onClose: function() {
            select.multiSelect('deselect_all');
            dialog.css('display', 'none');
        }
    });

    //关联按钮和角色授权对话框

    btn_del.linkbutton({ plain: true, iconCls: 'icon-remove'});
    btn_add.linkbutton({ plain: true, iconCls: 'icon-add'});
    btn_save.linkbutton({ plain: true, iconCls: 'icon-save'});
    btn_undo.linkbutton({ plain: true, iconCls: 'icon-undo'});
    btn_authorize.linkbutton({plain: true, iconCls: 'icon-reload'});
    btn_del.linkbutton('disable');
    btn_save.linkbutton('disable');
    btn_undo.linkbutton('disable');
    btn_authorize.linkbutton('disable');

    btn_del.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row) {
                $.ajax({
                    url: '/management/role_del/', method: 'POST',
                    data: {'id': selected_row['id']},
                    success: function (data) {
                        if (data.success) {
                            $.messager.show({title: '提示', msg: '删除角色完成', timeout: 1500})
                        } else {
                            $.messager.alert('提示', '删除角色失败', 'warning');
                        }
                    }
                });
                datagrid.datagrid('reload');
            } else {
                $.messager.alert('提示', '请选择所要删除的角色', 'info');
            }
        }
    });

    btn_add.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            btn_add.linkbutton('disable');
            btn_del.linkbutton('disable');
            btn_authorize.linkbutton('disable');
            btn_save.linkbutton('enable');
            btn_undo.linkbutton('enable');
            datagrid.datagrid('insertRow', { index: 0, row: {} });
            datagrid.datagrid('beginEdit', 0);
            edit_row = 0;

            var field = datagrid.datagrid('getEditor', { index: edit_row, field: 'is_staff' });
            $(field.target).combobox({
                valueField: 'value', textField: 'text', panelHeight: 48,
                data: [
                    {'value': 0, 'text': '服务提供者'},
                    {'value': 1, 'text': '管理员'}
                ],
                onLoadSuccess: function () {
                    $(this).combobox('setValue', 0);
                }
            });
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('endEdit', edit_row);
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            btn_add.linkbutton('enable');
            btn_del.linkbutton('disable');
            btn_authorize.linkbutton('disable');
            btn_save.linkbutton('disable');
            btn_undo.linkbutton('disable');
            edit_row = undefined;
            selected_row = undefined;
            datagrid.datagrid('rejectChanges');
        }
    });

    btn_authorize.bind('click', function() {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row) {
                $.ajax({
                    url: '/management/service_item_options/', method: 'POST',
                    data: { 'service_type_name': 'true' },
                    success: function (data) {
                        data = eval('(' + data + ')');
                        $.each(data, function (index, item) {
                            if (item.id) {
                                select.multiSelect('addOption',
                                    {value: item.id, text: item.name, index: 0, nested: item.service_type_name});
                            }
                        });
                        $.ajax({
                            url: '/management/get_role_authorize/',
                            method: 'POST',
                            data: { 'role_id': selected_row.id },
                            success: function (data) {
                                data = eval('(' + data + ')');
                                select.multiSelect('select', data);
                            }
                        });
                        $('#role_authorize').dialog('open');
                    }
                })
            }
        }
    });

    var selected_row = undefined;
    var edit_row = undefined;

    datagrid.datagrid({
        title: '系统用户角色列表', url: '/management/role_list/',
        toolbar: '#roles_toolbar', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'name', title: '角色名称', width: 10, editor: {
                type: 'textbox', options: { required: true }
            } },
            { field: 'is_staff', title: '类别', width: 10, formatter: function(value){
                if (value) { return '管理员'; } else { return '服务提供者'; }
            }, editor: {
                type: 'combobox', options: { required: true, editable: false }
            }},
            { field: 'user_num', title: '用户数量', width: 10 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                    datagrid.datagrid('unselectRow', index);
                    selected_row = undefined;
                    btn_authorize.linkbutton('disable');
                    btn_del.linkbutton('disable');
            } else {
                    selected_row = row;
                    btn_authorize.linkbutton('enable');
                    btn_del.linkbutton('enable');
            }
        },
        onAfterEdit: function () {
            var inserted_row = datagrid.datagrid('getChanges', 'inserted');
            if (inserted_row.length > 0) {
                $.ajax({
                    url: '/management/role_add/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        datagrid.datagrid('reload');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '添加角色完成'});
                    }
                });
            }
            edit_row = undefined; selected_row = undefined;
            btn_add.linkbutton('enable');
            btn_save.linkbutton('disable');
            btn_undo.linkbutton('disable');
            btn_authorize.linkbutton('disable');
        }
    });
});