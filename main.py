import requests

url = 'http://quotes.toscrape.com'

print(f"Tentando conectar em: {url}")

resposta = requests.get(url)

print(f"O código da resposta foi: {resposta.status_code}")

if resposta.status_code == 200:
    print("Sucesso! A porta está aberta.")
else:
    print("Erro! Algo deu errado.")