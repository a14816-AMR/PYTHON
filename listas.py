from random import randint

nums = []
for _ in range (30):
    nums.append (randint(1,100))

soma = sum(nums)
maior = max (nums)
menor = min (nums)
media = soma/len(nums)

acimaMedia = []
numerosAcimaMedia = 0

i = 0
for _ in range (30):
    if nums[i] > media:
        acimaMedia.append(nums[i])
    i = i + 1
    if acimaMedia[i]
    


print ("---- SOMA DOS NUMEROS ---- ", soma)
print ("---- MAIOR DOS NUMEROS ---- ", maior)
print ("---- MENOR DOS NUMEROS ---- ", menor)
print ("---- MEDIA DOS NUMEROS ---- ", media)
print ("---- ACIMA DA MEDIA ---- ", acimaMedia)







# #Imprimir a lista
# print(nums) #[2,5,8,11,9,13]

# #Imprimir um elemento da lista
# print(nums[2]) # 8

# # Inserir um novo elemento no final da lista 
# nums.append(17) # [2,5,8,11,9,13,17]

# #Inserir Varios elementos no final da lista
# nums.extend([12,16]) # [2,5,8,11,9,13,17,12,16]

# # Inserir numa posicao expecifica na lista pelo indice
# nums.insert(3,29) # [2,5,8.29,11,9,13,17,12,16]

# # Remover o elemento no final da lista 
# nums.pop() # [2,5,8,11,9,13]

# #Remover Varios elementos no final da lista
# nums.pop(2) # [2,5,8,11,9,13,17,12,16]

# # Remover numa posicao expecifica da lista pelo valor
# nums.remove(17) # [2,5,8.29,11,9,13,17,12,16]

# # nº elementos da lista 
# total = len(nums)

# for n in nums: # para cada elemento da minha lsita
#     if n <=10:
#         print(n,end=" ")
# for indice in range (len(nums)):
#     if nums [indice] <= 10:
#         print(nums[indice], end=" ")