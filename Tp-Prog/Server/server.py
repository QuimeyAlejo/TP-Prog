
from flask import Flask, jsonify,request,render_template
from flask_cors import CORS 
import requests

app = Flask(__name__ ,template_folder="../Client/templates") #esta  linea sirve para crear una app de flask e indicar __name__ a flask donde se encuenta el archivo principal de nuestro sv corte un main
CORS(app) #cors nos permite que nuestra app o rutas de flask puedan realizar solicitudes y recibirlas
@app.route('/dolar', methods=['GET'])
def get_api_data():  
    api_url = "https://dolarapi.com/v1/dolares"  
    response = requests.get(api_url)   
    print("GET DOLARES")  
    if response.status_code == 200: #el cod 200 es cuando todo esta OK 
        data = response.json()
        info_moneda = [];
        
        for i in data:
            info_moneda.append({
                'casa': i['casa'],
                'compra': i['compra'],
                'venta': i['venta'],
                'nombre': i['nombre'],
                'moneda': i['moneda'],
                'fechaActualizacion': i['fechaActualizacion']
                
            })
        return jsonify(info_moneda)
    else:
        return jsonify({'error': 'Paren la rotativa, hay un error...'}), response.status_code


@app.route('/', methods=['GET'])
def get_cotizaciones():  
    api_url = "https://dolarapi.com/v1/cotizaciones"  
    response = requests.get(api_url) 
    print("GET COTIZACIONES")    
    if response.status_code == 200: #el cod 200 es cuando todo esta OK 
        data = response.json()
        info_moneda = [];
        
        for i in data:
            info_moneda.append({
                'casa': i['casa'],
                'compra': i['compra'],
                'venta': i['venta'],
                'nombre': i['nombre'],
                'moneda': i['moneda'],
                'fechaActualizacion': i['fechaActualizacion']
                
            })
        return jsonify(info_moneda)
    else:
        return jsonify({'error': 'Paren la rotativa, hay un error...'}), response.status_code

@app.route('/historico', methods=['GET'])
def get_historico_data():  
    api_url = "https://api.argentinadatos.com/v1/cotizaciones/dolares/"  
    response = requests.get(api_url)   
    print("GET HISTORICO")  
    if response.status_code == 200: #el cod 200 es cuando todo esta OK 
        data = response.json()
        info_moneda = [];
        
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
    
@app.route('/consulta', methods=["GET", "POST"])
def email():
    if request.method == "POST":
        print("POST")
        return jsonify({"message": "POST request received"})
    else:
        return render_template("contactoprueba.html")

if __name__ == '__main__': #la aplicacion se ejecute solo cuando el archivo se ejecuta directamente, no cuando se importa.
    app.run(debug=True) # el modo debug en true sirve para que flask te tire los errores detallados si salta algo mal y vuelve a cargar cuando hay cambios en el codigo


           