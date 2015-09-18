$(function () {
    var tabs = $('#workload_stat_tabs');

    tabs.tabs({
        fit: true, border: false
    });

    tabs.tabs('add', {
        title: '卫生院工作量', closable: true, href: '/management/workload_town_clinics_page/'
    });

});