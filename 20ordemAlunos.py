import random
alunos = []
print("SORTEIO DA ORDEM DE APRESENTAÇÃO")
for i in range(5):
    nome=input("digite seu nome:")
    alunos.append(nome)
print("-------------------------------------------------------------------------------------")
print("NOMES NO SORTEIO:",alunos)
random.shuffle(alunos)
print("NOMES EM ORDEM PARA APRESENTAÇÃO:",alunos)
