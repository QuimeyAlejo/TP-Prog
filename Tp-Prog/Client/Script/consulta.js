document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("consultaForm");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();  // Evita la recarga de la página

        const nombre = document.getElementById("nombre").value;
        console.log(nombre)
        const email = document.getElementById("correo").value;
        console.log(email)
        const consulta = document.getElementById("consulta").value;
        console.log(consulta)
        await getConsulta(nombre, email, consulta); // Llama a la función para manejar el envío
    });
});

const getConsulta = async (nombre, email, consulta) => {
    try {
        const queryParams = new URLSearchParams({ nombre, email, consulta }).toString();
        const response = await fetch(`http://127.0.0.1:5000/consulta?${queryParams}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message);
            alert("Consulta procesada exitosamente.");
            window.location.href = "postMensaje.html"; // Redirige después del éxito
        } else {
            const errorData = await response.json();
            console.error("Error en la consulta:", errorData.error);
            alert("Hubo un problema: " + errorData.error);
        }
    } catch (error) {
        console.error("Error al realizar la consulta:", error);
        alert("Error al realizar la consulta.");
    }
};


