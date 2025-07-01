from PPlay.sprite import *
import config
import pygame
import inimigos

# cria o sprite e seta a posicção da nave mãe
naveMae = Sprite("Assets/nave.png", 1)
naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)

# inicia o jogo
def start():

    clock = pygame.time.Clock()

    while (True):
        config.janela.set_background_color((0,0,0))
        
        # para mostrar o fps na tela
        config.cronometro += config.janela.delta_time()
        config.tempo += config.janela.delta_time()
        fps = int(clock.get_fps())
        config.janela.draw_text(f"FPS: {fps}", 10, 5, size = 15, color=(255,255,255), font_name="Arial", bold=True, italic=False)     
        config.janela.draw_text(f"Vidas: {config.vidas_nave}", 10, 30, size = 15, color=(255,255,255), font_name="Arial", bold=True, italic=False)     
        config.janela.draw_text(f"Points: {config.inimigos_mortos}", 10, 50, size = 15, color=(255,255,255), font_name="Arial", bold=True, italic=False)     

        if config.esta_visivel:
            naveMae.draw()
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break
        if (config.teclado.key_pressed("SPACE") and config.cronometro > config.tempo_recarga_tiro_player):
            inimigos.criarProjetil(config.projetil)
            config.cronometro = 0

        # movimento da nave mãe
        if (naveMae.x <= 0):
            naveMae.x = 0
        if (config.teclado.key_pressed("A")):
            naveMae.x -= config.janela.delta_time() * config.vel_NaveMae

        if (config.teclado.key_pressed("D") and naveMae.x < config.janela.width - naveMae.width):
            naveMae.x += config.janela.delta_time() * config.vel_NaveMae

        # desenha o projetil
        for i in config.projetil:
            i.y -= config.janela.delta_time() * config.vel_Projetil_player
            i.draw()
            if (i.y < 0 - i.height):
                config.projetil.remove(i)
        
        # cria matriz de inimigos
        if (len(config.matrizDeInimigos) == 0):
            inimigos.criar_matriz_inimigos(config.matrizDeInimigos, config.linha, config.coluna)
        
        # controla o movimento da matriz de inimigos
        config.direcao_inimigos = inimigos.mover_inimigos(config.matrizDeInimigos, config.vel_Inimigos, config.direcao_inimigos)
        
        # desenha a matriz de inimigos
        inimigos.draw_inimigos(config.matrizDeInimigos)
        
        inimigos.kill_otimizado(config.projetil, config.matrizDeInimigos)

        # cria tiros inimigos
        if (config.tempo > config.tempo_recarga_tiro_inimigos):
            config.tempo = 0
            inimigos.cria_projetil_inimigo(config.projetil_inimigos, config.matrizDeInimigos)
        
        # move os tiros inimigos e verifica se bateu na nave Mae
        bateu = inimigos.draw_tiros_inimigos(config.projetil_inimigos, config.vidas_nave, config.imortal)

        if (bateu):
            config.imortal = True
            config.vidas_nave -= 1
            if (config.vidas_nave == 0):
                inimigos.jogo_acabou()

        if (config.imortal):
            config.tempo_respawn += config.janela.delta_time()
            config.tempo_total += config.janela.delta_time()
            if (config.tempo_respawn > config.respawn_cooldown):
                config.imortal = False
                config.tempo_respawn = 0
                config.esta_visivel = True
            else:
                if (config.tempo_total > config.intervalo_piscar):
                    config.tempo_total = 0
                    config.esta_visivel = not(config.esta_visivel)
                    naveMae.set_position((config.janela.width - naveMae.width)/2, config.janela.height - 50)

        primeira_linha_nao_vazia = next((linha for linha in config.matrizDeInimigos if linha), None)
        if not primeira_linha_nao_vazia:
            inimigos.criar_matriz_inimigos(config.matrizDeInimigos, config.linha, config.coluna)
            config.vel_Inimigos *= 1.15
            config.vel_Projetil_player *= 1.2

        clock.tick(120)
        config.janela.update()