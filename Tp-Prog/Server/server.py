
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/dolar', methods=['GET'])
def get_api_data():  
    api_url = "https://dolarapi.com/v1/dolares"  
    response = requests.get(api_url)   
    print(response.json(), "Que traigo")  
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'No se pudo encontrar algo...'}), response.status_code


@app.route('/cotizaciones', methods=['GET'])
def get_api_cotizaciones():
    api_url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(api_url)
    print(response.json(),"cotizaciones")  
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'No se pudo encontrar algo...'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)


           