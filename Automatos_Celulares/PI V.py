import random
import pygame

infec = 10 # número entre 0 e 1: infectabilidade
viagem = 5 # n em um 10000
velocidade = 2  # milisegundos
mortes = 11    # n em 10000
rec = 15   # n em 10000
vls = [velocidade,infec,mortes,rec,viagem]
vls0 = [velocidade,infec,mortes,rec,viagem]
pontos =[ 0  for x in range(100*100)]
histEst = []
def infect(b):
    pontos[b] = 1


pygame.init()
 
size = [1710, 1010]
screen = pygame.display.set_mode(size)
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GREY =  (200, 200, 200)


class Slider():
    def __init__(self, txt, location,whome, action, bg=WHITE, fg=BLACK, size=(2, 20), font_name="Segoe Print", font_size=16):
        self.color = bg  # cor estática (normal)
        self.bg = bg  # cor de fundo real, pode mudar com o mouse
        self.fg = fg  # cor do texto
        self.size = size
        self.whome = whome 
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action
    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # passe o mouse sobre a cor

    def call_back(self):
        self.call_back_(self.whome)


class Button():
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(500, 50), font_name="freesansbold.ttf", font_size=52):
        self.color = bg  # cor estatica (normal)
        self.bg = bg  # cor de fundo real, pode mudar com o mouse
        self.fg = fg  # cor do texto
        self.size = size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREEN # passe o mouse sobre a cor

    def call_back(self):
        self.call_back_()

def infect_prim():

    for x in range(len(pontos)): # defina todos os valores para 0 = íntegro
        pontos[x] = 0

    for x in range(102): # desenhe as linhas
        pygame.draw.line(screen, GREY, [x*10, 0], [x*10,1010], 1)
    for y in range(102):
        pygame.draw.line(screen, GREY, [0, y*10], [1010,y*10], 1)
            
    # infectar o primeiro ponto
    while True:
        i = random.randint(0,len(pontos)-1); 
        if pontos[i] == 0:
            infect(i)
            break
def reset():
    infect_prim()


    for i in range(len(vls)):
        vls[i]=vls0[i] # isso deve redefinir todos os valores
        #se izpis
        slid([i,vls0[i]])

def restart():
    # infecta o primeiro individuo
    infect_prim()


def slid(t):        
    vls[t[0]]=t[1] # Atualização de valores dos parametros

    if t[0]==0:
        besedilo = "Velocidade: "
    elif t[0]==1:
        besedilo = "Infecção: "
    elif t[0]==2:
        besedilo = "Letalidade: "
    elif t[0]==3:
        besedilo = "Recuperados:"
    elif t[0]==4:
        besedilo = "Percorre: "
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(besedilo+str(t[1]), True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.center= (1220,(t[0]+2)*70)
    pygame.draw.line(screen, WHITE, [1012, (t[0]+2)*70],  [1395, (t[0]+2)*70], 50)
    screen.blit(text, textRect)



def mousebuttondown():
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()
    for slider in sliders:
        if slider.rect.collidepoint(pos):
            slider.call_back()

screen.fill(WHITE)
reset()

pygame.display.set_caption("Simulador de SIR")
 
done = False
clock = pygame.time.Clock()

#buttons
button_01 = Button("Reiniciar", (1350,570), reset,bg= (150,150,150))
#button_02 = Button("Restart!", (1350,500), restart,bg= GREY)
#button_03 = Button("Simulador de SIR", (1350,50), reset,bg= (250,50,50))
buttons = [button_01]

#controles deslizantes
sliders = []
for n in range(5):
    for x in range(100):
        sliders.append(Slider("", (1400+x*2, (n+2)*70),[n,x], slid, bg=(2*x+50, 250-x,20)))


while not done:
    if vls[0] == 0:
        pygame.time.wait(1000)
    elif vls[0] != 99:
        pygame.time.wait(int(100/vls[0])) 


    for i in range(100*100): 
        if pontos[i] == 1: # 1 significa que o ponto está infectado 
        #infecte os que estão ao seu redor
            for n in [1,-1, 100,-100, 101,99, -101, -99]: #todos os vizinhos
                if (i+n > 0) and (i+n < 100*100):
                    if pontos[i+n] == 0:
                        if random.randint(0,100) < vls[1]: # Não lavou as mãos 
                            infect(i+n)

            if random.randint(0,10000) < vls[2]:# mortos
                pontos[i] = 2 
            if random.randint(0,10000) < vls[3]: #recuperados
                pontos[i] = 3

    #viagem
    for i in range(100*100):
         if (pontos[i] != -1) and (pontos[i] != 2): # deve estar vivo para viagem
            if random.randint(0,100000) < vls[4]: 
                ni = random.randint(0,len(pontos)-1)
                if (pontos[ni] != -1) and (pontos[ni] != 2):
                    op = pontos[ni]  # alternar os dois pontos
                    pontos[ni] = pontos[i]
                    pontos[i]  = op

    # desenhe e obtenha estatísticas para um gráfico 
    # 0 pontos saudáveis 1 pontos infectados 2 pontos mortos 3 pontos recuperados
    stats = [0,0,0,0]
    color = [GREEN, RED, BLACK, BLUE]
    for i in range(len(pontos)):
        y = i//100
        x = i - (i//100)*100

        if pontos[i] == 0:
            stats[0] += 1
            pygame.draw.circle(screen, GREEN, [5+x*10, 5+y*10], 4)
        elif pontos[i] == 1:
            stats[1] += 1
            pygame.draw.circle(screen, RED, [5+x*10, 5+y*10], 4)
        elif pontos[i] == 2:
            stats[2] += 1
            pygame.draw.circle(screen,  BLACK, [5+x*10, 5+y*10], 4)
        elif pontos[i] == 3:
            stats[3] += 1
            pygame.draw.circle(screen,  BLUE, [5+x*10, 5+y*10], 4)
    # desenha o grafico
    pontosum = sum(stats)
    histEst.append(stats)
    for n in range(len(histEst)):
        x = n*2+1014 # gráfico está no lado direito do main principal
        y = 0
        hy = 0
        for v in range(4):
            y += (histEst[n][v]*400)/pontosum
            pygame.draw.line(screen, color[v], [x,hy+600], [x,y+600], 4)
            hy = y
    if len(histEst) > 350:
        histEst.pop(0)




    for event in pygame.event.get(): # Usuario fez algo
        if event.type == pygame.QUIT: # Se o usuario clicou em fechar
            done=True # Sinalize que terminamos, então saímos desse loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown()

    for button in buttons:
        button.draw()
    for slider in sliders:
        slider.draw()
    pygame.display.flip()
 
pygame.quit()