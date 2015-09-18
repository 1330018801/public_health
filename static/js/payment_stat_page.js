$(function () {
    var tabs = $('#payment_stat_tabs');

    tabs.tabs({
        fit: true, border: false
    });

    tabs.tabs('add', {
        title: '卫生院基本公卫费用', closable: true, href: '/management/payment_town_clinics_page/'
    });

});