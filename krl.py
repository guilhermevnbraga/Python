"""Escreva um programa em Python que implemente uma
calculadora para dois números. A calculadora deve ser capaz de realizar
as operações de soma, subtração, multiplicação e divisão. O programa
deve solicitar ao usuário que digite dois números e a operação desejada.
Em seguida, deve exibir o resultado da operação e perguntar se o
usuário deseja realizar outra operação.

O programa deve continuar perguntando dois números e a operação desejada
até que o usuário digite "fim" (sem aspas) como operação. Nesse caso, o
programa deve ser encerrado.

Certifique-se de tratar adequadamente casos em que o usuário digite valores
inválidos, como letras ou operações não suportadas pela calculadora."""

numeros = []
acabou = False
erro = False
dividirZero = False
while acabou == False:
    while len(numeros) < 2:
        numero = input(f'Digite o {len(numeros)+1}° número: ')
        if numero.replace('.', '').isnumeric():
            numeros.append(float(numero))
    erro = False
    operacao = input('Digite a operação desejada [adição/subtração/multiplicação/divisão]: ')
    if operacao == 'fim':
        acabou = True
        continue
    elif operacao == 'adição':
        resultado = sum(numeros)
    elif operacao == 'subtração':
        resultado = numeros[0] - numeros[1]
    elif operacao == 'multiplicação':
        resultado = numeros[0] * numeros[1]
    elif operacao == 'divisão':
        if numeros[1] == 0:
            print('Erro: Divisão por zero!')
            continue
        else:
            resultado = numeros[0] / numeros[1]
    else:
        print('Operação inválida!')
        erro = True
        continue
    print(resultado)
    numeros = []
