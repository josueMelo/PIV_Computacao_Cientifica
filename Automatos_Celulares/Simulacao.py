import sys
import pygame
import random
from threading import Thread
# Parâmetros do tamanho da simulação (cada célula em 5 pixels)
from Automatos_Celulares import PredadorPresa

random.seed(None)
tamanho = largura, altura = 1000, 1000
largura_tabuleiro = largura / 5
altura_tabuleiro = altura / 5
parado = False

# Estes são os códigos de cor que o pygame usa ((R,G,B))
preto = ((0, 0, 0))
vermelho = ((255, 0, 0))
azul = ((0, 0, 255))
cores = [preto, vermelho, azul]

pygame.init()
tela = pygame.display.set_mode(tamanho)

altura = int(input("Digite a altura do tabuleiro: "))
largura = int(input("Digite a largura do tabuleiro: "))

pp = PredadorPresa.Mapa(altura, largura)


# Pinta um quadrado de 3x3 pixels para cada nó
#  como cada nó tem 5 pixels, 2 pixels ficam para a borda da célula
def pintar(x, y, num_cor):
    tela.set_at((x, y), cores[num_cor])
    tela.set_at((x + 1, y), cores[num_cor])
    tela.set_at((x, y + 1), cores[num_cor])
    tela.set_at((x + 1, y + 1), cores[num_cor])
    tela.set_at((x + 2, y), cores[num_cor])
    tela.set_at((x, y + 2), cores[num_cor])
    tela.set_at((x + 2, y + 2), cores[num_cor])
    tela.set_at((x + 2, y + 1), cores[num_cor])
    tela.set_at((x + 1, y + 2), cores[num_cor])


# Pinta as espécies em cada ponto do tabuleiro
def pintar_mapa(tabuleiro):
    pa = pintar
    tamanho = len(tabuleiro)
    for x in range(0, tamanho):
        for y in range(0, tamanho):
            pa(x * 5, y * 5, tabuleiro[x][y].especie)


# Loop de jogo, pinta o mapa e calcula o próximo turno
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            parado = True
            sys.exit(0)
    pintar_mapa(pp.get_tabuleiro())
    pygame.display.flip()
    pp.turno()
