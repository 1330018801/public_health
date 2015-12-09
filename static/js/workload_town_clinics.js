$(function () {

    var datagrid = $('#workload_town_clinics_datagrid');
    var workload_town_toolbar = $('#workload_town_toolbar');
    var btn_workload_town_excel = workload_town_toolbar.find('#workload_town_excel');
    btn_workload_town_excel.linkbutton({ iconCls: 'icon-save', plain: true});

    workload_town_toolbar.find('#begin_date').datebox({
        width: 120, editable: false, formatter: myformatter, parser :myparser
    });
    workload_town_toolbar.find('#begin_date').datebox('setValue', newYearDay(new Date()));
    workload_town_toolbar.find('#end_date').datebox({
        width: 120, editable: false, formatter: myformatter, parser :myparser
    });
    workload_town_toolbar.find('#end_date').datebox('setValue', myformatter(new Date()));

    var btn_query = workload_town_toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('load');
        }
    });

    datagrid.datagrid({
        url: '/management/workload_town_clinics_datagrid/',
        toolbar: '#workload_town_toolbar',
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
        },
        onBeforeLoad: function(param) {
            param.begin_date = workload_town_toolbar.find('#begin_date').datebox('getValue');
            param.end_date = workload_town_toolbar.find('#end_date').datebox('getValue');
        },
        onDblClickRow: function(index, row) {
            var tabs = datagrid.parents('#workload_stat_tabs');
            if(!tabs.tabs('exists', row['clinic']+'工作量')){
                console.log(row['id']);
                console.log(row['clinic']);
                tabs.tabs('add', {
                    title: row['clinic'] + '工作量', closable: true,
                    //href: '/management/workload_village_clinics_page/' + row['id'] + '/'
                    href: '/management/workload_village_clinics_page/', method: 'POST',
                    queryParams: {town_clinic_id: row['id'],
                                    begin_date: workload_town_toolbar.find('#begin_date').datebox('getValue'),
                                    end_date: workload_town_toolbar.find('#end_date').datebox('getValue')
                    }
                });
            }
            else{
                //因为有可能用户在双击某乡镇卫生院后，再回到本页面重新设定起始时间和结束时间，然后再双击该乡镇卫生院，所以必须先对已存在的标签页更新为新的时间的标签页
                var tab = tabs.tabs('getTab', row['clinic']+'工作量');
                tabs.tabs('update', {
                            tab: tab,
                            options: {
                                title: row['clinic'] + '工作量', closable: true,
                                href: '/management/workload_village_clinics_page/', method: 'POST',
                                queryParams: {town_clinic_id: row['id'],
                                    begin_date: workload_town_toolbar.find('#begin_date').datebox('getValue'),
                                    end_date: workload_town_toolbar.find('#end_date').datebox('getValue')
                                }
                            }
                });
                tabs.tabs('select', row['clinic']+'工作量');
            }
        }
    });
});