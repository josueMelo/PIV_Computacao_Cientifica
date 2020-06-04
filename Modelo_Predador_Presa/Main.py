# %%

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# %%
phi = 1.0  # taxa de crescimento dos vegetais sem predador
x = 0.05  # chance de um coelho achar um vegetal
alfa = 0.8  # Taxa de crescimento dos coelhos sem predador
beta = 0.1  # Chance de uma raposa encontrar um coelho
gama = 0.75  # Taxa de crecimento das raposas com alimento
delta = 1.5  # Taxa de morte por inanição das raposas


# %%

# Sistema de equações difrenciais
def deriv(P, t):
    v, c, r = P  # Valores das populações
    dvdt = phi * v - x * c * v  # taxa de variação no tempo
    dcdt = alfa * c * phi - beta * c * r  # taxa de variação no tempo
    drdt = gama * r * beta * c - delta * r  # taxa de variação no tempo
    return dvdt, dcdt, drdt


# %%

# intervalo de integração (18 meses com 1000 pontos)
t = np.linspace(0, 18, 1000)

# população inicial (15 vegetais, 10 coelhos e 5 raposas)
P0 = [15, 10, 5]

# computa a solução do sistema de equações diferenciais
sol = odeint(deriv, P0, t)

vegetais = sol[:, 0]  # Solução numerica para vegetais
coelhos = sol[:, 1]  # Solução numerica para coelhos
raposas = sol[:, 2]  # Solução numerica para raposas

plt.plot(t, vegetais, label="Vegetais")  # Plot dos valores da solução em relação aos vegetais
plt.plot(t, coelhos, label="Coelhos")  # Plot dos valores da solução em relação aos coelhos
plt.plot(t, raposas, label="Raposas")  # Plot dos valores da solução em relação as raposas

plt.xlabel("Tempo (meses)")  # Plano X de representação do tempo
plt.ylabel("População")  # Plano Y de representação da população das soluções

plt.legend()  # Plotar legenda
plt.show()  # Plotar gráfico
