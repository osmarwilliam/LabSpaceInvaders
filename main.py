from PPlay.sprite import *
import jogo as jogo
import config
import ranking as ranking

play_button = Sprite("Assets/button2.png", 1)
diff_button = Sprite("Assets/button2.png", 1)
ranking_button = Sprite("Assets/button2.png", 1)
exit_button = Sprite("Assets/button2.png", 1)
play_button.set_position(300, 100,)
diff_button.set_position(300, 200,)
ranking_button.set_position(300, 300,)
exit_button.set_position(300, 400,)

facil_button = Sprite("Assets/button2.png", 1)
medio_button = Sprite("Assets/button2.png", 1)
hard_button = Sprite("Assets/button2.png", 1)

facil_button.set_position(350, 150,)
medio_button.set_position(350, 250,)
hard_button.set_position(350, 350,)
diff = 1

def menu():

    config.janela.set_background_color((200,200,200))
    config.janela.draw_text("play", 350, 100, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("difficulty", 350, 200, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("ranking", 350, 300, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("exit", 350, 400, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    click = False
    if config.mouse.is_button_pressed(1):
        click = True

    if config.mouse.is_over_object(play_button):
        if click:
            config.estado = 1
    
    if config.mouse.is_over_object(exit_button):
        if click:
            config.janela.close()
    
    if config.mouse.is_over_object(ranking_button):
        if click:
            config.estado = 3
    if config.mouse.is_over_object(diff_button):
        if click:
            config.estado = 2

    play_button.draw()
    diff_button.draw()
    ranking_button.draw()
    exit_button.draw()


def diff():
    config.janela.draw_text("facil", 400, 150, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("medio", 400, 250, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("dificil", 400, 350, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    if (config.teclado.key_pressed("ESC")):
        config.estado = 0
    
    click = False
    if config.mouse.is_button_pressed(1):
        click = True
    
    if config.mouse.is_over_object(facil_button):
        if click:
            config.tempo_recarga_tiro_player = 0.150
            config.vel_Projetil_player = 200
            config.vel_Inimigos = 400
            config.vel_projetil_inimigo = 400
            jogo.start()

    if config.mouse.is_over_object(medio_button):
        if click:
            config.tempo_recarga_tiro_player = 0.250
            config.vel_Projetil_player = 200
            config.vel_Inimigos = 500
            config.vel_projetil_inimigo = 450
            jogo.start()
    
    if config.mouse.is_over_object(hard_button):
        if click:
            config.tempo_recarga_tiro_player = 0.350
            config.vel_Projetil_player = 170
            config.vel_Inimigos = 600
            config.vel_projetil_inimigo = 475
            jogo.start()
    
    facil_button.draw()
    hard_button.draw()
    medio_button.draw()


while True:
    menu()
    

    if config.estado == 1:
        config.janela.set_background_color((200,200,200))
        jogo.start()
    if config.estado == 2:
        config.janela.set_background_color((100,100,100))
        diff()
    if config.estado == 3:
        ranking.ranking()

    config.janela.update()

