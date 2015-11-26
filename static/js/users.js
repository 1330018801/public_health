$(function() {
    var datagrid = $('#user_list');
    var toolbar = $('#user_list_toolbar');
    var panel = $('#user_add_panel');
    var form = $('#user_add_form');
    var table = $('#user_add_table');
    var password_dialog = $('#new_password_dialog');
    var password_form = $('#new_password_form');
    var password_table = $('#new_password_table');

    password_table.find('#passwd1').textbox({ type: 'password', required: true, width: 120 });
    password_table.find('#pswd_again').textbox({
        type: 'password', required: true, validType: 'equals["#passwd1"]', width: 120
    });

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true});
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true});
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true});
    var btn_pass = toolbar.find('#password').linkbutton({ iconCls: 'icon-edit', plain: true});
    btn_rm.linkbutton('disable');
    btn_pass.linkbutton('disable');

    var query_user_group = toolbar.find('#query_user_group');
    var query_town_clinic = toolbar.find('#query_town_clinic');
    var query_village_clinic = toolbar.find('#query_village_clinic');
    var query_name = toolbar.find('#query_name').textbox({width: 80});
    var btn_query = toolbar.find('#query').linkbutton({ iconCls: 'icon-search', plain: true });

    query_user_group.combobox({
        url: '/management/get_roles/',
        valueField: 'id', textField: 'name', editable: false, panelHeight: 144, width: 100,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        }
    });

    query_town_clinic.combobox({
        url: '/management/get_town_clinics/',
        valueField: 'id', textField: 'name', editable: false, width: 100,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            query_town_clinic.combobox('setValue', '0');
        },
        onSelect: function (rec) {
            var url = '/management/get_town_village_clinics/' + rec.id + '/';
            query_village_clinic.combobox('reload', url);
            query_village_clinic.combobox('setValue', '0');
        }
    });

    query_village_clinic.combobox({
        valueField: 'id', textField: 'name', editable: false, width: 150,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        data: [{ 'id': '0', 'name': '全部' }],
        onLoadSuccess: function () {
            query_village_clinic.combobox('setValue', '0');
        }
    });

    var selected_row = undefined;
    var edit_row = undefined;

    datagrid.datagrid({
        title: '系统用户列表', url: '/management/user_query_list/',
        toolbar: '#user_list_toolbar', fitColumns: true, rownumbers: true, singleSelect: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'username', title: '用户名', width: 8, editor: { type: 'textbox', options: { required: true } } },
            //{ field: 'name', title: '姓名', width: 8 },
            { field: 'role', title: '用户角色', width: 10, editor: { type: 'combobox', options: { required: true } } },
            { field: 'town_clinic', title: '所在卫生院', width: 15, editor: { type: 'combobox' } },
            { field: 'village_clinic', title: '所在卫生室', width: 10, editor: { type: 'combobox' } },
            { field: 'department', title: '科室', width: 10, editor: { type: 'textbox' } },
            { field: 'title', title: '职务', width: 10, editor: { type: 'textbox' } }
            //{ field: 'mobile', title: '电话', width: 12 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
                btn_rm.linkbutton('disable');
                btn_pass.linkbutton('disable');
            } else {
                selected_row = row;
                btn_rm.linkbutton('enable');
                btn_pass.linkbutton('enable');
            }
        },
        onAfterEdit: function () {
            var updated_row = datagrid.datagrid('getChanges', 'updated');

            if (updated_row.length > 0) {
                $.ajax({
                    url: '/management/user_update_test/', method: 'POST',
                    data: updated_row[0],
                    success: function (data) {
                        if (data.success) {
                            datagrid.datagrid('reload');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: data.message});
                        } else {
                            $.messager.alert('提示', data.message, 'warning');
                        }
                    }
                });
            }
            edit_row = undefined; selected_row = undefined;
            btn_save.hide(); btn_undo.hide();
            btn_add.linkbutton('enable');
            btn_rm.linkbutton('enable');
        }
    });

    $.extend($.fn.validatebox.defaults.rules, {
        same_as: {
            validator: function(value, param){
                //console.log('value' + value);
                //console.log('param[0]' + form.find('#pswd2').val());
                //console.log('param[0]' + $('#pswd2').val());
                //只要页面刷新一下，这个验证就失败，无法获取param的值，目前还不知道为什么
                return value == form.find('#pswd2').val();
            },
            message: '两次密码输入不匹配'
        }
    });

    form.find('#username').textbox({ required: true, width: 120 });
    form.find('#user_group').combobox({
        url: '/management/get_roles/',
        valueField: 'id', textField: 'name', editable: false,
        panelHeight: 124, width: 120,
        onBeforeLoad: function (param) {
            param.first_text = ''
        },
        onSelect: function(record){
            if (record.name == '卫生局管理员' || record.name == '财政局管理员') {
                form.find('#town_clinic').combobox('disable');
                form.find('#village_clinic').combobox('disable');
                form.find('#department').textbox('disable');
                form.find('#position').textbox('disable');
            } else if (record.name == '卫生院管理员') {
                form.find('#town_clinic').combobox('enable');
                form.find('#village_clinic').combobox('disable');
                form.find('#department').textbox('disable');
                form.find('#position').textbox('disable');
            } else if (record.name == '卫生院医生') {
                form.find('#town_clinic').combobox('enable');
                form.find('#village_clinic').combobox('disable');
                form.find('#department').textbox('enable');
                form.find('#position').textbox('enable');
            } else if (record.name == '村医') {
                form.find('#town_clinic').combobox('enable');
                form.find('#village_clinic').combobox('enable');
                form.find('#department').textbox('disable');
                form.find('#position').textbox('disable');
            }
        }
    });
    form.find('#pswd2').textbox({ required: true, width: 120 });
    form.find('#pswd2_again').textbox({
        required: true, validType: 'same_as["#pswd2"]', width: 120
    });
    form.find('#town_clinic').combobox({
        url: '/management/get_town_clinics/',
        valueField: 'id', textField: 'name', editable: false, width: 120,
        onBeforeLoad: function (param) {
            param.first_text = '';
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (rec) {
            var url = '/management/get_town_village_clinics/' + rec.id + '/';
            form.find('#village_clinic').combobox('reload', url);
            form.find('#village_clinic').combobox('setValue', '0');
        }
    });
    form.find('#village_clinic').combobox({
        valueField: 'id', textField: 'name', editable: false, width: 120,
        data: [{ 'id': '0', 'name': '' }],
        onBeforeLoad: function (param) {
            param.first_text = ''
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });
    form.find('#department').textbox({width: 120});
    form.find('#position').textbox({width: 120});

    panel.dialog({
        title: '添加用户', closed: true, width: 500, height: 220, cache: false, modal: true,
        buttons: [
            {
                text: '提交', iconCls: 'icon-ok',
                handler: function() {
                    form.form('submit', {
                        url: '/management/user_add/',
                        onSubmit: function(param) {
                            param.csrfmiddlewaretoken = $.cookie('csrftoken');
                            return form.form('validate');
                        },
                        success: function(data) {
                            var data_obj = eval('(' + data + ')');
                            if (data_obj.success) {
                                form.form('clear');
                                panel.dialog('close');
                                datagrid.datagrid('reload');
                                $.messager.show({ title: '提示', msg: data_obj.message, timeout: 2500 });
                            } else {
                                $.messager.alert('提示', data_obj.message, 'warning');
                            }
                        }
                    });
                }
            },
            {
                text: '取消', iconCls: 'icon-cancel',
                handler: function() { panel.dialog('close'); }
            }
        ],
        onClose: function() {
            form.form('clear');
            table.css('display', 'none')
        },
        onOpen: function() {
            table.css('display', 'block');
            panel.dialog('center');
        }
    });

    btn_query.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('reload', {
                query_user_group: query_user_group.combobox('getValue'),
                query_town_clinic: query_town_clinic.combobox('getValue'),
                query_village_clinic: query_village_clinic.combobox('getValue'),
                query_username: query_name.textbox('getValue')
            });
        }
    });
    btn_add.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.dialog('open');
        }
    });
    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('endEdit', edit_row);
        }
    });
    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            edit_row = undefined;
            datagrid.datagrid('rejectChanges');
            btn_save.hide();
            btn_undo.hide();
            btn_add.linkbutton('enable');
            btn_rm.linkbutton('enable');
        }
    });
    btn_rm.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row != undefined) {
                $.messager.confirm('提示', '要删除所选择的用户记录吗？', function (flag) {
                    if (flag) {
                        $.ajax({
                            url: '/management/user_del/', method: 'POST',
                            data: { user_id: selected_row['id']},
                            success: function (data) {
                                if (data.success) {
                                    datagrid.datagrid('reload');
                                    datagrid.datagrid('unselectAll');
                                    $.messager.show({title: '提示', msg: data.message, timeout: 1000});
                                } else {
                                    $.messager.alert('提示', data.message, 'warning');
                                }
                            }
                        });
                    }
                });
            }
        }
    });

    btn_pass.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            password_dialog.dialog({
                title: '修改用户：' + selected_row['username'] + '登录密码', width: 400, height: 200,
                buttons: [
                    {
                        text: '提交', iconCls: 'icon-ok',
                        handler: function () {
                            password_form.form('submit', {
                                url: '/services/change_password/',
                                onSubmit: function (param) {
                                    param.csrfmiddlewaretoken = $.cookie('csrftoken');
                                    param.id = selected_row['id'];
                                    return password_form.form('validate');
                                },
                                success: function (data) {
                                    var data_obj = eval('(' + data + ')');
                                    if (data_obj.success) {
                                        if (data_obj.message == null) {
                                            $.messager.show({ title: '提示', msg: '密码修改成功', timeout: 1500 });
                                        } else {
                                            $.messager.alert('提示', data_obj.message, 'info');
                                            window.location.href='/';
                                        }
                                    } else {
                                        $.messager.alert('提示', '密码修改失败：' + data_obj.message, 'warning');
                                    }
                                    password_form.form('clear');
                                    password_dialog.dialog('close');
                                }
                            });
                        }
                    },
                    {
                        text: '取消', iconCls: 'icon-cancel',
                        handler: function () {
                            password_form.form('clear');
                            password_dialog.dialog('close');
                        }
                    }
                ]
            });
            password_table.css('display', 'block');
        }
    });

    $.extend($.fn.validatebox.defaults.rules, {
        equals: {
            validator: function(value, param){
                return value == password_table.find('#passwd1').val();
            },
            message: '两次密码输入不匹配'
        }
    });

});