
def menu():
    """
    5.Crie um programa com menu de opções para:
    - ,
    - subtrair dois números,
    - multiplicar dois números,
    - dividir dois números,
    - sair do programa.
    """
    largura = 30
    opcoes = ["somar", "subtrair", "multiplicar", "dividir", "sair"]
    print("#" * largura)
    print(f"{'ADMINISTRACAO DE CLIENTES':^largura}")
    print("#" * largura)
    for index, name in enumerate(opcoes, start=1):
        print(f"{index}<--->{name}")
    opcao = input("Qual Acao deve ser feita?  --->").strip()
    if opcao:
        opcao = int(opcao[0])
        return opcao
    
def somar():
    """"
    somar dois números
    """
    n1 = int(input("Digite o primeiro número"))
    n2 = int(input("Digite o segundo número"))
    print(f"A soma dos números é {n1 + n2}")

def subtrair():
    """"
    subtrair dois números
    """
    n1 = int(input("Digite o primeiro número"))
    n2 = int(input("Digite o segundo número"))
    print(f"A subtração dos números é {n1 - n2}")
    
def multiplicar():
    """"
    multiplicar dois números
    """
    n1 = int(input("Digite o primeiro número"))
    n2 = int(input("Digite o segundo número"))
    print(f"A multiplicação dos números é {n1 * n2}")
    
def dividir():
    """"
    dividir dois números
    """
    n1 = int(input("Digite o primeiro número"))
    n2 = int(input("Digite o segundo número"))
    print(f"A divisão dos números é {n1 / n2}")


###############################################################
#               MAIN CÓDIGO
#################################################################

while True:
    opcao = menu()
    if opcao == 1:
        somar()
    elif opcao == 2:
        subtrair()
    elif opcao == 3:
        multiplicar()
    elif opcao == 4:
        dividir()
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")