$(function () {

    $.extend($.fn.validatebox.defaults.rules, {
        posNeg : {//判断阴阳性
            validator : function(value, param){
                return value == '-' | value == '+' | value == '++' | value == '+++' | value == '++++';
            },
            message : '请输入正确的阴阳极性。'
        }
    });
    var area = $('#pregnant_aftercare_1');
    var toolbar = area.find('#toolbar');
    var form = area.find('#form');
    var table = area.find('#table');

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_edit.linkbutton('disable');

    btn_print.bind('click', function () { table.find('.print_area').printThis(); });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/pregnant/aftercare_1_submit/', method: 'POST',
            onSubmit: function (param) {
                if(!form.find('input[name=disease_history]').is(":checked")){
                    $.messager.alert('提示', '请选择既往史', 'info');
                    return false;
                }
                if (!form.find('input[name=family_history]').is(":checked")) {
                    $.messager.alert('提示', '请选择家族史', 'info');
                    return false;
                }
                if(!form.find('input[name=personal_history]').is(":checked")){
                    $.messager.alert('提示', '请选择个人史', 'info');
                    return false;
                }
                if(!form.find('input[name=gynaecology_surgery_history]').is(":checked")){
                    $.messager.alert('提示', '请选择有无妇科手术史', 'info');
                    return false;
                }
                if(!form.find('input[name=ausculate_heart]').is(":checked")){
                    $.messager.alert('提示', '请选择听诊—心脏是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=ausculate_lung]').is(":checked")){
                    $.messager.alert('提示', '请选择听诊—肺部是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=vulva]').is(":checked")){
                    $.messager.alert('提示', '请选择妇科检查—外阴是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=vagina]').is(":checked")){
                    $.messager.alert('提示', '请选择妇科检查—阴道是否异常', 'info');
                    return false;
                }
                if (!form.find('input[name=cervix]').is(":checked")) {
                    $.messager.alert('提示', '请选择妇科检查—宫颈是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=uteri]').is(":checked")){
                    $.messager.alert('提示', '请选择妇科检查—子宫是否异常史', 'info');
                    return false;
                }
                if(!form.find('input[name=accessory]').is(":checked")){
                    $.messager.alert('提示', '请选择妇科检查—附件是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=total_evaluation]').is(":checked")){
                    $.messager.alert('提示', '请选择总体评估是否异常', 'info');
                    return false;
                }
                if(!form.find('input[name=guide]').is(":checked")){
                    $.messager.alert('提示', '请选择保健指导', 'info');
                    return false;
                }
                if(!form.find('input[name=transfer]').is(":checked")){
                    $.messager.alert('提示', '请选择是否转诊', 'info');
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