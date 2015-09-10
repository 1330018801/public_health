$(function() {
    var select = $('#service_item_select');
    select.multiSelect({
        keepOrder: true,
        selectableOptgroup: true,
        selectableHeader: '<div align="center" style="font-size: 14px;">未授权的服务项目</div>',
        selectionHeader: '<div align="center" style="font-size: 14px;">授权的服务项目</div>',
        afterInit: function () {
        }
    });

    //初始化角色授权对话框
    $('#role_authorize').dialog({
        title: '设置角色权限', width: 600, height: 400, closed: true, cache: false, modal: true,
        buttons: [
            { text: '确定', iconCls: 'icon-ok', handler: function() {
                $('#role_authorize_form').form('submit', {
                    url: '/management/role_authorize/',
                    onSubmit: function(param) {
                        param.role_id = selected_role.id;
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    },
                    success: function() { $.messager.show({ title: '提示', msg: '角色权限更新成功！' }); }
                });
                $('#role_authorize').dialog('close');
            }},
            { text: '取消', iconCls: 'icon-cancel', handler: function() { $('#role_authorize').dialog('close'); } }
        ],
        onOpen: function() {
            $(this).css('display', 'block');
            $(this).dialog('center');
        },
        onClose: function() {
            select.multiSelect('deselect_all');
            $(this).css('display', 'none');
        }
    });

    //关联按钮和角色授权对话框
    var btn_authorize = $('#roles_toolbar').find('#btn_authorize');
    var selected_role = undefined;

    btn_authorize.bind('click', function() {
        if (selected_role) {
            $.ajax({
                url: '/management/service_item_options/', method: 'POST',
                data: { 'service_type_name': 'true' },
                success: function (data) {
                    $.each(data, function(index, item) {
                        if (item.id) {
                            select.multiSelect('addOption',
                                {value: item.id, text: item.name, index: 0, nested: item.service_type_name});
                        }
                    });
                    $.ajax({
                        url: '/management/get_role_authorize/',
                        method: 'POST',
                        data: { 'role_id': selected_role.id },
                        success: function(data) {
                            select.multiSelect('select', data);
                        }
                    });
                    $('#role_authorize').dialog('open');
                }
            })
        }
    });

    $('#roles').datagrid({
        title: '系统用户角色列表', url: '/management/role_list_new/',
        toolbar: '#roles_toolbar', rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true},
            { field: 'name', title: '角色名称', width: 10 },
            { field: 'is_staff', title: '类别', width: 10, formatter: function(value){
                if (value) { return '管理员'; } else { return '服务提供者'; }
            }},
            { field: 'user_num', title: '用户数量', width: 10 }
        ]],
        onClickRow: function (index, row) {
            if (selected_role != undefined && selected_role == row) {
                    $(this).datagrid('unselectRow', index);
                    selected_role = undefined;
                    btn_authorize.linkbutton('disable');
            } else {
                    selected_role = $(this).datagrid('getSelected');
                    btn_authorize.linkbutton('enable');
            }
        }
    });
});