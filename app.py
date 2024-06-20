from src.print import CreatePrint
from src.getting_html import GetHTML
from src.send_email import SendEmail

def Init(url_site):

    html = GetHTML(url_site)

    CreatePrint(html)

    SendEmail("Teste - Docker with Selenium","teste@gmail.com","Teste de envio de email")

Init("https://www.google.com/")


