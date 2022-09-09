kms=float(input('digite a quantidade de KMs percorridos:'))
dias=float(input('digite a quantidade de dias alugados:'))
valorKm=kms*0.15
valorDia=dias*60
valorTotal=valorKm+valorDia
print('valor dos kms a ser pago= %.2f' % valorKm,'R$')
print('valor dos dias a ser pago= %.2f'% valorDia,'R$')
print('valor total a ser pago= %.2f' % valorTotal,'R$')
