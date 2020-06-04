from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt

print("PIV - CIENCIA DA COMPUTAÇÃO - SENAC - Estudo de Modelagem Epidêmica SIR", "\n"
                                                                                 "GRUPO 3 - LUCAS SOUTO, HIGOR VIANA, JOSUE MELO E YGOR KAIQUE",
      "\n")

# Para implementação dos Mortos foi utilizada a seguinte formula:
# M(t + deltat) = M(t) + lambda * I
# dM/dt = lambda * I
# onde lambda é a taxa de mortalidade
# Com dIdt = beta * S * I - gama * I - Lambda * I

# População total, N.
N = int(input("Digite a quantidade da população: "))
# Número inicial de indivíduos infectados, recuperados e mortos, I0, R0 e M0
I0, R0, M0 = 1, 0, 0
# Todos os outros, S0, são suscetíveis à infeção inicialmente.
S0 = N - I0 - R0 - M0
# Taxa de infecção (beta), taxa média de recuperação (gamma), e taxa de mortalidade (lambda)
beta = float(input("Digite o valor da taxa de infecção beta(quantidade infectada/10 mil pessoas): "))
beta = beta / 10000
gama = float(input("Digite o valor da taxa de recuperação gama(%): "))
gama = gama / 100
Lambda = float(input("Digite o valor da taxa de mortalidade lambda(%): "))
Lambda = Lambda / 100
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


# Vetor de condições iniciais
y0 = S0, I0, R0, M0

# Escolha do metodo de integração que sera utilizado
print("Escolha o método que será utilizado na simulação: ", "\n",
      "1)Runge-Kutta de ordem 5", "\n",
      "2)Runge-Kutta de ordem 3", "\n",
      "3)Runge-Kutta de ordem 8", "\n",
      "4)Runge-Kutta da família Radau de ordem 5", "\n",
      "5)Método implícito de ordem variável em várias etapas (1 a 5)", "\n",
      "6)Método Adams / BDF")
escolha = int(input("O metodo escolhido é: "))
if (escolha == 1):
    m = 'RK45'
elif (escolha == 2):
    m = 'RK23'
elif (escolha == 3):
    m = 'DOP853'
elif (escolha == 4):
    m = 'Radau'
elif (escolha == 5):
    m = 'BDF'
elif (escolha == 6):
    m = 'LSODA'

# Integração das equações do modelo pela grade de tempo, t.
sol = solve_ivp(deriv, pontos, y0, args=(N, beta, gama, Lambda), t_eval=eventos, method=m)


# Plota os dados em quatro curvas diferentes para S(t), I(t), R(t) e M(t)
def plot(sol):
    graf = plt.figure(facecolor='w')
    plt.title("GRÁFICO DA SIMULAÇÃO")
    plt.xlabel('Tempo /dias')
    plt.ylabel('Indivíduos')
    plt.plot(sol.t, sol.y[0], 'b', label='Suscetíveis')
    plt.plot(sol.t, sol.y[1], 'r', label='Infectados')
    plt.plot(sol.t, sol.y[2], 'g', label='Recuperados')
    plt.plot(sol.t, sol.y[3], 'k', label='Mortos')
    plt.legend(loc='right', shadow=False)
    plt.show()


plot(sol)
