$(function () {
    var datagrid = $('#doc_stat_table');

    datagrid.datagrid({
        title: '工作量统计', url: '/services/get_doc_stat/',
        rownumbers: false, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'service', title: '公卫服务类别', width: 10 },
            { field: 'count', title: '工作量', width: 10 }
        ]]
    });

});