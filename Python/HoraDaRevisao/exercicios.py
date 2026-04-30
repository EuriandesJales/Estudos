"""
OBS: essa lista de exercicio foi pensada pra funcionar como uma man então abra ela em formato interativo 
RECOMENDO O IPYTHON -> ipython -i ./nomedoarquivo.py

                        ANOTAÇÕES PARA CONSEITOS E USO GERAIS
    REPL -> Metodo de abrir arquivos de forma interativo pode ser chamado por o comoando python -i NomeDoArquivo
    As variaveis do python são por defult str
"""
from time import sleep #só pra brincar mesmo
from colorama import Fore as cor #frescurinha pra colorir msm

def HelloWord(): #Por motivos de supertição mesmo
    #print
    print("função que mostra texto ou variaveis na tela")
    entrada=str(input("Estou captando sua entrada e colcoando na var entrada: "))
    print(f"A sua entrada foi {entrada}") #colocando variaveis entre texto
    print("Wello world")
    ...


def EntradaDeDados(): #input e alguns dos seus tratamentos
    """
    Tenta fazer a captura de Nome e idade, converter os dados para str e int respectivamente
    e mostrar uma mensagem com base na idade se for maior ou menor de idade
    """
    
    try:
        nome=str(input("Digite seu Nome -> "))
        idade=int(input("Digite sua idade -> "))
        print(f"Legal te conhecer {nome}")
        if idade <= 18:
            print(f"Você é bem novo tem {idade}")
        else:
            print(f"Você já é mairo de idade então tem {idade}")
    except:
        print("Não consigo entender o que você quer dizer.")
    ...


def Textos1(): #brincando com cancatenação de strings
    """Tipos de Variaveis str int float, conversão e conctenação na pratica
    """


    print(10+11.5) #uma demostração que float pode ser somado com int
    print(f"vejamos vou tentar somar dos textos","Texto1", + "Texto2")
    var="observe que a soma"+"pode ser feita e muma variavel"
    print(f"Armazenei e somei uma frase direitamente em uma variavel:\n",
          var)
    var=1
    var+=1
    print(var)#como pode ver += soma o que tem com o novo valor atribuido a mesma função pode ser usada em str ou numeros
    #OBS -> diferente do bash comandos não são executados atraves de variaveis
    ...


def Tipos(): #Aranhando a idea de objeto e classes
    """
    OK, VAMOS COMEÇAR -> um conceito muito importante é Objetos visto que toda a programação de python é baseado nisso
    assim como no linux tudo é um arquivo, aqui tudo é um objeto, cada objeto pertence a uma classe que erda caracteristicas
    ou seja funções e propriedades, cada onjeto possui suas funções, cada função executa um ação retorna um dado ou obj"""
    var=""
    print(type(var)) #vai mostrar que var é uma str
    #é justamente atravez desse comando type que você pode esta verificando a que classe esse obj pertence ou que tipo de objeto ele 
    # é se assim preferir
    print(dir(var))
    ...


def Textos2(): #Um pequeno conjunto de tecnicas de manipulação de strings
    """ exibe textos e junta eles
    args:
        none
    return:
        none
    """
    texto=" usarei essa variavel para exemplificar algumas manipulações de string"
    texto2="e essa aqui também"
    numero=10
    print(f"vamos usar algumas variaveis para fazer experiencias a var \n >>> texto={texto} \n",
           f"var 2 >> texto 2={texto2}\n",
           f"temos um int também {numero} com tipo {type(numero)}\n",
           f"Eu posso fazer a conversão dele atravéz do metodo str() e agora o tipo de numero é {type(str(numero))}")
    print(f"vou exibir o texto da primeira variavel todo em caixa alta atr\n",
          f"{texto2.upper} agora o texto em caixa baixa >> {texto2.lower}, Agora com inicias maisculas {texto2.capitalize}")
    ...


def ControleDeFluxo(): #uso de algumas funções para controlar o fluxo do codigo if else try while break
    """Mostrando alguns calculos que da pra fazer """
    try:
        print("#" * 30,"\n","  O Que você que eu faça ?\n", "#" * 30,"\n",
                    "1 -> CALCULAR O IMC \n",
                    "2 Quero Calcular o Fatorial de um Número ->")
        menu=int(input(">>>"))

        if menu==1: #berifica de forma simples se o usuario quer calcular o imc atraves de verificação do valor da var menu
            while True: #começa um loop "eterno" ou ate ser que brado por break
                
                try: # esse comando tenta fazer algo, use ele pra evitar que tudo crash se de algum erro, ele também capta os erros em uma variavel
                    print("Vou calcular seu IMC pra mostrar operações aritimeticas ok? \n Mas Primeiro me diga...")
                    altura=float(input("Qual é a sua altura? >>>"))
                    peso=float(input("Quanto você pesa? (NÃO SEJA TIMIDO, DIGA A VERDADE !) >>>"))
                    print(f"Seu IMC é ....\n {peso/(altura*altura)}")
                    break
                except: #aqui ~e quando ele não consegue fazer oque ele estava tentando=try:
                    if str(input("O que?!! \n OLHA EU NÃO ENTENDI NADA!\n quer tentar de novo? (S/N)")) == "N" or "n":
                        print("ok então")
                        break  #quebra o loop
                    else:
                        print("OK ENTÃO... \n vamos tentar novamente, ve se a acerta dessa vez ta?..\n")
        
        #Calculando Fatorial
        if menu==2: #não e uma boa solução mas ta valendo skksksk
            n=int(input("OK, quer que eu calcule o fatorial de qual númeor? "))
            fatorial = 1
            # Usa um loop for para multiplicar todos os números inteiros positivos menores ou iguais a n
            for i in range(1, n+1):
                fatorial *= i
            print(f"TA, TA, TA {n} fatorial é {fatorial}")
    except:
        print("Você não quer fazer nada que eu sei fazer?? \nblz então seu chato FUIII")

    ...


def Menu(Titulo, Opcoes=None): #SIM uma fanção que faz um menu sei que sou muitoooo besta
    """Cria um titulo
    Args: 
        Titulo: texto que sera adicionado na "interface"
        Opcoes gera posteriomente um menu com mais opções...
    return:
        exibição com o titulo no meio
    """
    try:
        Titulo=str(Titulo) #Tenta converter logo o tiluto pra str afim de evitar erros
        texto_formatado = f"{cor.RED}{'#' * 40}\n{Titulo.capitalize().center(40)}\n{'#' * 40}\n{cor.RESET}" # Cria uma string formatada que inclui o título em negrito e um conjunto de caracteres "#"
        print(texto_formatado)# Retorna a string formatada
        ...
    except Exception as E:
        return f"Erro {E} A operação Foi finalizada"
    ...


def Erro(): #Preciso ajeitar a parte que mostra imagem
    #TenteardeNovo=False #por via das duvidas o padão de tentrar de novo vai ser falso
    try: #tenta importar uma biblioteca para mostrar um robo bravo (tentar não faz mau n~e)
        import cv2
        img = cv2.imread("./imagens/robo_chateado.jpg")
        cv2.imshow('Chateado', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        ...
    TenteardeNovo=str(input("Oque você disse???? eu não estou entendendo nada..\nQuer tentar de novo?")).upper()
    if TenteardeNovo == "S":
        print("OK, OK, mas dessa vez olhao o que diz em")
        TenteardeNovo=True
    else:
        print("Eu não queria mesmo")
    return False

    ...


def OperadoresLogicos(): #Faz testes com Operadores Logicos para vermos o comportamento deles or and not
    """and retorna True se ambas as expressões forem verdadeiras,
     or retorna True se pelo menos uma das expressões for verdadeira 
     not inverte o resultado da expressão
    """
    #Vamos primeiro testar o And
    Menu("Teste de Operadores Logicos")
    operador=int(input("And(1) OR(2) NOT(3)"))
    if operador==1: 
        while True:
            try:
                #Pequeno Script que verifica se alguem esta apto a dirigit
                Menu("Será que você pode dirigir?")
                idade=int(input("Vejamos quantos Anos você tem? NÃO VAI MENTIR EM!! >>>"))
                if str(input("Mas, você tem CNH?(S/N) >>>")).upper() == "S":
                    CNH=True
                if CNH==True and idade >= 18:
                    print("_____\n,"
                            "/     \  >>>>>> AAAAAAAAAAAAA\n",
                            "| O   O | ENTÃO SENDO ASSIM VOCÊ PODE DIRIGIRRRRRR\n",
                        " |   <   | \n",
                            "| \___/ | \n",
                            "\_____/ \n")
                    sleep(2)
                    print("Ei.", end="")
                    sleep(1)
                    print(".", end="")
                    sleep(1)
                    print(".", end="")
                    print("Você não mentiu né??? ")
                    break
                else:
                    print("Eu sinto muito, mas Você não por dirigir poirs ", end="")
                    if CNH != True:
                        print("Acontece que você não tem carteira de Motoriasta")
                    if idade < 18:
                        print("É que você é muito novinho")
                    break
                ...
            except:
                print("Você esta Falando cosias que eu não consigo entender, ISSO ME DEIXA BRAVO")
                if str(input("Você quer mais uma Chance???(S/N) >>")).upper() == "N":
                    print("Eu não queria mesmo, S-E-U C-H-A-T-O")
                    break
            ...
    if operador==2:
        try:
            while True:
                Menu("TESTE DA PREGUIÇA")
                if str(input("Você vai lavar a louça?(S/N)  >>>")).upper() == "N" or "Não": #pega o input deixa em caixa alta
                    #e verifica se é o mesmo que a letra n
                    pratos=False
                if str(input("Você vai varrer a casa (S/N) >>>> ")).upper() == "N" or "Não":
                    varrer=False
                if pratos or varrer == True:
                    print("Parabés Você não é um prefuiçoso, continue assim")
                    break
                else:
                    print("Você é muito preguiçoso devia se envergonhar")
                    break
        except:
            if Erro() == False:
                ...
        

    if operador==3:
        """Menu("Vou verificar se um Número é Par tá?") #ficou ooo uma merda

        try:
            numero=int(input("Me fala um número ai vai ....  >>>"))
            if n % 2 == 0:
                n=True
            else:
                n=False
            print(f"Vou te contar uma mentira pois me escreveram assim com um NOT portanto o {numero} ele é {n}\n",
                  f"Mas, eu vou dize que {if n not}")
            ...
        except:
            ...               
        """
    
    ...


def IndexStr(texto):
    QueroFalar=True
    while QueroFalar == True:
        try:
            c=0
            texto = str(texto)
            print(f"O Texto que você inseriu na função foi {texto}\n",
                f"Vamos conversar um pouco sobre ela o tamanho desse texto é {len(texto)}:\n",
                f"Sendo assim esse texto possui {len(texto)} Indices, no python não só tudo é objeto mas como toda str é uma lista, \n",
                f"E por isso que esse texto possui indices assim como uma lista, deixe eu te mostrar na pratica")
            for i in range(0, len(texto)):
                print(f"O index {i} pertence a letra {texto[i]}")
            # faça algo com cada elemento da sequência
            ...
        except:
           QueroFalar=Erro()
        ...


def MetodosStr(Frase="ISSO AQUI É UMA FARASE DE TESTE"):

    QueroFalar=True
    while QueroFalar == True:
        try:
            Frase=str(Frase)#primeiro vamos converter frase pra texto logo por via das duvidas apesar que ia dar erro no mesmo jeito é só pra facilitar na depuração msm
            print(f"Irei mostrar varios metodos Str aqui\n Como já dito e mostrado -> str são vistas como listas no python, ",
                  f"O que possibilita manipular elas por o seus metodos \n", 
                  f"vejamos um exemplo usando a {cor.RED}var Frase={Frase} {cor.RESET}\n",
                  f"frase.upper() {cor.RED} {Frase.upper()}\n {cor.RESET} frase.lower {cor.RED} {Frase.lower()}\n Frase={Frase} {cor.RESET}\n",
                  f"frase.captalize {cor.RED} {Frase.capitalize()} {cor.RESET}\n",
                   f"frase.strip(' ') {cor.RED} {list(Frase.strip(' '))} {cor.RESET} ->' '\n obs que essa expressão se refere ao caracter espaço\n",
                    f"A função strip() é provavelmente a mais importante pois possibilita trasformar str em objetos o que torna possiveis\n",
                     f"O uso de todos os metodos da lista\n \n")
            Frase=str(input("vamos testar o repace Digite um frase com a palavra odio >>")).lower
            if "odio" not in Frase:
                    print("Não atrapalhe o exemplo digite a palavra odio corretamente ta? \nVamos tentar de novo")
                    return TypeError
            else:
                print(f"Você falou {Frase}, Mas eu não gosto dessa Palavra Odio então vou mudar seu texto\n",
                    f"Frase.replace() {Frase.replace('odio', 'amor')}")
                break
                ...
        except Exception as E:
            if E == TypeError:
                QueroFalar=Erro()
            else:
                #print("Rapazzzz deu um eror ai em {E}\n Joga no Google BB :)")
                QueroFalar=Erro()
                ...  

    ...


def Destacar(Text): # só uma firula que muda a  cor de textos para melhro visualização
    return f"{cor.GREEN}, {Text} ,{cor.RESET}"
