$(function() {
    var nav = $('#admin_nav');
    var area = $('#admin_area');

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
            var node = nav.tree('find', 11);
            nav.tree('select', node.target);
            area.panel({
                href: node.url, fit: true, border: false
            });
        },
        onClick: function(node) {
            if (node.url) {
                if (node.url) {
                    area.panel({ href: node.url, fit: true, border: false });
                }
            }
        }
    });
});