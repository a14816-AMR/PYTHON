from random import randint
from collections import Counter

nums = []
for _ in range (15):
    nums.append (randint(1,20))

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
    


print ("---- SOMA DOS NUMEROS ---- ", soma)
print ("---- MAIOR DOS NUMEROS ---- ", maior)
print ("---- MENOR DOS NUMEROS ---- ", menor)
print ("---- MEDIA DOS NUMEROS ---- ", round(media))
print ("---- ACIMA DA MEDIA ---- ", acimaMedia)
print ("---- ACIMA DA MEDIA ---- ", len(acimaMedia))
