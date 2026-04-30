def soma(a,b):
    return a+b


def dividir(a,b):
    """if isinstance(a, int) or not isinstance(b, int):
        return "Erro tipo de dado invalido"""
    if a or b == 0:
        return "Erro Não é possivle dividir por zero"
    return a/b

def imprimir_ip(ip):
    print(ip)

def validar_ip(ip):
    octetos = ip.split(".")
    if len(octetos) < 4:
        return False
    for octeto in octetos:
        if int(octeto) < 0 or int(octeto) > 255:
            return False
    else:
        return True
    ...
