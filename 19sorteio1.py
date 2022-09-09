import random

alunos = []
sorteio = []

print("SORTEIO DE QUAL DOS 5 ALUNOS VAI APAGAR O QUADRO")

for i in range(5):
    nome=input("digite seu nome:")
    alunos.append(nome)
print("-------------------------------------------------------------------------------------")
print("NOMES EM ORDEM:",alunos)
print("NUMEROS EM ORDEM DOS SORTEADOS:['1', '2', '3', '4', '5']")

for i in range(1):
    sorteio.append(random.randint(1,5))
print("NUMERO SORTEADO:",sorteio)

if sorteio == [1]:
    print(alunos[0]," ganhou!")
elif sorteio == [2]:
    print(alunos[1]," ganhou!")
elif sorteio == [3]:
    print(alunos[2]," ganhou!")
elif sorteio == [4]:
    print(alunos[3]," ganhou!")
elif sorteio == [5]:
    print(alunos[4]," ganhou!" )
