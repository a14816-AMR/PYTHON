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
