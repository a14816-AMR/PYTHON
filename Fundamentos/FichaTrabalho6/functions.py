import random


# ---------- Dados iniciais ----------
def criar_jogador():
    return {
        "vida": 300,
        "ataque": 20,
        "pocoes": 2,
        "pontos": 0,
        "derrotados": 0
    }


def criar_inimigo(nome, vida, ataque, pontos):
    return {
        "nome": nome,
        "vida": vida,
        "ataque": ataque,
        "pontos": pontos
    }


def tipos_inimigo():
    return [
        criar_inimigo("Goblin", 40, 8, 100),
        criar_inimigo("Orc", 55, 11, 200),
        criar_inimigo("Troll", 70, 14, 300),
        criar_inimigo("Beast", 85, 17, 400),
        criar_inimigo("Dragão", 100, 20, 500)
    ]


def gerar_inimigos():
    tipos = tipos_inimigo()
    quantidade = random.randint(3, 5)
    inimigos = []
    for i in range(quantidade):
        escolhido = random.choice(tipos)
        inimigos.append(escolhido.copy())  # copy para cada inimigo ter a sua vida
    return inimigos


# ---------- Interface ----------
def titulo():
    print("========================================")
    print("          BATALHA DE MONSTROS           ")
    print("========================================")


def menu():
    print("\n========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")
    print("=============================\n")


def pedir_inteiro(mensagem):
    # devolve None se o utilizador não escrever um número (o programa não termina)
    try:
        return int(input(mensagem))
    except ValueError:
        return None


# ---------- Lógica ----------
def inimigos_vivos(inimigos):
    vivos = []
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            vivos.append(inimigo)
    return vivos


def listar_inimigos(inimigos):
    vivos = inimigos_vivos(inimigos)
    if len(vivos) == 0:
        print("Não existem inimigos vivos.")
        return
    for i, inimigo in enumerate(vivos, start=1):
        print(f"{i} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")


def consultar_estado(jogador, inimigos):
    vivos = len(inimigos_vivos(inimigos))
    print("\n--- Estado do jogador ---")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuação: {jogador['pontos']}")
    print(f"Inimigos derrotados: {jogador['derrotados']}")
    print(f"Inimigos vivos: {vivos}")
    print(f"Poções disponíveis: {jogador['pocoes']}")


def atacar(jogador, inimigos):
    vivos = inimigos_vivos(inimigos)
    if len(vivos) == 0:
        print("Não existem inimigos vivos.")
        return

    print("\nInimigos vivos:")
    listar_inimigos(inimigos)

    escolha = pedir_inteiro("Escolha o inimigo: ")
    if escolha is None or escolha < 1 or escolha > len(vivos):
        print(f"Escolha inválida! Introduza um número entre 1 e {len(vivos)}.")
        return

    inimigo = vivos[escolha - 1]

    # ataque do jogador
    dano = random.randint(10, 20)
    inimigo["vida"] = max(0, inimigo["vida"] - dano)
    print(f"\nAtacaste o {inimigo['nome']} e causaste {dano} de dano.")

    if inimigo["vida"] == 0:
        jogador["pontos"] += inimigo["pontos"]
        jogador["derrotados"] += 1
        print(f"{inimigo['nome']} foi derrotado! +{inimigo['pontos']} pontos.")
        return

    print(f"{inimigo['nome']} ficou com {inimigo['vida']} de vida.")

    # contra-ataque do inimigo
    contra = random.randint(5, inimigo["ataque"])
    jogador["vida"] = max(0, jogador["vida"] - contra)
    print(f"{inimigo['nome']} contra-atacou e causou {contra} de dano.")
    print(f"Ficaste com {jogador['vida']} de vida.")


def usar_pocao(jogador):
    if jogador["pocoes"] <= 0:
        print("Não tens poções disponíveis.")
        return
    if jogador["vida"] >= 100:
        print("Já tens 100 ou mais pontos de vida. Não podes usar poções.")
        return

    jogador["vida"] = min(100, jogador["vida"] + 25)
    jogador["pocoes"] -= 1
    print(f"Poção usada! Vida atual: {jogador['vida']} | Poções restantes: {jogador['pocoes']}")


def jogo_terminou(jogador, inimigos):
    return jogador["vida"] <= 0 or len(inimigos_vivos(inimigos)) == 0
