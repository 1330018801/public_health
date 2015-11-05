$(function () {
    var tabs = $('#ehr_setup_tabs');

    tabs.tabs({
        fit: true, border: false
    });

    tabs.tabs('add', {
        title: '辖区建档居民列表', closable: true, href: '/ehr/ehr_resident_list/'
    });

});