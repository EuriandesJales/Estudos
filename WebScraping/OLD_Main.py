import requests
from bs4 import BeautifulSoup

Diolinux = requests.get("https://diolinux.com.br/") #Obj Diolinux == return get web site
Site = BeautifulSoup(Diolinux.content, "html.parser")


def PegarNoticias(Site, Diolinux):
    
    Status = Diolinux.status_code # return da requisição
    #ConteudoDaPagina = Diolinux.content# Retorna todo o conteudo do html da page
    ConteudoDaPagina = (Site.prettify) #função prettify exibe informações na estrutura html comum

    #HTML da Noticia
    Noticias = (Site.findAll("div", attrs={"container container-content"})) 
    #print(Noticias.prettify) #Mostra todo o codigo de Noticia de forma mais legivel
    #Titulo da Noticia
    #Titulo = Noticias.find("h3")#h3 tag que contem titulo e link

    #Metodo find do Beautifulsoup procura por tags ("tag", attrs={dicionario com informações que diferencia essas tag das demoas tags iguais na pag})
    #print(Titulo.text)#.text pega somente o conteudo de texto contido no obj
    #print(Titulo.find("a")) #tentativa de pegar somente o link
    #print (Noticias, file=arquivo)
    #print(Noticias)
    return {"Status": Status,"HTML_Code":ConteudoDaPagina}

def Gravar(Texto):
    with open ('informações.html', 'w') as arquivo:
        print(Texto, file=arquivo)


Gravar(PegarNoticias(Site=Site, Diolinux=Diolinux))