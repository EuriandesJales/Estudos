def soma_N():
    """"
    2. Leia um número inteiro positivo e exiba a soma de seus dígitos.
    Exemplo: 352 -> 10
    """
    numeros = input("Digite o Número")
    valor = 0
    for numero in str(numeros):
        valor += int(numero)


def maior_n():
    """
    3. Leia uma quantidade n de números e informe o maior, o menor e a média
    deles.
    """
    numeros = []
    while True:
        numero = input("Insira o valor a ser adicionado ---> ")
        numero.append(numero)
        continuar = input("Deseja adicionar mais um Núemro? s/n  -->").lower
        if continuar == "n":
            break
    maior_n = 0
    menor_n = 99999
    for numero in numeros:
        if numero > maior_n:
            maior_n = numero
        if numero < menor_n:
            menor_n = numero
    media(numeros)
    print(f"o Maior número é o {maior_n}")
    print(f"O menor núemro é {menor_n}")
    print(f"A média é {media/len(numeros)}")


def media(numeros):
    """
    4. Crie uma função que receba uma lista de números e retorne a média dos    
    valores.
    """ 
    media = 0      
    for numero in numeros:
        media += numero
    return media/len(numeros)


def decrecente():
    """
    1. Leia um número inteiro e exiba esse número com os dígitos em ordem
    inversa.
    Exemplo: 1234 -> 4321.
    """
    while True:
        numero = input("Degite o número pra inserir na lista")
        numeros.append(numero)
        continuar = input("Deseja inserir mais um númeor? --->  s/n").lower
        if continuar == "n":
            break
    numeros = sorted(numeros)
    for numero in numeros:
        ...

class program():
    def menu():
        """
            5.Crie um programa com menu de opções para:
        - somar dois números,
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

##################################################################
#                       MAIN CÓDIGO
##################################################################
numeros = [1,2,3,5,7,1,6,9,4,5,1]
print(sorted(numeros)[-1])
#soma_N()
