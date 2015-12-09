$(function () {

    var panel = $('.workload_village_clinics').last();
    var datagrid = $('.workload_village_clinics_datagrid').last();

    var town_clinic_id = panel.find('input[name=town_clinic_id]').last().val();
    var begin_date = panel.find('input[name=begin_date]').last().val();
    var end_date = panel.find('input[name=end_date]').last().val();

    datagrid.datagrid({
        url: '/management/workload_village_clinics_datagrid/',
        queryParams: { town_clinic_id: town_clinic_id,
            begin_date: begin_date, end_date: end_date
        },
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'clinic', title: '卫生机构', width: 30 },
            { field: 'education', title: '健康教育', width: 20 },
            { field: 'vaccine', title: '预防接种', width: 20 },
            { field: 'child', title: '0-6岁儿童', width: 20 },
            { field: 'pregnant', title: '孕产妇', width: 20 },
            { field: 'old', title: '老年人', width: 20 },
            { field: 'hypertension', title: '高血压', width: 20 },
            { field: 'diabetes', title: '2型糖尿病', width: 20 },
            { field: 'psychiatric', title: '重性精神病', width: 20 },
            { field: 'tcm', title: '中医药', width: 20 },
            { field: 'infection', title: '传染病报告', width: 20 },
            { field: 'supervision', title: '卫生监督', width: 20 },
            { field: 'total', title: '合计', width: 20 }
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
            var tabs = datagrid.parents('#workload_stat_tabs');
            if(!tabs.tabs('exists', row['clinic'] + '医生工作量')){
                tabs.tabs('add', {
                    title: row['clinic'] + '医生工作量', closable: true,
                    href: '/management/workload_doctors_page/', method: 'POST',
                    queryParams: {clinic_id: row['id'],
                                   begin_date: begin_date,
                                   end_date: end_date
                    }
                });
            }
            else{
                // 因为有可能用户在双击某村卫生室后，再回到首页页面重新设定起始时间和结束时间，
                // 然后再双击该村卫生室，所以必须先对已存在的标签页更新为新的时间的标签页
                var tab = tabs.tabs('getTab', row['clinic'] + '医生工作量');
                tabs.tabs('update', {
                    tab: tab,
                    options: {
                        title: row['clinic'] + '医生工作量', closable: true,
                        href: '/management/workload_doctors_page/', method: 'POST',
                        queryParams: { clinic_id: row['id'],
                                       begin_date: begin_date,
                                       end_date: end_date
                        }
                    }
                });
                tabs.tabs('select', row['clinic'] + '医生工作量');
            }
        }
    });
});