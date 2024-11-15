from flask import Flask, jsonify, request, json
import requests
from clases import Tipo, Cotizacion
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__) 
CORS(app) 

# trae las cotizaciones generales
@app.route('/', methods=['GET'])
def get_info_cotizaciones(): 
    url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(url)   
    print(response.json(), "Datos recibidos de la API")  
    if response.status_code == 200: # OK 
        data = response.json()
        info_moneda = []
        
        for item in data:
                monedas = Cotizacion(
                    nombre_moneda=item.get('moneda'),
                    nombre=item.get('nombre'),
                    compra=item.get('compra'),
                    venta=item.get('venta'),
                    fecha=item.get('fechaActualizacion')
                )

                info_moneda.append({
                    'moneda': monedas.mostrar_moneda(),
                    'nombre': monedas.mostrar_nombre(),
                    'compra': monedas.mostrar_compra(),
                    'venta': monedas.mostrar_venta(),
                    'fecha': monedas.mostrar_fecha()
                })
        return jsonify(info_moneda), 200
    else:
            return jsonify({'error': 'No se pudieron obtener las cotizaciones'}), 500

# trae las cotizaciones del dolar
@app.route('/dolares', methods=['GET'])
def get_info_dolares(): 
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url)   
    print(response.json(), "Datos recibidos de la API")  
    if response.status_code == 200: # OK 
        data = response.json()
        info_moneda = []
        
        for item in data:
                monedas = Cotizacion(
                    nombre_moneda=item.get('moneda'),
                    nombre=item.get('nombre'),
                    compra=item.get('compra'),
                    venta=item.get('venta'),
                    fecha=item.get('fechaActualizacion')
                )

                info_moneda.append({
                    'moneda': monedas.mostrar_moneda(),
                    'nombre': monedas.mostrar_nombre(),
                    'compra': monedas.mostrar_compra(),
                    'venta': monedas.mostrar_venta(),
                    'fecha': monedas.mostrar_fecha()
                })
        return jsonify(info_moneda), 200
    else:
            return jsonify({'error': 'No se pudieron obtener las cotizaciones'}), 500



# Ruta para obtener cotizaciones
@app.route('/consulta', methods=['GET', 'POST'])
def consulta(): 
    url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info_moneda = []
        
        for i in data:
            fecha_actualizacion = i.get('fechaActualizacion')
            try:
                fecha_dt = datetime.strptime(fecha_actualizacion, "%Y-%m-%dT%H:%M:%S.%fZ")
            except ValueError:
                fecha_dt = datetime.strptime(fecha_actualizacion, "%Y-%m-%dT%H:%M:%SZ")
            
            fechaFormateada = fecha_dt.strftime('%d-%m-%Y %H:%M')
            
            info_moneda.append({
                'casa': i['casa'],
                'compra': i['compra'],
                'venta': i['venta'],
                'nombre': i['nombre'],
                'moneda': i['moneda'],
                'fechaActualizacion': fechaFormateada              
            })

        return jsonify(info_moneda), 200
    else:
        return jsonify({'error': 'No es posible cargar la info'}), response.status_code

# Función para enviar correos
def enviar_correo(nombre, correo, body_content):
    data = {
        'service_id': 'infodolar',
        'template_id': 'cotizaciones',
        'user_id': 'xLpu-WbDZiqP-AuSj',
        'accessToken': 'esPrth6Ahmt2NpKLUPo8O',
        'template_params': {
            'user_email': correo,
            'from_name': 'InfoDolar',
            'user_name': nombre,
            'message': body_content
        }
    }
    print(data, 'esto es dataaaaaaa')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.emailjs.com/api/v1.0/email/send',
        data=json.dumps(data),
        headers=headers
    )
    response.raise_for_status()

# Ruta para procesar solicitudes
@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    asunto = request.form.get('consulta')
    
    if not nombre or not correo:
        return jsonify({'error': "Completá bien los datos"}), 400
    
    if asunto == 'dolar':
        body_content = "Contenido relacionado con el dólar"  # Define esta lógica
    else:
        consulta_response = consulta()
        body_content = consulta_response.get_json()

    try:
        enviar_correo(nombre, correo, body_content)
        return f'Mensaje enviado correctamente a {correo}', 200
    except requests.exceptions.RequestException as error:
        return jsonify({'error': f'No se pudo enviar el correo: {error}'}), 500

    
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)