import requests
from bs4 import BeautifulSoup
import os
import webbrowser
from urllib.parse import urljoin

Diolinux = requests.get("https://diolinux.com.br/")  # Obj Diolinux == return get web site
Site = BeautifulSoup(Diolinux.content, "html.parser")

# Criação do diretório para salvar as imagens
if not os.path.exists('imagens'):
    os.makedirs('imagens')

def baixar_imagem(url_imagem, nome_arquivo):
    """Função para baixar a imagem e salvar localmente."""
    response = requests.get(url_imagem)
    if response.status_code == 200:
        with open(nome_arquivo, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Erro ao baixar a imagem: {url_imagem}")

def PegarNoticias(Site, Diolinux):
    Status = Diolinux.status_code  # return da requisição

    # HTML da Noticia
    Noticias = Site.find_all("div", class_="container container-content")  # Corrigido: uso de find_all

    # Iniciar estrutura do HTML com cabeçalho CSS para estilo básico
    html_conteudo = """
    <html>
    <head>
        <title>Noticias Diolinux</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }
            h1 {
                background-color: #4CAF50;
                color: white;
                padding: 20px;
                text-align: center;
                margin-bottom: 30px;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .news-item {
                display: flex;
                align-items: center;
                justify-content: space-between;
                border-bottom: 1px solid #ddd;
                padding: 10px 0;
            }
            .news-item img {
                width: 150px;
                height: auto;
                border-radius: 8px;
                margin-right: 20px;
            }
            .news-text {
                flex: 1;
            }
            a {
                color: #4CAF50;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Noticias Diolinux</h1>
        <div class="container">
    """

    # Para cada notícia encontrada, adicionar no HTML
    for idx, noticia in enumerate(Noticias):
        texto_noticia = noticia.get_text(strip=True)
        
        # Tenta encontrar a imagem associada à notícia
        img_tag = noticia.find('img')
        img_url = img_tag['src'] if img_tag else None

        # Se houver imagem, faz o download
        if img_url:
            img_url = urljoin(Diolinux.url, img_url)  # Faz o download completo da URL
            nome_arquivo_imagem = f"imagens/noticia_{idx}.jpg"
            baixar_imagem(img_url, nome_arquivo_imagem)
            img_path = nome_arquivo_imagem
        else:
            img_path = None

        # Extrair o link para a notícia, se disponível
        link_noticia = noticia.find('a')
        noticia_url = link_noticia['href'] if link_noticia else "#"

        if texto_noticia:  # Adiciona no HTML apenas se houver conteúdo
            html_conteudo += f"""
            <div class="news-item">
                <div class="news-text">
                    <p>{texto_noticia}</p>
                    <a href="{noticia_url}" target="_blank">Leia mais</a>
                </div>
                {f'<img src="{img_path}" alt="Imagem da notícia">' if img_path else ''}
            </div>
            """

    # Finaliza a estrutura HTML
    html_conteudo += """
        </div>
    </body>
    </html>
    """

    return html_conteudo

def GravarEAbrirHTML(conteudo_html):
    # Gravar o conteúdo no arquivo HTML
    with open('noticias.html', 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_html)
    
    # Abrir o arquivo no navegador
    webbrowser.open('noticias.html')

# Gerar o conteúdo HTML com as notícias
conteudo_html = PegarNoticias(Site=Site, Diolinux=Diolinux)

# Gravar e abrir o arquivo no navegador
GravarEAbrirHTML(conteudo_html)
