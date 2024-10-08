from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto

from random import *


def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela, BRANCO)
    
    # O seu código deve desenhar a tela do jogo aqui a partir dos valores no dicionário "estado"
    
    #desenha a tela
    for y in range(altura_tela):
        for x in range(largura_tela):
            motor.desenha_string(janela, x, y, " ", AMARELO_PRAIA, AMARELO_PRAIA)

    #Desenha branco da HUD:
    for y in range(0,2):
        for x in range(0,8):
            motor.desenha_string(janela,x,y," ", BRANCO, BRANCO)

    #Desenha vida com ~ no espaco restante
    string_vida = (estado["vidas"]*VIDA)+(estado["max_vidas"]-estado["vidas"])*DANO 
    motor.desenha_string(janela, 0,0, string_vida, BRANCO, VERMELHO_ESCURO)

    #Desenha o nivel do personagem na tela:
    niveltela = estado["nivel"]
    motor.desenha_string(janela, 0,1,f"Nível:{niveltela}", BRANCO,ROXO)

    #desenha os espinhos e o coracao e parede
    for objeto in estado["objetos"]:
        if objeto["tipo"] == ESPINHO:
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1], ESPINHO, AMARELO_PRAIA, MARROM_MAIS_ESCURO)
        elif objeto["tipo"] == MAÇA:
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1], MAÇA, AMARELO_PRAIA, VERMELHO)
        elif objeto["tipo"] == PAREDE:
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1], PAREDE,AMARELO_PRAIA, PRETO)
        elif objeto["tipo"] == MONSTRO:
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1], MONSTRO, AMARELO_PRAIA, objeto["cor"])
            qnt_vidas = objeto["vida"]
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1]-1, f"{qnt_vidas}", BRANCO, PRETO)
        elif objeto["tipo"] == MONSTRAO:
            qnt_vidas_monstrao = objeto["vida"]
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1], MONSTRAO, AMARELO_PRAIA, objeto["cor"])
            motor.desenha_string(janela, objeto["posicao"][0], objeto["posicao"][1]-1, f"{qnt_vidas_monstrao}", BRANCO, PRETO)

    #desenha o personagem principal
    motor.desenha_string(janela, estado["pos_jogador"][0], estado["pos_jogador"][1], JOGADOR, AMARELO_PRAIA, AZUL)

    #desenha as mensagens
    motor.desenha_string(janela,0, 29, estado['mensagem'], BRANCO, PRETO )

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    posicoes_ocupadas2 = []
    
    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    #andar direita e esquerda
    
    if tecla == motor.SETA_DIREITA and estado["pos_jogador"][0] < 29:
        estado["pos_jogador"][0]+=1
        moveu = "direita"
    if tecla == motor.SETA_ESQUERDA and estado["pos_jogador"][0] > 0:
        estado["pos_jogador"][0]-=1
        moveu = "esquerda"
    #andar cima e baixo
    if tecla == motor.SETA_CIMA and estado["pos_jogador"][1] > 0:
        estado["pos_jogador"][1]-=1
        moveu = "cima"
    if tecla == motor.SETA_BAIXO and estado["pos_jogador"][1] < 29:
        estado["pos_jogador"][1]+=1
        moveu = "baixo"

    
    #atualiza posicao dos itens abaixo para que os monstros nao colidam com eles
    tipos = [MAÇA, ESPINHO, PAREDE]
    pos_ocupadas = []
    for objeto in estado["objetos"]:
        if objeto["tipo"] in tipos:
            pos_ocupadas.append(objeto["posicao"])

    #monstro escolhe localizacao aleatoriamente para se mover, sem sair do mapa
    for objeto in estado["objetos"]:
        if objeto["tipo"] == MONSTRO or objeto["tipo"] == MONSTRAO:
            escolha_aleatória = randint(1,8)

            #50% de chance do monstro escolher mexer
            vou_mexer = choice([0,1])

            #1/3 de chance do MONSTRAO escolher se mexer
            if objeto["tipo"] == MONSTRAO:
                vou_mexer = choice([0,1,2])
            
            #se ele escolher mexer, ele sorteia uma direcao em volta dele e se mexe, ele lembra pra onde se mexeu no estado["moveu_para"]
            if vou_mexer == 1:
                if escolha_aleatória == 1:
                    if objeto["posicao"][0] > 0 and objeto["posicao"][1] >0:
                        objeto["posicao"][0] -=1
                        objeto["posicao"][1] -=1
                        objeto["moveu_para"] = "cima_esquerda"
                elif escolha_aleatória == 2:
                    if objeto["posicao"][1] > 0:
                        objeto["posicao"][1] -=1
                        objeto["moveu_para"] = "cima"
                elif escolha_aleatória ==3:
                    if objeto["posicao"][0] <29 and objeto["posicao"][1]  >0:
                        objeto["posicao"][0] +=1
                        objeto["posicao"][1] -=1
                        objeto["moveu_para"] = "cima_direita"
                elif escolha_aleatória == 4:
                    if objeto["posicao"][0] <29:
                        objeto["posicao"][0] +=1
                        objeto["moveu_para"] = "direita"
                elif escolha_aleatória == 5:
                    if objeto["posicao"][0] <29 and objeto["posicao"][1] <29:
                        objeto["posicao"][0] +=1
                        objeto["posicao"][1] +=1
                        objeto["moveu_para"] = "baixo_direita"
                elif escolha_aleatória == 6:
                    if objeto["posicao"][1] <29:
                        objeto["posicao"][1] +=1
                        objeto["moveu_para"] = "baixo"
                elif escolha_aleatória == 7:
                    if objeto["posicao"][0] >0 and objeto["posicao"][1] <29:
                        objeto["posicao"][0] -=1
                        objeto["posicao"][1] +=1
                        objeto["moveu_para"] = "baixo_esquerda"
                elif escolha_aleatória == 8:
                    if objeto["posicao"][0] >0:
                        objeto["posicao"][0] -=1
                        objeto["moveu_para"] = "esquerda"
            #checa se o monstro ta em uma posicao ocupada e volta ele caso ele esteja
            if objeto["posicao"] in pos_ocupadas:
                if objeto["moveu_para"] == "cima_esquerda":
                    objeto["posicao"][0] +=1
                    objeto["posicao"][1] +=1
                elif objeto["moveu_para"] == "cima":
                    objeto["posicao"][1] +=1
                elif objeto["moveu_para"] == "cima_direita":
                    objeto["posicao"][0] -=1
                    objeto["posicao"][1] +=1
                elif objeto["moveu_para"] == "direita":
                    objeto["posicao"][0] -=1
                elif objeto["moveu_para"] == "baixo_direita":
                    objeto["posicao"][0] -=1
                    objeto["posicao"][1] -=1
                elif objeto["moveu_para"] == "baixo":
                    objeto["posicao"][1] -=1
                elif objeto["moveu_para"] == "baixo_esquerda":
                    objeto["posicao"][0] +=1
                    objeto["posicao"][1] -=1
                elif objeto["moveu_para"] == "esquerda":
                    objeto["posicao"][0] +=1

    #checa se o jogador está tocando em um espinho ou coracao ou parede
    for objeto in estado["objetos"]:
        #checa se o jogador está tocando em um espinho:
        if objeto["tipo"] == ESPINHO:
            if objeto["posicao"] == estado["pos_jogador"]:
                estado["mensagem"] = "VOCE TOCOU NO ESPINHO!! -1HP"
                estado["vidas"] -=1
        #checa se o jogador está tocando em um coracao:
        elif objeto["tipo"] == MAÇA:
            if objeto["posicao"] == estado["pos_jogador"]:
                if estado["vidas"] < estado["max_vidas"]:
                    estado["mensagem"] = "VOCE PEGOU UMA VIDA!! +1HP"
                    estado["vidas"] +=1
                else:
                    estado["mensagem"] = "FULL HP!!"
                estado["objetos"].remove(objeto)
        #checa se o jogador está tocando em uma parede:
        elif objeto["tipo"] == PAREDE:
            if objeto["posicao"] == estado["pos_jogador"]:
                estado["mensagem"] = "VOCE NAO PODE PASSAR POR AQUI"
                if moveu == "direita":
                    estado["pos_jogador"][0]-=1
                elif moveu == "esquerda":
                    estado["pos_jogador"][0]+=1
                elif moveu == "cima":
                    estado["pos_jogador"][1]+=1
                elif moveu == "baixo":
                    estado["pos_jogador"][1]-=1
        
        elif objeto["tipo"] == MONSTRO or objeto["tipo"] == MONSTRAO:
            #checa se o jogador está em cima do monstro, volta o jogador e determina quem dá o dano
            if objeto["posicao"] == estado["pos_jogador"]:
                if moveu == "direita":
                    estado["pos_jogador"][0]-=1
                elif moveu == "esquerda":
                    estado["pos_jogador"][0]+=1
                elif moveu == "cima":
                    estado["pos_jogador"][1]+=1
                elif moveu == "baixo":
                    estado["pos_jogador"][1]-=1
                #checa quem ataca
                if random() <= objeto["probabilidade_de_ataque"]:
                    estado["mensagem"] = "O MONSTRO TE ATACOU!"
                    estado["vidas"] -=1
                else:
                    objeto["vida"] -=1
                    estado["mensagem"] = "VOCÊ ATACOU O MONSTRO!"
                #se o monstro levar dano e ficar com 0 de vida ele morre e sai da lista de objetos
                    if objeto["vida"] < 1:
                        estado["mensagem"] = "VOCÊ MATOU O MONSTRO!"
                        estado["pos_jogador"] = objeto["posicao"]
                        estado["objetos"].remove(objeto)
                        estado["barra_xp"] += 100 + 25*estado["nivel"]
                        if objeto["tipo"] == MONSTRAO:
                            estado["barra_xp"] += 100 + 50*estado["nivel"]
                        estado["nivel"] = estado["barra_xp"]//100

    nao_andar_hud = []

    for y in range(0,2):
        for x in range(0,8):
            nao_andar_hud.append([x,y])

    #não deixa o jogador nem inimigos andarem na hud
    for item in nao_andar_hud:
        if estado["pos_jogador"] in nao_andar_hud:
            if moveu == "direita":
                estado["pos_jogador"][0]-=1
            elif moveu == "esquerda":
                estado["pos_jogador"][0]+=1
            elif moveu == "cima":
                estado["pos_jogador"][1]+=1
            elif moveu == "baixo":
                estado["pos_jogador"][1]-=1
        
        for objeto in estado["objetos"]:
            if objeto["tipo"] == MONSTRO or objeto["tipo"] == MONSTRAO:
                if objeto["posicao"] in nao_andar_hud:
                    if objeto["moveu_para"] == "cima_esquerda":
                        objeto["posicao"][0] +=1
                        objeto["posicao"][1] +=1
                    elif objeto["moveu_para"] == "cima":
                        objeto["posicao"][1] +=1
                    elif objeto["moveu_para"] == "cima_direita":
                        objeto["posicao"][0] -=1
                        objeto["posicao"][1] +=1
                    elif objeto["moveu_para"] == "direita":
                        objeto["posicao"][0] -=1
                    elif objeto["moveu_para"] == "baixo_direita":
                        objeto["posicao"][0] -=1
                        objeto["posicao"][1] -=1
                    elif objeto["moveu_para"] == "baixo":
                        objeto["posicao"][1] -=1
                    elif objeto["moveu_para"] == "baixo_esquerda":
                        objeto["posicao"][0] +=1
                        objeto["posicao"][1] -=1
                    elif objeto["moveu_para"] == "esquerda":
                        objeto["posicao"][0] +=1

                
    #fecha o jogo se perder as vidas
    if estado["vidas"] == 0:
        estado["tela_atual"] = SAIR

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR