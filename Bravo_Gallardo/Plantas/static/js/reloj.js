let html = document.getElementById("tiempo");

setInterval(function(){
	tiempo = new Date();

	horas = tiempo.getHours();
	minutos = tiempo.getMinutes();
	segundos = tiempo.getSeconds();

	//evitar los 0 o numeros individuales
	if(horas<10)
		horas = "0"+horas;
	if(minutos<10)
		minutos = "0"+minutos;
	if(segundos<10)
		segundos = "0"+segundos;

	html.innerHTML = `${horas} : ${minutos} : ${segundos}`;
},1000);


let reloj = document.getElementById('reloj');
let botiempo = document.getElementById('cajaboton')
var cont = false;
let secion = document.getElementById('seccion');

document.getElementById("botiempo").addEventListener('click',()=>{

	if(!cont){
   		botiempo.style.left = '270px';
    	reloj.style.left = '0px';
		botiempo.style.transform = 'rotate(180deg)';


		cont = true;
	}else{
		botiempo.style.left = '6px';
		reloj.style.left = '-300px';
		botiempo.style.transform = 'rotate(360deg)';
		cont = false;

	}
})

let logo = document.getElementById("logo");
let texto = document.getElementById("texto");

texto.addEventListener("mouseover", function() {
	logo.classList.add("rotar");


});
  
texto.addEventListener("mouseout", function() {
	logo.classList.remove("rotar");

});


