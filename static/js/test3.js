$(function() {
    var tabs = $('#tabs');
    tabs.tabs({ border: false });

    tabs.tabs('add', {
        title: 'aaa'
    });

    var stat = $('#stat');
    stat.panel({ title: 'bbb' })

});