def media(numeros):
    """
    4. Crie uma função que receba uma lista de números e retorne a média dos    
    valores.
    """ 
    media = 0      
    for numero in numeros:
        media += numero
    return media/len(numeros)

numeros = [1,3,4,5,8,9,10]
print(media(numeros))