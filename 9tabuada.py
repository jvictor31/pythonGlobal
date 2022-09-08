num=int(input('digite um numero:'))
print('TABUADA')
cont=0
resultado=0
for i in range (10):
    cont=cont+1
    resultado=num*cont
    print(num,' x ',i+1,'=',resultado)
