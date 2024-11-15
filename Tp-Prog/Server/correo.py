import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

REMITENTE = os.getenv("EMAIL_USER")
CONTRASEÑA = os.getenv("EMAIL_PASSWORD")

def enviar_correo(destinatario, asunto, cuerpo_html):
    msg = MIMEMultipart()
    msg['From'] = REMITENTE
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo_html, 'html'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(REMITENTE, CONTRASEÑA)
        servidor.sendmail(REMITENTE, destinatario, msg.as_string())
        servidor.quit()
        print("Correo enviado con éxito pa")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")