# Prova de Algoritmos - Gerenciamento de Dispositivos de Rede
# versão 2.0 - 2026

# Variaveis Globais
dispositivos = [] # lista de dispositivos
#dispositivo = {"Nome":"", "id":"", "ip":"", "Type":"", "Ping":""} # modelo de dispositivo, cada dispositivo é um dicionário com essas chaves, e a lista de dispositivos é uma lista de dicionários



def Menu():
    print("#" * 30)
    print("Menu")
    print("#" * 30)
    print("1 -> Cadastrar Novo Dispositivo")
    print("2 -> Listar todos os dispositivos cadastrados")
    print("3 -> Buscar dispositivo pelo identificador.")
    print("4 -> Buscar dispositivo pelo endereço IP.")
    print("5 -> Listar dispositivos por tipo.")
    print("6 -> Mostrar o dispositivo com maior tempo de resposta.")
    print("7 -> Mostrar o dispositivo com menor tempo de resposta")
    print("8 -> Calcular a média de tempo de resposta dos dispositivos.")
    print("9 -> Remover dispositivo pelo identificador. ")
    print("10 -> Sair")


def cadastro():
    """""Cadastrar dispositivo. 
O usuário informa os dados do dispositivo e o sistema armazena essas 
informações em memória. Atenção O identificador não pode ser repetido."""

    #dispositivo = {"Nome":", {"id":""}, {"ip":""}, {"Type":""} # esta logica esta errada isso é um dicionario dentro de outro dicionario:
    # Logica correta dispositivo = {"Nome":"", "id":"", "ip":"", "Type":"", "Ping":""}
    while True:
        nome = str(input(f"Digite o nome do dispositivo  -->"))
        id = int(input(f"Digite o id do dispositivo {nome} -->"))
        if id_existente(id):
            print(f"Esse id {id} já existe, por favor insira um id diferente.")
            continue
        ip = str(input(f"Digite o ip do dispositivo {nome} -->"))
        if not ip_valido(ip): # verifica se a saida da funcao ip_valido é falsa, ou seja, se o ip é inválido
            print(f"O ip {ip} é inválido, por favor insira um ip válido.")
            continue
        if ip_existente(ip): # verifica se a saida da funcao ip_existente é verdadeira, ou seja, se o ip já existe no sistema
            print(f"Esse ip {ip} já existe, por favor insira um ip diferente.")
            continue
        tipo = str(input(f"Digite o tipo do Dispositivo {nome} -->"))
        ping = int(input("Qual é o ping? -->"))

        dispositivo = {"Nome": nome, "Id": id, "Ip": ip, "Type": tipo, "Ping": ping} # criando meu dispositivo
        break # o break é para sair do loop while, pois já temos todas as informações do dispositivo e não precisamos continuar pedindo informações
    print(f"o Dispositvo {dispositivo} será adicionado a lsita de dispositivos")
    dispositivos.append(dispositivo)

    ...


def viwDispositivos():
    """Cadastrar dispositivo. 
O usuário informa os dados do dispositivo e o sistema armazena essas 
informações em memória. Atenção O identificador não pode ser repetido."""
    if not dispositivos: # verificando se a lista de dispositivos esta vazia
        print("Não há dispositivos cadastrados.")
        return
    """
    # Imprime a lista de dispositivos em formato de tabela
        ID   | Nome           | IP             | Tipo       | Ping
        Embora funcional, esse formato pode ser fácilmente quebrado com qualquer adicição de informação ao dispostivo
    print(f"Dispositivos cadastrados:")
    print(f"\n{"ID":<5} | {"Nome":<15} | {"IP":<15} | {"Tipo":<10} | {"Ping":<6}") # Imprime o cabeçalho da tabela
    
    for d in dispositivos:
        # < alinhamento à esquerda e o número após a : é a largura do campo, em outras palavras alinhando com o cabeçalho
        print(f"{d['Id']:<5} | {d['Nome']:<15} | {d['Ip']:<15} | {d['Type']:<10} | {d['Ping']:<6}")
    
    """
    # esta outra forma garante que  funcionara independente de modificações futuras no dicionário do dispositivo, pois ele percorre todas as chaves e valores do dicionário
    for d in dispositivos:
        print(f"\n--- Dispositivo {d['Id']} ---") 
        for chave, valor in d.items(): # para cada valor em cada chave do dicionario dispositivos faça
            print(f"{chave}: {valor}") 
    ...

def busacar_id():
    """Buscar dispositivo pelo identificador."""

    id = int(input("Digie o ID do dispositivo a ser procurado no sistema -->"))
    encontrado = False # var de checkagem para verifcar se o dispositivo a ser procurado foi encontrado ou não, inicialmente é falso pois ainda não procuramos o dispositivo

    for d in dispositivos:
        if d["Id"] == id:
            print(f"O dispositivo é {d['Nome']}")
            for chave, valor in d.items():
                print(f"{chave}: {valor}")
                return
    
    if not encontrado: # verifica o valor do encontrou pra saber se ainda é falso, se for não foi encontrado
        print(f"Não há dispositivo com esse ID {id}")

def buscar_ip():
    """Buscar dispositivo pelo endereço IP"""
    
    ip = str(input("Digie o Ip do dispositivo a ser procurado no sistema"))
    encontrado = False # var de checkagem para verifcar se o dispositivo a ser procurado foi encontrado ou não, inicialmente é falso pois ainda não procuramos o dispositivo
    
    if ip_valido(ip) == False: # verifica se a saida da funcao ip_valido é falsa, ou seja, se o ip é inválido
        print(f"O ip {ip} é inválido, por favor insira um ip válido")
        return
    for d in dispositivos:
        if d["Ip"] == ip:
            print(f"O dispositivo é {d['Nome']}")
            for chave, valor in d.items():
                print(f"{chave}: {valor}")
                return
    
    if not encontrado: # verifica o valor do encontrou pra saber se ainda é falso, se for não foi encontrado
        print(f"Não há dispositivo com esse IP {ip}")


def organizar_tipo():
    """Listar dispositivos por tipo. 
    Lista de Tipos de Dispositivos:
        Gateway / Router: Roteadores de borda ou residenciais.
        Switch: Gerenciáveis (L2/L3) ou não-gerenciáveis.
        Access Point: Pontos de acesso Wi-Fi.
        Server: Servidores (Web, DNS, DHCP, AD).
        Workstation: PCs de usuários.
        Firewall: Dispositivos de segurança (como um pfSense ou Fortigate)."""
    
    if not dispositivos: # verificando se a lista de dispositivos esta vazia
        print("Não há dispositivos cadastrados.")
        return
    
    # Dicionário para armazenar os tipos de dispositivos
    agrupados = {}
   
    for d in dispositivos: # para cada dispositivo na lista de dispositivos faça
        tipo = d["Type"] # tipo recebe o valor da chave "Type" do dispositivo, em outras palavras tipo é igual a tipo do dispostivo atual

        
        if tipo not in agrupados: # se o tipo ainda não esta no dicionário de tipos(aqui camo de agrupados), precisamos cirar uma lsita vazia para ele
                agrupados[tipo] = [] # isso é um dicionário, repare agrupados recebe uma nova chave e o valor da chave o nome da chave é o tipo do dispositivo é uma lista vazia de dispositivos daquele tipo
       
        agrupados[tipo].append(d)  # Adicionamos o dispositivo à lista do tipo correspondente
    
    # Imprime os dispositivos agrupados por tipo
    print("\n=== DISPOSITIVOS POR CATEGORIA ===")
    for tipo, lista in agrupados.items(): # para cada tipo e lista(lista de dispositivos daquele tipo) no dicionário de agrupados faça
        print(f"\n> TIPO: {tipo.upper()} ({len(lista)} encontrado(s))") # um cabeçalho tipo tal contem n dispositivos
        for disp in lista: # para cada dispostivos na lista (essa lsita é a lista do for de cima) de dispostivos do tipo faça
            # Imprime o ID como destaque para separar os dispositivos da mesma categoria
            print(f"  [ Dispositivo ID: {disp.get('Id', 'N/A')} ]")
        
        # O "Pulo do Gato": percorre as chaves e valores do dicionário do dispositivo
            for chave, valor in disp.items():
                # Alinhamos as chaves para ficar visualmente limpo (ex: Nome: Switch01)
                print(f"    {chave:<10}: {valor}")
            
            print("-" * 20) # Linha fina para separar dispositivos da mesma categoria

def get_maior_ping():
    """"6. Mostrar o dispositivo com maior tempo de resposta."""
    maior_ping = 0
    for d in dispositivos:
        if d["Ping"] > maior_ping:
            maior_ping = d["Ping"]
            dispositivos_maiorPing = d
    print(f"O maior ping é {dispositivos_maiorPing['Ping']} do dispositivo {dispositivos_maiorPing['Nome']}")


def get_menor_ping():
    """"Mostrar o dispositivo com menor tempo de resposta"""
    menor_ping = 99999999999999999 # isso é um numero muito grande para garantir que o menor ping seja menor que ele
    for d in dispositivos: # para cada dispositivo na lista de dispositivos faça
        if d["Ping"] < menor_ping: # se o ping do dispositivo atual for menor que o menor ping registrado até agora, atualizamos o menor ping e o dispositivo com menor ping
            menor_ping = d["Ping"] # menor ping recebe o valor do ping do dispositivo atual
            dispositivos_menorPing = d 
    print(f"O menor ping é {dispositivos_menorPing['Ping']} do dispositivo {dispositivos_menorPing['Nome']}")
    ...

def media_ping():
    """"8. Calcular a média de tempo de resposta dos dispositivos."""
    soma_ping = 0
    if not dispositivos: # verificando se a lista de dispositivos esta vazia
        print("Não há dispositivos cadastrados.")
        return
    
    for d in dispositivos: # para cada dispositivo na lista de dispositivos faça, media_ping recebe a soma do ping de todos os dispositivos
        soma_ping += d["Ping"] # soma_ping recebe o valor atual de soma_ping mais o ping do dispositivo atual, ou seja, soma_ping é a soma de todos os pings dos dispositivos
    
    media_ping = soma_ping / len(dispositivos) # media_ping recebe o valor da soma dos pings dividido pelo número de dispositivos, ou seja, media_ping é a média dos pings dos dispositivos
    print(f"A media do ping dos {len(dispositivos)} é {media_ping}")
    ...

def remove_id():
    """""9. Remover dispositivo pelo identificador. """

    id = int(input("Digite o id do dispositivo a ser removido"))
    encontrou = False # var de checkagem para verifcar se o dispositivo a ser removido foi encontrado ou não, inicialmente é falso pois ainda não procuramos o dispositivo

    for d in dispositivos: # para cada dispositivo na lista de dispositivos faça
        if d["Id"] == id: # se o id do dispositivo atual for igual ao id informado pelo usuário, removemos o dispositivo da lista de dispositivos e imprimimos uma mensagem de sucesso
            dispositivos.remove(d) # remove o dispositivo da lista de dispositivos
            print(f"O dispositivo com id {id} foi removido com sucesso.") 
            encontrou = True # altera valor de encontrou para verdadeiro, pois encontramos o dispositivo a ser removido
            break # o break é para sair do loop for, pois já encontramos o dispositivo a ser removido e não precisamos continuar procurando
    
    if not encontrou: # verifica o valor do encontrou pra saber se ainda é falso, se for não foi encontrado
        print(f"Não há dispositivo com id {id} para remover.")
    ...

###############################################################################################################################################
# Funções de checkagem de dados, para garantir que o usuário insira os dados no formato correto, evitando erros futuros no programa
###############################################################################################################################################

def id_existente(id):
    """Função que verifica se o id já existe na lista de dispositivos"""
    for d in dispositivos:
        if d["Id"] == id:
            return True
    return False

# Verificações de ip, para garantir que o usuário insira um ip válido e que não haja ips repetidos no sistema, evitando erros futuros no programa
def ip_valido(ip):
    partes = ip.split('.') # divido o ip em uma lista onde cada parte coresponde a um octeto do ip, ou seja, o ip
    if len(partes) != 4: # verifico se o número de octetos é diferente de 4, se for diferente de 4 o ip é inválido, pois um ip válido deve conter exatamente 4 octetos
        return False # retorno falso pois esse não é um ip válido
    
    for parte in partes: #verificação de cada octeto
        if not parte.isdigit() or not (0 <= int(parte) <= 255): # se octeto não for somente número ou convertivel pra int e menor que 255
            return False # Não é
    return True

def ip_existente(ip_novo):
    """Verifica se o endereço IP já está cadastrado no sistema."""
    for d in dispositivos:
        if d["Ip"] == ip_novo:
            return True
    return False

def tipo_permitido(tipo_usuario):
    tipos_validos = ["Gateway", "Router", "Switch", "Access Point", "Server", "Workstation", "Firewall"]
    # .title() coloca a primeira letra em maiúsculo para bater com a lista
    return tipo_usuario.title() in tipos_validos


#############################################################################################################
# Main código é aqui onde esta o bloco principal do programa, onde o usuário interage com o menu e escolhe as opções para executar as funções
#############################################################################################################

while True:
    Menu()
    opcao = int(input("Digite o número correspondente a função  -->"))
    if opcao == 1:
        cadastro()
        ...
    elif opcao == 2:
        viwDispositivos()
        ...
    elif opcao == 3:
        busacar_id()
        ...
    elif opcao == 4:
        buscar_ip()
        ...
    elif opcao == 5:
        organizar_tipo()
        ...
    elif opcao == 6:
        get_maior_ping()
        ...
    elif opcao == 7:
        get_menor_ping()
        ...
    elif opcao == 8:
        media_ping()
        ...
    elif opcao == 9:
         remove_id()
        
    elif opcao == 10:
        break
    
    else:
        print("O Valor informado não representa nenhuma opção por favor insira um valor valido")