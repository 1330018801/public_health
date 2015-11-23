$(function () {
    var datagrid = $('#payment_town_clinics');

    var payment_town_toolbar = $('#payment_town_toolbar');
    var btn_payment_town_excel = payment_town_toolbar.find('#payment_town_excel');
    btn_payment_town_excel.linkbutton({ iconCls: 'icon-save', plain: true});

    payment_town_toolbar.find('#begin_date').datebox({
        width: 120, editable: false, formatter: myformatter, parser :myparser
    });
    payment_town_toolbar.find('#begin_date').datebox('setValue', newYearDay(new Date()));
    payment_town_toolbar.find('#end_date').datebox({
        width: 120, editable: false, formatter: myformatter, parser :myparser
    });
    payment_town_toolbar.find('#end_date').datebox('setValue', myformatter(new Date()));

    var btn_query = payment_town_toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('load');
        }
    });

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
        },
        onBeforeLoad: function(param) {
            param.begin_date = payment_town_toolbar.find('#begin_date').datebox('getValue');
            param.end_date = payment_town_toolbar.find('#end_date').datebox('getValue');
        },
        onDblClickRow: function(index, row) {
            var tabs = datagrid.parents('#payment_stat_tabs');
            tabs.tabs('add', {
                title: row['clinic'] + '公共卫生费用', closable: true,
                href: '/management/payment_village_clinics_page/' + row['id'] + '/'
            });
        }
    });
});