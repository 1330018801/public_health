$(function () {
    $('#child_health_1_2').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var resident_id = $('#resident_id').val();
    var item_alias = undefined;

    var btn_add_1 = toolbar.find('#add_1').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_2 = toolbar.find('#add_2').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_3 = toolbar.find('#add_3').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_4 = toolbar.find('#add_4').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });
    btn_save.linkbutton('disable');
    btn_undo.linkbutton('disable');


    btn_add_1.bind('click', function () {
        panel.panel({
            href: '/child/health_1_2_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_12_month' }
        });
        item_alias =  'aftercare_12_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_add_2.bind('click', function () {
        panel.panel({
            href: '/child/health_1_2_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_18_month' }
        });
        item_alias =  'aftercare_18_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });


    btn_add_3.bind('click', function () {
        panel.panel({
            href: '/child/health_1_2_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_24_month' }
        });
        item_alias =  'aftercare_24_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_add_4.bind('click', function () {
        panel.panel({
            href: '/child/health_1_2_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_30_month' }
        });
        item_alias =  'aftercare_30_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/child/health_1_2_submit/',
            onSubmit: function (param) {
                if(!form.find('input[name=weight_grade]').is(":checked")){
                    $.messager.alert('提示', '请选择体重等级', 'info');
                    return false;
                }
                if(!form.find('input[name=height_grade]').is(":checked")){
                    $.messager.alert('提示', '请选择身高等级', 'info');
                    return false;
                }
                if(!form.find('input[name=complexion]').is(":checked")){
                    $.messager.alert('提示', '请选择面色情况', 'info');
                    return false;
                }
                if(!form.find('input[name=skin]').is(":checked")){
                    $.messager.alert('提示', '请选择皮肤是否异常', 'info');
                    return false;
                }
                if(item_alias != 'aftercare_30_month'){
                    if(!form.find('input[name=bregma]').is(":checked")){
                        $.messager.alert('提示', '请选择前囟是否闭合', 'info');
                        return false;
                    }
                }
                if(!form.find('input[name=eye_appearance]').is(":checked")){
                    $.messager.alert('提示', '请选择眼外观是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=ear_appearance]').is(":checked")){
                    $.messager.alert('提示', '请选择耳外观是否异常', 'info');
                    return false;
                }
                if(item_alias == 'aftercare_12_month' | item_alias == 'aftercare_24_month'){
                    if(!form.find('input[name=hearing]').is(":checked")){
                        $.messager.alert('提示', '请选择听力是否通过', 'info');
                        return false;
                    }
                }
                if(!form.find('input[name=heart_lung]').is(":checked")){
                    $.messager.alert('提示', '请选择心肺是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=abdomen]').is(":checked")){
                    $.messager.alert('提示', '请选择腹部是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=all_fours]').is(":checked")){
                    $.messager.alert('提示', '请选择四肢是否异常', 'info');
                    return false;
                }
                if(item_alias != 'aftercare_12_month'){
                    if(!form.find('input[name=step]').is(":checked")){
                        $.messager.alert('提示', '请选择步态是否异常', 'info');
                        return false;
                    }
                }
                if(item_alias != 'aftercare_30_month'){
                    if(!form.find('input[name=growth_evaluate]').is(":checked")){
                        $.messager.alert('提示', '请选择发育评估情况', 'info');
                        return false;
                    }
                }
                if(!form.find('input[name=two_visit_disease]').is(":checked")){
                    $.messager.alert('提示', '请选择两次随访间患病情况', 'info');
                    return false;
                }
                if(!form.find('input[name=transfer_treatment_suggestion]').is(":checked")){
                    $.messager.alert('提示', '请选择转诊建议', 'info');
                    return false;
                }
                if(!form.find('input[name=guide]').is(":checked")){
                    $.messager.alert('提示', '请选择指导方式', 'info');
                    return false;
                }

                if(form.form('validate')){
                    param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    param.item_alias = item_alias;
                    return true;
                }
                else{
                    return false;
                }
            },
            success: function (data) {
                var data_obj = eval('(' + data + ')');
                if (data_obj.success) {
                    $.messager.show({title: '提示', msg: '随访记录保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '随访记录保存失败', 'warning');
                }
                panel.panel({ href: '/child/health_1_2_review/' });
                btn_save.linkbutton('disable');
                btn_undo.linkbutton('disable');
            }
        });
    });

    btn_undo.bind('click', function () {
        panel.panel({ href: '/child/health_1_2_review/' });
        btn_add_1.linkbutton('enable');
        btn_add_2.linkbutton('enable');
        btn_add_3.linkbutton('enable');
        btn_add_4.linkbutton('enable');
    });

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    panel.panel({ href: '/child/health_1_2_review/' });

});