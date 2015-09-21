$(function () {
    var toolbar = $('#toolbar');
    var panel = $('#table');
    var form = $('#form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    //var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    //btn_edit.linkbutton('disable');
    var btn_suspend = toolbar.find('#suspend').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_suspend.bind('click', function () {
        form.form('submit', {
            url: '/psychiatric/body_exam_suspend/', method: 'POST',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
            },
            success: function (json_data) {
                var data = eval('(' + json_data + ')');
                if (data.success) {
                    $.messager.alert('提示', '重性精神疾病健康体检暂存完成', 'info');
                } else {
                    $.messager.alert('提示', '重性精神疾病健康体检暂存失败', 'info');
                }
            }
        })
    });


    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/psychiatric/body_exam_submit/', method: 'POST',
            onSubmit: function (param) {
                if(!form.find('input[name=mouth_lip]').is(":checked")){
                    $.messager.alert('提示', '请选择脏器功能—口腔—口唇', 'info');
                    return false;
                }
                if (!form.find('input[name=mouth_tooth]').is(":checked")) {
                    $.messager.alert('提示', '请选择脏器功能—口腔—齿列', 'info');
                    return false;
                }
                if (!form.find('input[name=mouth_throat]').is(":checked")) {
                    $.messager.alert('提示', '请选择脏器功能—口腔—咽部', 'info');
                    return false;
                }
                if (!form.find('input[name=hearing]').is(":checked")) {
                    $.messager.alert('提示', '请选择脏器功能—听力', 'info');
                    return false;
                }
                if (!form.find('input[name=movement_function]').is(":checked")) {
                    $.messager.alert('提示', '请选择脏器功能—运动功能', 'info');
                    return false;
                }
                if (!form.find('input[name=skin]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—皮肤', 'info');
                    return false;
                }
                if (!form.find('input[name=lymph_node]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—淋巴结', 'info');
                    return false;
                }
                if(!form.find('input[name=lung_barrel_chested]').is(":checked")){
                    $.messager.alert('提示', '请选择查体—肺—桶状胸', 'info');
                    return false;
                }
                if (!form.find('input[name=lung_breath_sound]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—肺—呼吸音', 'info');
                    return false;
                }
                if (!form.find('input[name=lung_rale]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—肺—罗音', 'info');
                    return false;
                }
                if (!form.find('input[name=heart_rhythm]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—心脏—心律', 'info');
                    return false;
                }
                if (!form.find('input[name=heart_noise]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—心脏—杂音', 'info');
                    return false;
                }
                if (!form.find('input[name=stomach_tenderness]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—腹部—压痛', 'info');
                    return false;
                }
                if (!form.find('input[name=stomach_enclosed_mass]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—腹部—包块', 'info');
                    return false;
                }
                if(!form.find('input[name=stomach_hepatomegaly]').is(":checked")){
                    $.messager.alert('提示', '请选择查体—腹部—肝大', 'info');
                    return false;
                }
                if (!form.find('input[name=stomach_slenauxe]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—腹部—脾大', 'info');
                    return false;
                }
                if (!form.find('input[name=stomach_shifting_dullness]').is(":checked")) {
                    $.messager.alert('提示', '请选择查体—腹部—移动性浊音', 'info');
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
                    panel.panel('refresh', '/psychiatric/body_exam_form/');
                    $.messager.show({title: '提示', msg: '重性精神疾病患者健康体检保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '重性精神疾病患者健康体检保存失败', 'info');
                }
            }
        });
    });

    panel.panel({ href: '/psychiatric/body_exam_form/', method: 'POST' });
});