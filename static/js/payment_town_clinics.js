$(function () {
    var datagrid = $('#payment_town_clinics');

    datagrid.datagrid({
        url: '/management/payment_town_clinics_datagrid/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编码', hidden: true },
            { field: 'clinic', title: '卫生院', width: 30 },
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
            var tabs = datagrid.parents('#payment_stat_tabs');
            console.log(row['id']);
            console.log(row['clinic']);
            tabs.tabs('add', {
                title: row['clinic'] + '公共卫生费用', closable: true,
                href: '/management/payment_village_clinics_page/' + row['id'] + '/'
            });
        }
    });
});