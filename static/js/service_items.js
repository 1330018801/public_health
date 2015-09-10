$(function() {

    // 返回数据表格中某行的某个字段的对象
    // index：数据表格的行索引
    // field：行中字段的名称
    function get_edit_field(index, field) {
        return datagrid.datagrid('getEditor', { index: index, field: field });
    }

    // 编辑数据表格中某行时，所属服务类别的下拉菜单选项
    // field: 所属服务类别字段
    function serviceTypeOptions(field) {
        var current_service_type = $(field.target).combobox('getValue');
        $(field.target).combobox({
            url: '/management/service_type_options/',
            valueField: 'name', textField: 'name', editable: false,
            onBeforeLoad: function (param) {
                param.first_text = ''
            },
            onLoadSuccess: function() {
                if (current_service_type) {
                    $(this).combobox('setValue', current_service_type);
                } else {
                    $(this).combobox('setValue', '');
                }
            }
        });
    }

    var selected_row = undefined;   // 选定行对象
    var edit_row = undefined;       // 编辑行的index

    // 工具栏及其上按钮和空间初始化
    var toolbar = $('#service_items_tb');

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_query = toolbar.find('#query').linkbutton({
        iconCls: 'icon-glyphicons-28-search', plain: true
    });
    btn_save.hide(); btn_undo.hide();
    btn_edit.linkbutton('disable');
    btn_rm.linkbutton('disable');

    var query_service_type = $('#query_service_type').combobox({
        url: '/management/service_type_options/',
        valueField: 'id', textField: 'name', editable: false, width: 200,
        onBeforeLoad: function (param) {
            param.first_text = '全部'
        },
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });
    var query_service_item_name = $('#query_service_item_name').textbox({ width: 100 });

    // 工具栏按钮的事件绑定
    btn_add.bind('click', function() {
        if (edit_row == undefined) {
            btn_save.show(); btn_undo.show();
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            datagrid.datagrid('insertRow', { index: 0, row: {} });
            datagrid.datagrid('beginEdit', 0);
            edit_row = 0;
            serviceTypeOptions(get_edit_field(edit_row, 'service_type'));
        }
    });
    btn_save.bind('click', function () {
        datagrid.datagrid('endEdit', edit_row);
    });

    btn_edit.bind('click', function () {
        if (selected_row == undefined) {
            $.messager.alert('警告', '请先选定记录再修改！', 'warning');
        } else {
            edit_row = datagrid.datagrid('getRowIndex', selected_row);
            datagrid.datagrid('beginEdit', edit_row);
            // 修改服务项目信息，不能修改其所属的服务类别
            //serviceTypeOptions(get_edit_field(edit_row, 'service_type'));
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            btn_save.show(); btn_undo.show();
        }
    });

    btn_rm.bind('click', function () {
        var rows = datagrid.datagrid('getSelections');
        if (rows.length > 0) {
            $.messager.confirm('确认操作', '要删除所选择的服务项目吗？', function(flag) {
                if (flag) {
                    var ids = [];
                    for (var i = 0; i < rows.length; i++) {
                        ids.push(rows[i].id);
                    }
                    $.ajax({
                        url: '/management/service_item_del_test/', method: 'POST',
                        data: { service_item_id: ids[0] },
                        success: function (data) {
                            if (data) {
                                datagrid.datagrid('load');
                                datagrid.datagrid('unselectAll');
                                selected_row = undefined;
                                btn_edit.linkbutton('disable');
                                btn_rm.linkbutton('disable');
                                $.messager.show({ title: '提示', timeout: 1000, msg: '服务项目删除成功！' })
                            }
                        }
                    });
                }
            });
        } else {
            $.messager.alert('提示', '请选择所要删除的服务项目', 'info');
        }
    });

    btn_undo.bind('click', function () {
        datagrid.datagrid('rejectChanges');
        selected_row = undefined; edit_row = undefined;
        btn_save.hide(); btn_undo.hide();
        btn_add.linkbutton('enable');
        btn_edit.linkbutton('disable');
        btn_rm.linkbutton('disable');
    });

    btn_query.bind('click', function () {
        datagrid.datagrid('load', {
            query_service_type: query_service_type.combobox('getValue'),
            query_service_item_name: query_service_item_name.textbox('getValue')
        });
    });

    // 数据表格定义
    var datagrid = $('#service_items');

    datagrid.datagrid({
        title: '基本公共卫生服务计费项目列表', toolbar: '#service_items_tb',
        url: '/management/service_item_list_new/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'service_type', title: '所属服务类别', width: 20 },
            { field: 'name', title: '服务项目名称', width: 20, editor: {
                type: 'validatebox', options: { required: true } } },
            { field: 'unit', title: '计价单位', width: 10, editor: {
                type: 'textbox', options: { required: true } } },
            { field: 'price', title: '单价', width: 10, editor: {
                type: 'numberbox', options: { min: 0, precision: 2, required: true } } }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
                btn_edit.linkbutton('disable');
                btn_rm.linkbutton('disable');

            } else {
                selected_row = datagrid.datagrid('getSelected');
                btn_edit.linkbutton('enable');
                btn_rm.linkbutton('enable');
            }
        },
        onAfterEdit: function() {
            btn_save.hide(); btn_undo.hide();
            var inserted = datagrid.datagrid('getChanges', 'inserted');
            var updated = datagrid.datagrid('getChanges', 'updated');

            if (inserted.length > 0) {
                $.ajax({
                    url: '/management/service_item_add_test/', method: 'POST',
                    data: inserted[0],
                    success: function (data) {
                        if (data) {
                            console.log(data);
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '服务项目添加成功！' })
                        }
                    }
                });
            }
            if (updated.length > 0) {
                $.ajax({
                    url: '/management/service_item_update_test/', method: 'POST',
                    data: updated[0],
                    success: function (data) {
                        if (data.success) {
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '服务项目更新成功！' })
                        } else {
                            alert('错误');
                        }
                    }
                });
            }
            edit_row = undefined; selected_row = undefined;
            datagrid.datagrid('unselectAll');
            btn_add.linkbutton('enable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            btn_save.hide(); btn_undo.hide();
        }
    });

});