$(function () {
    var form = $('#personal_info_form');
    var table = $('#personal_info_table');

    var datagrid = table.parents('#ehr_setup_tabs').find('#ehr_resident_list');
    var selected_row = datagrid.datagrid('getSelected');

    var save_btn = $('#personal_info_save').linkbutton({ iconCls: 'icon-save', plain: true});
    var print_btn = $('#personal_info_print').linkbutton({ iconCls: 'icon-print', plain: true});
    print_btn.linkbutton('disable');

    print_btn.bind('click', function(){
        if($(this).linkbutton('options').disabled == false){
            table.find('.print_area').printThis();
        }
    });

    save_btn.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/ehr/personal_info_submit/', method: 'POST',
                onSubmit: function (param) {
                    if (!form.find('input[name=gender]').is(":checked")) {
                        $.messager.alert('提示', '请选择性别', 'info');
                        return false;
                    }
                    if (!form.find('input[name=residence_type]').is(":checked")) {
                        $.messager.alert('提示', '请选择常住类型', 'info');
                        return false;
                    }
                    if (!form.find('input[name=nation]').is(":checked")) {
                        $.messager.alert('提示', '请选择民族', 'info');
                        return false;
                    }
                    /*
                     if(!form.find('input[name=blood_type]').is(":checked")){
                     $.messager.alert('提示', '请选择血型', 'info');
                     return false;
                     }
                     if(!form.find('input[name=blood_rh]').is(":checked")){
                     $.messager.alert('提示', '请选择是是否RH阴性', 'info');
                     return false;
                     }
                     */
                    if (!form.find('input[name=education]').is(":checked")) {
                        $.messager.alert('提示', '请选择文化程度', 'info');
                        return false;
                    }
                    if (!form.find('input[name=occupation]').is(":checked")) {
                        $.messager.alert('提示', '请选择职业', 'info');
                        return false;
                    }
                    if (!form.find('input[name=marriage]').is(":checked")) {
                        $.messager.alert('提示', '请选择婚姻状况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=payment_way]').is(":checked")) {
                        $.messager.alert('提示', '请选择医疗费用支付方式', 'info');
                        return false;
                    }
                    if (!form.find('input[name=allergy_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择药物过敏史', 'info');
                        return false;
                    }
                    if (!form.find('input[name=expose_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择暴露史', 'info');
                        return false;
                    }
                    if (!form.find('input[name=disease_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择既往史—疾病', 'info');
                        return false;
                    }
                    if (!form.find('input[name=surgery_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择既往史—手术', 'info');
                        return false;
                    }
                    if (!form.find('input[name=injury_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择既往史—外伤', 'info');
                        return false;
                    }
                    if (!form.find('input[name=transfusion_history]').is(":checked")) {
                        $.messager.alert('提示', '请选择既往史—输血', 'info');
                        return false;
                    }
                    if (!form.find('input[name=family_history_father]').is(":checked")) {
                        $.messager.alert('提示', '请选择家族史—父亲患病情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=family_history_mother]').is(":checked")) {
                        $.messager.alert('提示', '请选择家族史—母亲患病情况', 'info');
                        return false;
                    }
                    /*
                     if(!form.find('input[name=family_history_sibling]').is(":checked")){
                     $.messager.alert('提示', '请选择家族史—兄弟姐妹患病情况', 'info');
                     return false;
                     }
                     if(!form.find('input[name=family_history_children]').is(":checked")){
                     $.messager.alert('提示', '请选择家族史—子女患病情况', 'info');
                     return false;
                     }
                     */
                    if (!form.find('input[name=genetic_disease]').is(":checked")) {
                        $.messager.alert('提示', '请选择有无遗传病史', 'info');
                        return false;
                    }
                    if (form.form('validate')) {
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                        if (selected_row && selected_row['personal_info'] == '否')
                            param.resident_id = selected_row['id'];

                        return true;
                    }
                    else {
                        return false;
                    }
                },
                success: function (data) {
                    var data = eval('(' + data + ')');
                    if (data.success) {
                        $.messager.show({title: '提示', msg: '个人基本信息表保存完成', timeout: 2000});
                        table.panel({
                            href: '/ehr/personal_info_review/', method: 'POST',
                            queryParams: {resident_id: data.resident_id}
                        });
                        print_btn.linkbutton('enable');
                        save_btn.linkbutton('disable');
                        var tabs = form.parents('#ehr_setup_tabs');
                        tabs.find('#ehr_resident_list').datagrid('reload');
                    } else {
                        $.messager.alert('提示', '个人基本信息表保存失败', 'warning');
                    }
                }
            })
        }
    });

    table.panel({
        href: '/ehr/personal_info_setup/',
        onLoad: function () {
            if (selected_row) {
                form.find('input[textboxname=resident_name]').textbox('setValue', selected_row['name']);
                if (selected_row['identity'])
                    form.find('input[textboxname=identity]').textbox('setValue', selected_row['identity']);
                if (selected_row['birthday'])
                    var b = selected_row['birthday'].split("-");
                    var birth = new Date(b[0], b[1], b[2]);
                    var today = new Date();
                    if(today.getFullYear()-birth.getFullYear()<6){
                        form.find('input[textboxname=identity]').textbox({required: false});
                    }
                    else if(today.getFullYear()-birth.getFullYear()==6){
                        if(today.getMonth()>birth.getMonth())
                            form.find('input[textboxname=identity]').textbox({required: true});
                        else if(today.getMonth()==birth.getMonth())
                            if(today.getDate()<birth.getDate())
                                form.find('input[textboxname=identity]').textbox({required: false});
                            else
                                form.find('input[textboxname=identity]').textbox({required: true});
                        else
                            form.find('input[textboxname=identity]').textbox({required: false});
                    }
                    else
                        form.find('input[textboxname=identity]').textbox({required: true});
                    form.find('input[textboxname=birthday]').datebox('setValue', selected_row['birthday']);
                if(selected_row['ehr_no']){
                    form.find('input[textboxname=ehr_village_no]').textbox('setValue', selected_row['ehr_no'].substring(9, 12));
                    form.find('input[textboxname=ehr_unique_no]').textbox('setValue', selected_row['ehr_no'].substring(12, 17));
                }
            }
        }
    });

});