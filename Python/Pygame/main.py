import pygame
#from random import randint
#from time import sleep
import sys
from func import mover_personagem  # Importando a função diretamente do arquivo func.py
from func import centralizar_imagem

# Variáveis Globais
rodando = True

# Inicializando o pygame
pygame.init()

# Definindo as variáveis de dimensões da tela
Largura_Tela = 1040
Altura_Tela = 900
tela = pygame.display.set_mode((Largura_Tela, Altura_Tela))  # Criando a tela



# Definindo título da janela
pygame.display.set_caption("A Aventura da Fran")

# Definindo a cor de fundo
COR_FUNDO = (0, 0, 0)  # Cor preta
#carregando uma imagem para ser usada no fundo
fundo = pygame.image.load("Python/Mygame/Assets/Arena01.jpg")
fundo_rect = fundo.get_rect(center=(Largura_Tela // 2, Altura_Tela // 2))
#---------------------------------------------
#carregando uma imagem para ser usada no personagem
personagem = pygame.image.load("Python/Mygame/Assets/char01.png")
personagem = pygame.transform.scale(personagem, (40, 40))
personagem_rect = personagem.get_rect(center=fundo_rect.center)
velocidade = 5 # velocidade de movimento do personagem
#---------------------------------------------

# define as posições
pos_fundo = centralizar_imagem(tela, fundo)
pos_personagem = centralizar_imagem(tela, personagem, y_offset=100)

# Definindo taxa de quadros
clock = pygame.time.Clock()

# Loop principal
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False  # Quando o evento de fechar a janela é ativado, rodando recebe False

    
    # 🔹 Chamando a função de movimentação
    personagem_rect = mover_personagem(personagem_rect, velocidade, fundo_rect)
    
    # Preenche a tela com a cor de fundo
    #tela.fill(COR_FUNDO)
    #tela.blit(fundo, (pos_fundo))#desenha a imagem de fundo na tela
    tela.fill((0, 0, 0))
    tela.blit(fundo, fundo_rect.topleft)
    tela.blit(personagem, personagem_rect.topleft)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros
    clock.tick(60)  # 60 FPS

# Fecha o pygame ao sair
pygame.quit()
sys.exit()
