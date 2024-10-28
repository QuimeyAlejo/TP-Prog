// tradingViewWidget.js

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    // Crear el contenedor principal del widget
    const widgetContainer = document.createElement('div');
    widgetContainer.className = 'tradingview-widget-container';

    // Crear el div para el widget
    const widgetDiv = document.createElement('div');
    widgetDiv.className = 'tradingview-widget-container__widget';
    widgetContainer.appendChild(widgetDiv);

    // Crear la sección de derechos de autor
    const copyrightDiv = document.createElement('div');
    copyrightDiv.className = 'tradingview-widget-copyright';
    copyrightDiv.innerHTML = '<a href="https://es.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Siga los mercados en TradingView</span></a>';
    widgetContainer.appendChild(copyrightDiv);

    // Agregar el contenedor del widget a un lugar específico
    document.getElementById('tradingview-widget-container').appendChild(widgetContainer); // Cambia esto si necesitas agregarlo en un lugar específico

    // Crear y agregar el script del widget
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js';
    script.async = true;

    // Configuración del widget
    const config = {
        "symbols": [
            { "description": "USDT A ARS", "proName": "BINANCE:USDTARS" },
            { "description": "USDT A BTC", "proName": "MEXC:BTCUSDT" },
            { "description": "BTC A USD", "proName": "COINBASE:BTCUSD" }
        ],
        "showSymbolLogo": true,
        "isTransparent": false,
        "displayMode": "adaptive",
        "colorTheme": "light",
        "locale": "es"
    };

    // Asignar la configuración del widget como atributo de datos
    script.setAttribute('data-config', JSON.stringify(config));

    // Agregar el script al contenedor del widget
    widgetContainer.appendChild(script);
});
