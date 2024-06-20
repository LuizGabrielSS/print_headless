import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from private.data import email

def SendEmail(Titulo,Email_To,mensagem):

    smtp = 'smtp.gmail.com'
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email['user'], email['password'])

    message = MIMEMultipart()
    message["From"] = Titulo

    message["To"] = Email_To
    message["Cc"] = Email_To
    message["Subject"] = Titulo

    filename = "teste.jpg"

    attachment = open(filename,'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    message.attach(part)

    attachment.close()

    message.attach(MIMEText(mensagem, 'html'))

    server.sendmail(email['user'],Email_To,message.as_string())

    server.quit()