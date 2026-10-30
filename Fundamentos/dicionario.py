aluno = {
    "Nome": "Carlos",
    "Idade": 17, 
    "Cidade": "Famalicao",
    "Diciplinas": ["MAT", "PROG", "ING"],
    "Notas": {
        "mat": [17.5,12], 
        "prog": [18.25,13], 
        "ing":[12.25,7.25]
        } 
}


soma = 0
no_notas = 0
#MEdia de todas as notas 
for notas_diciplina in aluno["Notas"].values():
    soma += sum(notas_diciplina)
    no_notas += len(notas_diciplina)

print(aluno["Notas"]["prog"][1])

# Alterar o valor de uma chave
aluno["Idade"] = 18

#Inserir uma nova chave
aluno ["Estado civil"] = "Solteiro"

#Imprimir caracteristicas do aluno
for chave in aluno.keys():
    print(f"{chave}", end = " ")

#Imprimir somente os valores 
for valor in aluno.values():
    print (f"{valor}", end = " ")

#Imprimir a chave e o valor 
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


#Imprimir Diciplinas
aluno["Diciplinas"].append("PORT")
for diciplina in aluno["Diciplinas"]: 
    print(diciplina)




#-------------------------------------------------------------------------

quadrados = {str(i): i*i for i in range (1,11)}
print(quadrados)

palavras = ["Alicate", "Dados", "Parlamento", "Python", "Dicionario"]
dic_palavras = {palavra: len(palavra) for palavra in palavras}
print(dic_palavras)

notas = {"Ana": 18, "Bruno": 15, "Carla": 17, "David": 12, "Eva": 19}
melhores_alunos = {alunos: nota for alunos,nota in notas.items () if nota >= 15}
print(melhores_alunos)
