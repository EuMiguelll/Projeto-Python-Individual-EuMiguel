from random import *

from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código


def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    # Implemente esta função para o nível básico
    # A função deve retornar uma posição aleatória dentro da janela que não esteja na lista de posições ocupadas.
    # Uma posição é uma lista com exatas dois elementos: a posição x e a posição y.
    # Além disso, a posição gerada deve ser adicionada à lista de posições ocupadas.
    
    #ocupa o espaco do coracao
    for x in range(0,5):
        posicoes_ocupadas.append([x,0])

    #gera uma posicao desocupada
    x_pos = randint(0, 29)
    y_pos = randint(0, 29)

    while [x_pos,y_pos] in posicoes_ocupadas:
        x_pos = randint(0, 29)
        y_pos = randint(0, 29)
    posicoes_ocupadas.append([x_pos,y_pos])

    return [x_pos, y_pos]

def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
    objetos = []

    normais = [JOGADOR, ESPINHO, PAREDE, VIDA, DANO, MAÇA]

    if tipo in normais:
        for i in range(quantidade):
            posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
            })
    
    cores = [[0, 0, 0], [0, 180, 0], [0, 100, 0], [0, 0, 130], [255, 0, 0], [200, 0, 200]]
    
    if tipo == MONSTRO:
        for i in range(quantidade):
            posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': choice(cores),
                'vida': 3,
                'moveu_para': '',
                'probabilidade_de_ataque': 0.2,
            })
        
    return objetos


def inicializa_estado():
    # Cria lista de listas, cada uma com 50 espaços em branco
    # Você pode mudar esta lista, inclusive seu tamanho, à vontade
    mapa = [
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
        [' '] * 30,
    ]
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    # Você pode colocar o jogador em outro lugar, se preferir
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    
    # Cria outros objetos do mapa
    posicoes_ocupadas = [pos_jogador]
    objetos = []
    objetos += gera_objetos(5, MAÇA, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(12, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(8, MONSTRO, BRANCO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(5, PAREDE, MARROM_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)

    return {
        'tela_atual': TELA_JOGO,
        'pos_jogador': pos_jogador,
        'vidas': 5,  # Quantidade atual de vidas do jogador - ele pode perder vidas ao colidir com espinhos ou ganhar vidas ao pegar corações
        'max_vidas': 5,  # Quantidade máxima de vidas que o jogador pode ter - o valor da chave 'vidas' nunca pode ser maior que o valor da chave 'max_vidas'
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',  # Use esta mensagem para mostrar mensagens ao jogador, como "Você perdeu uma vida" ou "Você ganhou uma vida"
        'posicoes_ocupadas':posicoes_ocupadas
    }
