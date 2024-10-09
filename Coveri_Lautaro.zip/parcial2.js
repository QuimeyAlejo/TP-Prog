const tablero = document.querySelector('.board');
const mensajeDiv = document.getElementById('mensaje');
let jugadorActual = 'jugador1'; 
let estadoTablero = ['', '', '', '', '', '', '', '', ''];
const color1 = 'red';
const color2 = 'blue';

tablero.addEventListener('click', manejarClicCelda);

function manejarClicCelda(event) {
    const celda = event.target;
    const index = celda.getAttribute('data-index');

    if (estadoTablero[index] !== '') return;

    estadoTablero[index] = jugadorActual;
    celda.style.backgroundColor = jugadorActual === 'jugador1' ? color1 : color2;

    if (verificarGanador()) {
        mostrarMensaje(`${jugadorActual === 'jugador1' ? 'Jugador 1' : 'Jugador 2'} gana!`);
        tablero.removeEventListener('click', manejarClicCelda);
    } else if (estadoTablero.every(celda => celda !== '')) {
        mostrarMensaje('Empate!');
    } else {
        jugadorActual = jugadorActual === 'jugador1' ? 'jugador2' : 'jugador1'; 
    }
}

function verificarGanador() {
    const combinacionesGanadoras = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    return combinacionesGanadoras.some(combinacion => {
        const [a, b, c] = combinacion;
        return estadoTablero[a] === jugadorActual && estadoTablero[b] === jugadorActual && estadoTablero[c] === jugadorActual;
    });
}

function mostrarMensaje(mensaje) {
    mensajeDiv.textContent = mensaje;
    mensajeDiv.style.display = 'block'; 

    setTimeout(() => {
        mensajeDiv.style.display = 'none'; 
    }, 5000);
}

// Reiniciar juego
const restartBtn = document.querySelector('.restart-btn');
restartBtn.addEventListener('click', reiniciarJuego);

function reiniciarJuego() {
    estadoTablero.fill('');
    Array.from(tablero.children).forEach(celda => {
        celda.style.backgroundColor = '#fff'; 
    });
    jugadorActual = 'jugador1'; 
    mensajeDiv.style.display = 'none'; 
    tablero.addEventListener('click', manejarClicCelda); 
}
