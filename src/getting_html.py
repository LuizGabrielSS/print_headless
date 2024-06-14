from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def GetHTML(url):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox') 

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    html = driver.page_source

    driver.quit()

    return html