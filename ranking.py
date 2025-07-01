import json
import config

RANKING_FILE = 'ranking.json'

def salvar_pontuação(nome_jogador, pontuacao):
    nova_pontuação = {'nome': nome_jogador, 'pontuacao': pontuacao}

    ranking = []

    try:
        with open(RANKING_FILE, 'r') as f:
            ranking = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking = []
    

    ranking.append(nova_pontuação)

    ranking.sort(key=lambda item: item['pontuacao'], reverse=True)

    ranking = ranking[:10]

    with open(RANKING_FILE, 'w') as f:
        json.dump(ranking, f, indent=4)        

    print(f'Pontuação de {pontuacao} para {nome_jogador} salva com sucesso!')

def carregar_ranking():
    try:
        with open(RANKING_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def ranking():
    config.janela.set_background_color((0,0,0))

    ranking_atual = carregar_ranking()

    if not ranking_atual:
        config.janela.draw_text(f"Não há ranking com pontuações registradas!!", 10, 30, size = 15, color=(255,255,255), font_name="Arial", bold=True, italic=False)     
    else:
        config.janela.draw_text(f"RANKING", config.janela.width/3  , 10, size = 50, color=(255,255,255), font_name="Arial", bold=True, italic=False)
        for i, entrada in enumerate(ranking_atual):
            posicao = i + 1
            nome = entrada['nome']
            pontos = entrada['pontuacao']
            config.janela.draw_text(f"{posicao}. {nome} - {pontos}", 20, 50 + posicao * 33, size = 30, color=((211, 157, 44)), font_name="Arial", bold=True, italic=False)     

    while (True):
        if (config.teclado.key_pressed("ESC")):
            config.estado = 0
            break
        config.janela.update()