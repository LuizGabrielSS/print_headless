from src.print import CreatePrint
from src.getting_html import GetHTML

def Init(url_site):

    html = GetHTML(url_site)

    CreatePrint(html)

    pass

Init("https://www.google.com/")
