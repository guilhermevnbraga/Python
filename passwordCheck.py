''' Uma senha robusta deve ter pelo menos oito caracteres,
deve conter tanto letras maiúsculas quanto letras minúsculas
e ter pelo menos um dígito. '''

import re

password = input('Digite sua senha: ')
lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
numberRegex = re.compile(r'[0-9]')
quantityRegex = re.compile(r'.{8,}')
check1 = re.search(lowerRegex, password)
check2 = re.search(upperRegex, password)
check3 = re.search(numberRegex, password)
check4 = re.search(quantityRegex, password)
if check4 != None and check3 != None and check2 != None and check1 != None:
    print('Sua senha é Forte, muito bem!')
else:
    print('Sua senha é Fraca, refaça!')