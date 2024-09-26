fetch("https://dolarapi.com/v1/dolares")
  .then(response => response.json())
  .then(data => {console.log(data[5].venta); console.log (data[4].venta)});/*document.write(data[5].venta); document.write(data[4].venta)});*/
