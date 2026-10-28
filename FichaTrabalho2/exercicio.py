
lista = []
copia = []

resposta = ""

while resposta != "0":
    print("\n--- GESTOR DE TAREFAS ---")
    print(" 1 - Adicionar tarefa")
    print(" 2 - Adicionar varias tarefas")
    print(" 3 - Adicionar tarefa numa posicao especifica")
    print(" 4 - Remover a tarefa pelo nome")
    print(" 5 - Remover ultima tarefa ou por indice")
    print(" 6 - Remover todas as tarefas")
    print(" 7 - Contar ocorrencias de tarefa")
    print(" 8 - Encontrar indice de tarefa")
    print(" 9 - Ordenar tarefas em ordem alfabetica")
    print(" 10 - Inverter ordem das tarefas")
    print(" 11 - Copiar lista de tarefas")
    print(" 0 - Sair")
    print("**LISTA DE TAREFAS --> ", lista)

    resposta = input("Qual menu deseja selecionar? ")

    if resposta == "1":
        tarefa = input("Nome da tarefa: ")
        lista.append(tarefa)
        print("Tarefa adicionada!")


    elif resposta == "2":
        novas_tarefas = input("Novas tarefas (separadas por virgula): ")
        lista.extend(novas_tarefas.split(','))
        print("Tarefas adicionadas!")

    elif resposta == "3":
        tarefa = input("Nome da tarefa: ")
        posicao = int(input("Posicao (0 a " + str(len(lista)) + "): "))
        lista.insert(posicao, tarefa)
        print("Tarefa inserida na posicao", posicao)


    elif resposta == "4":
        tarefa = input("Nome da tarefa a remover: ")
        if tarefa in lista:
            lista.remove(tarefa)
            print("Tarefa removida!")
        else:
            print("Essa tarefa nao existe na lista.")

    elif resposta == "5":
        if len(lista) == 0:
            print("A lista esta vazia.")
        else:
            indice = input("Indice a remover (Enter para remover a ultima): ")
            if indice == "":
                removida = lista.pop()
                print("Removida a ultima tarefa:", removida)
            elif 0 <= int(indice) < len(lista):
                removida = lista.pop(int(indice))
                print("Removida a tarefa:", removida)
            else:
                print("Indice invalido.")


    elif resposta == "6":
        lista.clear()
        print("Todas as tarefas foram removidas!")


    elif resposta == "7":
        tarefa = input("Nome da tarefa a contar: ")
        print("A tarefa", tarefa, "aparece", lista.count(tarefa), "vez(es).")


    elif resposta == "8":
        tarefa = input("Nome da tarefa a procurar: ")
        if tarefa in lista:
            print("A tarefa", tarefa, "esta no indice", lista.index(tarefa))
        else:
            print("Essa tarefa nao existe na lista.")

    # 9 - Ordenar as tarefas em ordem alfabetica
    elif resposta == "9":
        lista.sort()
        print("**LISTA ORDENADA --> ", lista)

    # 10 - Inverter a ordem das tarefas
    elif resposta == "10":
        lista.reverse()
        print("**LISTA INVERTIDA --> ", lista)


    elif resposta == "11":
        copia = lista.copy()
        print("**LISTA ORIGINAL --> ", lista)
        print("**COPIA DA LISTA --> ", copia)

    elif resposta == "0":
        print("Adeus!")

    else:
        print("Opcao invalida, tente novamente.")
