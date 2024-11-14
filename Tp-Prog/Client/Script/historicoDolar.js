const form = document.getElementById('precio-historico'); //obtenemos los datos
const resultadoDiv = document.querySelector('.carta-container-historico'); // busca el elemento que contiene para mas tarde manipularlo

form.addEventListener('submit', async function(event) { // clickea 'submit' y ocurre un evento por default
    event.preventDefault();

    const fecha = document.getElementById('fecha').value;
    const dolarTipo = document.getElementById('dolar').value;

    // aca modifico la fecha porque lo tiraba con - y no con / a lo que me daba error al momento
    // de tirar el get
    const fechaFormateada = fecha.replace(/-/g, '/');

    let url = `https://api.argentinadatos.com/v1/cotizaciones/dolares/${dolarTipo}/${fechaFormateada}`;
    console.log('URL:', url); // Verifica la URL si contiene las variables

    try {
        const response = await fetch(url); // solicitud HTTP a la URL 
        if (!response.ok) {
            resultadoDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        }
            
            
/*             throw new Error('Error en la solicitud: ' + response.statusText); //estado 400-404-500
 */
        const data = await response.json(); // lo parsea a objeto
        resultadoDiv.innerHTML = `
            <div class="carta">
                <h2>Dolar ${dolarTipo.toUpperCase()} - ${fechaFormateada}</h2>
                <hr/>
                <p>Precio Compra: ${data.compra ?? 'N/A'}</p>
                <p>Precio Venta: ${data.venta ?? 'N/A'}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        resultadoDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
