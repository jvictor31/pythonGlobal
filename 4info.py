digitos = input('Digite algo no teclado:')
print('INFORMAÇÕES\n')
print('[',digitos,']','é do tipo primitivo:', type(digitos))
print('[',digitos,']','tem espaços? ', digitos .isspace())
print('[',digitos,']','é um número? ', digitos .isnumeric())
print('[',digitos,']','é alfabético? ', digitos .isalpha())
print('[',digitos,']','é alfanumérico? ', digitos .isalnum())
print('[',digitos,']','está com letras maiúsculas? ', digitos .isupper())
print('[',digitos,']','esta com letras minúsculas? ', digitos .islower())
print('[',digitos,']','está capitalizada? ', digitos .istitle())
