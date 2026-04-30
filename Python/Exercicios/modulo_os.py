import os
import utilidades

#os.getcwd()
ip = int(input("Escreva um Ip valido: -->> "))

utilidades.imprimir_ip(ip)
print(utilidades.validar_ip(ip))