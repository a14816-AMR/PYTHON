from random import randint
nums = []

numsPares = []
numsImpares = []

for _ in range (30):
    nums.append (randint(1,100))

soma = sum(nums)
maior = max (nums)
menor = min (nums)
media = soma/len(nums)

acimaMedia = []


i = 0
for _ in range (30):
    if nums[i] % 2 == 0:
        numsPares.append(nums[i])
    elif nums[i] % 2 != 0:
        numsImpares.append(nums[i])
    
    if nums[i] > media:
        acimaMedia.append(nums[i])
    i = i + 1

ttpares = len(numsPares)
ttimpares = len(numsImpares)

print ("---- LISTA DOS NUMEROS ---- ", nums)
print ("---- LISTA DOS NUMEROS PARES ---- ", ttpares)
print ("---- LISTA DOS NUMEROS IMPARES ---- ", ttimpares)
print ("---- MAIOR DOS NUMEROS ---- ", maior)
print ("---- MENOR DOS NUMEROS ---- ", menor)
print ("---- MEDIA DOS NUMEROS ---- ", round(media))
print ("---- NUMEROS ACIMA DA MEDIA ---- ", len(acimaMedia))
print ("---- ACIMA DA MEDIA ---- ", acimaMedia)

