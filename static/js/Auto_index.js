// 将问题发送到后台，并接收相应
function sendtoserver(text)
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      //  相应完成，则显示出来
      // document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
      var answer=xmlhttp.responseText;
      show($.trim(answer));
    }
  }
  xmlhttp.open("POST","/Auto_add",true);
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  // xmlhttp.send("id=bei&q="+$.trim(text));
    xmlhttp.send("id=bei&q="+$.trim(text));
}

function getpaper(){
    // var title=document.getElementById('info').value;
    var title=$('#info').val();
    // window.alert(test);
    sendtoserver(title);
}



function show(data) {
    var p = "<div class='item'>" + data + '</div>';
    $('#paper').append(p);
    $('#paper').scrollTop($('#paper')[0].scrollHeight);
}
