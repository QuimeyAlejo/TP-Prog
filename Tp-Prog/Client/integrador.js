

const getDolares = async () => {
  try {
     const response = await fetch("https://dolarapi.com/v1/dolares")
     const data = await response.json()
     const cotizaciones =
      data.map( rucula => ({
        nombre: rucula.nombre,
        venta: rucula.venta,
        compra: rucula.compra
      })) 
     console.log("cotizacion de la rucula ", data)
       return cotizaciones;
  } catch (error) {
    console.error('Error al obtener el Dólar Oficial:', error);
  }
 }

 getDolares()




