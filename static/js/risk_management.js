$(function() {
    var selected_row = undefined;
    var edit_row = undefined;

    var toolbar = $('#risk_management_toolbar');

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    btn_save.hide(); btn_undo.hide();

    btn_add.bind('click', function () {
        if (edit_row == undefined) {
            btn_save.show(); btn_undo.show();
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            datagrid.datagrid('insertRow', { index: 0, row: {} });
            datagrid.datagrid('beginEdit', 0);
            edit_row = 0;

        }
    });

    btn_rm.bind('click', function () {
        if (selected_row) {
            $.messager.confirm('确认操作', '是要删除所选择的风险管理记录吗？', function(flag) { if (flag) {
                $.ajax({
                    url: '/infectious/risk_management_del/', method: 'POST',
                    data: { id: selected_row.id },
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', msg: '风险管理记录删除成功！' });
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
        datagrid.datagrid('load');
    });

    var datagrid = $('#risk_management').datagrid({
        title: '传染病疫情和突发公卫事件风险管理', url: '/infectious/risk_management_list/',
        toolbar: '#risk_management_toolbar', autoRowHeight: false, nowrap: false,
        rownumbers: true, singleSelect: true, fitColumns: true, pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'risk_inspection', title: '风险排查', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'risk_information', title: '风险信息', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'risk_evaluation', title: '风险评估', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'contingency_plan', title: '应急预案', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            }},
            { field: 'report_time', title: '报告时间', width: 10 }
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
                    url: '/infectious/risk_management_add/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '风险管理记录成功！'});
                    }
                });
            }
            if (updated_row.length > 0) {
                $.ajax({
                    url: '/infectious/risk_management_update/', method: 'POST',
                    data: updated_row[0],
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '风险管理记录更新成功！' });
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