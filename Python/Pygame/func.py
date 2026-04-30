import pygame
#from main import velocidade
from random import randint
from time import sleep
import sys


def centralizar_imagem(tela, imagem, x_offset=0, y_offset=0):
    """
    Centraliza uma imagem na tela.

    Parâmetros:
    - tela: Surface onde a imagem será desenhada.
    - imagem: Surface da imagem a ser centralizada.
    - x_offset: Ajuste opcional na posição X.
    - y_offset: Ajuste opcional na posição Y.

    Retorna:
    - Tupla (pos_x, pos_y) com as coordenadas centralizadas.
    """
    largura_tela, altura_tela = tela.get_size()
    largura_img, altura_img = imagem.get_size()

    pos_x = (largura_tela - largura_img) // 2 + x_offset
    pos_y = (altura_tela - altura_img) // 2 + y_offset

    return pos_x, pos_y

import pygame

# Função para movimentar personagem
def mover_personagem(personagem_rect, velocidade, fundo_rect):
    """Move o personagem baseado nas teclas pressionadas e verifica colisão com o fundo."""
    teclas = pygame.key.get_pressed()

    # Movimentação
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:  
        personagem_rect.x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:  
        personagem_rect.x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:  
        personagem_rect.y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:  
        personagem_rect.y += velocidade

    # Colisão com as bordas do fundo
    if personagem_rect.left < fundo_rect.left:
        personagem_rect.left = fundo_rect.left
    if personagem_rect.right > fundo_rect.right:
        personagem_rect.right = fundo_rect.right
    if personagem_rect.top < fundo_rect.top:
        personagem_rect.top = fundo_rect.top
    if personagem_rect.bottom > fundo_rect.bottom:
        personagem_rect.bottom = fundo_rect.bottom

    return personagem_rect  # Retorna a nova posição
