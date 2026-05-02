from time import sleep
#from random import randint


def verificar_tipo(msg, msg2):
   while True:
        dado = input(msg)
        try:
            dado = int(dado)
            return dado  # Retorna o dado convertido para inteiro
        except ValueError:
            print(msg2) # Exibe a mensagem de erro e continua o loop para solicitar novamente
            continue

def verificar_codigo(codigo): # aex 1
    codigo = verificar_tipo("Qual é o código? ", "O código deve ser um número inteiro.")
    if codigo == 200:
        print("Dispositivo Ativo.")
    ... 

def verif_porta(): # ex 2
    porta = verificar_tipo("Qual é a porta? ", "A porta deve ser um número inteiro.")
    if porta > 0 and porta < 65535:
        print("Porta válida.")
    else:
        print("Porta inválida. A porta deve ser um número entre 1 e 65535.")

def Classificar_pacote(): # ex 3
    pacote = verificar_tipo("Qual é o tamanho do pacote? ", "O tamanho do pacote deve ser um número inteiro.")
    if pacote <= 500:
        print("Pacote pequeno.")
    elif pacote > 500 and pacote <= 1500:
        print("Pacote médio.")
    elif pacote > 1500:
        print("Pacote grande.")
    else:
        print("Error: não foi possivel determinar o tamanho do pacote.")

def log_pacotes(): #ex 4
    n_pacotes = verificar_tipo("Quantos pacotes foram recebidos?","O número de pacotes deve ser um número inteiro.")
    while True:
        if n_pacotes <= 0:
            return "Operação chegou ao final"
        else:
            print(f"Processando o pacote de Número{n_pacotes}...")
            sleep(1)  # Simula o processamento do pacote com um atraso de 1 segundo

def verificar_ip(): # ex5
    while True:
        ip = input("Digite o endereço IP: ")
        try:
            ip = str(ip).split(".")
            if len(ip) != 4:
                print("Endereço IP inválido. O endereço IP deve conter 4 octetos.")
                continue
        except ValueError:
            print("Endereço IP inválido. o endereço deve ser um número com 4 octetos. separados por pontos.")
            continue
        break
    if ip[0] == "192" and ip[1] == "168":
        print("Endereço pertece a rede local.")
            
    else:
        print("Endereço pertece a rede externa")

def tentativas_login(): # ex 6
    for i in range(3):
        if i == 3:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")
            return
        password = input("Digite a senha: ")
        if password == "senha":
            print("Login bem-sucedido.")
            return
        else:
            print("Senha incorreta. Tente novamente.")

def Tamanho_pacotes(): # ex 7
    N_intervaulos = verificar_tipo("Quantos intervalos de latência foram registrados? ", "O número de intervalos deve ser um número inteiro.")
    
    total_pacote = 0
    
    for i in range(N_intervaulos):
        total_pacote += verificar_tipo(f"Digite o tamanho do pacote {i+1}, em MB: ", "O tamanho do pacote deve ser um número inteiro.")

    print(f"Total de MB {total_pacote}.")

def pacotes_perdidos(): # ex 8
    N_pacotes_enviados = verificar_tipo("Quantos pacotes foram enviados? ", "O número de pacotes enviados deve ser um número inteiro.")
    N_pacotes_recebidos = verificar_tipo("Quantos pacotes foram recebidos? ", "O número de pacotes recebidos deve ser um número inteiro.")

    print(f"Número de pacotes perdidos: {N_pacotes_enviados - N_pacotes_recebidos}")

def latencia_media(): # ex 9
    N_Medicoes = verificar_tipo("Quantas medições de latência foram realizadas? ", "O número de medições deve ser um número inteiro.")
    for i in range(N_Medicoes):
        latencia += verificar_tipo(f"Digite a latência da medição {i+1}, em ms: ", "A latência deve ser um número inteiro.")
    print("A latencia média é: ", latencia/N_Medicoes)

def check_sobrecarga(): # ex 10
    capacidade_maxima = 100 # Capacidade máxima do servidor em MB
    carga_atual = verificar_tipo("Qual é a carga atual do servidor em MB? ", "A carga atual deve ser um número inteiro.")
    if carga_atual > capacidade_maxima:
        print("Servidor sobrecarregado.")
    else:
        print(f"Servidor operando dentro da capacidade, {carga_atual}/{capacidade_maxima} MB utilizados. {capacidade_maxima-carga_atual} MB disponíveis.")


