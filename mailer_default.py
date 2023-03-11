import os
from email.message import EmailMessage
import ssl
import smtplib



email_emisor = 'email_emisor@dominio.com'
#email_contraseña = os.environ.get('EMAIL_PASWORD')
email_contraseña = 'contraseña_email_emisor' #Ingresar contraseña del email emisor

email_receptor = ['email_receptor1@dominio.com', 'email_receptor2@dominio.com'] #Ingresar los emails receptores que necesita

asunto = 'Test Automatización Mailer'
cuerpo = """
Este es un mensaje de prueba del mailer. 
El envío de este correo es automático, por favor no lo responda.
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)


contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contraseña)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())