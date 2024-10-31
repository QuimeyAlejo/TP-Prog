function obtenerDatos() {
  let casaElegida = document.querySelector('#casaElegida').value; // Suponiendo que hay un select con casas
  let fechaElegida = document.querySelector('#fechaElegida').value; // Suponiendo que hay un input para la fecha

  fetch('https://api.argentinadatos.com/v1/cotizaciones/dolares/') // Reemplaza con tu URL real
      .then(response => response.json())
      .then(data => {
          // Filtra los datos para encontrar el objeto que coincida con la casa y la fecha elegidas
          let resultado = data.find(entry => entry.casa === casaElegida && entry.fecha === fechaElegida);

          if (resultado) {
              mostrarResultado(casaElegida, fechaElegida, resultado.compra, resultado.venta);
          } else {
              console.error("No se encontraron datos para la casa y fecha seleccionadas.");
          }
      })
      .catch(error => console.error('Error en la solicitud:', error));
}

function mostrarResultado(casa, fecha, compra, venta) {
  const resultadoDiv = document.getElementById('resultado');

  // Muestra el resultado
  resultadoDiv.innerHTML = `
      <h2>Resultados para ${casa} el ${fecha}:</h2>
      <p>Compra: ${compra}</p>
      <p>Venta: ${venta}</p>
  `;
}

// Llama a la función al hacer clic en un botón, por ejemplo
document.getElementById('buscarButton').addEventListener('click', obtenerDatos);