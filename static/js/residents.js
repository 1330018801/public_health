$(function() {

    /*
        这个列表中包括刷身份证获得的居民信息，部分居民还没有建档
        当前设计中，不能增加居民信息，不能删除居民信息，
        只能修改居民所在乡镇、村庄、地址以及电话等信息
     */

    $.extend($.fn.validatebox.defaults.rules, {
        maxLength: {
            validator: function(value, param){
                return value.length >= param[0];
            },
            message: '身份证号码最多{0}位'
        }
    });

    // 工具栏初始化
    var toolbar = $('#resident_toolbar');

    var btn_add = toolbar.find('#add').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_rm = toolbar.find('#remove').linkbutton({ iconCls: 'icon-remove', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });

    var btn_hypt = toolbar.find('#hypertension').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_diab = toolbar.find('#diabetes').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_psyc = toolbar.find('#psychiatric').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_preg = toolbar.find('#pregnant').linkbutton({ iconCls: 'icon-add', plain: true });

    var btn_query = toolbar.find('#query').linkbutton({
        iconCls: 'icon-glyphicons-28-search', plain: true
    });
    btn_save.hide(); btn_undo.hide();
    btn_edit.linkbutton('disable'); btn_rm.linkbutton('disable');

    var query_town = toolbar.find('#query_town');
    query_town.combobox({
        url: '/management/get_towns/',
        valueField: 'id', textField: 'name', editable: false, width: 120,
        onLoadSuccess: function () { $(this).combobox('setValue', '0'); },
        onSelect: function (rec) {
            var url = '/management/get_town_villages/' + rec.id + '/';
            query_village.combobox('reload', url);
            query_village.combobox('setValue', '0');
        }
    });

    var query_village = toolbar.find('#query_village');
    query_village.combobox({
        valueField: 'id', textField: 'name', editable: false, width: 100,
        data: [{ 'id': '0', 'name': '全部' }],
        onLoadSuccess: function () { $(this).combobox('setValue', '0'); }
    });

    var query_ehr_no = toolbar.find('#query_ehr_no').combobox({
        valueField: 'id', textField: 'status', editable: false, width: 80,
        data: [{ 'id': 0, 'status': '全部'}, { 'id': -1, 'status': '未建档'},
               { 'id': 1, 'status': '已建档'}],
        panelHeight: 72
    });

    var query_crowd = toolbar.find('#query_crowd').combobox({
        valueField: 'alias', textField: 'text', editable: false, width: 80,
        data: [{ 'alias': 'all', 'text': '全体'},
               { 'alias': 'hypertension', 'text': '高血压'},
               { 'alias': 'diabetes', 'text': '2型糖尿病'},
               { 'alias': 'psychiatric', 'text': '重性精神疾病'},
               { 'alias': 'pregnant', 'text': '孕产妇'},
               { 'alias': 'old', 'text': '老年人'},
               { 'alias': 'child', 'text': '0-6岁儿童'}
        ],
        panelHeight: 168
    });

    var query_name = toolbar.find('#query_name').textbox({ width: 80 });
    var query_identity = toolbar.find('#query_identity').textbox({ width: 150, options: { validateType: 'maxLength(18)'}});

    // 工具栏事件绑定

    btn_add.bind('click', function () {
        datagrid.datagrid('insertRow', { index: 0, row: {} });
        edit_row = 0;
        btn_save.show(); btn_undo.show();
        btn_add.linkbutton('disable');
        btn_edit.linkbutton('disable');
        btn_rm.linkbutton('disable');
        datagrid.datagrid('beginEdit', edit_row);
        townOptions(get_edit_field(edit_row, 'town'), edit_row);
    });

    btn_edit.bind('click', function () {
        if (selected_row == undefined) {
            $.messager.alert('警告', '请先选定记录再修改！', 'warning');
        } else {
            edit_row = datagrid.datagrid('getRowIndex', selected_row);
            btn_save.show(); btn_undo.show();
            btn_add.linkbutton('disable');
            btn_edit.linkbutton('disable');
            btn_rm.linkbutton('disable');
            datagrid.datagrid('beginEdit', edit_row);
            // 如果该居民没有建档，那么无法编辑其健康档案编号
            var ehr_no = get_edit_field(edit_row, 'ehr_no');
            if (selected_row['ehr_no'] == null) {
                $(ehr_no.target).textbox('disable');
            }
            townOptions(get_edit_field(edit_row, 'town'), edit_row);
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
                        url: '/management/resident_del_test/', method: 'POST',
                        data: { resident_id: ids[0] },
                        success: function (data) {
                            if (data) {
                                datagrid.datagrid('reload');
                                datagrid.datagrid('unselectAll');
                                selected_row = undefined;
                                btn_edit.linkbutton('disable');
                                btn_rm.linkbutton('disable');
                                edit_row = undefined;
                                $.messager.show({ title: '提示', timeout: 1000, msg: '居民信息成功！' })
                            }
                        }
                    });
                }
            });
        } else {
            $.messager.alert('提示', '请选择所要删除的卫生室', 'info');
        }
    });

    btn_query.bind('click', function () {
        datagrid.datagrid('reload');
    });

    btn_save.bind('click', function () {
        datagrid.datagrid('endEdit', edit_row);
    });

    btn_undo.bind('click', function () {
        datagrid.datagrid('rejectChanges');
        selected_row = undefined; edit_row = undefined;
        btn_save.hide(); btn_undo.hide();
        btn_add.linkbutton('enable');
    });

    btn_hypt.bind('click', function () {
        if (selected_row != undefined) {
            $.ajax({
                url: '/management/resident_add_hypertension/', method: 'POST',
                data: {resident_id: selected_row['id']},
                success: function (data) {
                    if (data.success) {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入高血压人群成功',
                            timeout: 1000
                        });
                    } else {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入高血压人群失败: '+data.message,
                            timeout: 1000
                        });
                    }
                }
            });
        } else {
            $.messager.alert('提示', '请选择将要加入高血压人群的居民', 'info');
        }
    });

    btn_diab.bind('click', function () {
        if (selected_row != undefined) {
            $.ajax({
                url: '/management/resident_add_diabetes/', method: 'POST',
                data: {resident_id: selected_row['id']},
                success: function (data) {
                    if (data.success) {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入2型糖尿病人群成功',
                            timeout: 1000
                        });
                    } else {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入2型糖尿病人群失败: '+data.message,
                            timeout: 1000
                        });
                    }
                }
            });
        } else {
            $.messager.alert('提示', '请选择将要加入2型糖尿病人群的居民', 'info');
        }
    });

    btn_psyc.bind('click', function () {
        if (selected_row != undefined) {
            $.ajax({
                url: '/management/resident_add_psychiatric/', method: 'POST',
                data: {resident_id: selected_row['id']},
                success: function (data) {
                    if (data.success) {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入重性精神疾病人群成功',
                            timeout: 1000
                        });
                    } else {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入重性精神疾病人群失败: '+data.message,
                            timeout: 1000
                        });
                    }
                }
            });
        } else {
            $.messager.alert('提示', '请选择将要加入重性精神疾病人群的居民', 'info');
        }
    });

    btn_preg.bind('click', function () {
        if (selected_row != undefined) {
            $.ajax({
                url: '/management/resident_add_pregnant/', method: 'POST',
                data: {resident_id: selected_row['id']},
                success: function (data) {
                    if (data.success) {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入孕产妇人群成功',
                            timeout: 1000
                        });
                    } else {
                        $.messager.show({
                            title: '提示',
                            msg: selected_row['name']+'添加进入孕产妇人群失败: '+data.message,
                            timeout: 1000
                        });
                    }
                }
            });
        } else {
            $.messager.alert('提示', '请选择将要加入孕产妇人群的居民', 'info');
        }
    });

    // 工具栏上按钮的可用状态以及是否显示，决定于这两个变量的值
    var selected_row = undefined;
    var edit_row = undefined;

    var datagrid = $('#resident_list');
    datagrid.datagrid({
        toolbar: '#resident_toolbar',
        url: '/management/resident_query_list/',
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
            { field: 'gender', title: '性别', width: 6,
                formatter: function(value) {
                    switch (value) {
                        case '0': return '女';
                        case '1': return '男';
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
            { field: 'address', title: '地址', width: 20, editor: { type: 'textbox' } },
            { field: 'mobile', title: '电话', width: 12, editor: {
                type: 'textbox', options: { required: true } } }
        ]],
        onBeforeLoad: function (param) {
            param.query_town = query_town.combobox('getValue');
            param.query_village = query_village.combobox('getValue');
            param.query_name = query_name.textbox('getValue');
            param.query_identity = query_identity.textbox('getValue');
            param.query_ehr_no = query_ehr_no.combobox('getValue');
            param.query_crowd = query_crowd.combobox('getValue');
        },
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
            var inserted = datagrid.datagrid('getChanges', 'inserted');
            var updated = datagrid.datagrid('getChanges', 'updated');

            if (inserted.length > 0) {
                $.ajax({
                    url: '/management/resident_add_test/', method: 'POST',
                    data: inserted[0],
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('reload');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '居民信息记录添加成功！' })
                        }
                    }
                });
            }
            if (updated.length > 0) {
                $.ajax({
                    url: '/management/resident_update_test/', method: 'POST',
                    data: updated[0],
                    success: function (data) {
                        if (data) {
                            datagrid.datagrid('load');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '居民信息记录更新成功！' })
                        }
                    }
                });
            }
            edit_row = undefined;
            btn_save.hide(); btn_undo.hide();
            selected_row = undefined;
            btn_add.linkbutton('enable');
        }
    });

    function townOptions(field, index) {
        var current = $(field.target).combobox('getValue');
        $(field.target).combobox({
            url: '/management/get_towns_edit/',
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
                param.town_name = town_name
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