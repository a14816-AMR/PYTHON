def saudacao (nome, curso = "GPSI"):
    print (f"Bem vindo ao curso de {curso}, {nome} !")

saudacao("Carlos")

def criar_lista(*alunos):
    lista = []
    for aluno in alunos:
        lista.append(aluno)
    return lista



x = criar_lista("Ana", "joao")
y = criar_lista("Rui", "Maria", "Fernando", "Joana", "Isa")
z = ["A1", "A2", "A3"]
nova_lista = criar_lista(*z)
print(x,y, nova_lista)


def config (**conficuracoes):
    for chave, valor in conficuracoes.items():
        print(f"{chave}: {valor}")

config (memoria ="16GB", disco ="SSD 256 GB", sistema ="Windows 11")

dicionario ={"Memoria": "8GB", "Disco": "SSD 512 GB", "Sistema": "Ubuntu"}
config (**dicionario)

def maiores_dois_valores (n1,n2,n3):
    maior = n1
    maior2 = 0
    if n2 > maior and n2 > n3:
        maior = n2
        if n1 > n3:
            maior = n1
        else: 
            maior = n3
    return (maior, maior2)
