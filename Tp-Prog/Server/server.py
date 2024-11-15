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

