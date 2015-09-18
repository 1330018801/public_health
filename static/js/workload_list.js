$(function () {

    var panel = $('.workload_list').last();
    var provider_id = panel.find('input[name=provider_id]').last().val();
    var datagrid = $('.workload_list_datagrid').last();

    datagrid.datagrid({
        url: '/management/workload_list_datagrid/' + provider_id + '/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '记录编号', hidden: true },
            { field: 'resident_id', title: '居民编号', hidden: true },
            { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                if (value == null) {
                    return '未建档';
                }
                if (value == '13108200000000000') {
                    return '未编号';
                }
                return value;
            } },
            { field: 'resident_name', title: '居民', width: 4 },
            { field: 'doctor_name', title: '医生', width: 4 },
            { field: 'service_type', title: '服务类别', width: 10 },
            { field: 'service_item', title: '服务项目', width: 10 },
            { field: 'submit_time', title: '服务时间', width: 8 }
        ]],
        onClickRow: function (index, row) {
            /*
            if (selected_row == row) {
                $(this).datagrid('unselectRow', index);
                selected_row = undefined;
            } else {
                selected_row = $(this).datagrid('getSelected');
            }
            */
        },
        onDblClickRow: function(index, row) {
            /*
            var tabs = datagrid.parents('#workload_stat_tabs');
            console.log(row['id']);
            console.log(row['clinic']);
            tabs.tabs('add', {
                title: row['clinic'] + '工作量', closable: true,
                href: '/management/workload_list_page/' + row['id'] + '/'
            });
            */
        },
        onDblClickCell: function (index, field, value) {
            if (field == 'resident_name') {
                var rows = datagrid.datagrid('getRows');
                var resident_id = rows[index]['resident_id'];
                var tabs = datagrid.parents('#workload_stat_tabs');
                console.log(rows[index]['name']);
                tabs.tabs('add', {
                    title: rows[index]['resident_name'] + '的服务记录', closable: true,
                    href: '/management/resident_records_page/' + resident_id + '/'
                });
            }
        }
    });
});