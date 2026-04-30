def media(numeros):
    """
    4. Crie uma função que receba uma lista de números e retorne a média dos    
    valores.
    """ 
    media = 0      
    for numero in numeros:
        media += numero
    return media/len(numeros)

def analisando_n():
    """
    3. Leia uma quantidade n de números e informe o maior, o menor e a média
    deles.
    """
    numeros = []
    while True:
        numero = input("Insira o valor a ser adicionado ---> ")
        numeros.append(numero)
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

analisando_n()