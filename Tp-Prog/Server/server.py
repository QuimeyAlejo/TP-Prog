from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
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

# Función para enviar correos electrónicos con los resultados de la consulta
def enviar_correo(destinatario, asunto, cuerpo_html):
    remitente = "tpintegrador58@gmail.com"  
    contraseña = "mlam rbgr yhlb rczi"  # Después tengo que agregar en una variable de entorno estos datos que son sensibles
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
        print("Correo enviado con éxito pa")  # Esta línea imprime para depurar
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Ruta para procesar las consultas y enviar un correo con los resultados
@app.route('/consulta', methods=["GET", "POST"])
def procesar_consulta():
    if request.method == "GET":
        return render_template("contacto.html")  # Muestra el formulario para hacer la consulta

    # Procesa la consulta recibida por POST
    email = request.json.get("email")
    consulta = request.json.get("consulta")
    nombre = request.json.get("nombre")

    # Verifica que todos los campos estén completos
    if not email or not consulta or not nombre:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    print(f"Email recibido: {email}")
    print(f"Consulta recibida: {consulta}")
    print(f"Nombre recibido: {nombre}")

    try:
        # Dependiendo de la consulta, obtiene los datos
        if consulta == "dolar":
            datos = Dolar.obtener_datos()
        elif consulta == "cotizaciones":
            datos = Cotizacion.obtener_datos()
        else:
            return jsonify({"error": "Consulta no válida"}), 400

        # Prepara el cuerpo del correo en formato HTML
        cuerpo_html = f"<h1>Resultados de la consulta: {consulta}</h1><ul>"
        for item in datos:
            info = item.mostrar_info()
            cuerpo_html += f"<li><strong>Casa:</strong> {info['casa']}, <strong>Compra:</strong> {info['compra']}, <strong>Venta:</strong> {info['venta']}</li>"
        cuerpo_html += "</ul>"

        # Envía el correo con los resultados
        enviar_correo(email, f"Hola {nombre}. Resultados de {consulta}", cuerpo_html)
        return jsonify({"message": "Consulta procesada exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
