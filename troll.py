acabou = False
while not acabou:
    numero1 = input('Digite o primeiro número:')
    if not (numero1.isnumeric() or ('.' in numero1 and ''.join(numero1.split('.')))):
        continue
    numero2 = input('Digite o segundo número:')
    if not (numero2.isnumeric() or ('.' in numero2 and ''.join(numero2.split('.')))):
        continue
    operacao = input('Digite a operação (fim para encerrar):')
    if operacao == 'adição':
        resultado = float(numero1) + float(numero2)
    elif operacao == 'subtração':
        resultado = float(numero1) - float(numero2)
    elif operacao == 'multiplicação':
        resultado = float(numero1) * float(numero2)
    elif operacao == 'divisão':
        if float(numero2) == 0:
            print('Impossível dividir por zero, tente novamente.')
            continue
        else:
            resultado = float(numero1) / float(numero2)
    elif operacao == 'fim':
        acabou = True
        continue
    else:
        print('Operação não suportada, tente novamente.')
        continue
    print(resultado)
