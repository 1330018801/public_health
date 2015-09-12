$(function () {

    $('#excel').linkbutton({ plain: true, iconCls: 'icon-save' });

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