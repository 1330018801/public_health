$(function () {
    $('#psychiatric_aftercare').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var resident_id = $('#resident_id').val();
    var item_alias = undefined;

    var btn_add = [9];
    for (var i = 1; i < 9; i++) {
        btn_add[i] = toolbar.find('#add_'+i).linkbutton({ iconCls: 'icon-add', plain: true });
    }

    btn_add[1].bind('click', function () {
        panel.panel({ href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_1' }
        });
        item_alias = 'aftercare_1';
    });

    btn_add[2].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_2' }
        });
        item_alias = 'aftercare_2';
    });

    btn_add[3].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_3' }
        });
        item_alias = 'aftercare_3';
    });

    btn_add[4].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_4' }
        });
        item_alias = 'aftercare_4';
    });

    btn_add[5].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_5' }
        });
        item_alias = 'aftercare_5';
    });

    btn_add[6].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_6' }
        });
        item_alias = 'aftercare_6';
    });

    btn_add[7].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_7' }
        });
        item_alias = 'aftercare_7';
    });

    btn_add[8].bind('click', function () {
        panel.panel({
            href: '/psychiatric/aftercare_form/', method: 'POST',
            queryParams: { item_alias: 'aftercare_8' }
        });
        item_alias = 'aftercare_8';
    });

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
             url: '/psychiatric/aftercare_submit/',
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
                 panel.panel({
                     href: '/psychiatric/aftercare_form/', method: 'POST',
                     queryParams: {item_alias: item_alias}
                 })
             }
        });
    });

    btn_undo.bind('click', function () {});
    btn_print.bind('click', function () {});

    // panel.panel({ href: '/psychiatric/aftercare_review/' });
    /*
    $.ajax({
        url: '/services/pregnant/aftercare_finished/',
        success: function (data) {
            finished = data.finished;
            $.each(finished, function (index, item) {

            });
        }
    });
    */
});