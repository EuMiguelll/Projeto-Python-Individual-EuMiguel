from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    # Você pode usar esta função como base para a sua função desenha_tela do arquivo tela_jogo.py
    # Esta tela é mostrada quando o jogador aperta a tecla 'i' (você provavelmente vai querer 
    # alterar este arquivo no nível avançado)
    motor.preenche_fundo(janela, BRANCO)

    motor.desenha_string(janela, largura//2-9,altura//2,f"Projeto Individual", BRANCO, PRETO)
    motor.desenha_string(janela, largura//2-6,altura//2+1,f"Por Miguel D.", BRANCO, PRETO)
    motor.desenha_string(janela, largura//2-14,25,f"Pressione <ENTER> para jogar", BRANCO, PRETO)
    motor.desenha_string(janela, largura//2-6,26,f"ou <ESC> para sair", BRANCO, PRETO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == motor.ENTER:
        estado['tela_atual'] = TELA_JOGO
    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR