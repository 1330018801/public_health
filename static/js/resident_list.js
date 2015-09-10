$(function() {

    $('#resident_add_form').form({
        url: '/management/resident_add_test/',
        onSubmit: function(param) {
            return $(this).form('validate');
        },
        success: function(data) {
            //将返回的json类型转化为JS对象
            var data = eval('(' + data + ')');

            if (data.success) {
                $.messager.show({
                    title: '提示',
                    msg: '新居民【' + data.name + '】添加成功！',
                    showType: null,
                    timeout: 1500,
                    style: {
                        top: 100
                    }
                });
                $('#resident_add').dialog('close');
            }
        }
    });

    $('#town').combobox({
        url: '/management/get_towns/',
        valueField: 'id',
        textField: 'name',
        onLoadSuccess: function() {
            $(this).combobox('setValue', '0');
        },
        onSelect: function(rec) {
            var url = '/management/get_town_villages/' + rec.id + '/';
            $('#village').combobox('reload', url);
            $('#village').combobox('setValue', '0');
        }
    });

    $('#village').combobox({
        valueField: 'id',
        textField: 'name'
    });

    $('#resident_query_form').form({
        url: '/management/resident_query_test/',
        onSubmit: function(param) {},
        success: function(data) {
        }
    });

    $('#resident_list').datagrid({
        title: '居民列表',
        url: '/management/resident_query_list/',
        width: 850,
        rownumbers: true,
        singleSelect: true,
        toolbar: '#tb',
        fitColumns: true,
        columns: [[
            {
                field: 'name',
                title: '姓名',
                width: 10,
                editor: {
                    type: 'text',
                    options: {
                        required: true
                    }
                }
            },
            { field: 'gender', title: '性别' },
            { field: 'age', title: '年龄' },
            {
                field: 'birthday',
                title: '出生日期',
                editor: {
                    type: 'datebox',
                    options: {
                        required: true
                    }
                }
            },
            { field: 'identity', title: '身份证号码' },
            { field: 'town', title: '乡镇' },
            { field: 'village', title: '村/街道' },
            { field: 'address', title: '地址' },
            { field: 'mobile', title: '电话' }
        ]],
        pagination: true,
        onAfterEdit: function(rowIndex, rowData, chagnes) {
            $('#save, #undo').hide();
            obj.editRow = false;
            console.log(rowData);
        }
    });

    obj = {
        editRow : false,
        search: function() {
            $('#resident_list').datagrid('load', {
                query_town: $('input[name="query_town"]').val(),
                query_village: $('input[name="query_village"]').val(),
                query_name: $('input[name="query_name"]').val(),
                query_identity: $('input[name="query_identity"]').val()
            });
        },
        add: function() {
            if (!this.editRow) {
                $('#save, #undo').show();
                $('#resident_list').datagrid('insertRow', {
                    index: 0,
                    row: {

                    }
                });
                $('#resident_list').datagrid('beginEdit', 0);
                this.editRow = true;
            }
        },
        save: function() {
            $('#resident_list').datagrid('endEdit', 0);
        },
        undo: function() {
            $('#save, #undo').hide();
            this.editRow = false;
            $('#resident_list').datagrid('rejectChanges');
        }
    };

    $('#query_town').combobox({
        url: '/management/get_towns/',
        valueField: 'id',
        textField: 'name',
        editable: false,
        onLoadSuccess: function () {
            $(this).combobox('setValue', '0');
        },
        onSelect: function (rec) {
            var url = '/management/get_town_villages/' + rec.id + '/';
            $('#query_village').combobox('reload', url);
            $('#query_village').combobox('setValue', '0');
        }
    });

    $('#query_village').combobox({
        valueField: 'id',
        textField: 'name',
        editable: false
    });

    $('#resident_query_btn').click(function () {
        $('#resident_query_form').submit();
    });

    //创建新增居民的对话框
    $('#resident_add').dialog({
        title: '添加居民',
        closed: true,
        width: 600,
        height: 260,
        cache: false,
        modal: true,
        buttons: [
            {
                text: '提交',
                iconCls: 'icon-ok',
                handler: function() {
                    $('#resident_add_form').submit();
                }
            },
            {
                text: '取消',
                iconCls: 'icon-cancel',
                handler: function() {
                    $('#resident_add').dialog('close');
                }
            }
        ],
        onClose: function() {
            $('#resident_add_form').form('clear');
        }
    });

    //打开新增居民的对话框
    $('#resident_add_btn').click(function() {
        $('#resident_add').dialog('open');
    });

    //新增居民对话框中的乡镇和村庄选择框
    //通过ajax动态得到复选框的选项内容
    $('#town1').combobox({
        url: '/management/get_towns/',
        valueField: 'id',
        textField: 'name',
        onLoadSuccess: function() {
            $(this).combobox('setValue', '0');
        },
        onSelect: function(rec) {
            var url = '/management/get_town_villages/' + rec.id + '/';
            $('#village1').combobox('reload', url);
            $('#village1').combobox('setValue', '0');
        }
    });

    $('#village1').combobox({
        valueField: 'id',
        textField: 'name'
    });

    //删除居民的提示
    $('.resident_del').click(function() {
        var resident_id = $(this).attr('resident_id');
        console.log(resident_id);
        $.messager.confirm('删除确认', '确定要删除该居民吗？', function(flag) {
            if (flag) {
                $.ajax({
                    url: '/management/resident_del_test/',
                    method: 'POST',
                    data: {
                        resident_id: resident_id
                    },
                    success: function(data, status, xhr) {
                        //更新居民列表
                    }
                });
            }
        });
    });

});