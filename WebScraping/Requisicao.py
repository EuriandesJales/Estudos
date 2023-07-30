import requests

Diolinux = requests.get("https://diolinux.com.br/") #Obj Diolinux == return get web site

"""
#guardando as informações em um arquivo de texto para manipualr posteriomente
with open("informações.txt", "w+r") as infoDio:
    infoDio = """
print("Status da Requisição:  ", Diolinux.status_code) # return da requisição
print("Conteudo", Diolinux.content) # Retorna todo o conteudo do html da page