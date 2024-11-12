const form = document.getElementById('precio-historico'); //obtenemos los datos
const resultadoDiv = document.querySelector('.carta-container-historico');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const fecha = document.getElementById('fecha').value;
    const dolarTipo = document.getElementById('dolar').value;
 /*  */
    if (!fecha || !dolarTipo) {
        resultadoDiv.innerHTML = '<p>Por favor, complete todos los campos.</p>';
        return;
    }

    // aca modifico la fecha porque lo tiraba con - y no con / a lo que me daba error al momento
    // de tirar el get
    const fechaFormateada = fecha.replace(/-/g, '/');

    let url = `https://api.argentinadatos.com/v1/cotizaciones/dolares/${dolarTipo}/${fechaFormateada}`;
    console.log('URL:', url); // Verifica la URL

    try {
        //const response = await fetch("http://127.0.0.1:5000/historico"); 
        const response = await fetch(url);
        if (!response.ok) throw new Error(console.log("error"));
        
        const data = await response.json();
        console.log(data);
        
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
        resultadoDiv.innerHTML = `<div class="error">Error en la solicitud. Seleccione fecha correcta (03/01/2011-Actualidad)</div>`;
    }
});
