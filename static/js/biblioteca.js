window.onload = init; function init() {
var button = document.getElementById("submit");
button.onclick = handleButtonClick; }
function handleButtonClick() {
    var textInput= document.getElementById("titulo");
    var titulo=textInput.value;
    var li=document.createElement("li");
    li.innerHTML=titulo;
    var ul = document.getElementById("zonadelibros");
    ul.appendChild(li);}