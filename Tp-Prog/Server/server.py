from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from clases2 import Tipo, Cotizacion, Moneda,crear_instancias_dolar_desde_api,crear_instancias_cotizaciones_desde_api

app = Flask(__name__, template_folder="../Client/templates")  # Esta línea sirve para crear una app de Flask e indicar __name__ a Flask donde se encuentra el archivo principal de nuestro server
CORS(app)  # CORS nos permite que nuestra app o rutas de Flask puedan realizar solicitudes y recibirlas

# RUTAS
@app.route('/dolar', methods=['GET'])
def obtener_dolar():
    monedas = crear_instancias_dolar_desde_api()
    resultado = []
    for nombre_moneda, moneda in monedas.items():
        for tipo in moneda.tipo_casas:
            for cotizacion in tipo.mostrar_cotizaciones():
                resultado.append({
                    "moneda": moneda.mostrar_nombre(),
                    "tipo": tipo.mostrar_nombre_tipo(),
                    "compra": cotizacion.mostrar_compra(),
                    "venta": cotizacion.mostrar_venta(),
                    "fecha_actualizacion": cotizacion.mostrar_actualizacion().isoformat()
                })
    
    return jsonify(resultado)


@app.route('/', methods=['GET'])
def obtener_cotizaciones():
    monedas = crear_instancias_cotizaciones_desde_api()
    resultado = []
    for nombre_moneda, moneda in monedas.items():
        for tipo in moneda.tipo_casas:
            for cotizacion in tipo.mostrar_cotizaciones():
                resultado.append({
                    "moneda": moneda.mostrar_nombre(),
                    "tipo": tipo.mostrar_nombre_tipo(),
                    "compra": cotizacion.mostrar_compra(),
                    "venta": cotizacion.mostrar_venta(),
                    "fecha_actualizacion": cotizacion.mostrar_actualizacion().isoformat()
                })
    
    return jsonify(resultado)

# Historico
@app.route('/historico', methods=['GET'])
def get_historico_data():  
    api_url = "https://api.argentinadatos.com/v1/cotizaciones/dolares/"  
    response = requests.get(api_url)   
    print("GET HISTORICO")  # Esta línea imprime para depurar
    if response.status_code == 200:  # El código 200 es cuando todo está OK
        data = response.json()
        info_moneda = []
        for i in data:
            info_moneda.append({
                'casa': i['casa'],
                'compra': i['compra'],
                'venta': i['venta'],
                'fecha': i['fecha']
            })
        return jsonify(info_moneda)
    else:
        return jsonify({'error': 'Paren la rotativa, hay un error...'}), response.status_code


def enviar_correo(destinatario, asunto, cuerpo_html):
    remitente = "tpintegrador58@gmail.com"  
    contraseña = "mlam rbgr yhlb rczi"  
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo_html, 'html'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, msg.as_string())
        servidor.quit()
        print("Correo enviado con éxito pa")  
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


@app.route('/consulta', methods=["GET", "POST"])
def procesar_consulta():
    if request.method == "GET":
        return render_template("contacto.html")

    email = request.json.get("email")
    consulta = request.json.get("consulta")
    nombre = request.json.get("nombre")

    if not email or not consulta or not nombre:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    # antes haciamos  si el valor era dolar apunte a la api dolar si no era cotizacion, ahora
    # lo que hacemos es invocar al metodo correspondiende te las clases
    consultas_disponibles = {
        "dolar": crear_instancias_dolar_desde_api,
        "cotizaciones": crear_instancias_cotizaciones_desde_api
    }

    if consulta not in consultas_disponibles:
        return jsonify({"error": "Consulta no válida"}), 400

    try:
       
        monedas = consultas_disponibles[consulta]()
        
        cuerpo_html = f"<h1>Resultados de la consulta: {consulta}</h1><ul>"

        # Recorriendo las monedas, tipos y cotizaciones
        for moneda in monedas.values():
            for tipo in moneda.tipo_casas:
                for cotizacion in tipo.mostrar_cotizaciones():
                    # armamos el cuerpo html para ser enviado por correo
                    cuerpo_html += f"""
                    <li>
                        <strong>Moneda:</strong> {moneda.mostrar_nombre()}<br>
                        <strong>Tipo:</strong> {tipo.mostrar_nombre_tipo()}<br>
                        <strong>Compra:</strong> {cotizacion.mostrar_compra()}<br>
                        <strong>Venta:</strong> {cotizacion.mostrar_venta()}<br>
                        <strong>Fecha de Actualización:</strong> {cotizacion.mostrar_actualizacion().isoformat()}<br>
                    </li>
                    """
        cuerpo_html += "</ul>"

        # Enviar el correo con los resultados
        enviar_correo(email, f"Hola {nombre}. Resultados de {consulta}", cuerpo_html)
        return jsonify({"message": "Consulta procesada exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
