from random import randint
from re import match
from functions import mostrar_menu, atacar_inimigo, consultar_estado_jogador, listar_inimigos_vivos, usar_pocao_cura, verificar_fim_jogo

print ("---- RPG DE LUTA ----")


jogador = {
    "vida": 300,
    "ataque_base": 20,
    "pocao_cura": 2, 
    "pontos_recuperados": 0,
    "inimigos_derrotados": 0
}

inimigos = [
    {
        "nome": "Goblin",
        "vida": 40,
        "ataque": 8,
        "pontos": 100
    },
    {
        "nome": "Orc",
        "vida": 55,
        "ataque": 11,
        "pontos": 200
    },
    {
        "nome": "Troll",
        "vida": 70,
        "ataque": 14,
        "pontos": 300
    },
    {
        "nome": "Beast",
        "vida": 85,
        "ataque": 17,
        "pontos": 400
    }, 
    {
        "nome": "Dragao",
        "vida": 100,
        "ataque": 20,
        "pontos": 500
    }
]

inimigos_combater = []

for i in range(randint(3, 5)):
    inimigo = inimigos[randint(0, len(inimigos) - 1)]
    if inimigo not in inimigos_combater:
        inimigos_combater.append(inimigo)



ganhou_jogo = False
while ganhou_jogo == False:
    mostrar_menu()
    menu_selecionado = input("Escolha um menu: ")
    ganhou_jogo = verificar_fim_jogo(inimigos_combater, jogador)
    match menu_selecionado:
        case "1":
            atacar_inimigo(inimigos_combater, jogador)
        case "2":
            consultar_estado_jogador(inimigos_combater, jogador)
        case "3":
            listar_inimigos_vivos(inimigos_combater)
        case "4":
            usar_pocao_cura(jogador)
        case "5":
            print("Você fugiu do jogo!")
            break
        case _:
            print("Opção inválida. Tente novamente.")
