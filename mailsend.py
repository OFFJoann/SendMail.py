import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

smtp_server = 'smtp.mail.com'
smtp_port = 587  
smtp_username = 'your@mail.com'
smtp_password = 'password'

dia_semana_actual = datetime.datetime.now().weekday()

if dia_semana_actual == 0: 
    destinatario = 'mail'
    copia = 'mailcopy'
    subject = 'ENCABEZADO'
    carpeta = 'CONCATENAR'
elif dia_semana_actual == 1: 
    destinatario = 'mail'
    copia = 'mailcopy'
    subject = 'ENCABEZADO'
    carpeta = 'CONCATENAR'
elif dia_semana_actual == 2: 
    destinatario = 'mail'
    copia = 'mailcopy'
    subject = 'ENCABEZADO'
    carpeta = 'CONCATENAR'
elif dia_semana_actual == 3:
    destinatario = 'mail'
    copia = 'mailcopy'
    subject = 'ENCABEZADO'
    carpeta = 'CONCATENAR'
elif dia_semana_actual == 4:
    destinatario = 'mail'
    copia = 'mailcopy'
    subject = 'ENCABEZADO'
    carpeta = 'CONCATENAR'

msg = MIMEMultipart()
msg['From'] = 'your@mail.com.co'
msg['To'] = destinatario
msg['Subject'] = subject
msg['CC'] = copia


body = """
cuerpo del correo
""".format(carpeta)
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() 
server.login(smtp_username, smtp_password)

server.send_message(msg)

server.quit()