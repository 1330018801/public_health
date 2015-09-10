$(function() {
    $('#query_user_group').combobox({
        url: '/management/get_roles/',
        valueField: 'id', textField: 'name', editable: false, panelHeight: 144,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        }
    });

    $('#query_town_clinic').combobox({
        url: '/management/get_town_clinics/',
        valueField: 'id',
        textField: 'name',
        editable: false,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (rec) {
            var url = '/management/get_town_village_clinics/' + rec.id + '/';
            $('#query_village_clinic').combobox('reload', url);
            $('#query_village_clinic').combobox('setValue', '0');
        }
    });

    $('#query_village_clinic').combobox({
        valueField: 'id',
        textField: 'name',
        editable: false,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        data: [{ 'id': '0', 'name': '全部' }],
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    var selected_row = undefined;

    $('#user_list').datagrid({
        title: '系统用户列表',
        url: '/management/user_query_list/',
        rownumbers: true,
        singleSelect: true,
        toolbar: '#user_list_tb',
        fitColumns: true,
        pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50],
        pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'username', title: '用户名', width: 8, editor: { type: 'validatebox', options: { required: true } } },
            { field: 'name', title: '姓名', width: 8 },
            { field: 'role', title: '用户角色', width: 10, editor: { type: 'combobox', options: { required: true } } },
            { field: 'town_clinic', title: '所在卫生院', width: 15, editor: { type: 'combobox' } },
            { field: 'village_clinic', title: '所在卫生室', width: 10, editor: { type: 'combobox' } },
            { field: 'department', title: '科室', width: 10, editor: { type: 'text' } },
            { field: 'title', title: '职务', width: 10, editor: { type: 'text' } },
            { field: 'mobile', title: '电话', width: 12 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row != undefined && selected_row == row) {
                $('#user_list').datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = $('#user_list').datagrid('getSelected');
            }

        }
    });

    $.extend($.fn.validatebox.defaults.rules, {
        equals: {
            validator: function(value,param){
                return value == $(param[0]).val();
            },
            message: '两次密码输入不匹配'
        }
    });

    var user_add_form = $('#user_add_form');

    user_add_form.find('input[name=username]').textbox({
        required: true
    });
    user_add_form.find('input[name=password]').textbox({
        required: true
    });
    user_add_form.find('input[name=password_again]').textbox({
        required: true,
        validType: 'equals["input[name=password]"]'
    });
    user_add_form.find('input[name=town_clinic]').combobox({
        url: '/management/get_town_clinics/',
        valueField: 'id',
        textField: 'name',
        editable: false,
        onBeforeLoad: function (param) {
            param.first_text = ''
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (rec) {
            var url = '/management/get_town_village_clinics/' + rec.id + '/';
            user_add_form.find('input[name=village_clinic]').combobox('reload', url);
            user_add_form.find('input[name=village_clinic]').combobox('setValue', '0');
        }
    });
    user_add_form.find('input[name=village_clinic]').combobox({
        valueField: 'id',
        textField: 'name',
        editable: false,
        data: [{ 'id': '0', 'name': '' }],
        onBeforeLoad: function (param) {
            param.first_text = ''
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });
    user_add_form.find('input[name=department]').textbox();
    user_add_form.find('input[name=title]').textbox();
    user_add_form.find('input[name=user_group]').combobox({
        url: '/management/get_roles/',
        valueField: 'id',
        textField: 'name',
        editable: false,
        onBeforeLoad: function (param) {
            param.first_text = ''
        },
        onSelect: function(record){
            if (record.name == '卫生局管理员' || record.name == '财政局管理员') {
                user_add_form.find('#town_clinic').combobox('disable');
                user_add_form.find('#village_clinic').combobox('disable');
                user_add_form.find('#department').textbox('disable');
                user_add_form.find('#title').textbox('disable');
            } else if (record.name == '卫生院管理员') {
                user_add_form.find('#town_clinic').combobox('enable');
                user_add_form.find('#village_clinic').combobox('disable');
                user_add_form.find('#department').textbox('disable');
                user_add_form.find('#title').textbox('disable');
            } else if (record.name == '卫生院医生') {
                user_add_form.find('#town_clinic').combobox('enable');
                user_add_form.find('#village_clinic').combobox('disable');
                user_add_form.find('#department').textbox('enable');
                user_add_form.find('#title').textbox('enable');
            } else if (record.name == '村医') {
                user_add_form.find('#town_clinic').combobox('enable');
                user_add_form.find('#village_clinic').combobox('enable');
                user_add_form.find('#department').textbox('disable');
                user_add_form.find('#title').textbox('disable');
            }
        }
    });

    user_add_form.dialog({
        title: '添加用户', closed: true, width: 600, cache: false, modal: true,
        buttons: [
            {
                text: '提交',
                iconCls: 'icon-ok',
                handler: function() {
                    $(this).form('submit', {
                        url: '/management/user_add_test/',
                        onSubmit: function(param) {
                            param.csrfmiddlewaretoken = $.cookie('csrftoken');
                            return $(this).form('validate');
                        },
                        success: function(data) {
                            //将返回的json类型转化为JS对象
                            var data_obj = eval('(' + data + ')');
                            if (data_obj.success) {
                                $.messager.show({
                                    title: '提示',
                                    msg: data_obj.message,
                                    showType: null,
                                    timeout: 1500,
                                    style: {
                                        top: 100
                                    }
                                });
                                $(this).form('reset');
                                $('#user_add').dialog('close');
                                $('#user_list').datagrid('reload');
                            }
                        }
                    });
                }
            },
            {
                text: '取消',
                iconCls: 'icon-cancel',
                handler: function() {
                    $('#user_add_form').dialog('close');
                }
            }
        ],
        onClose: function() {
            $(this).form('clear');
        },
        onOpen: function() {
            $(this).dialog('center');
        }
    });

    obj = {
        search: function() {
            $('#user_list').datagrid('load', {
                query_user_group: $('input[name="query_user_group"]').val(),
                query_town_clinic: $('input[name="query_town_clinic"]').val(),
                query_village_clinic: $('input[name="query_village_clinic"]').val(),
                query_username: $('input[name="query_username"]').val()
            });
        },
        add: function() {
            $('#user_add_form').css('display','block');
            $('#user_add_form').dialog('open');
        },
        edit: function () {
            var rows = $('#user_list').datagrid('getSelections');
            if (rows.length == 1) {
                if (this.editRow != undefined) {
                    $('#user_list').datagrid('rejectChanges');
                    $('#user_list').datagrid('endEdit', this.editRow);
                } else {
                    $('#save, #undo').show();
                    $('#add, #edit, #remove').linkbutton('disable');
                }
                var index = $('#user_list').datagrid('getRowIndex', rows[0]);
                this.editRow = index;
                $('#user_list').datagrid('beginEdit', index);
                towLevelClinicOptions(getEditRow(index, 'town_clinic'), index);
            } else if (rows.length > 1) {
                $.messager.alert('警告', '不能同时修改多条用户记录信息！', 'warning');
            } else if (rows.length == 0) {
                $.messager.alert('警告', '请先选定用户记录再修改！', 'warning');
            }
        },
        remove: function() {
            var rows = $('#user_list').datagrid('getSelections');
            if (rows.length > 0) {
                $.messager.confirm('确认操作', '要删除所选择的用户记录吗？', function(flag) {
                    if (flag) {
                        var ids = [];
                        for (var i = 0; i < rows.length; i++) {
                            ids.push(rows[i].id);
                        }
                        $.ajax({
                            method: 'POST',
                            url: '/management/user_del_test/',
                            data: {
                                user_id: ids[0]
                            },
                            success: function (data) {
                                if (data) {
                                    $('#user_list').datagrid('load');
                                    $('#user_list').datagrid('unselectAll');
                                    $.messager.show({
                                        title: '提示',
                                        msg: '用户信息记录删除成功！'
                                    })
                                }
                            }
                        });
                    }
                });
            } else {
                $.messager.alert('提示', '请选择所要删除的记录', 'info');
            }
        },
        save: function() {
            $('#user_list').datagrid('endEdit', this.editRow);
        },
        undo: function() {
            $('#save, #undo').hide();
            $('#add, #edit, #remove').linkbutton('enable');
            this.editRow = undefined;
            $('#user_list').datagrid('rejectChanges');
        }
    };

});