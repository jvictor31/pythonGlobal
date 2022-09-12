frase=str(input('digite uma frase:').lower())
print('frase completa:',frase)

#count() encontra a última ocorrência do valor especificado
print('a letra [a] aparece:',frase.count('a'),'vezes')

#find() encontra a primeira ocorrência do valor especificado
print('posição em que aparece [a] pela primeira vez:', frase.find('a')+1)

#rfind() encontra a última ocorrência do valor especificado
print('posição em que aparece [a] pela ultima vez:', frase.rfind('a')+1)
