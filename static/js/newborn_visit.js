$(function () {
    var area = $('#newborn_visit');
    var toolbar = area.find('#toolbar');
    var table = area.find('#table');
    var form = area.find('#form');

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    btn_edit.linkbutton('disable');
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        table.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/child/newborn_visit_submit/', method: 'POST',
            onSubmit: function (param) {
                if (!form.find('input[name=gender]').is(":checked")) {
                    $.messager.alert('提示', '请选择性别', 'info');
                    return false;
                }
                if (!form.find('input[name=birth_situation]').is(":checked")) {
                    $.messager.alert('提示', '请选择出生情况', 'info');
                    return false;
                }
                if (!form.find('input[name=newborn_asphyxia]').is(":checked")) {
                    $.messager.alert('提示', '请选择新生儿窒息', 'info');
                    return false;
                }
                if (!form.find('input[name=malformation_or_not]').is(":checked")) {
                    $.messager.alert('提示', '请选择是否有畸形', 'info');
                    return false;
                }
                if (!form.find('input[name=newborn_hearing_screening]').is(":checked")) {
                    $.messager.alert('提示', '请选择新生儿听力筛查', 'info');
                    return false;
                }
                if (!form.find('input[name=feed_way]').is(":checked")) {
                    $.messager.alert('提示', '请选择喂养方式', 'info');
                    return false;
                }
                if (!form.find('input[name=bregma_1]').is(":checked")) {
                    $.messager.alert('提示', '请选择前囟', 'info');
                    return false;
                }

                if (!form.find('input[name=eye_appearance]').is(":checked")) {
                    $.messager.alert('提示', '请选择眼外观是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=ear_appearance]').is(":checked")) {
                    $.messager.alert('提示', '请选择耳外观是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=nose]').is(":checked")) {
                    $.messager.alert('提示', '请选择鼻是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=oral_cavity]').is(":checked")) {
                    $.messager.alert('提示', '请选择口腔是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=heart_lung_auscultation]').is(":checked")) {
                    $.messager.alert('提示', '请选择心肺听诊是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=abdomen_palpation]').is(":checked")) {
                    $.messager.alert('提示', '请选择腹部触诊是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=all_fours_activity]').is(":checked")) {
                    $.messager.alert('提示', '请选择四肢活动度是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=neck_enclosed_mass]').is(":checked")) {
                    $.messager.alert('提示', '请选择颈部包块是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=skin]').is(":checked")) {
                    $.messager.alert('提示', '请选择皮肤是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=anus]').is(":checked")) {
                    $.messager.alert('提示', '请选择肛门是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=externalia]').is(":checked")) {
                    $.messager.alert('提示', '请选择外生殖器是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=spine]').is(":checked")) {
                    $.messager.alert('提示', '请选择脊柱是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=navel]').is(":checked")) {
                    $.messager.alert('提示', '请选择脐部状态', 'info');
                    return false;
                }
                if (!form.find('input[name=transfer_treatment_suggestion]').is(":checked")) {
                    $.messager.alert('提示', '请选择转诊建议', 'info');
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
                    table.panel('refresh');
                    $.messager.show({title: '提示', msg: '新生儿家庭访视记录表保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '新生儿家庭访视记录表保存失败', 'info');
                }
            }
        });
    });
    table.panel({ href: '/child/newborn_visit_table/', method: 'POST' })

});