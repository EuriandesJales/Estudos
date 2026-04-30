def soma_N():
    """"
    2. Leia um número inteiro positivo e exiba a soma de seus dígitos.
    Exemplo: 352 -> 10
    """
    numeros = input("Digite o Número")
    valor = 0
    for numero in str(numeros):
        valor += int(numero)
    return valor

print(soma_N())