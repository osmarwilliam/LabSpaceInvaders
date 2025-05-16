# O código funcionava normalmente.

# Mas, foi necessário apenas a modularização do código, visto que inicialmente só existia um arquivo principal,

# criei o diretório states, nele adicionei alguns estados do jogo. Para facilitar o controle.

# mudei o nome do arquivo principal de "menu.py" para "main.py"

# Para algum dos botões na tela menu é necessário clicar na bola vermelha ao lado esquerdo,
# isso por que os textos não são sprites, algo que vou alterar mais para frente, quando tiver tempo

# Criei um arquivo "config.py" para colocar algumas configurações globais que serão utilizadas em cada segmento do

# O código não estava comentando quando recebi, terei que adicionar os comentários, embora que,
# era um código de fácil compreensão.

# falta algumas configurações como ao clicar no ranking o jogo automaticamente fecha

# tirei algumas redundâncias, possivelmente há outras

from PPlay.sprite import *
import states.jogo as jogo
import config


play_button = Sprite("Assets/button2.png", 1)
diff_button = Sprite("Assets/button2.png", 1)
ranking_button = Sprite("Assets/button2.png", 1)
exit_button = Sprite("Assets/button2.png", 1)
play_button.set_position(350, 100,)
diff_button.set_position(350, 200,)
ranking_button.set_position(350, 300,)
exit_button.set_position(350, 400,)

diff = 1


def menu():

    
    config.janela.set_background_color((200,200,200))
    config.janela.draw_text("play", 400, 100, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("difficulty", 400, 200, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("ranking", 400, 300, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
    config.janela.draw_text("exit", 400, 400, size = 50, color=(0,0,0), font_name= "Arial", bold= True, italic = False)
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
            config.janela.close()
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



while True:
    menu()
    print("a")
    if config.estado == 1:
        config.janela.set_background_color((200,200,200))
        jogo.start()
    if config.estado == 2:
        config.janela.set_background_color((100,100,100))
        diff()
    
    config.janela.update()

