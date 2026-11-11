import functions as f

jogador = f.criar_jogador()
inimigos = f.gerar_inimigos()
resultado = ""

f.titulo()
print(f"\nSurgiram {len(inimigos)} inimigos! Boa sorte!")


def jogar():
    global resultado
    opcao = 0

    while not f.jogo_terminou(jogador, inimigos):
        f.menu()
        opcao = f.pedir_inteiro("Escolha uma opção: ")

        match (opcao):
            case 1:
                f.atacar(jogador, inimigos)
            case 2:
                f.consultar_estado(jogador, inimigos)
            case 3:
                f.listar_inimigos(inimigos)
            case 4:
                f.usar_pocao(jogador)
            case 5:
                resultado = "FUGA"
                break
            case _:
                print("Opção inválida! Escolha entre 1 e 5.")

    if resultado == "":
        if jogador["vida"] <= 0:
            resultado = "DERROTA"
        else:
            resultado = "VITÓRIA"


jogar()

print("\n========================================")
if resultado == "VITÓRIA":
    print("PARABÉNS! Derrotaste todos os inimigos!")
elif resultado == "DERROTA":
    print("GAME OVER! A tua vida chegou a zero.")
else:
    print("Fugiste da batalha. Partida terminada por FUGA.")
print(f"Resultado: {resultado} | Pontuação final: {jogador['pontos']} | Derrotados: {jogador['derrotados']}")
print("========================================")
