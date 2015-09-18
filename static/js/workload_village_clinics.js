$(function () {

    var panel = $('.workload_village_clinics').last();
    var town_clinic_id = panel.find('input[name=town_clinic_id]').last().val();
    var datagrid = $('.workload_village_clinics_datagrid').last();

    datagrid.datagrid({
        url: '/management/workload_village_clinics_datagrid/' + town_clinic_id + '/',
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
            console.log(row['id']);
            console.log(row['clinic']);
            tabs.tabs('add', {
                title: row['clinic'] + '医生工作量', closable: true,
                href: '/management/workload_doctors_page/' + row['id'] + '/'
            });
        }
    });
});