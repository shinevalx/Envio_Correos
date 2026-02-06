from email.message import EmailMessage

import ssl
import smtplib

correo_remitente="gilcamilo99@gmail.com"
contraseña="redacted"
correo_destino="gbricenor@ucentral.edu.co"

asunto="Presentación"
cuerpo= """
    Somos Cristian Camilo Gil Rodriguez y Dana Valentina Sanches Fandiño tenemos 20 años y nos encontramos en octavo semestre de ingeniería de sistemas
    URL Github: https://github.com/shinevalx/Envio_Correos
"""

em= EmailMessage()
em["From"] = correo_remitente
em["To"] = correo_destino
em["Subject"] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contexto) as smtp:
    smtp.login(correo_remitente,contraseña)
    smtp.sendmail(correo_remitente,correo_destino,em.as_string())
