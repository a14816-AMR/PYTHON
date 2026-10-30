from random import randint
import os
resposta = "S"
while resposta == "S":
    os.system("clear")
    # Declarar e inicializar as variáveis
    tentativas = 0
    pontuacao = 0
    pontuacoes = [100,80,60,40,30,20,10]
    numGerado = randint(1, 100)
    #Ciclo para as tentativas
    while tentativas < 7:
        meuNumero = int(input("Tente o valor gerado: "))
        while meuNumero < 1 or meuNumero > 100:
            print("Valor inválido! O valor deve estar entre 1 e 100.")
            meuNumero = int(input("Tente Novamente: "))
            os.system("clear")
        if meuNumero == numGerado:
            pontuacao = pontuacoes[tentativas]
            print(f"Parabéns! Acertou em {tentativas + 1} tentativas e tiveste pontuação de {pontuacao}.")
            break
        tentativas = tentativas + 1
        if meuNumero > numGerado:
            print("O número gerado é menor que o da tentativa.")
        else:
            print("O número gerado é maior que o da tentativa.")
    if tentativas >= 7:
        print(f"Que pena! O número gerado foi {numGerado}")
    resposta =(input("Deseja jogar novamente? (S/N)")).upper()
    # if tentativas == 1:
    #     pontos += 100
    # elif tentativas == 2:
    #     pontos += 80
    # elif tentativas == 3:
    #     pontos += 60
    # elif tentativas == 4:
    #     pontos += 40
    # elif tentativas == 5:
    #     pontos