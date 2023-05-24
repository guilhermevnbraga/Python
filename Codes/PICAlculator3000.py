import PySimpleGUI as sg
import math


def find_operator(sentence):
    c = 0
    cp = 0
    p1 = 0
    p2 = 0
    sentence = sentence.split()
    while True:
        if ''.join(''.join(sentence).split('.')).isnumeric():
            break
        while '(' in sentence or ')' in sentence:
            for n in sentence:
                if n == '(':
                    p1 = cp
                if n == ')':
                    p2 = cp
                if p1 and p2 != 0:
                    sentence2 = sentence[p1:p2+1]
                    break
                cp += 1
            cp = 0
            while '^' in sentence2:
                for n in sentence2:
                    if n == '^':
                        op = str(math.pow((float(sentence2[c - 1])), float(sentence2[c + 1])))
                        del sentence2[c:c + 2]
                        sentence2[c - 1] = op
                        break
                    c += 1
            c = 0
            while '*' in sentence2 or '/' in sentence2:
                for n in sentence2:
                    if n == '*':
                        op = str(float(sentence2[c - 1]) * float(sentence2[c + 1]))
                        del sentence2[c:c + 2]
                        sentence2[c - 1] = op
                        break
                    elif n == '/':
                        op = str(float(sentence2[c - 1]) / float(sentence2[c + 1]))
                        del sentence2[c:c + 2]
                        sentence2[c - 1] = op
                        break
                    c += 1
                c = 0
            while '+' in sentence2 or '-' in sentence2:
                for n in sentence2:
                    if n == '+':
                        op = str(float(sentence2[c - 1]) + float(sentence2[c + 1]))
                        del sentence2[c:c + 2]
                        sentence2[c - 1] = op
                        break
                    elif n == '-':
                        op = str(float(sentence2[c - 1]) - float(sentence2[c + 1]))
                        del sentence2[c:c + 2]
                        sentence2[c - 1] = op
                        break
                    c += 1
                c = 0
                if '+' in sentence2 or '-' in sentence2:
                    continue
                sentence[p1] = ''.join(sentence2)
                del sentence[p1+1:p2+1]
                sentence2 = ''
            p1 = 0
            p2 = 0
        c = 0
        cp = 0
        for n in sentence:
            if '(' in n:
                for x in n:
                    if x == '(':
                        p1 = cp
                    if x == ')':
                        p2 = cp
                    if p1 or p2 != 0:
                        sentence2 = n[p1 + 1:p2]
                    cp += 1
                cp = 0
                sentence[c] = sentence2
            c += 1
        c = 0
        while '^' in sentence:
            for n in sentence:
                if n == '^':
                    op = str(math.pow((float(sentence[c - 1])), float(sentence[c + 1])))
                    sentence[c-1] = ''.join(sentence[c-1:c+2])
                    del sentence[c:c+2]
                    sentence[c-1] = op
                    break
                c += 1
        c = 0
        while '*' in sentence or '/' in sentence:
            for n in sentence:
                if n == '*':
                    op = str(float(sentence[c - 1]) * float(sentence[c + 1]))
                    sentence[c-1] = ''.join(sentence[c-1:c+2])
                    del sentence[c:c+2]
                    sentence[c-1] = op
                    break
                elif n == '/':
                    op = str(float(sentence[c - 1]) / float(sentence[c + 1]))
                    sentence[c-1] = ''.join(sentence[c-1:c+2])
                    del sentence[c:c+2]
                    sentence[c-1] = op
                    break
                c += 1
            c = 0
        for n in sentence:
            if n == '+':
                op = str(float(sentence[c - 1]) + float(sentence[c + 1]))
                del sentence[c:c+2]
                sentence[c-1] = op
                c = 0
                break
            elif n == '-':
                op = str(float(sentence[c - 1]) - float(sentence[c + 1]))
                del sentence[c:c+2]
                sentence[c-1] = op
                c = 0
                break
            c += 1
    c = 0
    point = 0
    flot = 0
    sentence = ''.join(sentence)
    for n in sentence:
        if n == '.' or point == 1:
            point = 1
            if c + 1 == len(sentence):
                break
            if sentence[c + 1] == '0':
                flot = 0
            else:
                flot = 1
                break
        c += 1
    if flot == 1:
        return sentence
    else:
        return str(int(float(sentence)))


sentence = ''
sentence2 = ''
m = ''
sg.theme('DarkGreen3')
layout = [
    [sg.Text('PICAlculator 3000       ', justification='r', size=(23, 1), font='Arial 18'),
     sg.Button('⚙', key='settings', size=(2,1))],
    [sg.Text('')],
    [sg.Text(size=(300,1), key='num2', justification='r')],
    [sg.Text('0', size=(300, 3), justification='r', key='num')],
    [sg.Button('MS', key='memory_store', size=(5, 2), ), sg.Button('MR', key='memory_restore', size=(5, 2)),
     sg.Button('M+', key='memory_sum', size=(5, 2)), sg.Button('M-', key='memory_sub', size=(5, 2)),
     sg.Button('C', key='clear', size=(5, 2))],
    [sg.Button('sen', key='sin', size=(5, 2)), sg.Button('cos', key='cos', size=(5, 2)),
     sg.Button('tan', key='tan', size=(5, 2)), sg.Button('x²', key='pot_two', size=(5, 2)),
     sg.Button('√x', key='square_root', size=(5, 2))],
    [sg.Button('π', key='pi', size=(5, 2)), sg.Button('(', key='par1', size=(5, 2)),
     sg.Button(')', key='par2', size=(5, 2)), sg.Button('x!', key='factorial', size=(5, 2)),
     sg.Button('/', key='div', size=(5, 2))],
    [sg.Button('x^y', key='pot_x', size=(5, 2)), sg.Button('7', key='seven', size=(5, 2)),
     sg.Button('8', key='eight', size=(5, 2)), sg.Button('9', key='nine', size=(5, 2)),
     sg.Button('X', key='mult', size=(5, 2))],
    [sg.Button('10^x', key='ten_pot', size=(5, 2)), sg.Button('4', key='four', size=(5, 2)),
     sg.Button('5', key='five', size=(5, 2)), sg.Button('6', key='six', size=(5, 2)),
     sg.Button('-', key='minus', size=(5, 2))],
    [sg.Button('|x|', key='model_x', size=(5, 2)), sg.Button('1', key='one', size=(5, 2)),
     sg.Button('2', key='two', size=(5, 2)), sg.Button('3', key='three', size=(5, 2)),
     sg.Button('+', key='plus', size=(5, 2))],
    [sg.Button('log', key='log', size=(5, 2)), sg.Button('+/-', key='inverter', size=(5, 2)),
     sg.Button('0', key='zero', size=(5, 2)), sg.Button('.', key='point', size=(5, 2)),
     sg.Button('=', key='equal', size=(5, 2))]
]
layout2 = [
    [sg.Button('←', key='turn', size=(2,1))]
]
janela = sg.Window('PICAlculator 3000', layout, size=(390, 500))
settings = sg.Window('PICAlculator 3000', layout2, size=(300, 250))
set = False
while True:
    if set == False:
        eventos, valores = janela.read()
        janela.maximize()
        if eventos == 'settings':
            set = True
            janela.minimize()
            continue
        if eventos == 'memory_store':
            m = sentence
        if eventos == 'memory_restore':
            sentence = m
            janela['num'].update(sentence)
        if eventos == 'memory_sum':
            m = find_operator(f'{m} + {sentence}')
        if eventos == 'memory_sub':
            m = find_operator(f'{m} - {sentence}')
        if eventos == 'clear':
            sentence = ''
            sentence2 = ''
            janela['num'].update('0')
            janela['num2'].update('')
        if eventos == 'sin':
            sentence = math.sin(math.radians(float(sentence)))
            janela['num'].update(sentence)
        if eventos == 'cos':
            sentence = math.cos(math.radians(float(sentence)))
            janela['num'].update(sentence)
        if eventos == 'tan':
            sentence = math.tan(math.radians(float(sentence)))
            janela['num'].update(sentence)
        if eventos == 'pot_two':
            sentence = math.pow(float(sentence), 2)
            janela['num'].update(sentence)
        if eventos == 'square_root':
            sentence = math.sqrt(float(sentence))
            janela['num'].update(sentence)
        if eventos == 'pi':
            sentence = 3.1415926535897932384626433832795
            janela['num'].update(sentence)
        if eventos == 'par1':
            sentence2 += sentence + ' ( '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'par2':
            sentence2 += sentence + ' ) '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'factorial':
            sentence = str(math.factorial(sentence))
            janela['num'].update(sentence)
        if eventos == 'div':
            sentence2 += sentence + ' / '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'pot_x':
            sentence2 += sentence + ' ^ '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'seven':
            sentence += '7'
            janela['num'].update(sentence)
        if eventos == 'eight':
            sentence += '8'
            janela['num'].update(sentence)
        if eventos == 'nine':
            sentence += '9'
            janela['num'].update(sentence)
        if eventos == 'mult':
            sentence2 += sentence + ' * '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'ten_pot':
            sentence = find_operator(f'10 ^ {sentence}')
            janela['num'].update(sentence)
        if eventos == 'four':
            sentence += '4'
            janela['num'].update(sentence)
        if eventos == 'five':
            sentence += '5'
            janela['num'].update(sentence)
        if eventos == 'six':
            sentence += '6'
            janela['num'].update(sentence)
        if eventos == 'minus':
            sentence2 += sentence + ' - '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'model_x':
            if sentence[0] == '-':
                sentence = str(float(sentence) * -1)
                janela['num'].update(sentence)
        if eventos == 'one':
            sentence += '1'
            janela['num'].update(sentence)
        if eventos == 'two':
            sentence += '2'
            janela['num'].update(sentence)
        if eventos == 'three':
            sentence += '3'
            janela['num'].update(sentence)
        if eventos == 'plus':
            sentence2 += sentence + ' + '
            sentence = ''
            janela['num'].update('0')
            janela['num2'].update(sentence2)
        if eventos == 'log':
            if '.' not in sentence:
                sentence = str(math.log10(int(sentence)))
            else:
                sentence = str(math.log10(float(sentence)))
            janela['num'].update(sentence)
        if eventos == 'inverter':
            if sentence[0] == '-':
                if '.' in sentence:
                    sentence = str(float(sentence) * -1)
                else:
                    sentence = str(int(sentence) * -1)
                janela['num'].update(sentence)
            else:
                sentence = '-' + sentence
                janela['num'].update(sentence)
        if eventos == 'zero':
            sentence += '0'
            janela['num'].update(sentence)
        if eventos == 'point':
            sentence += '.'
            janela['num'].update(sentence)
        if eventos == 'equal':
            sentence2 += sentence
            sentence = find_operator(sentence2)
            janela['num'].update(sentence)
            janela['num2'].update('')
            sentence = ''
            sentence2 = ''
    else:
        eventos, valores = settings.read()
        settings.maximize()
        if eventos == 'turn':
            set = False
            settings.minimize()
            continue
    if eventos == sg.WINDOW_CLOSED:
        break
