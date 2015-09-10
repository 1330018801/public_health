$(function() {
    var selected_row = undefined;
    var edit_row = undefined;

    var toolbar = $('#inspection_toolbar');

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
            $.messager.confirm('确认操作', '是要删除所选择的巡查登记吗？', function(flag) { if (flag) {
                $.ajax({
                    url: '/supervision/inspection_del/', method: 'POST',
                    data: { id: selected_row.id },
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', msg: '巡查登记删除成功！' });
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
    toolbar.find('#inspector').textbox({width: 100});

    var btn_query = toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        datagrid.datagrid('load');
    });

    var datagrid = $('#inspections').datagrid({
        title: '卫生监督协管巡查登记', url: '/supervision/inspection_list/',
        toolbar: '#inspection_toolbar', autoRowHeight: false, nowrap: false,
        rownumbers: true, singleSelect: true, fitColumns: true, pagination: true,
        pageList: [10, 15, 20, 25, 30, 40, 50], pageSize: 15,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'place_content', title: '巡查地点与内容', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'main_problem', title: '发现的主要问题', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'inspection_date', title: '巡查日期', width: 10, editor: {
                type: 'datebox', options: { required: true, editable: false }
            } },
            { field: 'inspector', title: '巡查人员', width: 5, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            }},
            { field: 'remarks', title: '备注', width: 15, editor: {
                type: 'textbox', options: { required: true, multiline: true, height: 100 }
            } },
            { field: 'create_by', title: '登记人员', width: 5 },
            { field: 'create_time', title: '登记时间 ', width: 10 },
            { field: 'update_time', title: '最后修改时间 ', width: 10 }
        ]],
        onBeforeLoad: function(param) {
            param.begin_date = toolbar.find('#begin_date').datebox('getValue');
            param.end_date = toolbar.find('#end_date').datebox('getValue');
            param.inspector = toolbar.find('#inspector').textbox('getValue');
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
            $('#save, #undo').hide();
            var inserted_row = $(this).datagrid('getChanges', 'inserted');
            var updated_row = $(this).datagrid('getChanges', 'updated');

            if (inserted_row.length > 0) {
                $.ajax({
                    url: '/supervision/inspection_add/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '卫生监督协管巡查登记成功！'});
                    }
                });
            }
            if (updated_row.length > 0) {
                $.ajax({
                    url: '/supervision/inspection_update/', method: 'POST',
                    data: updated_row[0],
                    success: function () {
                        datagrid.datagrid('load');
                        datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '卫生监督协管巡查登记更新成功！' });
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

    $.extend($.fn.datagrid.defaults.editors, {
        textarea1: {
            init: function(container, options){
                var input = $('<textarea class="datagrid-editable-input" rows='+options.rows+'></textarea>').appendTo(container);
                return input;
            },
            getValue: function(target){
                return $(target).val();
            },
            setValue: function(target, value){
                $(target).val(value);
            },
            resize: function(target, width){
                var input = $(target);
                if ($.boxModel == true){
                    input.width(width - (input.outerWidth() - input.width()));
                } else {
                    input.width(width);
                }
            }
        }
    });
});