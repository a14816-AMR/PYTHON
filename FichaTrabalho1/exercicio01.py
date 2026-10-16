from random import randint
numsPares = []
nums = []
for _ in range (30):
    nums.append (randint(1,100))

soma = sum(nums)
maior = max (nums)
menor = min (nums)
media = soma/len(nums)

acimaMedia = []

i = 0
for _ in range (30):
    if nums[i] > media:
        acimaMedia.append(nums[i])
    i = i + 1


    

print ("---- LISTA DOS NUMEROS ---- ", nums)
print ("---- SOMA DOS NUMEROS ---- ", soma)
print ("---- MAIOR DOS NUMEROS ---- ", maior)
print ("---- MENOR DOS NUMEROS ---- ", menor)
print ("---- MEDIA DOS NUMEROS ---- ", round(media))
print ("---- ACIMA DA MEDIA ---- ", acimaMedia)
print ("---- NUMEROS ACIMA DA MEDIA ---- ", len(acimaMedia))
