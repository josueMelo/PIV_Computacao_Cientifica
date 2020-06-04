# -*- coding: utf-8 -*-
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
import random
import sys
import copy
from Automatos_Celulares import Simulacao as sim
#random.seed(None)

print("PI V - CIÊNCIA DA COMPUTAÇÃO - SENAC - SIMULAÇÃO DE AUTOMATOS CELULARES", "\n"
      "GRUPO 3 - LUCAS SOUTO, HIGOR VIANA, JOSUE MELO E YGOR KAIQUE", "\n")

# Altura do tabuleiro | largura do tabuleiro
altura = int(input("Digite a altura do tabuleiro: "))
largura = int(input("Digite a largura do tabuleiro: "))

# Tamanho do tabuleiro (quantidade de células)
N = altura*largura

# Número inicial de indivíduos infectados, recuperados e mortos, I0, R0 e M0
I, R, M = 1, 0, 0
# Todos os outros, S0, são suscetíveis à infeção inicialmente.
S = N - I - R - M

beta = float(input("Digite o valor da taxa de infecção beta(quantidade infectada/10 mil pessoas): "))
beta = beta/10000
gama = float(input("Digite o valor da taxa de recuperação gama(%): "))
gama = gama/100
Lambda = float(input("Digite o valor da taxa de mortalidade lambda(%): "))
Lambda = Lambda/100
# Quantidade de pontos que queremos monitorar (dias)
q = int(input("Digite o valor de dias que serão monitorados na simulação: "))
eventos = range(0, q)
# Quantidade de pontos a integrar (intervalo de integração)
pontos = [0, 1001]

# Sistema de equações diferenciais
def deriv(t, y, N, beta, gama, Lambda):
    S, I, R, M = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gama * I - Lambda * I
    dRdt = gama * I 
    dMdt = Lambda * I
    return dSdt, dIdt, dRdt, dMdt

mapa = sim.Mapa()
mapa.altura = 10
mapa.largura = 10
