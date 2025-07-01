from PPlay.window import *
import config

estado = 0
janela = Window(940, 820)
teclado = janela.get_keyboard()
mouse = janela.get_mouse()

# lidam com o tempo
cronometro = 0
tempo = 0
 
# a quantidade de vidas da nave
vidas_nave = 3

# respawn cooldown
respawn_cooldown = 2

 # configuações iniciais do jogo
projetil_inimigos= []
projetil = []
matrizDeInimigos = []

inimigos_mortos = 0

vel_NaveMae = 1000
tempo_recarga_tiro_player = 0.150
vel_Projetil_player = 200
tempo_respawn = 0
direcao_inimigos = 1
MAX_DELTA_TIME = 1/15.0

coluna = 4
linha = 4
tempo_recarga_tiro_inimigos = 1
vel_Inimigos = 400
vel_projetil_inimigo = 400

 # algumas variaveis que lidam caso o player tenha sido atingido
imortal = False
esta_visivel = True
intervalo_piscar = 0.2
tempo_total = 0

# quanto a nave irá descer após bater nas paredes laterais
descida_inimigos = 30


def default():
    # reinicia as configuações do jogo

    # a quantidade de vidas da nave
    config.vidas_nave = 3

     # configuações iniciais do jogo
    config.projetil_inimigos= []
    config.projetil = []
    config.matrizDeInimigos = []

    config.inimigos_mortos = 0

    config.vel_NaveMae = 1000
    config.tempo_recarga_tiro_player = 0.150
    config.vel_Projetil_player = 200
    config.tempo_respawn = 0
    config.direcao_inimigos = 1

    config.tempo_recarga_tiro_inimigos = 1
    config.vel_Inimigos = 400
    config.vel_projetil_inimigo = 400

     # algumas variaveis que lidam caso o player tenha sido atingido
    config.imortal = False
    config.esta_visivel = True
    config.intervalo_piscar = 0.2
    config.tempo_total = 0