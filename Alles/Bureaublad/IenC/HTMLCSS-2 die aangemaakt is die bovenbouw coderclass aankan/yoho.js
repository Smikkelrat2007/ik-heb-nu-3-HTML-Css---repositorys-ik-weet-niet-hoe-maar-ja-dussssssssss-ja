console.log("yohohohohohohohohoohohohohoohho");
console.log("Hello");
var buttons = document.getElementsByClassName("nav");
var menu = document.getElementById("menu");
menu.addEventListener("click", classes);


function classes()
{
  console.log("Hello");
  menu.classList.toggle('open');

  for (let i = 0; i < buttons.length; i++) {
  buttons[i].classList.toggle('open');
  }
}
