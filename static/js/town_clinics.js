$(function () {

    var selected_row = undefined;
    var datagrid = $('#town_clinics');

    datagrid.datagrid({
        title: '乡镇卫生院信息列表',
        url: '/management/town_clinic_list_new/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'name', title: '卫生院名称', width: 10 },
            { field: 'address', title: '地址', width: 20 },
            { field: 'village_clinic_num', title: '村卫生室数量', width: 5 },
            { field: 'doctor_user_num', title: '医生用户数量', width: 5 },
            { field: 'town_name', title: '所在乡镇', width: 10 }
        ]],
        onClickRow: function (index, row) {
            if (selected_row == row) {
                datagrid.datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = datagrid.datagrid('getSelected');
            }
        },
        onDblClickRow: function(index, row) {
            alert('clinic on the row');
        }
    });
});