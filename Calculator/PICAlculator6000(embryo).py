import PySimpleGUI as sg


# Find the coordinates for the desired operation on the sentence
def operationFinder(operator, sentence):
    for c in range(sentence.index(operator) - 1, -1, -1):
        if not sentence[c].isnumeric() or c == 0:
            init = c
            break
    for c in range(sentence.index(operator) + 1, len(sentence)):
        if not sentence[c].isnumeric() or c == len(sentence) - 1:
            final = c
            break

    return [init, final]


# Computes all operation on the sentence
def operations(sentence):
    while '^' in sentence:
        coordinates = operationFinder('^', sentence)
        init = coordinates[0]
        final = coordinates[1]
        power = float(sentence[init:sentence.index('^')]) ** float(sentence[sentence.index('^') + 1:final + 1])

        if not str(power).isdecimal():
            power = int(power)

        sentence = sentence.split(sentence[init:final + 1])
        sentence = str(power).join(sentence)
        print(sentence)

    while '*' in sentence or '/' in sentence:
        if '*' in sentence and ('/' not in sentence or sentence.index('*') < sentence.index('/')):
            coordinates = operationFinder('*', sentence)
            init = coordinates[0]
            final = coordinates[1]
            mult = float(sentence[init:sentence.index('*')]) * float(sentence[sentence.index('*') + 1:final])

            if not str(mult).isdecimal():
                mult = int(mult)

            sentence = sentence.split(sentence[init:final])
            sentence = str(mult).join(sentence)
            print(sentence)
        else:
            coordinates = operationFinder('/', sentence)
            init = coordinates[0]
            final = coordinates[1]
            div = float(sentence[init:sentence.index('/')]) / float(sentence[sentence.index('/') + 1:final])

            if not str(div).isdecimal():
                div = int(div)

            sentence = sentence.split(sentence[init:final])
            sentence = str(div).join(sentence)
            print(sentence)


# Separates the sentence blocks and calculates each one in the right order
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
# calculatorGUI.read()
print(operations('44/22*22'))
