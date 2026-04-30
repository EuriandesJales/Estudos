#global Vars
clientes = []
largura = 30

def menu():
    opcoes = ["Cadastrar", "Ver Clientes", "Remover Clientes", "Sair"] 
    print("#" * largura)
    print(f"{'ADMINISTRACAO DE CLIENTES':^30}")
    print("#" * largura)
    for index, name in enumerate(opcoes, start=1):
        print(f"{index}<--->{name}")
    opcao = input("Qual Acao deve ser feita?  --->").strip()
    if opcao:
        opcao = int(opcao[0])
    return opcao

def cadastro():
    cliente = str(input("Digite o Nome do cliente -->"))
    clientes.append(cliente)
    print(f"O clinete {cliente} foi adicionado ao banco de dados")
    input("Digite qualquer coisa pra continuar")  

def ver_clientes():
    print("#" * largura)
    print(f"{'Lista de Clientes:':^30}")
    print("#" * largura)
    for cliente in clientes:
        print(cliente)
    input("Digite qualquer coisa pra continuar")

def remover():
    ver_clientes()
    nome = input("Qual cliente você quer remover?  -->")
    indice = 0
    for cliente in clientes:
        if nome in cliente:
            comfirmacao = input(f"Deseja remover o cleinte {cliente}?   s/n  -->").lower
            if comfirmacao == "s":
             print(f"{cliente} foi removido do  banco de dados")
             del clientes[indice]
            input("Digite qualquer coisa pra continuar")
            return
        indice += 1

while True:
    opcao = menu()
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        ver_clientes()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        break
    else:
        print("Valor invalido, por favor digite um valor valido")
