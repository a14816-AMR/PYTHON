from math import pow

nome = "MarcelO ViEiRa amoriM"
lista = [1,2,3,4,5,6,7,8,9,10]
pares = [] 
nums_quadrados = []
nums_maiores = []
nome_maiusculo = nome.upper()
lista_multiplos = [1,2,3,4,5,6,7,8,9,10]


for num in lista:
    if num % 2 ==0:
        if num < 5:
            pares.append(num+1)
        else: 
            pares.append(num)

for num in lista: 
    if pow(num,2) <= 10:
        nums_quadrados.append(num)

for num in lista: 
    if num >5:
        nums_maiores.append(num)

dobro = [num*2 if num % 3 == 0 else num for num in lista]

print("**LISTA COMPLETA --> ", lista)
print("**LISTA DOS PARES --> ", pares)
print("**LISTA DOS QUADRADOS --> ", nums_quadrados)
print("**LISTA DOS QUADRADOS --> ", nums_maiores)
print("**NOME MAIOR --> ", nome_maiusculo)
print("**LISTA MULTIPLOS --> ", dobro)