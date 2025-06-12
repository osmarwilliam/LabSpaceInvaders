from PPlay.sprite import *
import config
import pygame
import random

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

# calculo para verificar se o tiro ta dentro da matriz e eliminar os inimigos 
def kill_otimizado(lista_projeteis, matriz_inimigos):
    
    # verifica se a matriz de ininmigos ta vazia e retorna a primeira linha que possui inimigos
    primeira_linha_nao_vazia = next((linha for linha in matriz_inimigos if linha), None)
    if not primeira_linha_nao_vazia:
        #print("matriz vazia")
        return 
    
    # 
    primeiro_inimigo = primeira_linha_nao_vazia[0]
    min_x = primeiro_inimigo.x
    max_x = primeiro_inimigo.x + primeiro_inimigo.width
    min_y = primeiro_inimigo.y
    max_y = primeiro_inimigo.y + primeiro_inimigo.height 
    
    for linha in matriz_inimigos:
        for inimigo in linha:
            if inimigo.x < min_x:
                min_x = inimigo.x
            if inimigo.x + inimigo.width > max_x:
                max_x = inimigo.x + inimigo.width
            if inimigo.y < min_y:
                min_y = inimigo.y
            if inimigo.y + inimigo.height > max_y:
                max_y = inimigo.y + inimigo.height
    
    for projetil in lista_projeteis[:]: 
        if (projetil.x >= min_x and projetil.x <= max_x and
            projetil.y >= min_y and projetil.y <= max_y):
            
            for linha_inimigos in matriz_inimigos:
                for inimigo in linha_inimigos[:]:
                    if projetil.collided(inimigo):
                        lista_projeteis.remove(projetil)
                        linha_inimigos.remove(inimigo)
                        break 
                else:
                    continue
                break

def cria_projetil_inimigo(projetil_inimigos, matriz_inimigos):
    shooting = Sprite("Assets/projetil2.png", 1)
    primeira_linha_nao_vazia = next((linha for linha in matriz_inimigos if linha), None)
    
    if not primeira_linha_nao_vazia:
        return

    pos = random.randint(0, len(primeira_linha_nao_vazia) - 1)
    
    shooting.set_position(primeira_linha_nao_vazia[pos].x, primeira_linha_nao_vazia[pos].y)
    projetil_inimigos.append(shooting)

def draw_tiros_inimigos(projetil_inimigos, vidas_nave, imortal):
    if len(projetil_inimigos) == 0:
        return

    for i in projetil_inimigos:
        i.y += config.janela.delta_time() * 400
        i.draw()
        if (i.y > config.janela.height + i.height):
            projetil_inimigos.remove(i)

        if i.collided(naveMae) and not imortal:
            projetil_inimigos.remove(i)
            return True
            


# inicia o jogo
def start():

    clock = pygame.time.Clock()
    cronometro = 0
    tempo = 0

    
    # a quantidade de vidas da nave
    vidas_nave = 3

    # respawn cooldown
    respawn_cooldown = 2

    # configuações iniciais do jogo
    projetil_inimigos= []
    projetil = []
    vel_NaveMae = 1000
    tempo_recarga_tiro_inimigos = 1
    tempo_recarga_tiro_player = 0.150
    vel_Projetil = 200
    vel_Inimigos = 400
    matrizDeInimigos = []
    direcao_inimigos = 1
    MAX_DELTA_TIME = 1/15.0
    linha = 4
    coluna = 4
    tempo_respawn = 0

    # algumas variaveis que lidam caso o player tenha sido atingido
    imortal = False
    esta_visivel = True
    intervalo_piscar = 0.2
    tempo_total = 0

    while (True):
        config.janela.set_background_color((0,0,0))
        
        # para mostrar o fps na tela
        cronometro += config.janela.delta_time()
        tempo += config.janela.delta_time()
        fps = int(clock.get_fps())
        config.janela.draw_text(f"FPS: {fps}", 10, 5, size = 20, color=(255,255,255), font_name="Arial", bold=True, italic=False)     
        
        if esta_visivel:
            naveMae.draw()
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break

        if (config.teclado.key_pressed("SPACE") and cronometro > tempo_recarga_tiro_player):
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
            criar_matriz_inimigos(matrizDeInimigos, linha,coluna)
        
        # controla o movimento da matriz de inimigos
        direcao_inimigos = mover_inimigos(matrizDeInimigos, vel_Inimigos, direcao_inimigos)
        
        # desenha a matriz de inimigos
        draw_inimigos(matrizDeInimigos)
        
        kill_otimizado(projetil, matrizDeInimigos)

        # cria tiros inimigos
        if (tempo > tempo_recarga_tiro_inimigos):
            tempo = 0
            cria_projetil_inimigo(projetil_inimigos, matrizDeInimigos)
        
        # move os tiros inimigos e verifica se bateu na nave Mae
        bateu = draw_tiros_inimigos(projetil_inimigos, vidas_nave, imortal)

        if (bateu):
            imortal = True
            print(f"número de vidas:{vidas_nave}")
            vidas_nave -= 1
            if (vidas_nave == 0):
                jogo_acabou()

        if (imortal):
            tempo_respawn += config.janela.delta_time()
            tempo_total += config.janela.delta_time()
            if (tempo_respawn > respawn_cooldown):
                imortal = False
                tempo_respawn = 0
                esta_visivel = True
            else:
                if (tempo_total > intervalo_piscar):
                    tempo_total = 0
                    esta_visivel = not(esta_visivel)
                    naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)


        clock.tick(120)
        config.janela.update()