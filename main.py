import requests 
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
print(f"Tentando conectar em: {url}")

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("Saborr porta está aberta.")
    soup = BeautifulSoup(resposta.text, 'html.parser')
    livros = soup.find_all('article', class_='product_pod')

    for livro in livros:
        tag_titulo = livro.find('h3').find('a')
        titulo = tag_titulo['title']
        print(f"Saborr titulo do livro:{titulo}")

        tag_preco = livro.find('p', class_='price_color') # Pegando preço no elemento html
        preco = tag_preco.text
        print(f"Saborr preço do livro: {preco}")

else:
    print("SABOR deu ruim o scraping....")