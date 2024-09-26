

/*

fetch("https://dolarapi.com/v1/dolares")
  .then(response => response.json())
  .then(data => {console.log(data[5].venta); console.log (data[4].venta)});


  fetch("https://dolarapi.com/v1/dolares")
  .then(response => response.json())
  .then(data => {document.getElementsByClassName("precio-venta")[0].innerHTML= data[5].venta});



 */

fetch("https://dolarapi.com/v1/cotizaciones")
  .then(response => response.json())
  .then(data => {for (i=0; i<data.length; i++){
    agregarCotizacion(data[i].nombre, data[i].venta, data[i].compra)}});

  function agregarCotizacion(nombre, venta, compra){
    var x = document.getElementsByClassName("dolar-oficial")[0].cloneNode(true)

    x.querySelector(".dolar").innerHTML= nombre
    x.querySelector(".precio-venta").innerHTML= venta
    x.querySelector(".precio-compra").innerHTML= compra
    document.body.appendChild(x)
  }

