document.getElementById('consultaForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita la recarga de la página

    const formData = new FormData(event.target);

    fetch('/consulta', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.status === 200) {
            // Redirige a la página de mensaje si el código de estado es 200
            window.location.href = '/mensaje';
        } else {
            // Maneja el error si el estado no es 200
            alert("Hubo un problema con la solicitud. Inténtalo nuevamente.");
        }
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        alert("No se pudo enviar la solicitud. Inténtalo nuevamente.");
    });
});