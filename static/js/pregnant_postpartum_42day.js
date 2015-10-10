$(function () {
    var area = $('#postpartum_42day');
    var toolbar = area.find('#toolbar');
    var form = area.find('#form');
    var table = area.find('#table');

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            table.find('#print_area').printThis();
        }
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/pregnant/postpartum_42day_submit/', method: 'POST',
                onSubmit: function (param) {
                    if (!form.find('input[name=breast]').is(":checked")) {
                        $.messager.alert('提示', '请选择乳房是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=lochia]').is(":checked")) {
                        $.messager.alert('提示', '请选择恶露是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=uterus]').is(":checked")) {
                        $.messager.alert('提示', '请选择子宫是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=wound]').is(":checked")) {
                        $.messager.alert('提示', '请选择伤口是否异常', 'info');
                        return false;
                    }
                    if (!form.find('input[name=classification]').is(":checked")) {
                        $.messager.alert('提示', '请选择分类', 'info');
                        return false;
                    }
                    if (!form.find('input[name=guide]').is(":checked")) {
                        $.messager.alert('提示', '请选择指导', 'info');
                        return false;
                    }
                    if (!form.find('input[name=dispose]').is(":checked")) {
                        $.messager.alert('提示', '请选处理', 'info');
                        return false;
                    }

                    if (form.form('validate')) {
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                        return true;
                    } else {
                        return false;
                    }
                },
                success: function (json_data) {
                    var data = eval('(' + json_data + ')');
                    if (data.success) {
                        table.panel({
                            href : '/pregnant/postpartum_42day_table/',
                            onLoad: function () {
                                if (form.find('input[name=visit_date]').length == 0) {
                                    btn_save.linkbutton('disable');
                                    btn_print.linkbutton('enable');
                                } else {
                                    btn_save.linkbutton('enable');
                                    btn_print.linkbutton('disable');
                                }
                            }
                        });
                        $.messager.show({title: '提示', msg: '产后42天健康检查表保存成功', timeout: 1000});
                    } else {
                        $.messager.alert('提示', '产后42天健康检查表保存失败', 'info');
                    }
                }
            });
        }
    });

    table.panel({
        href : '/pregnant/postpartum_42day_table/',
        onLoad: function () {
            if (form.find('input[name=visit_date]').length == 0) {
                btn_save.linkbutton('disable');
                btn_print.linkbutton('enable');
            } else {
                btn_save.linkbutton('enable');
                btn_print.linkbutton('disable');
            }
        }
    })
});