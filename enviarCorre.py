#davidcanojuanesteban92@gmail.com
#paugallego92@hotmail.com
import smtplib #Este módulo permite interactuar con servidores SMTP (Simple Mail Transfer Protocol), que son los responsables de enviar correos electrónicos.
from email.mime.multipart import MIMEMultipart #Permite crear un correo en formato MIME (Multipurpose Internet Mail Extensions
from email.mime.text import MIMEText #Se utiliza para crear el contenido del correo en formato de texto plano o HTML.

your_email = 'davidcanojuanesteban92@gmail.com'
your_password = 'aykn gwnq gpax ohye'

recipent = 'paugallego92@hotmail.com' #donde vamos a enviar el correo

message = MIMEMultipart()
message['From'] = your_email
message['to'] = recipent
message['subject'] = 'Emial  of test'

body = ' Este es un mensaje de prueba creado enviado con ptyon ' 
message.attach(MIMEText(body,'plain')) #es una forma de incluir texto simple como cuerpo del correo.

smtp_server = smtplib.SMTP('smtp.gmail.com', 587) # llamar al servidor de gmial
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email,recipent,message.as_string()) #se utiliza para enviar un correo electrónico a través de un servidor SMTP
smtp_server.quit()
print('Email enviado')