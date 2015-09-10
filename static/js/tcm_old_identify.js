$(function () {
    var toolbar = $('#toolbar');
    var panel = $('#table');
    var form = $('#form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });
    btn_edit.linkbutton('disable');

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/tcm/old_identify_submit/', method: 'POST',
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
                    panel.panel('refresh', '/tcm/old_identify_form/');
                    $.messager.show({title: '提示', msg: '重性精神疾病患者健康体检保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '重性精神疾病患者健康体检保存失败', 'info');
                }
            }
        });
    });

    panel.panel({ href: '/tcm/old_identify_form/', method: 'POST' });
});