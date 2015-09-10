$(function () {
    var selected_row = undefined;
    var datagrid = $('#service_types');
    datagrid.datagrid({
        title: '基本公共卫生服务类别',
        url: '/management/service_type_list_new/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'name', title: '服务类别名称', width: 20 },
            { field: 'should_weight', title: '应该权重', width: 10 },
            { field: 'real_weight', title: '实际权重', width: 10 },
            { field: 'item_num', title: '服务项目数量', width: 10 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = $(this).datagrid('getSelected');
            }
        },
        onDblClickRow: function(index, row) {
            //
        }
    });
});