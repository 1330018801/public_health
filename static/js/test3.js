$(function() {
    var my_select = $('#my-select');
    my_select.multiSelect({
        //keepOrder: true,
        selectableHeader: '<div align="center">Seletable items</div>',
        selectionHeader: '<div align="center">Selection items</div>',
        afterInit: function() {
            my_select.multiSelect('addOption', {value: 'elem_1', text: 'ELEM 1', index: 0, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_2', text: 'ELEM 2', index: 1, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_3', text: 'ELEM 3', index: 2, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_4', text: 'ELEM 4', index: 3, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_5', text: 'ELEM 5', index: 4, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_6', text: 'ELEM 6', index: 5, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_7', text: 'ELEM 7', index: 6, nested: 'Summer'});
            my_select.multiSelect('addOption', {value: 'elem_8', text: 'ELEM 8', index: 0, nested: 'Winter'});
            my_select.multiSelect('addOption', {value: 'elem_9', text: 'ELEM 9', index: 1, nested: 'Winter'});
            my_select.multiSelect('addOption', {value: 'elem_10', text: 'ELEM 10', index: 2, nested: 'Winter'});
            my_select.multiSelect('addOption', {value: 'elem_11', text: 'ELEM 11', index: 3, nested: 'Winter'});
            my_select.multiSelect('addOption', {value: 'elem_12', text: 'ELEM 12', index: 4, nested: 'Winter'});
            my_select.multiSelect('select', ['elem_2', 'elem_4']);
        }
    });

    $('#box').dialog({
        width: 600,
        height: 300,
        title: '添加用户',
        cache: false,
        modal: true,
        buttons: [
            {
                text: '提交',
                iconCls: 'icon-ok',
                handler: function() {
                    $('#box').form('submit');
                }
            },
            {
                text: '取消',
                iconCls: 'icon-cancel',
                handler: function() {
                    $('#box').dialog('close');
                }
            }
        ],
        onClose: function() {
            $('#box').form('clear');
        }
    });
});