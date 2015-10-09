$(function() {
    var ehr_accordion = $('#family_ehr');
    // panel 1
    var toolbar = $('#family_toolbar');
    var family_datagrid = $('#family_list');
    var adult_add_dialog = $('#adult_add_dialog');
    var adult_add_tb = $('#adult_add_tb');
    // panel 2
    var personal_info_form = $('#personal_info_form');
    var personal_info_table = $('#personal_info_table');
    // panel 3
    var body_exam_form = $('#body_exam_form');
    var body_exam_table = $('#body_exam_table');
    // panel 4
    var records_datagrid = $('#records_datagrid');

    // 家庭成员列表中选中和被编辑的行
    var selected_row = undefined;   // 行对象
    var edit_row = undefined;       // 行索引

    // 按钮声明和初始化
    // panel 1
    var child_add_btn = toolbar.find('#child_add').linkbutton({ iconCls: 'icon-add', plain: true });
    var child_edit_btn = toolbar.find('#child_edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var child_save_btn = toolbar.find('#child_save').linkbutton({ iconCls: 'icon-save', plain: true });
    var child_undo_btn = toolbar.find('#child_undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var adult_add_btn = toolbar.find('#adult_add').linkbutton({ iconCls: 'icon-add', plain: true });
    var old_add_btn = toolbar.find('#old_add').linkbutton({ iconCls: 'icon-add', plain: true });
    var chg_resident_btn = toolbar.find('#chg_resident').linkbutton({ iconCls: 'icon-add', plain: true });
    var member_rm_btn = toolbar.find('#member_rm').linkbutton({ iconCls: 'icon-remove', plain: true });

    // panel 2
    var personal_info_save_btn = $('#personal_info_save').linkbutton({ iconCls: 'icon-save', plain: true});
    var personal_info_edit_btn = $('#personal_info_edit').linkbutton({ iconCls: 'icon-edit', plain: true});
    var personal_info_undo_btn = $('#personal_info_undo').linkbutton({ iconCls: 'icon-undo', plain: true});
    var personal_info_print_btn = $('#personal_info_print').linkbutton({ iconCls: 'icon-print', plain: true});

    // panel 3
    var body_exam_save_btn = $('#body_exam_save').linkbutton({ iconCls: 'icon-save', plain: true});
    var body_exam_edit_btn = $('#body_exam_edit').linkbutton({ iconCls: 'icon-edit', plain: true});
    var body_exam_undo_btn = $('#body_exam_undo').linkbutton({ iconCls: 'icon-undo', plain: true});
    var body_exam_print_btn = $('#body_exam_print').linkbutton({ iconCls: 'icon-print', plain: true});

    //old_add_btn.linkbutton('disable');
    old_add_btn.hide();

    child_save_btn.linkbutton('disable');
    child_undo_btn.linkbutton('disable');
    child_edit_btn.hide();

    member_rm_btn.linkbutton('disable');
    chg_resident_btn.linkbutton('disable');
    personal_info_edit_btn.linkbutton('disable');
    personal_info_undo_btn.linkbutton('disable');
    body_exam_edit_btn.linkbutton('disable');
    body_exam_undo_btn.linkbutton('disable');

    child_add_btn.bind('click', function () {
        if (edit_row == undefined) {
            child_add_btn.linkbutton('disable');
            child_edit_btn.linkbutton('disable');
            child_save_btn.linkbutton('enable');
            child_undo_btn.linkbutton('enable');
            family_datagrid.datagrid('insertRow', { index: 0, row: {} });
            family_datagrid.datagrid('beginEdit', 0);
            edit_row = 0;

            var field = family_datagrid.datagrid('getEditor', { index: edit_row, field: 'gender' });
            $(field.target).combobox({
                valueField: 'value', textField: 'text', panelHeight: 72,
                data: [{'value': 2, 'text': '未知'},
                       {'value': 1, 'text': '男'},
                       {'value': 0, 'text': '女'}],
                onLoadSuccess: function() {
                    $(this).combobox('setValue', 2);
                }
            });
        }
    });

    child_edit_btn.bind('click', function () {
        $.messager.alert('提示', '暂时未开通此功能', 'info');
    });

    child_undo_btn.bind('click', function () {
        child_add_btn.linkbutton('enable');
        child_edit_btn.linkbutton('enable');
        child_save_btn.linkbutton('disable');
        child_undo_btn.linkbutton('disable');
        edit_row = undefined;
        selected_row = undefined;
        family_datagrid.datagrid('rejectChanges');
    });

    child_save_btn.bind('click', function () {
        family_datagrid.datagrid('endEdit', edit_row);
    });

    adult_add_btn.bind('click', function () {
        adult_add_dialog.dialog('open');
        adult_add_dialog.css('display', 'block');
    });

    chg_resident_btn.bind('click', function () {
        //当前，只有备切换对象的年龄小于16周岁时，才能切换成功
        if (selected_row) {
            //
            if (selected_row['age'] > 16) {
                $.messager.alert('提示', '只能切换给16周岁以下无身份证的居民', 'info');
            } else {
                $.ajax({
                    url: '/ehr/change_resident/', method: 'POST',
                    data: {'id': selected_row['id']},
                    success: function (data) {
                        if (data.success) {
                            $.cookie('resident_id', selected_row['id']);
                            $.cookie('resident_name', selected_row['name']);
                            $.cookie('resident_ehr_no', selected_row['ehr_no']);
                            $('#resident').html(data.message);
                            $.messager.show({title: '提示', msg: '当前服务对象切换为' + data.message, timeout: 1000});
                            selected_row = undefined;
                            chg_resident_btn.linkbutton('disabled');
                        } else {
                            $.messager.alert('提示', '服务对象切换失败', 'warning');
                        }
                    }
                });
            }
        } else {
            $.messager.alert('提示', '请在列表中选择被切换对象', 'info');
        }
    });

    member_rm_btn.bind('click', function () {
        if (selected_row) {
            var name = selected_row['name'];
            $.messager.confirm('操作确认', '真的要将'+name+'从家庭中删除吗？', function(flag) {
                if (flag) {
                    $.ajax({
                        url: '/ehr/family_member_rm/', method: 'POST',
                        data: {'id': selected_row['id']},
                        success: function () {
                            family_datagrid.datagrid('reload');
                            $.messager.show({'title': '操作提示', msg: '删除家庭成员完成', timeout: 1000});
                        }
                    });
                }
            });
        }
    });

    personal_info_save_btn.bind('click', function () {
        personal_info_form.form('submit', {
            url: '/ehr/personal_info_submit/', method: 'POST',
            onSubmit: function (param) {
                if(!personal_info_form.find('input[name=gender]').is(":checked")){
                    $.messager.alert('提示', '请选择性别', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=residence_type]').is(":checked")){
                    $.messager.alert('提示', '请选择常住类型', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=nation]').is(":checked")){
                    $.messager.alert('提示', '请选择民族', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=blood_type]').is(":checked")){
                    $.messager.alert('提示', '请选择血型', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=blood_rh]').is(":checked")){
                    $.messager.alert('提示', '请选择是是否RH阴性', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=education]').is(":checked")){
                    $.messager.alert('提示', '请选择文化程度', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=occupation]').is(":checked")){
                    $.messager.alert('提示', '请选择职业', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=marriage]').is(":checked")){
                    $.messager.alert('提示', '请选择婚姻状况', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=payment_way]').is(":checked")){
                    $.messager.alert('提示', '请选择医疗费用支付方式', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=allergy_history]').is(":checked")){
                    $.messager.alert('提示', '请选择药物过敏史', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=expose_history]').is(":checked")){
                    $.messager.alert('提示', '请选择暴露史', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=disease_history]').is(":checked")){
                    $.messager.alert('提示', '请选择既往史—疾病', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=surgery_history]').is(":checked")){
                    $.messager.alert('提示', '请选择既往史—手术', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=injury_history]').is(":checked")){
                    $.messager.alert('提示', '请选择既往史—外伤', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=transfusion_history]').is(":checked")){
                    $.messager.alert('提示', '请选择既往史—输血', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=family_history_father]').is(":checked")){
                    $.messager.alert('提示', '请选择家族史—父亲患病情况', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=family_history_mother]').is(":checked")){
                    $.messager.alert('提示', '请选择家族史—母亲患病情况', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=family_history_sibling]').is(":checked")){
                    $.messager.alert('提示', '请选择家族史—兄弟姐妹患病情况', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=family_history_children]').is(":checked")){
                    $.messager.alert('提示', '请选择家族史—子女患病情况', 'info');
                    return false;
                }
                if(!personal_info_form.find('input[name=genetic_disease]').is(":checked")){
                    $.messager.alert('提示', '请选择有无遗传病史', 'info');
                    return false;
                }
                if(personal_info_form.form('validate')){
                    param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    param.resident_id = selected_row['id'];
                    return true;
                }
                else{
                    return false;
                }
            },
            success: function (data) {
                var data_obj = eval('(' + data + ')');
                if (data_obj.success) {
                    $.messager.alert('提示', '个人基本信息表保存完成', 'info');
                    //var personal_info_panel = ehr_accordion.accordion('getSelected');
                    personal_info_table.panel('refresh');
                    family_datagrid.datagrid('reload');
                } else {
                    $.messager.alert('提示', '个人基本信息表保存失败', 'warning');
                }
            }
        })
    });

    personal_info_print_btn.bind('click', function () {
        personal_info_table.find('.print_area').printThis();
    });

    // 提交成年人家庭成员对话框的工具栏的控件及事件绑定
    adult_add_tb.find('#name').textbox();
    adult_add_tb.find('#gender').combobox({
        valueField: 'value', textField: 'text', panelHeight: 72, width: 50,
        data: [{'value': 2, 'text': '全部'},
               {'value': 1, 'text': '男'},
               {'value': 0, 'text': '女'}],
        onLoadSuccess: function() {
            $(this).combobox('setValue', 2);
        }
    });

    adult_add_tb.find('#identity').textbox({ width: 150 });
    var adult_add_query = adult_add_tb.find('#query').linkbutton({
        iconCls: 'icon-glyphicons-28-search', plain: true
    });

    adult_add_query.bind('click', function () {
        adult_add_dg.datagrid('reload');
    });

    // 向家庭添加成人成员时显示的候选人列表
    var adult_add_dg = $('#adult_add_dg').datagrid({
        url: '/ehr/family_add_adult_query/',
        toolbar: '#adult_add_tb', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'name', title: '姓名', width: 5 },
            { field: 'gender', title: '性别', width: 4 },
            { field: 'age', title: '年龄', width: 4 },
            { field: 'birthday', title: '出生日期', width: 8 },
            { field: 'nation', title: '民族', width: 4 },
            { field: 'identity', title: '身份证号码', width: 10 },
            { field: 'address', title: '住址', width: 15 },
            { field: 'mobile', title: '电话', width: 6 }
        ]],
        onBeforeLoad: function (param) {
            param.name = adult_add_tb.find('#name').textbox('getValue');
            param.gender = adult_add_tb.find('#gender').combobox('getValue');
            param.identity = adult_add_tb.find('#identity').textbox('getValue');
        }
    });

    body_exam_save_btn.bind('click', function () {
        body_exam_form.form('submit', {
            url: '/ehr/body_exam_submit/', method: 'POST',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                param.resident_id = selected_row['id'];
            },
            success: function (data) {
                var data_obj = eval('(' + data + ')');
                if (data_obj.success) {
                    $.messager.alert('提示', '健康体检表保存完成', 'info');
                    //var personal_info_panel = ehr_accordion.accordion('getSelected');
                    body_exam_table.panel('refresh');
                    family_datagrid.datagrid('reload');
                } else {
                    $.messager.alert('提示', '健康体检表保存失败', 'warning');
                }
            }
        })
    });

    body_exam_print_btn.bind('click', function () {
        // 打印体检表的内容
    });

    // 添加成年人家庭成员的对话框
    adult_add_dialog.dialog({
        title: '添加成年人进入家庭', closed: true, height: 300,
        buttons: [
            {
                text: '添加',
                iconCls: 'icon-ok',
                handler: function () {
                    //将此居民加入家庭
                    if (adult_add_dg.datagrid('getSelected')){
                        console.log(adult_add_dg.datagrid('getSelected')['id']);
                        $.ajax({
                            url: '/ehr/family_add_adult/', method: 'POST',
                            data: {'id': adult_add_dg.datagrid('getSelected')['id']},
                            success: function () {
                                adult_add_dialog.dialog('close');
                                family_datagrid.datagrid('reload');
                                $.messager.show({title: '提示', msg: '添加家庭成员完成', timeout: 1000});
                            }
                        });
                    }
                }
            },{
                text: '取消',
                iconCls: 'icon-cancel',
                handler: function () {
                    adult_add_dialog.dialog('close');
                }
            }
        ],
        onOpen: function () {
        },
        onClose: function () {
            adult_add_tb.find('#name').textbox('reset');
            adult_add_tb.find('#identity').textbox('reset');
            adult_add_tb.find('#gender').textbox('reset');
            adult_add_dg.datagrid('loadData', [])
        }
    });

    // 家庭成员列表
    family_datagrid.datagrid({
        url: '/ehr/family_list/',
        toolbar: '#family_toolbar', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                if (value == null) return '未建档';
                if (value == '13108200000000000') return '未编号';
                return value;
            } },
            { field: 'name', title: '姓名', width: 5, editor: {
                type: 'textbox', options: { required: true }
            } },
            { field: 'gender', title: '性别', width: 4, editor: {
                type: 'combobox', options: { required: true, editable: false }
            } },
            { field: 'age', title: '年龄', width: 4 },
            { field: 'birthday', title: '出生日期', width: 8, editor: {
                type: 'datebox', options: { required: true, editable: false }
            } },
            { field: 'nation', title: '民族', width: 4, editor: {
                type: 'textbox', options: { required: true }
            } },
            { field: 'identity', title: '身份证号码', width: 10 },
            { field: 'address', title: '住址', width: 8, editor: {
                type: 'textbox'
            } },
            { field: 'speciality', title: '所属重点人群', width: 10 },
            { field: 'mobile', title: '电话', width: 6 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
                member_rm_btn.linkbutton('disable');
                chg_resident_btn.linkbutton('disable');
            } else {
                selected_row = row;
                member_rm_btn.linkbutton('enable');
                if (row['age'] > 16 || row['id'] == $.cookie('resident_id')) {
                    chg_resident_btn.linkbutton('disable');
                } else {
                    chg_resident_btn.linkbutton('enable');
                }
            }
        },
        onAfterEdit: function() {
            var inserted_row = $(this).datagrid('getChanges', 'inserted');
            var updated_row = $(this).datagrid('getChanges', 'updated');

            if (inserted_row.length > 0) {
                $.ajax({
                    url: '/ehr/child_add_new/', method: 'POST',
                    data: inserted_row[0],
                    success: function() {
                        family_datagrid.datagrid('reload');
                        family_datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '婴幼儿添加进入家庭成功！'});
                    }
                });
            }
            if (updated_row.length > 0) {
                $.ajax({
                    url: '/ehr/child_update_new/', method: 'POST',
                    data: updated_row[0],
                    success: function () {
                        family_datagrid.datagrid('reload');
                        family_datagrid.datagrid('unselectAll');
                        $.messager.show({ title: '提示', timeout: 1000, msg: '婴幼儿信息更新成功！' });
                    }
                });
            }
            edit_row = undefined; selected_row = undefined;
            child_add_btn.linkbutton('enable');
            child_edit_btn.linkbutton('enable');
            child_save_btn.linkbutton('disable');
            child_undo_btn.linkbutton('disable');
        }
    });

    ehr_accordion.accordion({
        onSelect: function (title, index) {
            if (index == 3) {
                records_datagrid.datagrid({
                    url: '/ehr/record_list/', rownumbers: true, singleSelect: true, fitColumns: true,
                    columns: [[
                        { field: 'id', title: '编码', hidden: true},
                        { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                            if (value == null) {
                                return '未建档';
                            }
                            if (value == '13108200000000000') {
                                return '未编号';
                            }
                            return value;
                        } },
                        { field: 'resident_name', title: '居民', width: 4 },
                        { field: 'doctor_name', title: '医生', width: 4 },
                        { field: 'service_type', title: '服务类别', width: 10 },
                        { field: 'service_item', title: '服务项目', width: 10 },
                        { field: 'submit_time', title: '服务时间', width: 8 }
                    ]],
                    onBeforeLoad: function (param) {
                        if (selected_row == undefined) {
                            $.messager.alert('提示', '请选中居民后才能查看服务记录', 'warning');
                            return false;
                        } else {
                            param.resident_id = selected_row['id'];
                            return true;
                        }
                    },
                    onDblClickRow: function (index, row) {
                        var detail = $('#record_detail_review').dialog({
                            title: '服务详情', width: 820, height: 500, method: 'POST', modal: true,
                            href: '/ehr/record_detail_review/', queryParams: {record_id: row['id']},
                            buttons: [{
                                text: '打印', iconCls: 'icon-print',
                                handler: function () {
                                    detail.find('.print_area').printThis();
                                }
                            },{
                                text: '关闭', iconCls: 'icon-cancel',
                                handler: function () {
                                    detail.dialog('close');
                                }
                            }]
                        });
                        detail.css('display', 'block');
                        detail.dialog('center');
                    }
                });
            } else if (index == 1) {
                if (selected_row != undefined) {
                    personal_info_table.panel({
                        href: '/ehr/personal_info_review_new/', method: 'POST',
                        queryParams: {resident_id: selected_row['id']}
                    });
                    /*
                    if (selected_row['ehr_no'] == null) {
                        personal_info_save_btn.linkbutton('enable');
                        personal_info_undo_btn.linkbutton('enable');
                        personal_info_edit_btn.linkbutton('disable');
                    } else {
                        personal_info_edit_btn.linkbutton('enable');
                        personal_info_save_btn.linkbutton('disable');
                        personal_info_undo_btn.linkbutton('disable');
                    }
                    */
                } else {
                    $.messager.alert('提示', '请在家庭成员列表中选择居民', 'info');
                }
            } else if (index == 2) {
                if (selected_row !== undefined) {
                    body_exam_table.panel({
                        href: '/ehr/body_exam_table/', method: 'POST',
                        queryParams: {resident_id: selected_row['id']}
                    });
                    // some code goes here
                } else {
                    $.messager.alert('提示', '请在家庭成员列表中选择居民', 'info');
                }
            }
        }
    });

});