$(function () {
    var table = $('#personal_info_review_tab_table');

    var print_btn = $('#personal_info_review_tab_print').linkbutton({ iconCls: 'icon-print', plain: true});

    print_btn.bind('click', function(){
        if($(this).linkbutton('options').disabled == false){
            table.find('.print_area').printThis();
        }
    });
    
});