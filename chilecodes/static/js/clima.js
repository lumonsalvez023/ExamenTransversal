/*LINK DEL TIEMPO*/
/*http://api.openweathermap.org/data/2.5/weather?id=3872348&appid=aa9cc6341e3c98e8b27b796fd450ef8e*/

/*Variables*/

let input = document.querySelector('.input_text'); 
let main = document.querySelector('.name');
let temp = document.querySelector('.temp');
let desc = document.querySelector('.desc');
let humidity = document.querySelector('.humidity');
let clouds = document.querySelector('.clouds');
let idicon = document.querySelector('.idicon')
let button= document.querySelector('.submit');




button.addEventListener('click', function(name){
/*Conexion con los datos del tiempo*/
fetch('https://api.openweathermap.org/data/2.5/weather?q='+input.value+'&appid=aa9cc6341e3c98e8b27b796fd450ef8e')
.then(response => response.json())
.then(data => {
  
  /*Retiro de datos mediante listas */

  var tempValue = data['main']['temp'];
  var nameValue = data['name'];
  var descValue = data['weather'][0]['description'];
  var humidityValue = data['main']['humidity'];
  var idiconValue = data['weather'][0]['icon']
    
  /*Insertando los datos de la API a Html*/

  main.innerHTML = nameValue;
  temp.innerHTML = "Temperatura: "+(tempValue-273.15).toFixed(2)+'C°';
  
  

  humidity.innerHTML="Humedad: "+" "+ humidityValue+'%';
  input.value ="";

/*Condicional del clima*/
function climaespañol(descValue){

    switch (descValue) {
        case 'clear sky':
            desc.innerHTML = "Clima: Cielo Despejado";
            break;
        case 'few clouds':
            desc.innerHTML = "Clima: Cielo con Pocas Nubes";
            break;
        case 'scattered clouds':
            desc.innerHTML = "Parcialmente Nublado";
            break;
        case 'broken clouds':
            desc.innerHTML = "Clima: Nublado";
        default:
            break;

    }
    return desc.innerHTML;
}

/*Condicional de icono*/
function invocacionIcono(idiconValue){
    switch (idiconValue) {
        case '01d':
        case '01n':
            idicon.innerHTML='<img src="/static/img/cielodespejado.jpg" alt="">'; 
            break;
        case '02d':
        case '02n':
            idicon.innerHTML='<img src="/static/img/pocasnubesd.png" alt="">'; 
            break;
        case '03d':
        case '03n':
            idicon.innerHTML='<img src="/static/img/nubesdispersasd.jpg" alt="">'; 
            break;
        case '04d':
        case '04n':
            idicon.innerHTML='<img src="/static/img/nublado.jpg" alt="">'; 
            break;
        
    
        default:
            break;
    }
    return idicon.innerHTML;
}



/* Llamando a la funcion del clima*/
climaespañol(descValue);
/* Llamando al icono del clima*/
invocacionIcono(idiconValue);


})

.catch(err => alert("Error, la ciudad ingresada no existe"));
})