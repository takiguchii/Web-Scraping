import requests 
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
print(f"Tentando conectar em: {url}")

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("Sucesso! A porta está aberta.")