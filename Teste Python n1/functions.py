import random
def mostrar_menu():
    print("\n     === BATALHA ===")
    print("     1- Atacar inimigo")
    print("     2 - Consultar estado jogador")
    print("     3 - listar inimigos vivos")
    print("     4 - Usar poção de cura")
    print("     5 - Fugir / Terminar jogo")



def atacar_inimigo (inimigos_combater, jogador):
    print("\n     === INIMIGOS A COMBATER ===")
    i = 1
    for inimigo in inimigos_combater:
        print(f"     {i} - Nome: {inimigo['nome']}, Vida: {inimigo['vida']}, Ataque: {inimigo['ataque']}, Pontos: {inimigo['pontos']}")
        i += 1

    opcao_inimigo = int(input("Escolha um inimigo para atacar: ")) 
    dano_jogador = random.randint(10, 20)
    inimigo_selecionado = inimigos_combater[opcao_inimigo-1]

    dano_inimigo = random.randint(5, inimigo_selecionado["ataque"])

    inimigo_selecionado["vida"] -= dano_jogador
    print(f"Você atacou o {inimigo_selecionado['nome']} e causou {dano_jogador} de dano.")

    print (f"O {inimigo_selecionado['nome']} atacou você e causou {dano_inimigo} de dano.")
    jogador["vida"] -= dano_inimigo


    if inimigo_selecionado["vida"] <= 0:
        print(f"**** PARABENS! Você derrotou o {inimigo_selecionado['nome']}!\n Você recuperou {inimigo_selecionado['pontos']} pontos! ****")
        jogador["pontos"] += inimigo_selecionado["pontos"]
        jogador["inimigos_derrotados"] += 1
        inimigos_combater.remove(inimigo_selecionado)


def consultar_estado_jogador(inimigos_combater, jogador):
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuação: {jogador['pontos']}")
    print(f"Inimigos derrotados: {jogador['inimigos_derrotados']}")
    print(f"Inimigos restantes: {len(inimigos_combater)}")
    print(f"Poções de cura disponíveis: {jogador['pocao_cura']}")

def listar_inimigos_vivos(inimigos_combater):
    print("\n     === INIMIGOS VIVOS ===")
    for inimigo in inimigos_combater:
        print(f"     Nome: {inimigo['nome']}, Vida: {inimigo['vida']}, Ataque: {inimigo['ataque']}, Pontos: {inimigo['pontos']}")

def usar_pocao_cura(jogador):
    if jogador["pocao_cura"] > 0 and jogador["vida"] < 300:
        jogador["vida"] += 25
        vida_anterior = jogador["vida"] - 25
        if jogador["vida"] > 300:
            jogador["vida"] = 300
        jogador["pocao_cura"] -= 1
        print(f" *** Você usou uma poção de cura!\n Vida anterior: {vida_anterior} ===> {jogador['vida']}\n Poções de cura restantes: {jogador['pocao_cura']}")
    else:
        print("Não é possível usar uma poção de cura agora.")


def verificar_fim_jogo(inimigos_combater, jogador):
    if jogador["vida"] <= 0:
        print("Você perdeu o jogo! Sua vida chegou a zero.")
        return True
    elif len(inimigos_combater) == 0:
        print("Parabéns! Você derrotou todos os inimigos e venceu o jogo!")
        return True
    return False