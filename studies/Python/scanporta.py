###############################################################################################
# ScanPorta - A simple port scanner in Python
##################################################################################################
""" Esse script não é de minha autoria, estou copiando código pra praticar e aprender. O código original pode ser encontrado em:
"""

import socket as s # Importa a biblioteca de sockets para criar conexões de rede
from sys import argv, exit # Importa argv para acessar argumentos de linha de comando e exit para encerrar o programa

#########################################################################################################
# Variáveis globais
#####################################################################################################
portasabertas = [] # Lista para armazenar as portas abertas encontradas

def portsacan(alvo, porta_inicial, porta_final):
    """
    
    """
    print(f"Escaneando {alvo} do porto {porta_inicial} ao {porta_final}...") # Imprime uma mensagem indicando o alvo e as portas que estão sendo escaneadas
    for porta in range (porta_inicial, porta_final + 1):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM) # Cria um socket TCP/IP
        sock.settimeout(0.5) # Define um tempo limite para a conexão
        
        sock.connect_ex((alvo, porta)) # Tenta conectar ao alvo na porta especificada
        if sock.connect_ex((alvo, _porta)) == 0: # Verifica se
            portas_pabertas.append(porta) # Se a conexão for bem-sucedida, adiciona a porta à lista de portas abertas

if __name__ == "__main__":
    if len(argv) != 4: # Verifica se o número de argumentos é diferente de 4 (o nome do script + 3 argumentos)
        print("Uso: python scanporta.py <alvo> <_> <porta_final>") # Imprime uma mensagem de uso caso os argumentos estejam incorretos
        exit(1) # Encerra o programa com um código de erro

    alvo = argv[1] # O primeiro argumento é o alvo (endereço IP ou nome de domínio)
    _ = int(argv[2]) # O segundo argumento é a porta inicial,
    porta_final = int(argv[3]) # O terceiro_pargumento é a porta final

    port_sacan(alvo, _, porta_final) # Chama a funçã_p de escaneamento de portas