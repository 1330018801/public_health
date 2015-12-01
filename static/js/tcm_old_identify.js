$(document).ready(function () {

    /*alert($("input[name='yes_trend_qixu']").get(0).disabled);*/
    //alert($('#id_yes_trend_qixu_0').html());
    //$('input[name=yes_trend_qixu]').eq(1).attr("checked", true);
    /*yes_trend_qixu[0].disabled=true;
    yes_trend_yangxu.disabled=true;
    yes_trend_yinxu.disabled=true;
    yes_trend_tanshi.disabled=true;
    yes_trend_shire.disabled=true;
    yes_trend_xueyu.disabled=true;
    yes_trend_qiyu.disabled=true;
    yes_trend_tebing.disabled=true;
    yes_trend_pinghe.disabled=true;*/

    var toolbar = $('#toolbar');
    var panel = $('#table');
    var form = $('#form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });

    btn_save.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            form.form('submit', {
                url: '/tcm/old_identify_submit/', method: 'POST',
                onSubmit: function (param) {
                    if (!form.find('input[name=q1]').is(":checked")) {
                        $.messager.alert('提示', '请选择第1题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q2]').is(":checked")) {
                        $.messager.alert('提示', '请选择第2题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q3]').is(":checked")) {
                        $.messager.alert('提示', '请选择第3题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q4]').is(":checked")) {
                        $.messager.alert('提示', '请选择第4题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q5]').is(":checked")) {
                        $.messager.alert('提示', '请选择第5题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q6]').is(":checked")) {
                        $.messager.alert('提示', '请选择第6题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q7]').is(":checked")) {
                        $.messager.alert('提示', '请选择第7题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q8]').is(":checked")) {
                        $.messager.alert('提示', '请选择第8题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q9]').is(":checked")) {
                        $.messager.alert('提示', '请选择第9题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q10]').is(":checked")) {
                        $.messager.alert('提示', '请选择第10题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q11]').is(":checked")) {
                        $.messager.alert('提示', '请选择第11题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q12]').is(":checked")) {
                        $.messager.alert('提示', '请选择第12题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q13]').is(":checked")) {
                        $.messager.alert('提示', '请选择第13题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q14]').is(":checked")) {
                        $.messager.alert('提示', '请选择第14题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q15]').is(":checked")) {
                        $.messager.alert('提示', '请选择第15题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q16]').is(":checked")) {
                        $.messager.alert('提示', '请选择第16题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q17]').is(":checked")) {
                        $.messager.alert('提示', '请选择第17题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q18]').is(":checked")) {
                        $.messager.alert('提示', '请选择第18题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q19]').is(":checked")) {
                        $.messager.alert('提示', '请选择第19题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q20]').is(":checked")) {
                        $.messager.alert('提示', '请选择第20题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q21]').is(":checked")) {
                        $.messager.alert('提示', '请选择第21题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q22]').is(":checked")) {
                        $.messager.alert('提示', '请选择第22题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q23]').is(":checked")) {
                        $.messager.alert('提示', '请选择第23题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q24]').is(":checked")) {
                        $.messager.alert('提示', '请选择第24题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q25]').is(":checked")) {
                        $.messager.alert('提示', '请选择第25题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q26]').is(":checked")) {
                        $.messager.alert('提示', '请选择第26题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q27]').is(":checked")) {
                        $.messager.alert('提示', '请选择第27题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q28]').is(":checked")) {
                        $.messager.alert('提示', '请选择第28题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q29]').is(":checked")) {
                        $.messager.alert('提示', '请选择第29题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q30]').is(":checked")) {
                        $.messager.alert('提示', '请选择第30题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q31]').is(":checked")) {
                        $.messager.alert('提示', '请选择第31题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q32]').is(":checked")) {
                        $.messager.alert('提示', '请选择第32题', 'info');
                        return false;
                    }
                    if (!form.find('input[name=q33]').is(":checked")) {
                        $.messager.alert('提示', '请选择第33题', 'info');
                        return false;
                    }

                    if (form.find('input[name=yes_trend_qixu]').is(":checked") && !form.find('input[name=health_care_guide_qixu]').is(":checked")) {
                        $.messager.alert('提示', '请选择气虚质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_yangxu]').is(":checked") && !form.find('input[name=health_care_guide_yangxu]').is(":checked")) {
                        $.messager.alert('提示', '请选择阳虚质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_yinxu]').is(":checked") && !form.find('input[name=health_care_guide_yinxu]').is(":checked")) {
                        $.messager.alert('提示', '请选择阴虚质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_tanshi]').is(":checked") && !form.find('input[name=health_care_guide_tanshi]').is(":checked")) {
                        $.messager.alert('提示', '请选择痰湿质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_shire]').is(":checked") && !form.find('input[name=health_care_guide_shire]').is(":checked")) {
                        $.messager.alert('提示', '请选择湿热质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_xueyu]').is(":checked") && !form.find('input[name=health_care_guide_xueyu]').is(":checked")) {
                        $.messager.alert('提示', '请选择血瘀质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_qiyu]').is(":checked") && !form.find('input[name=health_care_guide_qiyu]').is(":checked")) {
                        $.messager.alert('提示', '请选择气郁质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_tebing]').is(":checked") && !form.find('input[name=health_care_guide_tebing]').is(":checked")) {
                        $.messager.alert('提示', '请选择特禀质的中医药保健指导', 'info');
                        return false;
                    }
                    if (form.find('input[name=yes_trend_pinghe]').is(":checked") && !form.find('input[name=health_care_guide_pinghe]').is(":checked")) {
                        $.messager.alert('提示', '请选择平和质的中医药保健指导', 'info');
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
                    //alert(json_data);
                    var data = eval('(' + json_data + ')');
                    if (data.success) {
                        panel.panel('refresh', '/tcm/old_identify_form/');
                        $.messager.show({title: '提示', msg: '老年人中医药健康管理服务记录表保存成功', timeout: 2000});
                    } else {
                        $.messager.alert('提示', '老年人中医药健康管理服务记录表保存失败', 'info');
                    }
                }
            });
        }
    });

    panel.panel({ href: '/tcm/old_identify_form/', method: 'POST' });
});
