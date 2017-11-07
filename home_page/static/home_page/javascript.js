
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
function show(){
    modal.style.display="block";
}
function dont_show(){
    modal.style.display = "none";
}
window.onclick = function(event){
	if(event.target == modal2){
		modal.style.display = "none";
	}
}

var modal2 =document.getElementById('myModal2');
function show2(){
	modal2.style.display="block";
}
function dont_show2(){
	modal2.style.display = "none";
}
window.onclick = function(event){
	if(event.target == modal2){
		modal2.style.display = "none";
	}
}