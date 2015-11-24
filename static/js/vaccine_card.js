$(function () {

    var resident_id = $('#resident_id').val();
    var username = $('#username').val();
    var head_table = $('#head_table').panel({ border: false });
    var head_tb = $('#head_tb');
    var head_form = $('#head_form');
    var list_tb = $('#list_tb');
    var card_exist = false;

    var btn_head_save = head_tb.find('#head_save').linkbutton({ plain: true, iconCls: 'icon-save' });
    var btn_head_edit = head_tb.find('#head_edit').linkbutton({ plain: true, iconCls: 'icon-edit' });
    var btn_head_undo = head_tb.find('#head_undo').linkbutton({ plain: true, iconCls: 'icon-undo' });
    var btn_head_print = head_tb.find('#head_print').linkbutton({ plain: true, iconCls: 'icon-print' });

    btn_head_print.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            head_table.find('.print_area').printThis();
        }
    });

    btn_head_save.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            head_form.form('submit', {
                url: '/vaccine/vaccine_card_head_save/',
                onSubmit: function (param) {
                    if ($('#register_local').is(':checked')){
                        head_form.find('#register_province').textbox('setValue', '河北');
                        head_form.find('#register_city').textbox('setValue', '廊坊');
                        head_form.find('#register_county').textbox('setValue', '三河');
                        var home_town = head_form.find('#home_town').combobox('getValue');
                        head_form.find('#register_town').textbox('setValue', home_town);
                        console.log(head_form.find('#register_town').textbox('getValue'));
                    }
                    param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    param.resident_id = resident_id;
                    param.home_county = '三河市'
                },
                success: function (data) {
                    var data_obj = eval('(' + data + ')');
                    if(data_obj.success) {
                        $.ajax({
                            url: '/vaccine/vaccine_card_head/', method: 'POST',
                            data: {'resident_id': resident_id},
                            success: function (data) {
                                if (data.success) {
                                    head_table.html(data.message);
                                    head_table.css('display', 'block');
                                    head_table.panel('refresh');
                                }
                            }
                        });
                        card_exist = true;
                        $.messager.show({title: '提示', msg: '新生儿建卡完成'});
                    } else {
                        $.messager.alert('提示', '新生儿建卡失败', 'info');
                    }
                }
            })
        }
    });
    btn_head_edit.bind('click', function () {});
    btn_head_undo.bind('click', function () {});

    head_form.find('#ehr_village_no').textbox({width: 40, required: true, validType: 'length[3, 3]'});
    head_form.find('#ehr_unique_no').textbox({width: 60, required: true, validType: 'length[5, 5]'});
    head_form.find('#gender').combobox({ width: 40, panelHeight: 48,
        valueField: 'id', textField: 'text', required: true,
        data: [
            {'id': 2, 'text': ''},
            {'id': 0, 'text': '女'},
            {'id': 1, 'text': '男'}
        ] });
    head_form.find('#birth_date').datebox({ width: 100, required: true, editable: false });
    head_form.find('#guardian_name').textbox({ width: 80, required: true });
    head_form.find('#relation_to_child').textbox({ width: 80, required: true });
    head_form.find('#contact_number').numberbox({ width: 100, required: true });
    head_form.find('#home_town').combobox({width: 100, required: true, editable: false,
        valueField: 'id', textField: 'name', url: '/management/get_towns/',
        onBeforeLoad: function (param) {
            param.first_text = '';
        }});
    head_form.find('#register_province').textbox({width: 60, align: 'right'});
    head_form.find('#register_city').textbox({width: 60});
    head_form.find('#register_county').textbox({width: 60});
    head_form.find('#register_town').textbox({width: 60});
    head_form.find('#immigrate_time').datebox({ width: 100, editable: false });
    head_form.find('#emigrate_time').datebox({ width: 100, editable: false });
    head_form.find('#emigrate_reason').textbox({ width: 100 });
    head_form.find('#vaccine_abnormal_reaction_history').textbox({width: 400, required: true });
    head_form.find('#census_register_address_extra').textbox({width: 100 });
    head_form.find('#vaccinate_taboo').textbox({ width: 400, required: true });
    head_form.find('#infection_history').textbox({ width: 400, required: true });
    var today = myformatter(new Date());
    head_form.find('#found_card_date').datebox({ width: 100, required: true, editable: false, value: today });
    head_form.find('#found_card_person').textbox({ width: 80, required: true, value: username });


    var btn_list_save = list_tb.find('#save').linkbutton({ plain: true, iconCls: 'icon-save' });
    var btn_list_undo = list_tb.find('#undo').linkbutton({ plain: true, iconCls: 'icon-undo' });
    var btn_list_print = list_tb.find('#print').linkbutton({ plain: true, iconCls: 'icon-print' });

    btn_list_save.linkbutton('disable');
    btn_list_undo.linkbutton('disable');

    btn_list_print.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            datagrid.datagrid('getPanel').panel('body').printThis();
        }
    });

    btn_list_save.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            datagrid.datagrid('endEdit', edit_row);
        }
    });
    btn_list_undo.bind('click', function () {
        datagrid.datagrid('rejectChanges');
        selected_row = undefined;
        edit_row = undefined;
        btn_list_save.linkbutton('disable');
        btn_list_undo.linkbutton('disable');
    });

    var datagrid = $('#vaccine_dg');
    var selected_row = undefined;       // 当前选中的行对象
    var edit_row = undefined;           // 当前编辑的行索引

    var vaccine_position = [{text: '上臂三角肌'}, {text: '上臂三角肌中部略下处'}, {text: '上臂外侧三角肌'},
        {text: '上臂外侧三角肌附着处'}, {text: '上臂外侧三角肌下缘附着处'}, {text: '其他'}];

    datagrid.datagrid({
        url: '/vaccine/vaccine_records/',
        toolbar: '#list_tb', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'name', title: '疫苗与剂次', width: 10 },
            { field: 'visit_date', title: '接种日期', width: 10, editor: {
                type: 'textbox', options: { required: true, editable: false }
            } },
            { field: 'vaccinate_position', title: '接种部位', width: 12, editor: {
                type: 'combobox', options: {
                    valueField: 'text', textField: 'text', data: vaccine_position,
                    required: true, panelHeight: 144
                }
            } },
            { field: 'batch_number', title: '疫苗批号', width: 10, editor: {
                type: 'textbox', options: { required: true }
            } },
            { field: 'doctor_signature', title: '接种医生', width: 5, editor: {
                type: 'textbox', options: { required: true, editable:false }
            } },
            { field: 'remarks', title: '备注', width: 15, editor: {
                type: 'textbox'
            } },
            { field: 'next_vaccinate_date', title: '下次接种日期', width: 10, editor: {
                type: 'datebox', options: { editable: false }
            } }
        ]],
        onBeforeLoad: function(param) {
            param.resident_id = resident_id;
        },
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = datagrid.datagrid('getSelected');
            }
        },
        onDblClickRow: function (index, row) {
            if (card_exist) {
                if (row['visit_date']) {
                    $.messager.alert('提示', row['name']+'已经接种过', 'info');
                } else {
                    datagrid.datagrid('beginEdit', index);
                    edit_row = index;
                    selected_row = row;
                    var doctor_signature = get_edit_field(edit_row, 'doctor_signature');
                    $(doctor_signature.target).textbox('setValue', username);
                    var visit_date = get_edit_field(edit_row, 'visit_date');
                    $(visit_date.target).textbox('setValue', today);
                    btn_list_save.linkbutton('enable');
                    btn_list_undo.linkbutton('enable');
                }
            } else {
                $.messager.alert('提示', '请先建立预防接种卡基本信息', 'info');
            }
        },
        onAfterEdit: function () {
            var updated = datagrid.datagrid('getChanges', 'updated');
            if (updated.length > 0) {
                var param = updated[0];
                param['id'] = selected_row['id'];
                $.ajax({
                    url: '/vaccine/vaccinate_submit/', method: 'POST',
                    data: param,
                    success: function (data) {
                        if (data.success) {
                            datagrid.datagrid('reload');
                            datagrid.datagrid('unselectAll');
                            $.messager.show({ title: '提示', timeout: 1000, msg: '预防接种记录保存成功' })
                        }
                    }
                });
            }
            edit_row = undefined; selected_row = undefined;
            btn_list_save.linkbutton('disable');
            btn_list_undo.linkbutton('disable');
        }
    });

    // 页面初始化后，判断该居民是否已经建立过预防接种卡
    $.ajax({
        url: '/vaccine/vaccine_card_head/', method: 'POST',
        data: {'resident_id': resident_id},
        success: function (data) {
            if (data.success) {
                card_exist = true;
                btn_head_save.linkbutton('disable');
                btn_head_edit.linkbutton('disable');
                btn_head_undo.linkbutton('disable');
                head_table.html(data.message);
            }
            head_table.css('display', 'block');
        }
    });

    list_tb.css('display', 'block');
    head_tb.css('display', 'block');


    function get_edit_field(index, field) {
        return datagrid.datagrid('getEditor', { index: index, field: field })
    }

});