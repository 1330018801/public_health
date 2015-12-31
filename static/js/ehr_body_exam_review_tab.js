$(function(){
    var btn_print = $('#body_exam_review_tab_print').linkbutton({ iconCls: 'icon-print', plain: true});

    var table = $('#body_exam_review_tab_table');

    btn_print.bind('click', function(){
        if($(this).linkbutton('options').disabled == false){
            table.find('print_area').printThis();
        }
    });
});
