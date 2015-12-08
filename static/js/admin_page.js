$(function() {
    var nav = $('#admin_nav');
    var area = $('#admin_area');
    $.removeCookie('role');
    $.removeCookie('clinic_id');
    $.cookie('role', $('#role').val());
    $.cookie('clinic_id', $('#clinic_id').val());

    nav.tree({
        url: '/management/admin_nav/', animate: true,
        onLoadSuccess: function(data) {
            if (data)
                $(data).each(function () {
                    if (this.state == 'closed')
                        nav.tree('expandAll');
                })
        },
        onClick: function(node) {
            if (node.url)
                area.panel({ href: node.url, fit: true, border: false });
        }
    });

    area.panel({ href: '/management/graphs/', fit: true, border: false });

});