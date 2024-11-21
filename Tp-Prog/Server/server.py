from flask import Flask, jsonify, request, json
import requests
from clases import Tipo, Cotizacion
from datetime import datetime
from flask_cors import CORS
import os 
app = Flask(__name__) 
#CORS(app, origins=["https://tp-prog-c73rixcex-quimeyalejos-projects.vercel.app"]) 
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)



# Get cotizaciones generales
@app.route('/', methods=['GET'])
def get_info_cotizaciones(): 
    url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(url)   
 #   print(response.json(), "Datos recibidos de la API")  
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

# Get cotizaciones dolar
@app.route('/dolares', methods=['GET'])
def get_info_dolares(): 
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url)   
  #  print(response.json(), "Datos recibidos de la API")  
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



# Get cotizaciones dolar y estructura del mail
@app.route('/emailDolares', methods=['GET'])
def print_info_dolares(): 
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url)   
   # print(response.json(), "Datos recibidos de la API")  
    if response.status_code == 200: # OK 
        data = response.json()
        info_moneda = []
        
        for i in data:
            fecha_actualizacion = i.get('fechaActualizacion')
            if fecha_actualizacion:
                fecha_dt = datetime.strptime(fecha_actualizacion, "%Y-%m-%dT%H:%M:%S.%fZ")
                fecha_formateada = fecha_dt.strftime('%d-%m-%Y %H:%M') # formato fecha
            else:
                fecha_formateada = "Fecha no disponible"
            
            info_moneda.append({
                'casa': i['casa'],
                'compra': i['compra'],
                'venta': i['venta'],
                'nombre': i['nombre'],
                'moneda': i['moneda'],
                'fechaActualizacion': fecha_formateada               
            })
        email_body = "COTIZACIONES DOLARES\n\n"
        for item in info_moneda:
            email_body += f"{item['moneda']}\n"
            email_body += f"{item['nombre']}\n"
            email_body += f"Compra: {item['compra']}\n"
            email_body += f"Venta: {item['venta']}\n"
            email_body += f"Fecha de Actualización: {item['fechaActualizacion']}\n"
            email_body += "*" * 30 + "\n"  # Separador entre cada casa de cambio
        
        return email_body
    else:
        return jsonify({'error': 'No es posible cargar la info'}), response.status_code

# Get cotizaciones generales y estructura del mail
@app.route('/emailCotizaciones', methods=['GET'])
def print_info_general(): 
    url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(url)   
   # print(response.json(), "Datos recibidos de la API")  
    if response.status_code == 200: # OK 
        data = response.json()
        info_moneda = []
        
        for i in data:
            if i.get('moneda') == 'USD':
                continue
            fecha_actualizacion = i.get('fechaActualizacion')
            if fecha_actualizacion:
                fecha_dt = datetime.strptime(fecha_actualizacion, "%Y-%m-%dT%H:%M:%S.%fZ")
                fecha_formateada = fecha_dt.strftime('%d-%m-%Y %H:%M')
            else:
                fecha_formateada = "Fecha no disponible"
            
            compra = round(i['compra'], 2)
            venta = round(i['venta'], 2)

            info_moneda.append({
                'casa': i['casa'],
                'compra': compra,
                'venta': venta,
                'nombre': i['nombre'],
                'moneda': i['moneda'],
                'fechaActualizacion': fecha_formateada              
            })
        email_body = "\n\nCOTIZACIONES EXTRA\n\n"
        for item in info_moneda:
            email_body += f"{item['moneda']}\n"
            email_body += f"{item['nombre']}\n"
            email_body += f"Compra: {(item['compra'])}\n"
            email_body += f"Venta: {item['venta']}\n"
            email_body += f"Fecha de Actualización: {item['fechaActualizacion']}\n"
            email_body += "*" * 30 + "\n"  # Separador entre cada casa de cambio
        
        return email_body
    else:
        return jsonify({'error': 'No es posible cargar la info'}), response.status_code

body_content_dolares = print_info_dolares()
body_content_general = print_info_general()
body_content = body_content_dolares + body_content_general # contenido final para el mail
print(body_content)

# envio mail
@app.route('/procesar', methods=['POST'])
def procesar():
    #print(request.json)
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    if nombre and correo:
    #    print(f"Nombre: {nombre}")
     #   print(f"Correo: {correo}")
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
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Origin': 'http://127.0.0.1:5000/',  
            'Referer': 'http://127.0.0.1:5000/'
        }

        try:
            response = requests.post(
                'https://api.emailjs.com/api/v1.0/email/send',
                data=json.dumps(data),
                headers=headers
            )
            response.raise_for_status()
            print('La cotización fue enviada correctamente!')
        except requests.exceptions.RequestException as error:
            print(f'Oops... {error}')
            if error.response is not None:
                print(error.response.text)
    
        return jsonify({'message': f'Mensaje enviado correctamente a {correo}'}), 200   
    else:
        return jsonify({'error': "Datos incorrectos, verifique por favor"}), 405
    
       
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port, debug=True)