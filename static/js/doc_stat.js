$(function () {
    var datagrid = $('#doc_stat_table');
    var toolbar = $('#doc_stat_toolbar');

    toolbar.find('#begin_date').datebox({
        width: 100, editable: false, formatter: myformatter, parser :myparser
    });
    toolbar.find('#begin_date').datebox('setValue', newYearDay(new Date()));
    toolbar.find('#end_date').datebox({
        width: 100, editable: false, formatter: myformatter, parser :myparser
    });
    toolbar.find('#end_date').datebox('setValue', myformatter(new Date()));

    var btn_query = toolbar.find('#btn_query').linkbutton({
        iconCls: 'icon-glyphicons-28-search',
        plain: true
    });
    btn_query.bind('click', function() {
        if ($(this).linkbutton('options').disabled == false) {
            datagrid.datagrid('load');
        }
    });

    datagrid.datagrid({
        title: '工作量统计', url: '/services/get_doc_stat/',
        toolbar: '#doc_stat_toolbar',
        rownumbers: false, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'service', title: '公卫服务类别', width: 10 },
            { field: 'count', title: '工作量', width: 10 }
        ]],
        onBeforeLoad: function(param) {
            param.begin_date = toolbar.find('#begin_date').datebox('getValue');
            param.end_date = toolbar.find('#end_date').datebox('getValue');
        }
    });

});