$(function() {
    var selected_row = undefined;
    var edit_row = undefined;

    var toolbar = $('#info_report_toolbar');

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    btn_save.hide(); btn_undo.hide(); btn_edit.linkbutton('disable');

    btn_add.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (edit_row == undefined) {
                btn_save.show();
                btn_undo.show();
                btn_add.linkbutton('disable');
                btn_edit.linkbutton('disable');
                btn_rm.linkbutton('disable');
                datagrid.datagrid('insertRow', { index: 0, row: {} });
                datagrid.datagrid('beginEdit', 0);
                edit_row = 0;

                var field = datagrid.datagrid('getEditor', { index: edit_row, field: 'info_type' });
                $(field.target).combobox({
                    valueField: 'text', textField: 'text',
                    data: [
                        {'value': 1, 'text': '食品安全'},
                        {'value': 2, 'text': '饮用水卫生'},
                        {'value': 3, 'text': '职业病危害'},
                        {'value': 4, 'text': '学校卫生'},
                        {'value': 5, 'text': '非法行医（采供血）'},
                        {'value': 0, 'text': ''}
                    ],
                    onLoadSuccess: function () {
                        $(this).combobox('setValue', 0);
                    }
                });
            }
        }
    });

    btn_rm.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            if (selected_row) {
                $.messager.confirm('确认操作', '是要删除所选择的信息报告吗？', function (flag) {
                    if (flag) {
                        $.ajax({
                            url: '/supervision/info_report_del/', method: 'POST',
                            data: { id: selected_row.id },
                            success: function () {
                                datagrid.datagrid('load');
                                datagrid.datagrid('unselectAll');
                                $.messager.show({ title: '提示', msg: '信息报告登记删除成功！' });
                            }
                        });
                    }
                });
            } else {
                $.messager.alert('提示', '请选择所要删除的记录', 'info');
            }
            selected_row = undefined;
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('endEdit', edit_row);
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            btn_save.hide();
            btn_undo.hide();
            btn_add.linkbutton('enable');
            btn_edit.linkbutton('enable');
            btn_rm.linkbutton('enable');
            edit_row = undefined;
            selected_row = undefined;
            datagrid.datagrid('rejectChanges');
        }
    });

    toolbar.find('#begin_date').datebox({
        width: 100, editable: false, formatter: myformatter, parser :myparser
    });
    toolbar.find('#begin_date').datebox('setValue', newYearDay(new Date()));
    toolbar.find('#end_date').datebox({
        width: 100, editable: false, formatter: myformatter, parser :myparser
    });
    toolbar.find('#end_date').datebox('setValue', myformatter(new Date()));

    var btn_query = toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('load');
        }
    });

    var datagrid = $('#info_report').datagrid({
        title: '卫生监督协管信息报告登记', url: '/supervision/info_report_list/',
        toolbar: '#info_report_toolbar', autoRowHeight: false, nowrap: false,
        rownumbers: true, singleSelect: true, fitColumns: true, pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'discover_time', title: '发现时间', width: 10, editor: {
                type: 'datetimebox', options: { required: true, editable: false }
            } },
            { field: 'info_type', title: '信息类别', width: 10, editor: {
                type: 'combobox', options: { required: true, editable: false, panelHeight: 124 }
            } },
            { field: 'info_content', title: '信息内容', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'report_time', title: '报告时间', width: 10 },
            { field: 'reporter', title: '报告人', width: 5, editor: {
                type: 'textbox', options: { required: true }
            }}
        ]],
        onBeforeLoad: function(param) {
            param.begin_date = toolbar.find('#begin_date').datebox('getValue');
            param.end_date = toolbar.find('#end_date').datebox('getValue');
        },
        onClickRow: function (index, row) {
            if (selected_row != undefined && selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = $(this).datagrid('getSelected');
            }
        },
        onAfterEdit: function() {
            var inserted_row = $(this).datagrid('getChanges', 'inserted');
            var updated_row = $(this).datagrid('getChanges', 'updated');

            if (inserted_row.length > 0) {
                $.ajax({
                    url: '/supervision/info_report_add/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '卫生监督协管信息报告登记成功！'});
                    }
                });
            }
            if (updated_row.length > 0) {
                $.ajax({
                    url: '/supervision/info_report_update/', method: 'POST',
                    data: updated_row[0],
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '卫生监督协管信息报告登记更新成功！' });
                    }
                });
            }
            edit_row = undefined;
            selected_row = undefined;
            btn_add.linkbutton('enable');
            btn_edit.linkbutton('enable');
            btn_rm.linkbutton('enable');
            $('#save, #undo').hide();
        }
    });

});