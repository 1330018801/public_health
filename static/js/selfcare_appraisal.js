$(function () {
    var toolbar = $('#toolbar');
    var panel = $('#table');
    var form = $('#form');

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });


    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/old/living_selfcare_appraisal_submit/', method: 'POST',
                onSubmit: function (param) {
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
                        panel.panel({
                            href: '/old/living_selfcare_appraisal_review/', method: 'POST',
                            onLoad: function () {
                                if (form.find('input[name=total]').length == 0) {
                                    btn_save.linkbutton('disable');
                                    btn_print.linkbutton('enable');
                                } else {
                                    btn_save.linkbutton('enable');
                                    btn_print.linkbutton('disable');
                                }
                            }
                        });
                        $.messager.show({title: '提示', msg: '老年人生活自理能力评估保存成功', timeout: 1000});
                    } else {
                        $.messager.alert('提示', '老年人生活自理能力评估保存失败', 'info');
                    }
                }
            });
        }
    });

    panel.panel({
        href: '/old/living_selfcare_appraisal_review/', method: 'POST',
        onLoad: function () {
            if (form.find('input[name=total]').length == 0) {
                btn_save.linkbutton('disable');
                btn_print.linkbutton('enable');
            } else {
                btn_save.linkbutton('enable');
                btn_print.linkbutton('disable');
            }
        }
    });
});