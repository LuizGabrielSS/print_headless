from html2image import Html2Image

def CreatePrint(html):

    hti = Html2Image()

    hti.screenshot(
        size=(1109, 696),
        html_str=html, 
        save_as="teste.jpg"
    )

    pass