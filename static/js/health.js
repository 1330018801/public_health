function myformatter(date){
	var y = date.getFullYear();
	var m = date.getMonth() + 1;
	var d = date.getDate();
	return y+'-'+(m<10?('0'+m):m)+'-'+(d<10?('0'+d):d);
}

function myparser(s){
	if (!s) return new Date();
	var ss = (s.split('-'));
	var y = parseInt(ss[0],10);
	var m = parseInt(ss[1],10);
	var d = parseInt(ss[2],10);
	if (!isNaN(y) && !isNaN(m) && !isNaN(d)){
		return new Date(y,m-1,d);
	} else {
		return new Date();
	}
}

function myformatter2(time){
	return time.year + '-' +
           (t.month < 10 ? ('0' + t.month) : t.month) + '-' +
           (t.day < 10 ? ('0' + t.day) : t.day) + ' ' +
           (t.hour < 10 ? ('0' + t.hour) : t.hour) + ':' +
           (t.minute < 10 ? ('0' + t.minute) : t.minute) + ':' +
           (t.second < 10 ? ('0' + t.second) : t.second);
}

function print_table() {
    var html_body = window.document.body.innerHTML;     //获取当前页的html代码
    var sprnstr = "<!--printStart-->";          //设置打印开始区域
    var eprnstr = "<!--printEnd-->";            //设置打印结束区域
    var prnhtml = html_body.substring(html_body.indexOf(sprnstr) + 18);     //从开始代码向后取html
    prnhtml = prnhtml.substring(0, prnhtml.indexOf(eprnstr));           //从结束代码向前取html
    window.document.body.innerHTML = prnhtml;
    window.print();
    window.document.body.innerHTML = html_body;
}


//解决Ajax中POST方法与Django中csrf冲突的问题
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function newYearDay(date) {
    var y = date.getFullYear();
    return y+'-01-01';
}

function endYearDay(date) {
    var y = date.getFullYear();
    return y+'-12-31';
}
