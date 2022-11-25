function counting()
{
  var today = new Date();

  var hour = today.getHours();
  if (hour<10)hour = "0"+hour;
  var minut = today.getMinutes();
  if (minut<10)minut = "0"+minut;
  var second = today.getSeconds();
  if (second<10)second = "0"+second;

  document.getElementById("reload").innerHTML =
  +hour+":"+minut+":"+second;

  setTimeout('counting()',1000);
};
