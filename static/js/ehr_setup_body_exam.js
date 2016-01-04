$(function () {
    $.extend($.fn.validatebox.defaults.rules, {
        posNeg:{//判断阴阳性
            validator: function(value, param){
                return value == '-' | value == '+' | value == '++' | value == '+++' | value == '++++';
            },
            message:  '请输入正确的阴阳性'
        }
    });

    var form = $('#body_exam_form');
    var table = $('#body_exam_table');
    var tabs = form.parents('#ehr_setup_tabs');
    var resident_id = tabs.find('#ehr_resident_list').datagrid('getSelected')['id'];

    var save_btn = $('#body_exam_save').linkbutton({ iconCls: 'icon-save', plain: true});
    var print_btn = $('#body_exam_print').linkbutton({ iconCls: 'icon-print', plain: true});
    print_btn.linkbutton('disable');
    save_btn.bind('click', function () {
        if($(this).linkbutton('options').disabled == false){
            form.form('submit', {
                url: '/ehr/body_exam_submit/', method: 'POST',
                onSubmit: function (param) {
                    if (form.find('input[name=mouth_lip]').length && !form.find('input[name=mouth_lip]').is(":checked")) {
                            $.messager.alert('提示', '请选择脏器功能—口腔—口唇', 'info');
                            return false;
                        }
                        if (form.find('input[name=mouth_tooth]').length && !form.find('input[name=mouth_tooth]').is(":checked")) {
                            $.messager.alert('提示', '请选择脏器功能—口腔—齿列', 'info');
                            return false;
                        }
                        if (form.find('input[name=mouth_throat]').length && !form.find('input[name=mouth_throat]').is(":checked")) {
                            $.messager.alert('提示', '请选择脏器功能—口腔—咽部', 'info');
                            return false;
                        }
                        if (form.find('input[name=hearing]').length && !form.find('input[name=hearing]').is(":checked")) {
                            $.messager.alert('提示', '请选择脏器功能—听力', 'info');
                            return false;
                        }
                        if (form.find('input[name=movement_function]').length && !form.find('input[name=movement_function]').is(":checked")) {
                            $.messager.alert('提示', '请选择脏器功能—运动功能', 'info');
                            return false;
                        }
                        if (form.find('input[name=skin]').length && !form.find('input[name=skin]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—皮肤', 'info');
                            return false;
                        }
                        if (form.find('input[name=lymph_node]').length && !form.find('input[name=lymph_node]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—淋巴结', 'info');
                            return false;
                        }
                        if (form.find('input[name=lung_barrel_chested]').length && !form.find('input[name=lung_barrel_chested]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—肺—桶状胸', 'info');
                            return false;
                        }
                        if (form.find('input[name=lung_breath_sound]').length && !form.find('input[name=lung_breath_sound]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—肺—呼吸音', 'info');
                            return false;
                        }
                        if (form.find('input[name=lung_rale]').length && !form.find('input[name=lung_rale]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—肺—罗音', 'info');
                            return false;
                        }
                        if (form.find('input[name=heart_rhythm]').length && !form.find('input[name=heart_rhythm]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—心脏—心律', 'info');
                            return false;
                        }
                        if (form.find('input[name=heart_noise]').length && !form.find('input[name=heart_noise]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—心脏—杂音', 'info');
                            return false;
                        }
                        if (form.find('input[name=stomach_tenderness]').length && !form.find('input[name=stomach_tenderness]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—腹部—压痛', 'info');
                            return false;
                        }
                        if (form.find('input[name=stomach_enclosed_mass]').length && !form.find('input[name=stomach_enclosed_mass]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—腹部—包块', 'info');
                            return false;
                        }
                        if (form.find('input[name=stomach_hepatomegaly]').length && !form.find('input[name=stomach_hepatomegaly]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—腹部—肝大', 'info');
                            return false;
                        }
                        if (form.find('input[name=stomach_slenauxe]').length && !form.find('input[name=stomach_slenauxe]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—腹部—脾大', 'info');
                            return false;
                        }
                        if (form.find('input[name=stomach_shifting_dullness]').length && !form.find('input[name=stomach_shifting_dullness]').is(":checked")) {
                            $.messager.alert('提示', '请选择查体—腹部—移动性浊音', 'info');
                            return false;
                        }

                        if(form.form('validate')){
                            param.csrfmiddlewaretoken = $.cookie('csrftoken');
                            param.resident_id = resident_id;
                            return true;
                        }
                        else{
                            return false;
                        }
                },
                success: function (data) {
                    var data = eval('(' + data + ')');
                    if (data.success) {
                        $.messager.show({title: '提示', msg: '健康体检表保存完成', timeout: 2000});
                        table.panel({
                            href: '/ehr/body_exam_table/', method: 'POST',
                            queryParams: {resident_id: resident_id}
                        });
                        print_btn.linkbutton('enable');
                        save_btn.linkbutton('disable');
                        tabs.find('#ehr_resident_list').datagrid('reload');
                    } else {
                        $.messager.alert('提示', '健康体检表保存失败', 'warning');
                    }
                }
            })
        }
    });

    print_btn.bind('click', function(){
        if($(this).linkbutton('options').disabled == false){
            table.find('.print_area').printThis();
        }
    });

    table.panel({href: '/ehr/body_exam_setup/', method: 'POST',
        queryParams: {resident_id: resident_id}
    });
});
