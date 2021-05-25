import requests
from bs4 import BeautifulSoup

##Definindo meu user-agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
r = requests.get("https://www.nike.com.br/Snkrs/", headers=headers)

html = r.text ##Convertendo o html para string (Para conseguir manusear)
soup = BeautifulSoup(html, "html.parser") ##Definindo o objeto html

nome_produto = soup.find_all("h2", class_ = "produto__detalhe-titulo") ##Procurando o nome do produto
link = soup.find_all("a", class_ = "btn") ##Procurando o link do produto

for i in range(0, (len(nome_produto))): ##Fazendo um loop com base na quantidade de produtos
	r = requests.get(link[i]["href"], headers=headers) ##Fazendo uma requisição para entrar nos links de cada produto

	html2 = r.text ##Convertendo o html da nova requisição para string
	soup2 = BeautifulSoup(html2, "html.parser") ##Definindo o objeto html da nova requisição
	price = soup2.find_all("span", class_ = "js-valor-por") ##Procurando o preço de cada produto 

	##Filtrando as informações antes de adicionar na lista
	if price != []:
		##Printando as informações
	            print("\n", nome_produto[i].getText(), "\nLink: ", link[i]["href"], "\nPreço: ", price[0].getText())

	else:
		del(price)


print("Produtos em estoque: ", (len(nome_produto)))

