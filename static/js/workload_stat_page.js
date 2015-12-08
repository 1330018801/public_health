$(function () {
    var tabs = $('#workload_stat_tabs');

    tabs.tabs({
        fit: true, border: false
    });

    if ($.cookie('role') == '卫生院管理员') {
        tabs.tabs('add', {
            title: '卫生院工作量', closable: true, method: 'POST',
            href: '/management/workload_village_clinics_page/',
            queryParams: {town_clinic_id: $.cookie('clinic_id')}
        });
    } else {
        tabs.tabs('add', {
            title: '卫生院工作量', closable: true,
            href: '/management/workload_town_clinics_page/'
        });
    }

});