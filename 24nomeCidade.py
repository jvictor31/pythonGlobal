cidade=str(input('digite o nome da cidade:'))
primeiroNome=cidade.split()
print('primeiro nome da cidade:',primeiroNome[0])
if primeiroNome[0]=='santo' or primeiroNome[0]=='SANTO' or primeiroNome[0]=='Santo':
    print('começa com santo!')
else:
    print('não começa com santo!')
            
