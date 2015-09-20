$(function() {
    var nav = $('#admin_nav');
    var area = $('#admin_area');
    $.cookie['role'] = $('#role').val(); //记录当前登录用户的类型：超级管理员、卫生局管理员、财政局管理员

    nav.tree({
        url: '/management/admin_nav/', animate: true,
        onLoadSuccess: function(data) {
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
                if (node.url) {
                    area.panel({ href: node.url, fit: true, border: false });
                }
            }
        }
    });

    area.panel({ href: '/management/graphs/', fit: true, border: false });

});