$(function() {

    var query_town_clinic = $('#query_town_clinic');
    query_town_clinic.combobox({
        url: '/management/get_town_clinics/',
        valueField: 'id',textField: 'name', editable: false, width: 150,
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        }
    });

    var query_village = $('#query_village');
    query_village.textbox({ width: 100 });

    var toolbar = $('#village_clinic_tb');

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

    btn_add.bind('click', function () {
        if (edit_row == undefined) {
            btn_save.show(); btn_undo.show();
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            datagrid.datagrid('insertRow', { index: 0, row: {} });
            datagrid.datagrid('beginEdit', 0);
            edit_row = 0;
            townClinicOptions(get_edit_field(edit_row, 'town_clinic'));
        }
    });

    btn_edit.bind('click', function () {
        if (selected_row == undefined) {
            $.messager.alert('警告', '请先选定记录再修改！', 'warning');
        } else {
            edit_row = datagrid.datagrid('getRowIndex', selected_row);
            datagrid.datagrid('beginEdit', edit_row);
            townClinicOptions(get_edit_field(edit_row, 'town_clinic'));
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            btn_save.show(); btn_undo.show();
        }
    });

    btn_rm.bind('click', function () {
        var rows = datagrid.datagrid('getSelections');
        if (rows.length > 0) {
            $.messager.confirm('确认操作', '要删除所选择的卫生室吗？', function(flag) {
                if (flag) {
                    var ids = [];
                    for (var i = 0; i < rows.length; i++) {
                        ids.push(rows[i].id);
                    }
                    $.ajax({
                        url: '/management/village_clinic_del_test/', method: 'POST',
                        data: { service_item_id: ids[0] },
                        success: function (data) {
                            if (data) {
                                datagrid.datagrid('reload');
                                datagrid.datagrid('unselectAll');
                                selected_row = undefined; edit_row = undefined
                                btn_edit.linkbutton('disable');
                                btn_rm.linkbutton('disable');
                                $.messager.show({ title: '提示', timeout: 1000, msg: '卫生室删除成功！' })
                            }
                        }
                    });
                }
            });
        } else {
            $.messager.alert('提示', '请选择所要删除的卫生室', 'info');
        }
    });

    btn_save.bind('click', function () {
        datagrid.datagrid('endEdit', edit_row);
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
        datagrid.datagrid('reload', {
            query_town_clinic: query_town_clinic.combobox('getValue'),
            query_village: query_village.textbox('getValue')
        });
    });

    var selected_row = undefined;   // 选中行的对象
    var edit_row = undefined;       // 编辑行的index

    var datagrid = $('#village_clinics');
    datagrid.datagrid({
        title: '村卫生室信息列表', toolbar: '#village_clinic_tb',
        url: '/management/village_clinic_list_new/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        pagination: true, pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'name', title: '卫生室名称', width: 10, editor: {
                type: 'textbox', options: { required: true } } },
            { field: 'town_clinic', title: '所属卫生院', width: 20, editor: {
                    type: 'combobox', options: { editable: false, required: true } } },
            { field: 'address', title: '地址', width: 30, editor: {
                    type: 'textbox' } },
            { field: 'doctor_user_num', title: '医生用户数量', width: 20 }
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
        onDblClickRow: function(index, row) {
            alert('clinic on the row');
        },
        onAfterEdit: function() {
            btn_save.hide(); btn_undo.hide();
            var inserted = datagrid.datagrid('getChanges', 'inserted');
            var updated = datagrid.datagrid('getChanges', 'updated');

            if (inserted.length > 0) {
                $.ajax({
                    url: '/management/village_clinic_add_test/', method: 'POST',
                    data: inserted[0],
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '村卫生室添加成功！' })
                        }
                    }
                });
            }
            if (updated.length > 0) {
                $.ajax({
                    url: '/management/village_clinic_update_test/', method: 'POST',
                    data: updated[0],
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '村卫生室更新成功！' })
                        }
                    }
                });
            }
            edit_row = undefined;
            btn_add.linkbutton('enable');
            btn_edit.linkbutton('enable');
            btn_rm.linkbutton('enable');
        }
    });

    function townClinicOptions(field) {
        var current = $(field.target).combobox('getValue');
        $(field.target).combobox({
            url: '/management/get_town_clinic_edit/',
            valueField: 'name', textField: 'name', editable: false,
            onLoadSuccess: function() {
                if (current) {
                    $(this).combobox('setValue', current);
                } else {
                    $(this).combobox('setValue', '');
                }
            }
        });
    }

    function get_edit_field(index, field) {
        return datagrid.datagrid('getEditor', { index: index, field: field })
    }
});