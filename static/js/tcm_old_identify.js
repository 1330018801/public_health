$(document).ready(function () {
    var yes_trend_qixu = $('input[name=yes_trend_qixu]');
    var yes_trend_yangxu = $('input[name=yes_trend_yangxu]');
    var yes_trend_yinxu = $('input[name=yes_trend_yinxu]');
    var yes_trend_tanshi = $('input[name=yes_trend_tanshi]');
    var yes_trend_shire = $('input[name=yes_trend_shire]');
    var yes_trend_xueyu = $('input[name=yes_trend_xueyu]');
    var yes_trend_qiyu = $('input[name=yes_trend_qiyu]');
    var yes_trend_tebing = $('input[name=yes_trend_tebing]');
    var yes_trend_pinghe = $('input[name=yes_trend_pinghe]');

    /*alert($("input[name='yes_trend_qixu']").get(0).disabled);*/
    //alert($('#id_yes_trend_qixu_0').html());
    //$('input[name=yes_trend_qixu]').eq(1).attr("checked", true);
    /*yes_trend_qixu[0].disabled=true;
    yes_trend_yangxu.disabled=true;
    yes_trend_yinxu.disabled=true;
    yes_trend_tanshi.disabled=true;
    yes_trend_shire.disabled=true;
    yes_trend_xueyu.disabled=true;
    yes_trend_qiyu.disabled=true;
    yes_trend_tebing.disabled=true;
    yes_trend_pinghe.disabled=true;*/

    var toolbar = $('#toolbar');
    var panel = $('#table');
    var form = $('#form');
    var resident_id = $('#resident_id').val();

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_edit = toolbar.find('#edit').linkbutton({ iconCls: 'icon-edit', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });
    btn_edit.linkbutton('disable');

    btn_print.bind('click', function () {
        panel.find('.print_area').printThis();
    });

    btn_save.bind('click', function () {
        form.form('submit', {
            url: '/tcm/old_identify_submit/', method: 'POST',
            onSubmit: function (param) {
                /*if(!form.find('input[name=pinghe]').is(":checked")){
                    $.messager.alert('提示', '请选择是否平和质', 'info');
                    return false;
                }
                if(!form.find('input[name=qixu]').is(":checked")){
                    $.messager.alert('提示', '请选择是否气虚质', 'info');
                    return false;
                }
                if(!form.find('input[name=yangxu]').is(":checked")){
                    $.messager.alert('提示', '请选择是否阳虚质', 'info');
                    return false;
                }
                if(!form.find('input[name=yinxu]').is(":checked")){
                    $.messager.alert('提示', '请选择是否阴虚质', 'info');
                    return false;
                }
                if(!form.find('input[name=tanshi]').is(":checked")){
                    $.messager.alert('提示', '请选择是否痰湿质', 'info');
                    return false;
                }
                if(!form.find('input[name=shire]').is(":checked")){
                    $.messager.alert('提示', '请选择是否湿热质', 'info');
                    return false;
                }
                if(!form.find('input[name=xueyu]').is(":checked")){
                    $.messager.alert('提示', '请选择是否血瘀质', 'info');
                    return false;
                }
                if(!form.find('input[name=qiyu]').is(":checked")){
                    $.messager.alert('提示', '请选择是否气郁质', 'info');
                    return false;
                }
                if(!form.find('input[name=tebing]').is(":checked")){
                    $.messager.alert('提示', '请选择是否特秉质', 'info');
                    return false;
                }*/
                if(!form.find('input[name=q1]').is(":checked")){
                    $.messager.alert('提示', '请选择第1题', 'info');
                    return false;
                }
                if(!form.find('input[name=q2]').is(":checked")){
                    $.messager.alert('提示', '请选择第2题', 'info');
                    return false;
                }
                if(!form.find('input[name=q3]').is(":checked")){
                    $.messager.alert('提示', '请选择第3题', 'info');
                    return false;
                }
                if(!form.find('input[name=q4]').is(":checked")){
                    $.messager.alert('提示', '请选择第4题', 'info');
                    return false;
                }
                if(!form.find('input[name=q5]').is(":checked")){
                    $.messager.alert('提示', '请选择第5题', 'info');
                    return false;
                }
                if(!form.find('input[name=q6]').is(":checked")){
                    $.messager.alert('提示', '请选择第6题', 'info');
                    return false;
                }
                if(!form.find('input[name=q7]').is(":checked")){
                    $.messager.alert('提示', '请选择第7题', 'info');
                    return false;
                }
                if(!form.find('input[name=q8]').is(":checked")){
                    $.messager.alert('提示', '请选择第8题', 'info');
                    return false;
                }
                if(!form.find('input[name=q9]').is(":checked")){
                    $.messager.alert('提示', '请选择第9题', 'info');
                    return false;
                }
                if(!form.find('input[name=q10]').is(":checked")){
                    $.messager.alert('提示', '请选择第10题', 'info');
                    return false;
                }
                if(!form.find('input[name=q11]').is(":checked")){
                    $.messager.alert('提示', '请选择第11题', 'info');
                    return false;
                }
                if(!form.find('input[name=q12]').is(":checked")){
                    $.messager.alert('提示', '请选择第12题', 'info');
                    return false;
                }
                if(!form.find('input[name=q13]').is(":checked")){
                    $.messager.alert('提示', '请选择第13题', 'info');
                    return false;
                }
                if(!form.find('input[name=q14]').is(":checked")){
                    $.messager.alert('提示', '请选择第14题', 'info');
                    return false;
                }
                if(!form.find('input[name=q15]').is(":checked")){
                    $.messager.alert('提示', '请选择第15题', 'info');
                    return false;
                }
                if(!form.find('input[name=q16]').is(":checked")){
                    $.messager.alert('提示', '请选择第16题', 'info');
                    return false;
                }
                if(!form.find('input[name=q17]').is(":checked")){
                    $.messager.alert('提示', '请选择第17题', 'info');
                    return false;
                }
                if(!form.find('input[name=q18]').is(":checked")){
                    $.messager.alert('提示', '请选择第18题', 'info');
                    return false;
                }
                if(!form.find('input[name=q19]').is(":checked")){
                    $.messager.alert('提示', '请选择第19题', 'info');
                    return false;
                }
                if(!form.find('input[name=q20]').is(":checked")){
                    $.messager.alert('提示', '请选择第20题', 'info');
                    return false;
                }
                if(!form.find('input[name=q21]').is(":checked")){
                    $.messager.alert('提示', '请选择第21题', 'info');
                    return false;
                }
                if(!form.find('input[name=q22]').is(":checked")){
                    $.messager.alert('提示', '请选择第22题', 'info');
                    return false;
                }
                if(!form.find('input[name=q23]').is(":checked")){
                    $.messager.alert('提示', '请选择第23题', 'info');
                    return false;
                }
                if(!form.find('input[name=q24]').is(":checked")){
                    $.messager.alert('提示', '请选择第24题', 'info');
                    return false;
                }
                if(!form.find('input[name=q25]').is(":checked")){
                    $.messager.alert('提示', '请选择第25题', 'info');
                    return false;
                }
                if(!form.find('input[name=q26]').is(":checked")){
                    $.messager.alert('提示', '请选择第26题', 'info');
                    return false;
                }
                if(!form.find('input[name=q27]').is(":checked")){
                    $.messager.alert('提示', '请选择第27题', 'info');
                    return false;
                }
                if(!form.find('input[name=q28]').is(":checked")){
                    $.messager.alert('提示', '请选择第28题', 'info');
                    return false;
                }
                if(!form.find('input[name=q29]').is(":checked")){
                    $.messager.alert('提示', '请选择第29题', 'info');
                    return false;
                }
                if(!form.find('input[name=q30]').is(":checked")){
                    $.messager.alert('提示', '请选择第30题', 'info');
                    return false;
                }
                if(!form.find('input[name=q31]').is(":checked")){
                    $.messager.alert('提示', '请选择第31题', 'info');
                    return false;
                }
                if(!form.find('input[name=q32]').is(":checked")){
                    $.messager.alert('提示', '请选择第32题', 'info');
                    return false;
                }
                if(!form.find('input[name=q33]').is(":checked")){
                    $.messager.alert('提示', '请选择第33题', 'info');
                    return false;
                }

                if(form.find('input[name=yes_trend_qixu]').is(":checked") && !form.find('input[name=health_care_guide_qixu]').is(":checked")){
                    $.messager.alert('提示', '请选择气虚质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_yangxu]').is(":checked") && !form.find('input[name=health_care_guide_yangxu]').is(":checked")){
                    $.messager.alert('提示', '请选择阳虚质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_yinxu]').is(":checked") && !form.find('input[name=health_care_guide_yinxu]').is(":checked")){
                    $.messager.alert('提示', '请选择阴虚质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_tanshi]').is(":checked") && !form.find('input[name=health_care_guide_tanshi]').is(":checked")){
                    $.messager.alert('提示', '请选择痰湿质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_shire]').is(":checked") && !form.find('input[name=health_care_guide_shire]').is(":checked")){
                    $.messager.alert('提示', '请选择湿热质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_xueyu]').is(":checked") && !form.find('input[name=health_care_guide_xueyu]').is(":checked")){
                    $.messager.alert('提示', '请选择血瘀质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_qiyu]').is(":checked") && !form.find('input[name=health_care_guide_qiyu]').is(":checked")){
                    $.messager.alert('提示', '请选择气郁质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_tebing]').is(":checked") && !form.find('input[name=health_care_guide_tebing]').is(":checked")){
                    $.messager.alert('提示', '请选择特禀质的中医药保健指导', 'info');
                    return false;
                }
                if(form.find('input[name=yes_trend_pinghe]').is(":checked") && !form.find('input[name=health_care_guide_pinghe]').is(":checked")){
                    $.messager.alert('提示', '请选择平和质的中医药保健指导', 'info');
                    return false;
                }

                if (form.form('validate')) {
                    param.csrfmiddlewaretoken = $.cookie('csrftoken');
                    return true;
                } else {
                    return false;
                }
            },
            success: function (json_data) {
                //alert(json_data);
                var data = eval('(' + json_data + ')');
                if (data.success) {
                    panel.panel('refresh', '/tcm/old_identify_form/');
                    $.messager.show({title: '提示', msg: '老年人中医药健康管理服务记录表保存成功', timeout: 2000});
                } else {
                    $.messager.alert('提示', '老年人中医药健康管理服务记录表保存失败', 'info');
                }
            }
        });
    });

    panel.panel({ href: '/tcm/old_identify_form/', method: 'POST' });
});


function finish(){              //判断33个题是否都做完了，以决定是否评分
    var object0=new Array();

    object0[0]="q1";
    object0[1]="q2";
    object0[2]="q3";
    object0[3]="q4";
    object0[4]="q5";
    object0[5]="q6";
    object0[6]="q7";
    object0[7]="q8";
    object0[8]="q9";
    object0[9]="q10";
    object0[10]="q11";
    object0[11]="q12";
    object0[12]="q13";
    object0[13]="q14";
    object0[14]="q15";
    object0[15]="q16";
    object0[16]="q17";
    object0[17]="q18";
    object0[18]="q19";
    object0[19]="q20";
    object0[20]="q21";
    object0[21]="q22";
    object0[22]="q23";
    object0[23]="q24";
    object0[24]="q25";
    object0[25]="q26";
    object0[26]="q27";
    object0[27]="q28";
    object0[28]="q29";
    object0[29]="q30";
    object0[30]="q31";
    object0[31]="q32";
    object0[32]="q33";

    var object;
    for(var i=0;i<object0.length;i++){
        object = document.getElementsByName(object0[i]);
        for(var j=0;j<object.length;j++){
            if(object[j].checked)
            break;
        }
        if (j>=object.length){
            return false;
        }
    }
    return true;
    //alert("hhhh");
}

function getNameValue(tagName){             //获得被选中选项的值
    var value = 0;
    var object = document.getElementsByName(tagName);
    for ( var  i = 0 ;i < object.length;i ++ ){
        if(object[i].checked){
            value = object[i].value;
            break;
        }
    }
    return value;
}

function totalPoint(){                    //根据被选中选项的值计算总分
    var q1Value = getNameValue('q1');
    //alert(q1Value);
    var q2Value = getNameValue('q2');
    var q3Value = getNameValue('q3');
    var q4Value = getNameValue('q4');
    var q5Value = getNameValue('q5');
    var q6Value = getNameValue('q6');
    var q7Value = getNameValue('q7');
    var q8Value = getNameValue('q8');
    var q9Value = getNameValue('q9');
    var q10Value = getNameValue('q10');
    var q11Value = getNameValue('q11');
    var q12Value = getNameValue('q12');
    var q13Value = getNameValue('q13');
    var q14Value = getNameValue('q14');
    var q15Value = getNameValue('q15');
    var q16Value = getNameValue('q16');
    var q17Value = getNameValue('q17');
    var q18Value = getNameValue('q18');
    var q19Value = getNameValue('q19');
    var q20Value = getNameValue('q20');
    var q21Value = getNameValue('q21');
    var q22Value = getNameValue('q22');
    var q23Value = getNameValue('q23');
    var q24Value = getNameValue('q24');
    var q25Value = getNameValue('q25');
    var q26Value = getNameValue('q26');
    var q27Value = getNameValue('q27');
    var q28Value = getNameValue('q28');
    var q29Value = getNameValue('q29');
    var q30Value = getNameValue('q30');
    var q31Value = getNameValue('q31');
    var q32Value = getNameValue('q32');
    var q33Value = getNameValue('q33');

    //计算各种体质得分
    var points_qixu = parseInt(q2Value) + parseInt(q3Value) + parseInt(q4Value) + parseInt(q14Value);
    var points_yangxu = parseInt(q11Value) + parseInt(q12Value) + parseInt(q13Value) + parseInt(q29Value);
    var points_yinxu = parseInt(q10Value) + parseInt(q21Value) + parseInt(q26Value) + parseInt(q31Value);
    var points_tanshi = parseInt(q9Value) + parseInt(q16Value) + parseInt(q28Value) + parseInt(q32Value);
    var points_shire = parseInt(q23Value) + parseInt(q25Value) + parseInt(q27Value) + parseInt(q30Value);
    var points_xueyu = parseInt(q19Value) + parseInt(q22Value) + parseInt(q24Value) + parseInt(q33Value);
    var points_qiyu = parseInt(q5Value) + parseInt(q6Value) + parseInt(q7Value) + parseInt(q8Value);
    var points_tebing = parseInt(q15Value) + parseInt(q17Value) + parseInt(q18Value) + parseInt(q20Value);
    var points_pinghe = parseInt(q1Value) + (6 - parseInt(q2Value)) + (6 - parseInt(q4Value)) + (6 - parseInt(q5Value)) + (6 - parseInt(q13Value));

    //写入到得分框
    /*document.getElementsByName("points_qixu").value = point_qixu;*/
    /*var qixu=document.getElementsByName("points_qixu");
    qixu[0].value = point_qixu;*/
    /*document.getElementById("id_points_qixu").value = points_qixu;*/
    /*var haha = document.getElementById("id_points_qixu");
    haha.value = points_qixu;*/

    document.getElementById("id_points_qixu").innerText = points_qixu.toString();
    //document.getElementById("hh").value = points_qixu;
    document.getElementById("points_qixu").value = points_qixu;

    document.getElementById("id_points_yangxu").innerText = points_yangxu.toString();
    document.getElementById("points_yangxu").value = points_yangxu;

    document.getElementById("id_points_yinxu").innerText = points_yinxu.toString();
    document.getElementById("points_yinxu").value = points_yinxu;

    document.getElementById("id_points_tanshi").innerText = points_tanshi.toString();
    document.getElementById("points_tanshi").value = points_tanshi;

    document.getElementById("id_points_shire").innerText = points_shire.toString();
    document.getElementById("points_shire").value = points_shire;

    document.getElementById("id_points_xueyu").innerText = points_xueyu.toString();
    document.getElementById("points_xueyu").value = points_xueyu;

    document.getElementById("id_points_qiyu").innerText = points_qiyu.toString();
    document.getElementById("points_qiyu").value = points_qiyu;

    document.getElementById("id_points_tebing").innerText = points_tebing.toString();
    document.getElementById("points_tebing").value = points_tebing;

    document.getElementById("id_points_pinghe").innerText = points_pinghe.toString();
    document.getElementById("points_pinghe").value = points_pinghe;

    //alert('qixu'+ point_qixu);

    var flag=finish();                      //根据是否已经做完题，以及总分评定体质倾向
    //alert(flag);
    var yes_trend_qixu = document.getElementsByName("yes_trend_qixu");
    var yes_trend_yangxu = document.getElementsByName("yes_trend_yangxu");
    var yes_trend_yinxu = document.getElementsByName("yes_trend_yinxu");
    var yes_trend_tanshi = document.getElementsByName("yes_trend_tanshi");
    var yes_trend_shire = document.getElementsByName("yes_trend_shire");
    var yes_trend_xueyu = document.getElementsByName("yes_trend_xueyu");
    var yes_trend_qiyu = document.getElementsByName("yes_trend_qiyu");
    var yes_trend_tebing = document.getElementsByName("yes_trend_tebing");
    var yes_trend_pinghe = document.getElementsByName("yes_trend_pinghe");

    if(flag){
          if(points_qixu>=11){
                yes_trend_qixu[0].checked=true;

                //mild.disabled="disabled";
                //moderate.disabled="disabled";
                //serious.disabled="disabled";
                //$('#cddj').val('可自理');
                yes_trend_qixu[0].disabled=false;


          }
          else if(points_qixu>=9 && points_qixu<=10){
              yes_trend_qixu[1].checked=true;
              yes_trend_qixu[1].disabled=false;

          }
          else{

          }

          if(points_yangxu>=11){
              yes_trend_yangxu[0].checked=true;
              yes_trend_yangxu[0].disabled=false;
          }
          else if(points_yangxu>=9 && points_yangxu<=10){
              yes_trend_yangxu[1].checked=true;
              yes_trend_yangxu[1].disabled=false;
          }
          else{

          }

          if(points_yinxu>=11){
                yes_trend_yinxu[0].checked=true;
                yes_trend_yinxu[0].disabled=false;
          }
          else if(points_yinxu>=9 && points_yinxu<=10){
              yes_trend_yinxu[1].checked=true;
              yes_trend_yinxu[1].disabled=false;

          }
          else{

          }

          if(points_tanshi>=11){
              yes_trend_tanshi[0].checked=true;
              yes_trend_tanshi[0].disabled=false;
          }
          else if(points_tanshi>=9 && points_tanshi<=10){
              yes_trend_tanshi[1].checked=true;
              yes_trend_tanshi[1].disabled=false;
          }
          else{

          }

          if(points_shire>=11){
              yes_trend_shire[0].checked=true;
              yes_trend_shire[0].disabled=false;
          }
          else if(points_shire>=9 && points_shire<=10){
              yes_trend_shire[1].checked=true;
              yes_trend_shire[1].disabled=false;
          }
          else{

          }

          if(points_xueyu>=11){
                yes_trend_xueyu[0].checked=true;
                yes_trend_xueyu[0].disabled=false;
          }
          else if(points_xueyu>=9 && points_xueyu<=10){
              yes_trend_xueyu[1].checked=true;
              yes_trend_xueyu[1].disabled=false;

          }
          else{

          }

          if(points_qiyu>=11){
              yes_trend_qiyu[0].checked=true;
              yes_trend_qiyu[0].disabled=false;
          }
          else if(points_qiyu>=9 && points_qiyu<=10){
              yes_trend_qiyu[1].checked=true;
              yes_trend_qiyu[1].disabled=false;
          }
          else{

          }

          if(points_tebing>=11){
                yes_trend_tebing[0].checked=true;
                yes_trend_tebing[0].disabled=false;
          }
          else if(points_tebing>=9 && points_tebing<=10){
              yes_trend_tebing[1].checked=true;
              yes_trend_tebing[1].disabled=false;

          }
          else{

          }

          if(points_pinghe>=17 && points_qixu<8 && points_yangxu<8 && points_yinxu<8 && points_tanshi<8 && points_shire<8 && points_xueyu<8 && points_qiyu<8 && points_tebing<8){
              yes_trend_pinghe[0].checked=true;
              yes_trend_pinghe[0].disabled=false;
          }
          else if(points_pinghe>=17 && points_qixu<10 && points_yangxu<10 && points_yinxu<10 && points_tanshi<10 && points_shire<10 && points_xueyu<10 && points_qiyu<10 && points_tebing<10){
              yes_trend_pinghe[1].checked=true;
              yes_trend_pinghe[1].disabled=false;
          }
          else{

          }
    }
}