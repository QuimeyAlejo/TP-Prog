const crearCartaCotizacion = (cotizacion) => {
  
    const carta = document.createElement('div');
    carta.classList.add('dolar-oficial'); // Usa la misma clase que tenías
  
    //  ${cotizacion.tipoDeCambio}
    carta.innerHTML = `
            <div class="dolar"> Dolar ${cotizacion.nombre}</div>
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
  
    return carta; 
  };
  
  const actualizarCotizaciones = (cotizaciones) => {
    const container = document.querySelector('.carta-container'); // Selecciona el contenedor
  
    
    container.innerHTML = '';
  
    cotizaciones.forEach(cotizacion => {
        const carta = crearCartaCotizacion(cotizacion); 
        container.appendChild(carta); 
    });
  };
  
const peticionesDolares = async () => {
    try {
        const response = await fetch("https://dolarapi.com/v1/dolares");
        const data2 = await response.json();
        const cotizaciones = data2.map(moneda => ({
            nombre: moneda.nombre,
          //  tipoDeCambio: moneda.casa,

            venta: moneda.venta,
            compra: moneda.compra
        }));
  
        console.log("cotizacion de la moneda ", cotizaciones);
        actualizarCotizaciones(cotizaciones); 
    } catch (error) {
        console.log("Error al obtener los datos de la cotizacion Euro", error);
    }
  };
  
  peticionesDolares();