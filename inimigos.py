from PPlay.sprite import *
import config
import pygame
import random
import jogo
import ranking

# quanto a nave irá descer após bater nas paredes laterais
descida_inimigos = 30

# função para criar os projeteis
def criarProjetil(projetil):
    shooting = Sprite("Assets/tiro.png", 1)
    shooting.set_position(jogo.naveMae.x + jogo.naveMae.width/2 - 5, (jogo.naveMae.y - 10))
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
            if inimigo.y > config.janela.height or inimigo.collided(jogo.naveMae):
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
    # seta tudo para o padrão

    config.janela.set_background_color((0,0,0))
    config.janela.draw_text("GAME OVER", config.janela.width/2- 200, config.janela.height/2 - 50, size = 60, color=(255,255,255), font_name= "Arial", bold= True, italic = False)
    config.janela.update() 
    
    nome = input("Digite o seu nome: ")
    ranking.salvar_pontuação( nome, config.inimigos_mortos)

    config.default()
    
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
                        config.inimigos_mortos += 1
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
        i.y += config.janela.delta_time() * config.vel_projetil_inimigo
        i.draw()
        if (i.y > config.janela.height + i.height):
            projetil_inimigos.remove(i)

        if i.collided(jogo.naveMae) and not imortal:
            projetil_inimigos.remove(i)
            return True
            
