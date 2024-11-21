document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("consultaForm");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();  // Evita la recarga de la página

        const nombre = document.getElementById("nombre").value;
        console.log(nombre)
        const email = document.getElementById("correo").value;
        console.log(email)
        await getConsulta(nombre, email); // Llama a la función para manejar el envío
    });
});

const getConsulta = async (nombre, email) => {
    if (!nombre || !email) {
        alert("Por favor, completa todos los campos.");
        return;
    }

    if (!/\S+@\S+\.\S+/.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }

    try {
        
        //const response = await fetch("http://127.0.0.1:5000/procesar", {
        const response = await fetch("https://tp-prog.onrender.com/procesar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ nombre, correo: email }), // Envío de datos al servidor
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Respuesta del servidor:", data);
            alert("Consulta procesada exitosamente.");
            window.location.href = "postMensaje.html"; // Redirige después del éxito
        } else {
            const errorData = await response.json();
            console.error("Error en la consulta:", errorData.error);
            alert("Hubo un problema: " + errorData.error);
        }
    } catch (error) {
        console.error("Error al realizar la consulta:", error);
        alert("Error al realizar la consulta. Verifica tu conexión.");
    }
};


