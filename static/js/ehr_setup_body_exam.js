$(function () {
    var form = $('#body_exam_form');
    var table = $('#body_exam_table');
    var tabs = form.parents('#ehr_setup_tabs');
    var resident_id = tabs.find('#ehr_resident_list').datagrid('getSelected')['id'];

    var save_btn = $('#body_exam_save').linkbutton({ iconCls: 'icon-save', plain: true});
    var print_btn = $('#body_exam_print').linkbutton({ iconCls: 'icon-print', plain: true});
    print_btn.linkbutton('disable');
    save_btn.bind('click', function () {
        form.form('submit', {
            url: '/ehr/body_exam_submit/', method: 'POST',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                param.resident_id = resident_id;
            },
            success: function (data) {
                var data = eval('(' + data + ')');
                if (data.success) {
                    $.messager.show({title: '提示', msg: '健康体检表保存完成', timeout: 1000});
                    table.panel({
                        href: '/ehr/body_exam_table/', method: 'POST',
                        queryParams: {resident_id: resident_id}
                    });
                    tabs.find('#ehr_resident_list').datagrid('reload');
                } else {
                    $.messager.alert('提示', '健康体检表保存失败', 'warning');
                }
            }
        })
    });

    table.panel({href: '/ehr/body_exam_setup/', method: 'POST',
        queryParams: {resident_id: resident_id}
    });
});