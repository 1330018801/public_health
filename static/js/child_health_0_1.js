$(function () {
    $('#child_health_0_1').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
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
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_0_1_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_1_month' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_1_month';
            btn_add_1.linkbutton('disable');
            btn_add_2.linkbutton('disable');
            btn_add_3.linkbutton('disable');
            btn_add_4.linkbutton('disable');
            btn_save.linkbutton('enable');
            btn_undo.linkbutton('enable');
            btn_print.linkbutton('disable');
        }
    });

    btn_add_2.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_0_1_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_3_month' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_3_month';
            btn_add_1.linkbutton('disable');
            btn_add_2.linkbutton('disable');
            btn_add_3.linkbutton('disable');
            btn_add_4.linkbutton('disable');
            btn_save.linkbutton('enable');
            btn_undo.linkbutton('enable');
            btn_print.linkbutton('disable');
        }
    });


    btn_add_3.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_0_1_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_6_month' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_6_month';
            btn_add_1.linkbutton('disable');
            btn_add_2.linkbutton('disable');
            btn_add_3.linkbutton('disable');
            btn_add_4.linkbutton('disable');
            btn_save.linkbutton('enable');
            btn_undo.linkbutton('enable');
            btn_print.linkbutton('disable');
        }
    });

    btn_add_4.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_0_1_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_8_month' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_8_month';
            btn_add_1.linkbutton('disable');
            btn_add_2.linkbutton('disable');
            btn_add_3.linkbutton('disable');
            btn_add_4.linkbutton('disable');
            btn_save.linkbutton('enable');
            btn_undo.linkbutton('enable');
            btn_print.linkbutton('disable');
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/child/health_0_1_submit/',
                onSubmit: function (param) {
                    if (!form.find('input[name=weight_grade]').is(":checked")) {
                        $.messager.alert('提示', '请选择体重等级', 'info');
                        return false;
                    }
                    if (!form.find('input[name=height_grade]').is(":checked")) {
                        $.messager.alert('提示', '请选择身高等级', 'info');
                        return false;
                    }
                    if (!form.find('input[name=complexion]').is(":checked")) {
                        $.messager.alert('提示', '请选择面色情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=skin]').is(":checked")) {
                        $.messager.alert('提示', '请选择皮肤是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=bregma]').is(":checked")) {
                        $.messager.alert('提示', '请选择前囟是否闭合', 'info');
                        return false;
                    }
                    if (item_alias != 'aftercare_8_month') {
                        if (!form.find('input[name=neck_enclosed_mass]').is(":checked")) {
                            $.messager.alert('提示', '请选择是否有颈部包块', 'info');
                            return false;
                        }
                    }
                    if (!form.find('input[name=eye_appearance]').is(":checked")) {
                        $.messager.alert('提示', '请选择眼外观是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=ear_appearance]').is(":checked")) {
                        $.messager.alert('提示', '请选择耳外观是否异常', 'info');
                        return false;
                    }
                    if (item_alias == 'aftercare_6_month') {
                        if (!form.find('input[name=hearing]').is(":checked")) {
                            $.messager.alert('提示', '请选择听力是否通过', 'info');
                            return false;
                        }
                    }
                    if (item_alias == 'aftercare_1_month' | item_alias == 'aftercare_3_month') {
                        if (!form.find('input[name=oral_cavity]').is(":checked")) {
                            $.messager.alert('提示', '请选择口腔是否异常', 'info');
                            return false;
                        }
                    }
                    if (!form.find('input[name=heart_lung]').is(":checked")) {
                        $.messager.alert('提示', '请选择心肺是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=abdomen]').is(":checked")) {
                        $.messager.alert('提示', '请选择腹部是否异常', 'info');
                        return false;
                    }
                    if (item_alias == 'aftercare_1_month' | item_alias == 'aftercare_3_month') {
                        if (!form.find('input[name=navel]').is(":checked")) {
                            $.messager.alert('提示', '请选择脐部是否异常', 'info');
                            return false;
                        }
                    }
                    if (!form.find('input[name=all_fours]').is(":checked")) {
                        $.messager.alert('提示', '请选择四肢是否异常', 'info');
                        return false;
                    }
                    if (item_alias != 'aftercare_1_month') {
                        if (!form.find('input[name=rickets_symptom]').is(":checked")) {
                            $.messager.alert('提示', '请选择可疑佝偻病症状', 'info');
                            return false;
                        }
                    }
                    if (item_alias == 'aftercare_1_month' | item_alias == 'aftercare_3_month') {
                        if (!form.find('input[name=rickets_sign]').is(":checked")) {
                            $.messager.alert('提示', '请选择可疑佝偻病体征', 'info');
                            return false;
                        }
                    }
                    if (!form.find('input[name=anus_externalia]').is(":checked")) {
                        $.messager.alert('提示', '请选择肛门/外生殖是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=growth_evaluate]').is(":checked")) {
                        $.messager.alert('提示', '请选择发育评估情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=two_visit_disease]').is(":checked")) {
                        $.messager.alert('提示', '请选择两次随访间患病情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=transfer_treatment_suggestion]').is(":checked")) {
                        $.messager.alert('提示', '请选择转诊建议', 'info');
                        return false;
                    }
                    if (!form.find('input[name=guide]').is(":checked")) {
                        $.messager.alert('提示', '请选择指导方式', 'info');
                        return false;
                    }

                    if (form.form('validate')) {
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                        param.item_alias = item_alias;
                        return true;
                    }
                    else {
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
                    panel.panel({ href: '/child/health_0_1_review/' });
                    btn_save.linkbutton('disable');
                    btn_undo.linkbutton('disable');
                    btn_print.linkbutton('enable');
                }
            });
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_0_1_review/',
                onLoad: function () {
                    if ($.trim(panel.find('.1_month').html())) {
                        btn_add_1.linkbutton('disable');
                    } else {
                        btn_add_1.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.3_month').html())) {
                        btn_add_2.linkbutton('disable');
                    } else {
                        btn_add_2.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.6_month').html())) {
                        btn_add_3.linkbutton('disable');
                    } else {
                        btn_add_3.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.8_month').html())) {
                        btn_add_4.linkbutton('disable');
                    } else {
                        btn_add_4.linkbutton('enable');
                    }
                }
            });
            btn_save.linkbutton('disable');
            btn_undo.linkbutton('disable');
            btn_print.linkbutton('enable');
        }
    });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });

    panel.panel({
        href: '/child/health_0_1_review/',
        onLoad: function () {
            if ($.trim(panel.find('.1_month').html())) {
                btn_add_1.linkbutton('disable');
            }
            if ($.trim(panel.find('.3_month').html())) {
                btn_add_2.linkbutton('disable');
            }
            if ($.trim(panel.find('.6_month').html())) {
                btn_add_3.linkbutton('disable');
            }
            if ($.trim(panel.find('.8_month').html())) {
                btn_add_4.linkbutton('disable');
            }
        }
    });

});