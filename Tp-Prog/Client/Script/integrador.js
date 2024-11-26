const crearCartaCotizacion = (cotizacion) => {
  
  const carta = document.createElement('div');
  carta.classList.add('dolar-oficial');

  carta.innerHTML = `  
    <div class="dolar">${cotizacion.nombre} Oficial</div>
    <div class="compra-venta">
        <div class="compra">
            <span>Compra</span>
            <span class="precio-compra">$${parseFloat(cotizacion.compra).toFixed(2)}</span>
        </div>
        <div class="venta">
            <span>Venta</span>
            <span class="precio-venta">$${parseFloat(cotizacion.venta).toFixed(2)}</span>
        </div>
    </div>
  `;
  // que complicado es hacer backticks

  return carta; 
};

const actualizarCotizaciones = (cotizaciones) => {
  const container = document.querySelector('.carta-container');
  container.innerHTML = '';

  cotizaciones.forEach(cotizacion => {
      const carta = crearCartaCotizacion(cotizacion); 
      container.appendChild(carta); 
  });
};

const mostrarGifCarga = () => {
  document.getElementById('gifCarga').style.display = 'block';
};

const ocultarGifCarga = () => {
  document.getElementById('gifCarga').style.display = 'none';
};

const getCotizaciones = async () => {
  mostrarGifCarga();
  const timer = setTimeout(() => {
    ocultarGifCarga();
  }, 5000);

  try {
    // para usar el server de py descomentar la linea 50
      // const response = await fetch("https://tp-prog.onrender.com");
     //const response = await fetch("http://127.0.0.1:5000/"); 
     const response = await fetch("https://dolarapi.com/v1/cotizaciones");
      const data2 = await response.json();
      //console.log('cotiza',data2)
      const cotizaciones = data2.map(moneda => ({
          nombre: moneda.nombre,
          venta: moneda.venta,
          compra: moneda.compra
      }));

     // console.log("cotizacion de la moneda ", cotizaciones);
      actualizarCotizaciones(cotizaciones); 
  } catch (error) {
      console.log("Error al obtener los datos de la cotizacion", error);
  } finally {
      clearTimeout(timer);
      ocultarGifCarga();
  }
};

window.onload = getCotizaciones();
