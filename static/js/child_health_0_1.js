$(function () {
    $('#child_health_0_1').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var resident_id = $('#resident_id').val();
    var item_alias = undefined;

    var btn_add_1 = toolbar.find('#add_1').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_2 = toolbar.find('#add_2').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_3 = toolbar.find('#add_3').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_4 = toolbar.find('#add_4').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });
    btn_save.linkbutton('disable');
    btn_undo.linkbutton('disable');


    btn_add_1.bind('click', function () {
        panel.panel({
            href: '/child/health_0_1_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_1_month' }
        });
        item_alias =  'aftercare_1_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_add_2.bind('click', function () {
        panel.panel({
            href: '/child/health_0_1_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_3_month' }
        });
        item_alias =  'aftercare_3_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });


    btn_add_3.bind('click', function () {
        panel.panel({
            href: '/child/health_0_1_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_6_month' }
        });
        item_alias =  'aftercare_6_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_add_4.bind('click', function () {
        panel.panel({
            href: '/child/health_0_1_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_8_month' }
        });
        item_alias =  'aftercare_8_month';
        btn_save.linkbutton('enable');
        btn_undo.linkbutton('enable');
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/child/health_0_1_submit/',
            onSubmit: function (param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                param.item_alias = item_alias;
            },
            success: function (data) {
                var data_obj = eval('(' + data + ')');
                if (data_obj.success) {
                    $.messager.show({title: '提示', msg: '随访记录保存成功', timeout: 1000});
                } else {
                    $.messager.alert('提示', '随访记录保存失败', 'warning');
                }
                panel.panel({ href: '/child/health_0_1_review/' });
                btn_save.linkbutton('disable');
                btn_undo.linkbutton('disable');
            }
        });
    });

    btn_undo.bind('click', function () {
        panel.panel({ href: '/child/health_0_1_review/' });
        btn_add_1.linkbutton('enable');
        btn_add_2.linkbutton('enable');
        btn_add_3.linkbutton('enable');
        btn_add_4.linkbutton('enable');
    });

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    panel.panel({ href: '/child/health_0_1_review/' });

});