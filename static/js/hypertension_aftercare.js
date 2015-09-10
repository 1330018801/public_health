$(function () {
    $('#hypertension_aftercare').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var resident_id = $('#resident_id').val();
    var aftercare = undefined;
    // var finished = undefined;

    var btn_add_1 = toolbar.find('#add_1').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_2 = toolbar.find('#add_2').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_3 = toolbar.find('#add_3').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_4 = toolbar.find('#add_4').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_edit.linkbutton('disable');

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_add_1.bind('click', function () {
        panel.panel({
            href: '/hypertension/aftercare_form/', method: 'POST',
            queryParams: { aftercare: 1 }
        });
        aftercare = 'aftercare_1';
    });

    btn_add_2.bind('click', function () {
        panel.panel({
            href: '/hypertension/aftercare_form/', method: 'POST',
            queryParams: { aftercare: 2 }
        });
        aftercare = 'aftercare_2';
    });


    btn_add_3.bind('click', function () {
        panel.panel({
            href: '/hypertension/aftercare_form/', method: 'POST',
            queryParams: { aftercare: 3 }
        });
        aftercare = 'aftercare_3';
    });

    btn_add_4.bind('click', function () {
        panel.panel({
            href: '/hypertension/aftercare_form/', method: 'POST',
            queryParams: { aftercare: 4 }
        });
        aftercare = 'aftercare_4';
    });

    btn_save.bind('click', function () {
        form.form('submit', {
             url: '/hypertension/aftercare_submit/',
             onSubmit: function (param) {
                 param.csrfmiddlewaretoken = $.cookie('csrftoken');
                 param.aftercare = aftercare;
             },
             success: function (data) {
                 var data_obj = eval('(' + data + ')');
                 if (data_obj.success) {
                     $.messager.show({title: '提示', msg: '随访记录保存成功', timeout: 1000});
                 } else {
                     $.messager.alert('提示', '随访记录保存失败', 'warning');
                 }
                 panel.panel({ href: '/hypertension/aftercare_review/' })
             }
        });
    });

    btn_edit.bind('click', function () {});
    btn_undo.bind('click', function () {
        panel.panel({ href: '/hypertension/aftercare_review/' });
        btn_add_2.linkbutton('enable');
        btn_add_3.linkbutton('enable');
        btn_add_4.linkbutton('enable');
    });
    btn_print.bind('click', function () {});

    panel.panel({ href: '/hypertension/aftercare_review/' });
});