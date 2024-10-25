const getDolares = async () => {   // async devuelve automaticamente una promesa
  // no ahorramos un choclo de codigo y no usamos .then
  try { // y try catch es para manejar mas facil el tema de errores, muy grotesco decirlo como un ternario o un if
     const response = await fetch("https://dolarapi.com/v1/dolares") // await sirve para esperar que
     // la promesa se cumpla antes de seguir con el codigo, no afecta el resto del codigo solo la funcion en la que se lo llama
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


const getCotizaciones = async () => {
  try {
    const response = await fetch("https://dolarapi.com/v1/cotizaciones")
    const data2 = await response.json()
    const cotizaciones =
    data2.map(moneda => ({
      nombre:moneda.nombre,
      venta:moneda.venta,
      compra:moneda.compra
    }))
    console.log("cotizacion de la moneda ", data2)
    return cotizaciones;
  } catch (error) {
    console.log("Error al obtener los datos de la cotizacion Euro", error);
  }
}


getCotizaciones()
