aluno = {
    "Nome": "Ana silva",
    "Idade": 17,
    "Disciplinas" : [
        "Matematica",
        "Fisica",
        "informatica"
    ],
    "Notas": {
        "Matematica": 18,
        "Fisica": 17,
        "informatica": 19
    }
}

aluno["Disciplinas"] = "Portugues"
aluno["Notas"]["Portugues"] =  16

print(aluno["Notas"])