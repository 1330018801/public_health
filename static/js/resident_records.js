$(function () {

    var panel = $('.resident_records').last();
    var resident_id = panel.find('input[name=resident_id]').last().val();
    var datagrid = $('.resident_records_datagrid').last();

    var begin_date = panel.find('input[name=begin_date]').last().val();
    var end_date = panel.find('input[name=end_date]').last().val();

    datagrid.datagrid({
        //url: '/management/resident_records_datagrid/' + resident_id + '/',
        url: '/management/resident_records_datagrid/',
        queryParams: {
            resident_id: resident_id,
            begin_date: begin_date,
            end_date: end_date
        },
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '记录编号', hidden: true },
            { field: 'ehr_no', title: '健康档案编号', width: 10, formatter: function(value) {
                if (value == null) { return '未建档'; }
                if (value == '13108200000000000') { return '未编号'; }
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
            if(row['service_type'] != '健康档案建档'){
                var detail = $('#resident_record_detail_review').dialog({
                                title: '服务详情', width: 820, height: 500, method: 'POST', modal: true,
                                href: '/ehr/record_detail_review/', queryParams: {record_id: row['id']},
                                buttons: [{
                                    text: '打印', iconCls: 'icon-print',
                                    handler: function () {
                                        detail.find('.print_area').printThis();
                                    }
                                },{
                                    text: '关闭', iconCls: 'icon-cancel',
                                    handler: function () {
                                        detail.dialog('close');
                                    }
                                }]
                            });
                            detail.css('display', 'block');
                            detail.dialog('center');
            }
        },
        onDblClickCell: function (index, field, value) {
            /*
            var rows = datagrid.datagrid('getRows');
            var resident_id = rows[index]['resident_id'];
            var tabs = datagrid.parents('#workload_stat_tabs');
            console.log(rows[index]['name']);
            tabs.tabs('add', {
                title: rows[index]['resident_name'] + '的服务记录', closable: true,
                href: '/management/resident_records_page/' + resident_id + '/'
            });
            */
        }
    });
});