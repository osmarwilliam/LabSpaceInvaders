from PPlay.sprite import *
import config
import pygame

# quanto a nave irá descer após bater nas paredes laterais
descida_inimigos = 30

# cria o sprite e seta a posicção da nave mãe
naveMae = Sprite("Assets/nave.png", 1)
naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)

# função para criar os projeteis
def criarProjetil(projetil):
    shooting = Sprite("Assets/tiro.png", 1)
    shooting.set_position(naveMae.x + naveMae.width/2 - 5, (naveMae.y - 10))
    projetil.append(shooting)


# função para criar a matriz de inimigos
def criar_matriz_inimigos(matriz_inimigos, linhas, colunas):
    
    inimigo_exemplo = Sprite("Assets/inimigo.png", 1)

    espaco_x = inimigo_exemplo.width + inimigo_exemplo.width / 2
    espaco_y = inimigo_exemplo.width + inimigo_exemplo.height /2

    x_inicial = 10
    y_inicial = 10 

    for linha in range(linhas):
        linha_inimigos = [] 
        for coluna in range(colunas):
            inimigo_sprite = Sprite("Assets/inimigo.png", 1)

            x = x_inicial + coluna * espaco_x
            y = y_inicial + linha * espaco_y 

            inimigo_sprite.set_position(x, y)
            linha_inimigos.append(inimigo_sprite)
        matriz_inimigos.append(linha_inimigos)

# função para desenhar a matriz de inimigos
def draw_inimigos(matrizDeInimigos):
    for linha in matrizDeInimigos:
        for inimigo in linha:
            inimigo.draw()

# função para mover a matriz de inimigos
def mover_inimigos(matriz_inimigos, velocidadeInimigos, direcao_atual):
    bateu = False
    for linha in matriz_inimigos:
        for inimigo in linha:
            inimigo.x += velocidadeInimigos * config.janela.delta_time() * direcao_atual
            if ((inimigo.x + inimigo.width >= config.janela.width) or (inimigo.x <= 0)):
                bateu = True
            if inimigo.y > config.janela.height or inimigo.collided(naveMae):
                jogo_acabou()

    if (bateu):
        direcao_atual *= -1
        for linha in matriz_inimigos:
            for inimigos in linha:
                inimigos.y += descida_inimigos
                if direcao_atual == 1:
                    if inimigos.x + inimigos.width > config.janela.width:
                        inimigos.x = config.janela.width - inimigos.width - 2
                elif direcao_atual == -1:
                    if inimigos.x < 0:
                        inimigos.x = 0
    
    return direcao_atual

def jogo_acabou():
    while True:
        config.janela.set_background_color((0,0,0))

        config.janela.draw_text("GAME OVER", config.janela.width/2- 200, config.janela.height/2 - 50, size = 60, color=(255,255,255), font_name= "Arial", bold= True, italic = False)

        config.janela.update() 

        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break

def kill(listaProjeteis,matrizDeInimigos):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                    if (projetil.collided(inimigo)):
                        listaProjeteis.pop(j)
                        linhaDeInimigos.pop(i)

# inicia o jogo
def start():

    clock = pygame.time.Clock()
    cronometro = 0

    # configuações iniciais do jogo
    projetil = []
    vel_NaveMae = 1000
    tempo_recarga = 0.150
    vel_Projetil = 200
    vel_Inimigos = 600
    matrizDeInimigos = []
    direcao_inimigos = 1
    MAX_DELTA_TIME = 1/15.0
    
    while (True):
        config.janela.set_background_color((0,0,0))
        
        # para mostrar o fps na tela
        cronometro += config.janela.delta_time()
        fps = int(clock.get_fps())
        config.janela.draw_text(f"FPS: {fps}", 10, 5, size = 20, color=(255,255,255), font_name="Arial", bold=True, italic=False)     
        

        naveMae.draw()
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break

        if (config.teclado.key_pressed("SPACE") and cronometro > tempo_recarga):
            criarProjetil(projetil)
            cronometro = 0

        # movimento da nave mãe
        if (naveMae.x <= 0):
            naveMae.x = 0
        if (config.teclado.key_pressed("A")):
            naveMae.x -= config.janela.delta_time() * vel_NaveMae

        if (config.teclado.key_pressed("D") and naveMae.x < config.janela.width - naveMae.width):
            naveMae.x += config.janela.delta_time() * vel_NaveMae

        # desenha o projetil
        for i in projetil:
            i.y -= config.janela.delta_time() * vel_Projetil
            i.draw()
            if (i.y < 0 - i.height):
                projetil.remove(i)
        
        # cria matriz de inimigos
        if (len(matrizDeInimigos) == 0):
            criar_matriz_inimigos(matrizDeInimigos, 4,4)
        
        # controla o movimento da matriz de inimigos
        direcao_inimigos = mover_inimigos(matrizDeInimigos, vel_Inimigos, direcao_inimigos)
        
        # desenha a matriz de inimigos
        draw_inimigos(matrizDeInimigos)

        kill(projetil,matrizDeInimigos)


        clock.tick(60)
        config.janela.update()