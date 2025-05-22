from PPlay.sprite import *
import config
import pygame


naveMae = Sprite("Assets/nave.png", 1)
naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)

def criarProjetil(projetil):
    shooting = Sprite("Assets/tiro.png", 1)
    shooting.set_position(naveMae.x + naveMae.width/2 - 5, (naveMae.y - 10))
    projetil.append(shooting)


def criar_matriz_inimigos(inimigos, linhas,colunas, espacamento_x, espacamento_y):

    x_inicial = (espacamento_x) / 2 
    y_inicial = 5


    for linha in range(linhas):
        new_inimigos = []
        for coluna in range(colunas):
            inimigos_image = Sprite("Assets/button2.png", 1)

            x = x_inicial + coluna * espacamento_x
            y = y_inicial + linha * espacamento_y
            print(f'x = {x_inicial}')
            print(f'y = {y_inicial}')
            inimigos_image.set_position(x,y)
            new_inimigos.append(inimigos_image)
        inimigos.append(new_inimigos)

def draw_inimigos(matrizDeInimigos):
    for linha in matrizDeInimigos:
        for inimigo in linha:
            inimigo.draw()

def mover_inimigos(matriz_inimigos, velocidadeInimigos):
    bateu = False
    
    for linha in matriz_inimigos:
        for inimigo in linha:
            inimigo.x += velocidadeInimigos * config.janela.delta_time()
                # implementar o modo caso a matriz tenha batido com a lateral
                #if ():
            bateu = True
    #if (bateu):




def start():
    clock = pygame.time.Clock()
    matriz_inimigos = False

    projetil = []
    vel_NaveMae = 1000
    cronometro = 0
    tempo_recarga = 0.150
    vel_Projetil = 200
    vel_Inimigos = 100

    matrizDeInimigos = []



    while (True):
        config.janela.set_background_color((0,0,0))
        cronometro += config.janela.delta_time()

        fps = int(clock.get_fps())
        print(f'fps: {fps}')
        config.janela.draw_text(f"FPS: {fps}", 10, 5, size = 20, color=(255,255,255), font_name="Arial", bold=True, italic=False)     


        #config.janela.draw_text("press ESC to exit", 50, 50, size = 50, color=(0,0,255), font_name= "Arial", bold= True, italic = False)
        naveMae.draw()
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break

        if (config.teclado.key_pressed("SPACE") and cronometro > tempo_recarga):
            criarProjetil(projetil)
            cronometro = 0

        if (naveMae.x <= 0):
            naveMae.x = 0
        if (config.teclado.key_pressed("A")):
            naveMae.x -= config.janela.delta_time() * vel_NaveMae

        if (config.teclado.key_pressed("D") and naveMae.x < config.janela.width - naveMae.width):
            naveMae.x += config.janela.delta_time() * vel_NaveMae

        for i in projetil:
            i.y -= config.janela.delta_time() * vel_Projetil
            i.draw()
            if (i.y < 0 - i.height):
                projetil.remove(i)
        
        #if not matriz_inimigos:
        #   criar_matriz_inimigos(matrizDeInimigos, 4,5,60, 48)
        #  matriz_inimigos = True
        if (len(matrizDeInimigos) == 0):
            criar_matriz_inimigos(matrizDeInimigos, 4,5,50, 60)

        draw_inimigos(matrizDeInimigos)
        
        mover_inimigos(matrizDeInimigos, vel_Inimigos)
        clock.tick()
        config.janela.update()