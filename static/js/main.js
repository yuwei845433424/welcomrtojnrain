
$(document).ready(function() {
	$('#header')
	.css({ 'top':-30 })
	.delay(1000)
	.animate({'top': 0}, 800);
	
	$('#footer')
	.css({ 'bottom':-15 })
	.delay(1000)
	.animate({'bottom': 0}, 800);
})

  function upload(){
 	var name = $("#name").val();
 	 	//deal with the situation of null or blank 
 	if(name == null || name == ""){
 		alert("姓名为空,请输入后在提交");
 		return;
 	}
 	var tel = $("#tel").val();
    if(tel == null || tel == ""){
    	alert("联系方式为空,请输入后在提交");
    	return;
    }
    var content = $("#content").val();
    if(content == null || content == ""){
    	alert("自我介绍为空,请输入后在提交");
    	return;

 	}
        $.ajax({
        url: 'upload',
        type: 'GET',
        async:'false',
        dataType: 'text',
        data: {"name":name,"tel":tel,"content":content},
        success:function(data){

        },
        error:function() {
        }
    })

    }


   