import bs4,requests

#Extraer titulo de la pagina
#https://escueladirecta-blog.blogspot.com/

resultado=requests.get('https://escueladirecta-blog.blogspot.com/')

sopa=bs4.BeautifulSoup(resultado.text,'lxml')
print(sopa.select('title')[0].getText())

parrafo_especial=sopa.select('h2')[0].getText()
print(parrafo_especial)