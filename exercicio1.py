soma = 0
res = True
palavra = "s"

while res == True:
        num = int (input ("insira um numero: "))
        soma = soma + num
        palavra = input("Quer continuar?(s/n)")
        if palavra =="s":
            res = True
        elif palavra == "n":
            res = False

print ("O valor da soma dos numeros e ", soma)