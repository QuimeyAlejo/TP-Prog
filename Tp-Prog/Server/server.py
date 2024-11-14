from flask import Flask, jsonify,request,render_template,redirect, url_for
from flask_cors import CORS 
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    
def enviar_correo(destinatario, asunto, cuerpo_html):
    remitente = "tpintegrador58@gmail.com"  
    contraseña = "mlam rbgr yhlb rczi"  #despues tengo que agregar en una variable de entorno estos datos que son sensibles

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    
    msg.attach(MIMEText(cuerpo_html, 'html'))

    # aca se loguea y envia el sv y por ultimo el quit es para parar el proceso despues de enviar el correo
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, msg.as_string())
        servidor.quit()
        print("Correo enviado con exito pa")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    
@app.route('/consulta', methods=["GET", "POST"])
def procesar_consulta():
    if request.method == "GET":
        # Renderiza la plantilla cuando se accede con GET
        return render_template("contacto.html")
    email = request.form.get("email")
    consulta = request.form.get("consulta")
    nombre = request.form.get("nombre")

    print(f"Email recibido: {email}")
    print(f"Consulta recibida: {consulta}")
    print(f"Consulta recibida: {nombre}")
    
    if consulta == "dolar":
        api_url = "https://dolarapi.com/v1/dolares"
    elif consulta == "cotizaciones":
        api_url = "https://dolarapi.com/v1/cotizaciones"
    else:
        return jsonify({"error": "Consulta no valida"}), 400

    
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()

        # pasamos los datos al formato HTML para mandar el msj
        cuerpo_html = f"<h1>Resultados de la consulta: {consulta}</h1><ul>"
        for item in data:
            cuerpo_html += f"<li><strong>Casa:</strong> {item['casa']}, <strong>Compra:</strong> {item['compra']}, <strong>Venta:</strong> {item['venta']}</li>"
        cuerpo_html += "</ul>"

        # Enviar el correo con los datos de la consulta
        enviar_correo(email, f"Hola {nombre}.Resultados de {consulta}", cuerpo_html)
        return jsonify({"message": "Correo enviado con los resultados"}), 200
        #return render_template("index.html")
        #return redirect(url_for('procesar_consulta'))

    else:
        return jsonify({"error": "Error al obtener datos de la API"}), 500

@app.route('/mensaje' , methods=['get'])
def post_msj():
    return render_template('postMensaje.html') 

if __name__ == '__main__': #la aplicacion se ejecute solo cuando el archivo se ejecuta directamente, no cuando se importa.
    app.run(debug=True) # el modo debug en true sirve para que flask te tire los errores detallados si salta algo mal y vuelve a cargar cuando hay cambios en el codigo


           