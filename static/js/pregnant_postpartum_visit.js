$(function () {
    var toolbar = $('#toolbar');
    var table = $('#pregnant_postpartum_visit_table');
    var form = $('#pregnant_postpartum_visit_form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        table.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/pregnant/postpartum_visit_submit/', method: 'POST',
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
                    $.ajax({
                        url: '/pregnant/postpartum_visit_review/', method: 'POST',
                        data: {'resident_id': resident_id},
                        success: function (data) {
                            if (data.success) {
                                table.html(data.message);
                            }
                        }
                    });
                    $.messager.show({title: '提示', msg: '产后方式记录表保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '产后访视记录表保存失败', 'info');
                }
            }
        });
    });

    $.ajax({
        url: '/pregnant/postpartum_visit_review/', method: 'POST',
        data: {'resident_id': resident_id},
        success: function (data) {
            if (data.success) {
                table.html(data.message);
                table.css('display', 'block');
                btn_save.linkbutton('disable');
                btn_edit.linkbutton('disable');
            } else {
                table.css('display', 'block');
                btn_edit.linkbutton('disable');
                btn_print.linkbutton('disable');
            }
        }
    });
});