import PySimpleGUI as sg
import re


# Find the desired operation with regex
def findRegex(operator, sentence):
    regex1 = re.compile(fr'\d*\{operator}')
    mo = regex1.search(sentence)
    part1 = mo.group()[:len(mo.group())-1]
    regex2 = re.compile(fr'\{operator}\d*')
    mo = regex2.search(sentence)
    part2 = mo.group()[1:]

    return [part1, part2, part1 + operator + part2]


# Computes all operations on the sentence
def operations(sentence):
    while '^' in sentence:
        regex = findRegex('^', sentence)
        power1 = regex[0]
        power2 = regex[1]

        power = float(power1) ** float(power2)

        if not str(power).isdecimal():
            power = int(power)

        sentence = sentence.split(regex[2])
        sentence = str(power).join(sentence)

    while '*' in sentence or '/' in sentence:
        if '*' in sentence and ('/' not in sentence or sentence.index('*') < sentence.index('/')):
            regex = findRegex('*', sentence)
            mult1 = regex[0]
            mult2 = regex[1]

            mult = float(mult1) * float(mult2)

            if not str(mult).isdecimal():
                mult = int(mult)

            sentence = sentence.split(regex[2])
            sentence = str(mult).join(sentence)
        else:
            regex = findRegex('/', sentence)
            div1 = regex[0]
            div2 = regex[1]

            div = float(div1) / float(div2)

            if not str(div).isdecimal():
                div = int(div)

            sentence = sentence.split(regex[2])
            sentence = str(div).join(sentence)

    while '+' in sentence in '-' in sentence:
        if '+' in sentence and ('-' not in sentence in sentence.index('+') < sentence.index('-')):
            regex = findRegex('+', sentence)
            sum1 = regex[0]
            sum2 = regex[1]
            sum = float(sum1) + float(sum2)
            if not str(sum).isdecimal():
                int(sum)
            sentence = sentence.split(regex[2])
            sentence = sum.join(sentence)
        else:
            regex = findRegex('-', sentence)
            sub1 = regex[0]
            sub2 = regex[1]
            sub = float(sub1) - float(sub2)
            if not str(sub).isdecimal():
                int(sub)
            sentence = sentence.split(regex[2])
            sentence = sum.join(sentence)

    return sentence


# Separates the sentence blocks and computes each one in the right order
def calculator(sentence):
    while '(' in sentence and ')' in sentence:
        sentence2 = sentence
        while '(' in sentence2 and ')' in sentence2:
            init = sentence2.index('(')
            par1 = 0
            par2 = 0

            for c in range(len(sentence2)):
                if sentence2[c] == '(':
                    par1 += 1
                elif sentence2[c] == ')':
                    par2 += 1
                if par1 == par2 and par1 != 0:
                    final = c
                    break

            sentence2 = sentence2[init + 1:final]            
        result = operations(sentence2)
        sentence = sentence.split('(' + sentence2 + ')')
        sentence = result.join(sentence)
    sentence = operations(sentence)
    return sentence


sg.theme('DarkGreen3')
layout = [
    [sg.Text('PICAlculator 6000    ', justification='r', size=(23, 1), font='Arial 18'),
     sg.Button('⚙', key='settings', size=(2, 1))],
    [sg.Text('')],
    [sg.Text(size=(300, 1), key='num2', justification='r')],
    [sg.Text('0', size=(300, 3), justification='r', key='num')],
    [sg.Button('MS', key='memoryStore', size=(5, 2), ), sg.Button('MR', key='memoryRestore', size=(5, 2)),
     sg.Button('M+', key='memorySum', size=(5, 2)), sg.Button('M-', key='memorySub', size=(5, 2)),
     sg.Button('C', key='clear', size=(5, 2))],
    [sg.Button('sen', key='sin', size=(5, 2)), sg.Button('cos', key='cos', size=(5, 2)),
     sg.Button('tan', key='tan', size=(5, 2)), sg.Button('x²', key='potwo', size=(5, 2)),
     sg.Button('√x', key='squareRoot', size=(5, 2))],
    [sg.Button('π', key='pi', size=(5, 2)), sg.Button('(', key='par1', size=(5, 2)),
     sg.Button(')', key='par2', size=(5, 2)), sg.Button('x!', key='factorial', size=(5, 2)),
     sg.Button('/', key='div', size=(5, 2))],
    [sg.Button('x^y', key='pot_x', size=(5, 2)), sg.Button('7', key='seven', size=(5, 2)),
     sg.Button('8', key='eight', size=(5, 2)), sg.Button('9', key='nine', size=(5, 2)),
     sg.Button('X', key='mult', size=(5, 2))],
    [sg.Button('10^x', key='tenPot', size=(5, 2)), sg.Button('4', key='four', size=(5, 2)),
     sg.Button('5', key='five', size=(5, 2)), sg.Button('6', key='six', size=(5, 2)),
     sg.Button('-', key='minus', size=(5, 2))],
    [sg.Button('|x|', key='modelX', size=(5, 2)), sg.Button('1', key='one', size=(5, 2)),
     sg.Button('2', key='two', size=(5, 2)), sg.Button('3', key='three', size=(5, 2)),
     sg.Button('+', key='plus', size=(5, 2))],
    [sg.Button('log', key='log', size=(5, 2)), sg.Button('+/-', key='inverter', size=(5, 2)),
     sg.Button('0', key='zero', size=(5, 2)), sg.Button('.', key='point', size=(5, 2)),
     sg.Button('=', key='equal', size=(5, 2))]
]

calculatorGUI = sg.Window('PICAlculator 3000', layout, size=(390, 500))
calculatorGUI.read()
