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

    #Desenha vida com ~ no espaco restante
    string_vida = (estado["vidas"]*VIDA)+(estado["max_vidas"]-estado["vidas"])*DANO 
    motor.desenha_string(janela, 0,0, string_vida, BRANCO, VERMELHO_ESCURO)

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

    #monstro escolhe localizacao aleatoriamente para se mover, sem sair do mapa
    for objeto in estado["objetos"]:
        if objeto["tipo"] == MONSTRO:
            escolha_aleatória = randint(1,8)
            
            if escolha_aleatória == 1:
                if objeto["posicao"][0] > 0 and objeto["posicao"][1]  >0 and [objeto["posicao"][0]-1,objeto["posicao"][1]-1] not in posicoes_ocupadas2:
                    objeto["posicao"][0] -=1
                    objeto["posicao"][1] -=1
                    objeto["moveu_para"] = "cima_esquerda"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 2:
                if objeto["posicao"][1] > 0 and [objeto["posicao"][0],objeto["posicao"][1]-1] not in posicoes_ocupadas2:
                    objeto["posicao"][1] -=1
                    objeto["moveu_para"] = "cima"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 3:
                if objeto["posicao"][0] < 29 and objeto["posicao"][1]  >0 and [objeto["posicao"][0]+1,objeto["posicao"][1]-1] not in posicoes_ocupadas2:
                    objeto["posicao"][0] +=1
                    objeto["posicao"][1] -=1
                    objeto["moveu_para"] = "cima_direita"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 4:
                if objeto["posicao"][0] < 29 and [objeto["posicao"][0]+1,objeto["posicao"][1]] not in posicoes_ocupadas2:
                    objeto["posicao"][0] +=1
                    objeto["moveu_para"] = "direita"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 5:
                if objeto["posicao"][0] < 29 and objeto["posicao"][1] < 29 and [objeto["posicao"][0]+1,objeto["posicao"][1]+1] not in posicoes_ocupadas2:
                    objeto["posicao"][0] +=1
                    objeto["posicao"][1] +=1
                    objeto["moveu_para"] = "baixo_direita"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 6:
                if objeto["posicao"][1] < 29 and [objeto["posicao"][0],objeto["posicao"][1]+1] not in posicoes_ocupadas2:
                    objeto["posicao"][1] +=1
                    objeto["moveu_para"] = "baixo"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 7:
                if objeto["posicao"][0] > 0 and objeto["posicao"][1] < 29 and [objeto["posicao"][0]-1,objeto["posicao"][1]+1] not in posicoes_ocupadas2:
                    objeto["posicao"][0] -=1
                    objeto["posicao"][1] +=1
                    objeto["moveu_para"] = "baixo_esquerda"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            elif escolha_aleatória == 8:
                if objeto["posicao"][0] > 0 and [objeto["posicao"][0]-1,objeto["posicao"][1]] not in posicoes_ocupadas2:
                    objeto["posicao"][0] -=1
                    objeto["moveu_para"] = "esquerda"
                    posicoes_ocupadas2.append([objeto["posicao"][0],objeto["posicao"][1]])
            

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
        elif objeto["tipo"] == MONSTRO:
            if objeto["posicao"] == estado["pos_jogador"]:
                #volta a posicao do jogador
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

                    if objeto["vida"] < 1:
                        estado["mensagem"] = "VOCÊ MATOU O MONSTRO!"
                        estado["pos_jogador"] = objeto["posicao"]
                        estado["objetos"].remove(objeto)
            
            elif objeto["posicao"] in estado["posicoes_ocupadas"]:
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

            


                
    nao_andar_na_vida = [[0,0],[1,0],[2,0],[3,0],[4,0]]

    #não deixa o jogador andar pro cima da vida
    for item in nao_andar_na_vida:
        if estado["pos_jogador"] in nao_andar_na_vida:
            if moveu == "direita":
                estado["pos_jogador"][0]-=1
            elif moveu == "esquerda":
                estado["pos_jogador"][0]+=1
            elif moveu == "cima":
                estado["pos_jogador"][1]+=1
            elif moveu == "baixo":
                estado["pos_jogador"][1]-=1
                
    #fecha o jogo se perder as vidas
    if estado["vidas"] == 0:
        estado["tela_atual"] = SAIR

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR