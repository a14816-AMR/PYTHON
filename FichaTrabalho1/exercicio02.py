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
aprovados = []
reprovados = []
notaBoa = []

for i in range (15):
    if nums[i] > media:
        acimaMedia.append(nums[i])

    if nums[i] >= 10:
        aprovados.append(nums[i])
        if nums[i] >= 16:
            notaBoa.append(nums[i])
    else: 
        reprovados.append(nums[i])

    i = i + 1

nAlunos = len(nums)

aprovacao = (len(aprovados) * 100) / nAlunos

print ("Nº ALUNOS APROVADOS --> ", len(aprovados))
print ("Nº ALUNOS REPROVADOS --> ", len(reprovados))
print ("Nº ALUNOS COM NOTA MAIOR QUE 16 --> ", len(notaBoa))
print ("MAIOR NOTA --> ", maior)
print ("MENOR NOTA --> ", menor)
print ("MEDIA DA TURMA --> ", round(media))
print ("PORCENTAGEM APROVACAO --> ", round(aprovacao), "%")

