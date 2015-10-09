$(function () {
    $('#child_health_3_6').panel({ fit: true });
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
                href: '/child/health_3_6_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_3_year' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_3_year';
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
                href: '/child/health_3_6_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_4_year' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_4_year';
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
                href: '/child/health_3_6_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_5_year' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_5_year';
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
                href: '/child/health_3_6_form/', method: 'POST',
                queryParams: { item_alias: 'aftercare_6_year' },
                onLoad: function () {}
            });
            item_alias = 'aftercare_6_year';
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
                url: '/child/health_3_6_submit/',
                onSubmit: function (param) {
                    if (!form.find('input[name=weight_grade]').is(":checked")) {
                        $.messager.alert('提示', '请选择体重等级', 'info');
                        return false;
                    }
                    if (!form.find('input[name=height_grade]').is(":checked")) {
                        $.messager.alert('提示', '请选择身高等级', 'info');
                        return false;
                    }
                    if (!form.find('input[name=body_growth_evaluate]').is(":checked")) {
                        $.messager.alert('提示', '请选择体格发育评价情况', 'info');
                        return false;
                    }
                    if (item_alias == 'aftercare_3_year') {
                        if (!form.find('input[name=hearing]').is(":checked")) {
                            $.messager.alert('提示', '请选择听力是否通过', 'info');
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
                    panel.panel({
                        href: '/child/health_3_6_review/',
                        onLoad: function () {
                            if ($.trim(panel.find('.3_year').html())) {
                                btn_add_1.linkbutton('disable');
                            } else {
                                btn_add_1.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.4_year').html())) {
                                btn_add_2.linkbutton('disable');
                            } else {
                                btn_add_2.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.5_year').html())) {
                                btn_add_3.linkbutton('disable');
                            } else {
                                btn_add_3.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.6_year').html())) {
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
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/child/health_3_6_review/',
                onLoad: function () {
                    if ($.trim(panel.find('.3_year').html())) {
                        btn_add_1.linkbutton('disable');
                    } else {
                        btn_add_1.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.4_year').html())) {
                        btn_add_2.linkbutton('disable');
                    } else {
                        btn_add_2.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.5_year').html())) {
                        btn_add_3.linkbutton('disable');
                    } else {
                        btn_add_3.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.6_year').html())) {
                        btn_add_4.linkbutton('disable');
                    } else {
                        btn_add_4.linkbutton('enable');
                    }
                }
            });
            btn_add_1.linkbutton('enable');
            btn_add_2.linkbutton('enable');
            btn_add_3.linkbutton('enable');
            btn_add_4.linkbutton('enable');
        }
    });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });

    panel.panel({
        href: '/child/health_3_6_review/',
        onLoad: function () {
            if ($.trim(panel.find('.3_year').html())) {
                btn_add_1.linkbutton('disable');
            }
            if ($.trim(panel.find('.4_year').html())) {
                btn_add_2.linkbutton('disable');
            }
            if ($.trim(panel.find('.5_year').html())) {
                btn_add_3.linkbutton('disable');
            }
            if ($.trim(panel.find('.6_year').html())) {
                btn_add_4.linkbutton('disable');
            }
        }
    });

});