$(function () {
    var toolbar = $('#toolbar');
    var table = $('#psy_info_table');
    var form = $('#psy_info_form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        table.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/psychiatric/personal_info_submit/', method: 'POST',
            onSubmit: function (param) {
                if (!form.find('input[name=assent]').is(":checked")) {
                    $.messager.alert('提示', '请选是否同意参加管理', 'info');
                    return false;
                }
                if (!form.find('input[name=symptom]').is(":checked")) {
                    $.messager.alert('提示', '请选择既往主要症状', 'info');
                    return false;
                }
                if (!form.find('input[name=cure_outpatient]').is(":checked")) {
                    $.messager.alert('提示', '请选择既往治疗情况（门诊）', 'info');
                    return false;
                }
                if (!form.find('input[name=cure_effect]').is(":checked")) {
                    $.messager.alert('提示', '请选择最近一次治疗效果', 'info');
                    return false;
                }
                if (!form.find('input[name=lock]').is(":checked")) {
                    $.messager.alert('提示', '请选择关锁情况', 'info');
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
                    $.ajax({
                        url: '/psychiatric/personal_info_review/', method: 'POST',
                        data: {'resident_id': resident_id},
                        success: function (data) {
                            if (data.success) {
                                table.html(data.message);
                                table.refresh();
                            }
                        }
                    });
                    $.messager.show({title: '提示', msg: '重性精神疾病患者个人信息补充表保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '重性精神疾病患者个人信息补充表保存失败', 'info');
                }
            }
        });
    });

    $.ajax({
        url: '/psychiatric/personal_info_review/', method: 'POST',
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