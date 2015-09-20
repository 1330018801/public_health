$(function () {
    var panel = $('#login_panel');
    var form = $('#login_form');
    var footer = $('#login_panel_footer');
    var btn_login = footer.find('#btn_login');

    btn_login.linkbutton({ iconCls: 'icon-ok' });
    form.find('#username').textbox({ required: true, width: 150 });
    form.find('#password').textbox({ required: true, width: 150, validType: 'password' });

    /*
    btn_login.bind('click', function () {
        form.form('submit', {
            url: '/login_verify/',
            onSubmit: function(param) {
                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                return form.form('validate');
            },
            success: function(data) {
                var data_obj = eval('(' + data + ')');
                if (!data_obj.success) {
                    $('#message').html(data_obj.message);
                }
            }
        });
    });
    */

    panel.panel({
        title: '用户登录', width: 400, height: 200,
        footer: '#login_panel_footer'
    });
});