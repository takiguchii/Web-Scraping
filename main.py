import requests 
import mysql.connector
from bs4 import BeautifulSoup

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '170918',
    'database': 'library_scrape'
}


url = 'http://books.toscrape.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
print(f"Tentando conectar em: {url}")

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("Saborr site acessado -> tentando conectar ao banco de dados")
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        print("Saborr -> conectado")

        soup = BeautifulSoup(resposta.text, 'html.parser')
        livros = soup.find_all('article', class_='product_pod')

        salve_livros = 0 


        for livro in livros:
            titulo = livro.find('h3').find('a')['title']
            preco = livro.find('p', class_='price_color').text
            
            img_relativa = livro.find('div', class_='image_container').find('img')['src']
            img_completa = 'http://books.toscrape.com/' + img_relativa.replace('../', '')

            sql = "INSERT INTO livros (titulo, preco, url_imagem) VALUES (%s, %s, %s)"
            valores = (titulo, preco, img_completa)
            cursor.execute(sql, valores)
            salve_livros +=1
            print(f"\n Sabor sucesso: esse foram os sabores: {salve_livros} que deram certo")
            conexao.commit()

    except mysql.Connection.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")

else:
    print("SABOR deu ruim o scraping....")