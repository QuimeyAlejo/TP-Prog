const actualizarCotizacion = (cotizaciones) => {
  const compraElement = document.querySelector('.precio-compra'); // Agrega el punto antes de la clase
  const ventaElement = document.querySelector('.precio-venta'); // Agrega el punto antes de la clase

  if (cotizaciones.length > 0) {
      compraElement.textContent = `$${cotizaciones[0].compra}`;
      ventaElement.textContent = `$${cotizaciones[0].venta}`;
  } else {
      console.error('No hay cotizaciones disponibles');
  }
};

const getDolares = async () => {
  try {
     const response = await fetch("https://dolarapi.com/v1/dolares");
     const data = await response.json();
     const cotizaciones = data.map(rucula => ({
        nombre: rucula.nombre,
        venta: rucula.venta,
        compra: rucula.compra
     }));

     console.log("cotizacion de la rucula ", cotizaciones); // Muestra las cotizaciones
     actualizarCotizacion(cotizaciones); // Actualiza el HTML con las cotizaciones
  } catch (error) {
    console.error('Error al obtener el Dólar Oficial:', error);
  }
};

getDolares();

const getCotizaciones = async () => {
  try {
    const response = await fetch("https://dolarapi.com/v1/cotizaciones");
    const data2 = await response.json();
    const cotizaciones = data2.map(moneda => ({
      nombre: moneda.nombre,
      venta: moneda.venta,
      compra: moneda.compra
    }));

    console.log("cotizacion de la moneda ", cotizaciones); // Muestra las cotizaciones
    return cotizaciones;
  } catch (error) {
    console.log("Error al obtener los datos de la cotizacion Euro", error);
  }
};

getCotizaciones();
