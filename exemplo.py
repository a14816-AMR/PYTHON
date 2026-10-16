x=5 
if x > 3:
    pass
elif x < 8: 
    pass
while x < 10:
    print(x)
    x=x+1

for i in range (3,21):
    print (i)

for _ in range (10):
    print("Marcelo")


lista =  [n for n in range (1,101)]
print (lista)

impares = []
for num in lista:
    if num % 2 ==1:
        impares.append(num)
print (f"Impares: {impares}")

impares2 = [num for num in lista if num % 2 ==1]



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