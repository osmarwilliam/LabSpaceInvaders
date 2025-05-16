from PPlay.sprite import *
import config



naveMae = Sprite("Assets/nave.png", 1)
naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)

def criarProjetil(projetil):
    shooting = Sprite("Assets/tiro.png", 1)
    shooting.set_position(naveMae.x + naveMae.width/2 - 5, (naveMae.y - 10))
    projetil.append(shooting)

def start():

    projetil = []
    vel_NaveMae = 1000
    cronometro = 0
    tempo_recarga = 0
    vel_Projetil = 200

    while (True):
        print("b")
        config.janela.set_background_color((0,0,0))

        cronometro += config.janela.delta_time()


        config.janela.draw_text("press ESC to exit", 50, 50, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
        naveMae.draw()
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break

        if (config.teclado.key_pressed("SPACE") and cronometro > tempo_recarga):
            criarProjetil(projetil)
            tempo_recarga = 0.350
            cronometro = 0

        if (config.teclado.key_pressed("A") and naveMae.x > 0):
            naveMae.x -= config.janela.delta_time() * vel_NaveMae

        if (config.teclado.key_pressed("D") and naveMae.x < config.janela.width - naveMae.width):
            naveMae.x += config.janela.delta_time() * vel_NaveMae

        for i in projetil:
            i.y -= config.janela.delta_time() * vel_Projetil
            i.draw()
            if (i.y < 0 - i.height):
                projetil.remove(i)

        config.janela.update()