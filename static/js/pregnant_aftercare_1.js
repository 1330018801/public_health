$(function () {
    var area = $('#pregnant_aftercare_1');
    var toolbar = area.find('#toolbar');
    var form = area.find('#form');
    var table = area.find('#table');

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_suspend = toolbar.find('#suspend').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    //btn_edit.linkbutton('disable');

    btn_print.bind('click', function () { table.find('.print_area').printThis(); });

    btn_suspend.bind('click', function () {
        form.form('submit', {
            url: '/pregnant/aftercare_1_suspend/', method: 'POST',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
            },
            success: function (json_data) {
                var data = eval('(' + json_data + ')');
                if (data.success) {
                    $.messager.alert('提示', '第一次产前随访记录表暂存完成', 'info');
                } else {
                    $.messager.alert('提示', '第一次产前随访记录表暂存失败', 'info');
                }
            }
        })
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/pregnant/aftercare_1_submit/', method: 'POST',
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
                    /*
                    $.ajax({
                        url: '/pregnant/aftercare_1_review/', method: 'POST',
                        data: {'resident_id': resident_id},
                        success: function (data) {
                            if (data.success) {
                                table.html(data.message);
                            }
                        }
                    });
                    */
                    table.panel('refresh');
                    $.messager.show({title: '提示', msg: '第一次产前随访记录保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '第一次产前随访记录保存失败', 'info');
                }
            }
        });
    });
    /*
    $.ajax({
        url: '/pregnant/aftercare_1_review/', method: 'POST',
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
    */
    table.panel({ href : '/pregnant/aftercare_1_table/'})
});