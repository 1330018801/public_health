$(function () {
    var datagrid = $('#doc_info_table');
    var btn_new_password = $('#new_password');
    var dialog = $('#new_password_dialog');
    var form = $('#new_password_form');
    var table = $('#new_password_table');

    table.find('#passwd1').textbox({ type: 'password', required: true, width: 120 });
    table.find('#pswd_again').textbox({
        type: 'password', required: true, validType: 'equals["#passwd1"]', width: 120
    });


    btn_new_password.linkbutton({ iconCls: 'icon-add', plain: true });

    btn_new_password.bind('click', function () {
        dialog.dialog({
            title: '修改用户登录密码', width: 400, height: 200,
            buttons: [
                {
                    text: '提交', iconCls: 'icon-ok',
                    handler: function() {
                        form.form('submit', {
                            url: '/services/update_password/',
                            onSubmit: function(param) {
                                param.csrfmiddlewaretoken = $.cookie('csrftoken');
                                return form.form('validate');
                            },
                            success: function(data) {
                                var data_obj = eval('(' + data + ')');
                                if (data_obj.success) {
                                    $.messager.show({ title: '提示', msg: '密码修改成功', timeout: 1500 });
                                    window.location.href="/";  //返回到主页重新登录
                                } else {
                                    $.messager.alert('提示', '密码修改失败', 'warning');
                                }
                                form.form('clear');
                                dialog.dialog('close');
                            }
                        });
                    }
                },
                {
                    text: '取消', iconCls: 'icon-cancel',
                    handler: function() {
                        form.form('clear');
                        dialog.dialog('close');
                    }
                }
            ]
        });
        table.css('display', 'block');
    });
    datagrid.datagrid({
        title: '医生个人信息', url: '/services/get_doc_info/',
        toolbar: '#doc_info_toolbar',
        rownumbers: false, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'username', title: '用户名', width: 10 },
            //{ field: 'password', title: '登陆密码', width: 10 },
            { field: 'role', title: '用户角色', width: 10 },
            { field: 'town_clinic', title: '所属卫生院', width: 20 },
            { field: 'village_clinic', title: '所属卫生室', width: 20 },
            { field: 'department', title: '科室', width: 10 },
            { field: 'position', title: '岗位', width: 10 }
        ]]
    });

    $.extend($.fn.validatebox.defaults.rules, {
        equals: {
            validator: function(value, param){
                //console.log('value:' + value);
                //console.log('param:' + $(param[0]).val());
                //return value == $(param[0]).val();
                return value == table.find('#passwd1').val();
            },
            message: '两次密码输入不匹配'
        }
    });

});