$(function () {
    $('#psychiatric_aftercare').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var resident_id = $('#resident_id').val();
    var item_alias = undefined;

    var btn_add = [9];
    for (var i = 1; i < 9; i++) {
        btn_add[i] = toolbar.find('#add_'+i).linkbutton({ iconCls: 'icon-add', plain: true });
    }

    btn_add[1].bind('click', function () {
        panel.panel({ href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_1' }
        });
        item_alias = 'aftercare_1';
    });

    btn_add[2].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_2' }
        });
        item_alias = 'aftercare_2';
    });

    btn_add[3].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_3' }
        });
        item_alias = 'aftercare_3';
    });

    btn_add[4].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_4' }
        });
        item_alias = 'aftercare_4';
    });

    btn_add[5].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_5' }
        });
        item_alias = 'aftercare_5';
    });

    btn_add[6].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_6' }
        });
        item_alias = 'aftercare_6';
    });

    btn_add[7].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_7' }
        });
        item_alias = 'aftercare_7';
    });

    btn_add[8].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_8' }
        });
        item_alias = 'aftercare_8';
    });

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
             url: '/psychiatric/aftercare_submit/',
             onSubmit: function (param) {
                 if(!form.find('input[name=dangerousness]').is(":checked")){
                     $.messager.alert('提示', '请选择危险性等级', 'info');
                     return false;
                 }
                 if(!form.find('input[name=now_symptom]').is(":checked")){
                    $.messager.alert('提示', '请选择目前症状', 'info');
                    return false;
                 }
                if (!form.find('input[name=insight]').is(":checked")) {
                    $.messager.alert('提示', '请选择自知力', 'info');
                    return false;
                }
                if(!form.find('input[name=sleep_situation]').is(":checked")){
                    $.messager.alert('提示', '请选择睡眠情况', 'info');
                    return false;
                }
                if(!form.find('input[name=diet_situation]').is(":checked")){
                    $.messager.alert('提示', '请选择有饮食情况', 'info');
                    return false;
                }
                if(!form.find('input[name=society_function_individual_life_care]').is(":checked")){
                    $.messager.alert('提示', '请选择社会功能情况—个人生活料理情况', 'info');
                    return false;
                }
                if(!form.find('input[name=society_function_housework]').is(":checked")){
                    $.messager.alert('提示', '请选择听社会功能情况—家务劳动情况', 'info');
                    return false;
                }
                if(!form.find('input[name=society_function_productive_work]').is(":checked")){
                    $.messager.alert('提示', '请选择社会功能情况—生产劳动及工作情况', 'info');
                    return false;
                }
                if(!form.find('input[name=society_function_learn_ability]').is(":checked")){
                    $.messager.alert('提示', '请选择社会功能情况—学习能力情况', 'info');
                    return false;
                }
                if (!form.find('input[name=society_function_social_interpersonal]').is(":checked")) {
                    $.messager.alert('提示', '请选择社会功能情况—社会人际交往情况', 'info');
                    return false;
                }
                if(!form.find('input[name=lock_situation]').is(":checked")){
                    $.messager.alert('提示', '请选择关锁情况', 'info');
                    return false;
                }
                if(!form.find('input[name=hospitalized_situation]').is(":checked")){
                    $.messager.alert('提示', '请选择住院情况', 'info');
                    return false;
                }
                if(!form.find('input[name=laboratory_examination]').is(":checked")){
                    $.messager.alert('提示', '请选择有无实验室检查', 'info');
                    return false;
                }
                if(!form.find('input[name=take_medicine_compliance]').is(":checked")){
                    $.messager.alert('提示', '请选择药物依从性情况', 'info');
                    return false;
                }
                if(!form.find('input[name=medicine_untoward_effect]').is(":checked")){
                    $.messager.alert('提示', '请选择是否有药物不良反应', 'info');
                    return false;
                }
                 if(!form.find('input[name=treatment_effect]').is(":checked")){
                    $.messager.alert('提示', '请选择治疗效果情况', 'info');
                    return false;
                }
                if(!form.find('input[name=transfer_treatment]').is(":checked")){
                    $.messager.alert('提示', '请选择是否转诊', 'info');
                    return false;
                }
                if(!form.find('input[name=recovery_measure]').is(":checked")){
                    $.messager.alert('提示', '请选择康复措施', 'info');
                    return false;
                }
                if(!form.find('input[name=visit_classification]').is(":checked")){
                    $.messager.alert('提示', '请选择本次随访分类', 'info');
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
                 panel.panel({
                     href: '/psychiatric/aftercare_form/', method: 'POST',
                     queryParams: {item_alias: item_alias}
                 })
             }
        });
    });

    btn_undo.bind('click', function () {});
    btn_print.bind('click', function () {});

    // panel.panel({ href: '/psychiatric/aftercare_review/' });

    /*
    $.ajax({
        url: '/services/pregnant/aftercare_finished/',
        success: function (data) {
            finished = data.finished;
            $.each(finished, function (index, item) {

            });
        }
    });
    */
});