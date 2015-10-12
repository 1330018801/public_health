$(function () {
    var area = $('#tcm_child').panel({ fit: true });
    var toolbar = area.find('#toolbar');
    var form = area.find('#form');
    var panel = area.find('#table');
    var item_alias = undefined;

    var btn_add_1 = toolbar.find('#add_1').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_2 = toolbar.find('#add_2').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_3 = toolbar.find('#add_3').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_4 = toolbar.find('#add_4').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_5 = toolbar.find('#add_5').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_6 = toolbar.find('#add_6').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_save.linkbutton('disable');
    btn_undo.linkbutton('disable');

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/tcm/child_review/',
                onLoad: function () {
                    if ($.trim(panel.find('.6_month').html())) {
                        btn_add_1.linkbutton('disable');
                    } else {
                        btn_add_1.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.12_month').html())) {
                        btn_add_2.linkbutton('disable');
                    } else {
                        btn_add_2.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.18_month').html())) {
                        btn_add_3.linkbutton('disable');
                    } else {
                        btn_add_3.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.24_month').html())) {
                        btn_add_4.linkbutton('disable');
                    } else {
                        btn_add_4.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.30_month').html())) {
                        btn_add_5.linkbutton('disable');
                    } else {
                        btn_add_5.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.3_year').html())) {
                        btn_add_6.linkbutton('disable');
                    } else {
                        btn_add_6.linkbutton('enable');
                    }
                }
            });
            btn_save.linkbutton('disable');
            btn_undo.linkbutton('disable');
            btn_print.linkbutton('enable');
        }
    });

    btn_add_1.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_6_month';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_add_2.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_12_month';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_add_3.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_18_month';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_add_4.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_24_month';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_add_5.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_30_month';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_add_6.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            item_alias = 'aftercare_3_year';
            panel.panel({
                href: '/tcm/child_form/', method: 'POST',
                queryParams: { item_alias: item_alias },
                onLoad: function () {}
            });
            disable_buttons();
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/tcm/child_submit/',
                onSubmit: function (param) {
                    if (!form.find('input[name=guide]').is(":checked")) {
                        $.messager.alert('提示', '请选择中医药健康管理服务', 'info');
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
                        href: '/tcm/child_review/',
                        onLoad: function () {
                            if ($.trim(panel.find('.6_month').html())) {
                                btn_add_1.linkbutton('disable');
                            } else {
                                btn_add_1.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.12_month').html())) {
                                btn_add_2.linkbutton('disable');
                            } else {
                                btn_add_2.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.18_month').html())) {
                                btn_add_3.linkbutton('disable');
                            } else {
                                btn_add_3.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.24_month').html())) {
                                btn_add_4.linkbutton('disable');
                            } else {
                                btn_add_4.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.30_month').html())) {
                                btn_add_5.linkbutton('disable');
                            } else {
                                btn_add_5.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.3_year').html())) {
                                btn_add_6.linkbutton('disable');
                            } else {
                                btn_add_6.linkbutton('enable');
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

    panel.panel({
        href: '/tcm/child_review/', border: false,
        onLoad: function () {
            if ($.trim(panel.find('.6_month').html())) {
                btn_add_1.linkbutton('disable');
            }
            if ($.trim(panel.find('.12_month').html())) {
                btn_add_2.linkbutton('disable');
            }
            if ($.trim(panel.find('.18_month').html())) {
                btn_add_3.linkbutton('disable');
            }
            if ($.trim(panel.find('.24_month').html())) {
                btn_add_4.linkbutton('disable');
            }
            if ($.trim(panel.find('.30_month').html())) {
                btn_add_5.linkbutton('disable');
            }
            if ($.trim(panel.find('.3_year').html())) {
                btn_add_6.linkbutton('disable');
            }
        }
    });

    function disable_buttons () {
        btn_add_1.linkbutton('disable');
        btn_add_2.linkbutton('disable');
        btn_add_3.linkbutton('disable');
        btn_add_4.linkbutton('disable');
        btn_add_5.linkbutton('disable');
        btn_add_6.linkbutton('disable');

        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
        btn_print.linkbutton('disable');
    }
});