"""_summary_
    Pequeno scripting que faz pesquisa no Google permite acessar qualquer resultado na lista da primeira pagina
    ⚠️ Lista de links não obtida falta ajustes
    """

# Importando as bibliotecas necessárias (antes execute pip install -r requirements.txt)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random2

# Definindo a Classe Navegador e suas funções

class navegador:
    def __init__(self):
        #inicializa objeto navegador
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
        self.driver = webdriver.Chrome( #carrega o driver do Chrome
        service=Service(ChromeDriverManager().install()),# define o serviço do ChromeDriver (gerenciado automaticamente)
        options=options #  define as opções como o user-agent, headless, etc.
)

        
    
        self.driver.get("https://duckduckgo.com") # acessa o duckduckgo simplesmente por ser menos restritivo que o google
    
    def pesquisa(self, pesquisa):
        #realiza a pesquisa
        time.sleep(random2.randint(1, 3)) # espera um tempo aleatório entre 1 e 3 segundos (para parecer mais humano)
        Search_box = self.driver.find_element(By.NAME, "q") #encontra o elemento da barra de pesquisa por o nome "q" 
        """Mas, tem varias forams de fazer isso como:
        # Search_box = self.driver.find_element(By.ID, "q") #ou por ID
        # Search_box = self.driver.find_element(By.XPATH, "//input[@name='q']") #ou por XPATH
        # Search_box = self.driver.find_element(By.CSS_SELECTOR, "input[name='q']") #ou por CSS SELECTOR
        # Search_box = self.driver.find_element(By.CLASS_NAME, "gLFyf") #ou por CLASS NAME
        # Search_box = self.driver.find_element(By.LINK_TEXT, "Pesquisar") #ou por LINK TEXT"""
        Search_box.send_keys(pesquisa)
        time.sleep(random2.randint(1, 3)) # espera um tempo aleatório entre 1 e 3 segundos (para parecer mais humano)
        Search_box.send_keys(Keys.ENTER) #simula o pressionamento da tecla ENTER
        
        # criando uma lista de xpaths dos links obtidos como resultado
        self.resultados = self.driver.find_elements(By.XPATH, "//a[@data-testid='result-title-a']"
) #encontra todos os elementos que possuem o CSS SELECTOR "div.result__body a.result__url"
        #ou seja, todos os links dos resultados da pesquisa
        
        for i, link in enumerate(self.resultados):
            texto = link.text.strip() or "[sem texto visível]"
            print(f"{i}: {texto}")

        ...
    
    def acessar_resultado(self, indice=0):
        if not self.resultados:
            print("Nenhum resultado encontrado.")
            return None
        
        try:
            resultado = self.resultados[indice] #pega o resultado na posição "indice" da lista de resultados
            href = resultado.get_attribute("href") #pega o atributo "href" do resultado
            #ou seja, o link do resultado
            time.sleep(random2.randint(1, 3)) # espera um tempo aleatório entre 1 e 3 segundos (para parecer mais humano)
            resultado.click() #clica no resultado
        except IndexError:
            print(f"Resultado na posição {indice} não encontrado.")
            return None
        ...    


# Inicializa o objeto navegador
Navegador = navegador() # cria um objeto da classe navegador só pra agilizar o procesos de teste mesmo.
Navegador.pesquisa("Python webscraping") #realiza a pesquisa
print(Navegador.resultados) #imprime os resultados
time.sleep(10) #espera 5 segundos
Navegador.driver.quit() #fecha o navegador
# Finaliza o objeto navegador