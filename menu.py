from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *

estado = 0
janela = Window(920, 600)
teclado = janela.get_keyboard()
mouse = janela.get_mouse()
play_button = Sprite("Assets/button2.png", 1)
diff_button = Sprite("Assets/button2.png", 1)
ranking_button = Sprite("Assets/button2.png", 1)
exit_button = Sprite("Assets/button2.png", 1)
play_button.set_position(350, 100,)
diff_button.set_position(350, 200,)
ranking_button.set_position(350, 300,)
exit_button.set_position(350, 400,)
janela.set_background_color((200,200,200))
teclado = janela.get_keyboard()
mouse = janela.get_mouse()
diff = 1
naveMae = Sprite("Assets/button2.png", 1)
naveMae.set_position((janela.width - naveMae.width)/2, janela.height - 50)

def menu():

    janela.set_background_color((200,200,200))
    global estado
    janela.draw_text("play", 400, 100, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    janela.draw_text("difficulty", 400, 200, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    janela.draw_text("ranking", 400, 300, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    janela.draw_text("exit", 400, 400, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    click = False
    if mouse.is_button_pressed(1):
        click = True
    if mouse.is_over_object(play_button):
        if click:
            estado = 1
    if mouse.is_over_object(exit_button):
        if click:
            janela.close()
    if mouse.is_over_object(ranking_button):
        if click:
            janela.close()
            
    if mouse.is_over_object(diff_button):
        if click:
            estado = 2
    play_button.draw()
    diff_button.draw()
    ranking_button.draw()
    exit_button.draw()
    mouse.x, mouse.y = mouse.get_position()
    
    
def start():
    projetil = []
    vel_NaveMae = 1000
    cronometro = 0
    tempo_recarga = 0
    vel_Projetil = 200


    while (True):
        janela.set_background_color((0,0,0))

        cronometro += janela.delta_time()

        global estado

        janela.draw_text("press ESC to exit", 50, 50, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
        naveMae.draw()
        if (teclado.key_pressed("ESC")):
            estado = 0
            break

        if (teclado.key_pressed("SPACE") and cronometro > tempo_recarga):
            criarProjetil(projetil)
            tempo_recarga = 0.350
            cronometro = 0

        if (teclado.key_pressed("A") and naveMae.x > 0):
            naveMae.x -= janela.delta_time() * vel_NaveMae

        if (teclado.key_pressed("D") and naveMae.x < janela.width - naveMae.width):
            naveMae.x += janela.delta_time() * vel_NaveMae

        for i in projetil:
            i.y -= janela.delta_time() * vel_Projetil
            i.draw()
            if (i.y < 0 - i.height):
                projetil.remove(i)

        janela.update()

def criarProjetil(projetil):
    shooting = Sprite("Assets/button2.png", 1)
    shooting.set_position(naveMae.x , (naveMae.y - naveMae.height))
    projetil.append(shooting)

def diff():
    global estado
    janela.draw_text("facil", 400, 150, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    janela.draw_text("medio", 400, 250, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    janela.draw_text("dificil", 400, 350, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    if (teclado.key_pressed("ESC")):
        estado = 0



while True:
    menu()
    if estado == 1:
        janela.set_background_color((200,200,200))
        start()
    if estado == 2:
        janela.set_background_color((100,100,100))
        diff()
    
    janela.update()

