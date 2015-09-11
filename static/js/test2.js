$(function() {
    var nav = $('#admin_nav');
    var tabs = $('#tabs');
    var excel = $('#excel');

    excel.linkbutton({plain: true, iconCls: 'icon-save'});

    nav.tree({
        url: '/management/admin_nav/', animate: true,
        onLoadSuccess: function(node, data) {
            if (data) {
                $(data).each(function () {
                    if (this.state == 'closed') {
                        nav.tree('expandAll');
                    }
                })
            }
        },
        onClick: function(node) {
            if (node.url) {
                if (tabs.tabs('exists', node.text)) {
                    tabs.tabs('select', node.text);
                } else {
                    tabs.tabs('add', {
                        title: node.text, closable: true, href: node.url
                    });
                }
            }
        }
    });

    tabs.tabs({
        fit: true, border: false,
        onSelect: function () {
            var tab = $(this).tabs('getSelected');
            tab.panel('refresh');
        }
    });

    // 首页的统计图
    $.getJSON('/management/graph_workload/', function (data) {
        $('#graph_workload').highcharts({
            chart: { type: 'bar' },
            title: { text: '卫生院工作量汇总图' },
            xAxis: { categories: data.clinics },
            yAxis: { min: 0, title: { text: '工作量（人次）' }},
            legend: { reversed: true },
            plotOptions: { series: { stacking: 'normal' }},
            credits: { enabled: false },
            exporting: { enabled: false },
            series: data.series

        });
    });

    $.getJSON('/management/graph_payment/', function(data) {
        $('#graph_payment').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            credits: { enabled: false },
            exporting: { enabled: false },
            title: {
                text: '各卫生院支付金额比例'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    }
                }
            },
            series: [{
                name: "金额比例",
                colorByPoint: true,
                data: data
            }]
        });
    });

});