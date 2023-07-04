import PySimpleGUI as sg
import re
import math

# Find the desired operation with regex
# verify if there's only a negative number on the sentence
def isnegative(sentence):
    try:
        negativeRegex = re.compile(fr'^-\d*[.]?\d*$')
        mo = negativeRegex.search(sentence)
        mo.group()
    except AttributeError:
        return False
    return True


# replace duplicate signs
def signreplace(sentence):
    if '--' in sentence:
        sentence = sentence.replace('--', '+')
    if '++' in sentence:
        sentence = sentence.replace('++', '+')
    if '+-' in sentence:
        sentence = sentence.replace('+-', '-')
    if '-+' in sentence:
        sentence = sentence.replace('-+', '-')

    return sentence


def findregex(operator, sentence):
    extraMinus = ''
    if sentence.startswith('-'):
        extraMinus = '-'
        sentence = sentence[1:]

    regex1 = re.compile(fr'\d*\.?\d?\{operator}')
    mo = regex1.search(sentence)
    part1 = extraMinus + mo.group()[:len(mo.group())-1]
    regex2 = re.compile(fr'\{operator}\d*\.?\d?')
    mo = regex2.search(sentence)
    part2 = mo.group()[1:]

    return [part1, part2, part1 + operator + part2]


# Verify if the sentence isn't illegal
def validatesentence(sentence):
    if sentence.count('(') != sentence.count(')'):
        sentence = 'Syntax Error!'

    errorRegex = re.compile(r'[*/]{2,}')
    mo = errorRegex.search(sentence)
    try:
        mo.group()
        sentence = 'Syntax Error!'
    except AttributeError:
        return sentence
    return sentence


# Computes all operations on the sentence
def operations(sentence):
    while '!' in sentence:
        factorialRegex = re.compile(r'\d\.?\d?!')
        mo = factorialRegex.search(sentence)
        factorial = mo.group()
        factorial = factorial.replace('!', '')
        print(factorial)
        fact = math.factorial(int(factorial))
        sentence = sentence.replace(str(factorial) + '!', str(fact))
        print(sentence)

    while '^' in sentence or '√' in sentence:
        if '^' in sentence and ('√' not in sentence or sentence.index('^') < sentence.index('√')):
            regex = findregex('^', sentence)
            power1 = regex[0]
            power2 = regex[1]

            power = float(power1) ** float(power2)

            if power == int(power):
                power = int(power)

            sentence = sentence.split(regex[2])
            sentence = str(power).join(sentence)
            print(sentence)
        else:
            sqrtRegex = re.compile(r'√\d*')
            mo = sqrtRegex.search(sentence)
            square = mo.group()
            root = math.sqrt(float(square[1:]))
            if root == int(root):
                root = int(root)
            sentence = sentence.replace(square, str(root))

    while '*' in sentence or '/' in sentence:
        if '*' in sentence and ('/' not in sentence or sentence.index('*') < sentence.index('/')):
            regex = findregex('*', sentence)
            mult1 = regex[0]
            mult2 = regex[1]

            mult = float(mult1) * float(mult2)

            if mult == int(mult):
                mult = int(mult)

            sentence = sentence.split(regex[2])
            sentence = str(mult).join(sentence)
        else:
            regex = findregex('/', sentence)
            div1 = regex[0]
            div2 = regex[1]

            div = float(div1) / float(div2)

            if div == int(div):
                div = int(div)

            sentence = sentence.split(regex[2])
            sentence = str(div).join(sentence)
        print(sentence)

    while '+' in sentence or ('-' in sentence and not isnegative(sentence)):
        if isnegative(sentence):
            break

        if '+' in sentence and ('-' not in sentence[1:] or sentence.index('+') < sentence[1:].index('-')):
            regex = findregex('+', sentence)
            su1 = regex[0]
            su2 = regex[1]

            su = float(su1) + float(su2)

            if su == int(su):
                su = int(su)

            sentence = sentence.split(regex[2])
            sentence = str(su).join(sentence)
        else:
            regex = findregex('-', sentence)
            sub1 = regex[0]
            sub2 = regex[1]
            print(regex[2])
            sub = float(sub1) - float(sub2)

            if sub == int(sub):
                sub = int(sub)

            sentence = sentence.split(regex[2])
            sentence = str(sub).join(sentence)
        print(sentence)

    return sentence


# Separates the sentence's blocks and computes each one in the right order
def calculator(sentence):
    parRegex = re.compile(r'\(.*\)')
    sentence = signreplace(sentence)
    print(sentence)

    while '(' in sentence and ')' in sentence:
        sentence2 = sentence
        while '(' in sentence2 and ')' in sentence2:
            mo = parRegex.search(sentence2)
            par = mo.group()
            sentence2 = par[1:len(par)-1]
            print(sentence2)
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
    [sg.Text('0', size=(300, 3), justification='r', key='display')],
    [sg.Button('MS', key='memoryStore', size=(5, 2), ), sg.Button('MR', key='memoryRestore', size=(5, 2)),
     sg.Button('M+', key='memorySum', size=(5, 2)), sg.Button('M-', key='memorySub', size=(5, 2)),
     sg.Button('C', key='clear', size=(5, 2))],
    [sg.Button('sen', key='sin', size=(5, 2)), sg.Button('cos', key='cos', size=(5, 2)),
     sg.Button('tan', key='tan', size=(5, 2)), sg.Button('x²', key='potwo', size=(5, 2)),
     sg.Button('√x', key='squareRoot', size=(5, 2))],
    [sg.Button('π', key='pi', size=(5, 2)), sg.Button('(', key='par1', size=(5, 2)),
     sg.Button(')', key='par2', size=(5, 2)), sg.Button('x!', key='factorial', size=(5, 2)),
     sg.Button('/', key='div', size=(5, 2))],
    [sg.Button('x^y', key='potx', size=(5, 2)), sg.Button('7', key='seven', size=(5, 2)),
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

calculatorGUI = sg.Window('PICAlculator 6000', layout, size=(390, 500))
sentence = ''
memory = 0
while True:
    events, values = calculatorGUI.read()
    if events == 'clear':
        sentence = ''
    elif events == 'memoryStore':
        memory = float(sentence)
    elif events == 'memoryRestore':
        if not str(memory).isdecimal():
            memory = int(memory)
        sentence += str(memory)
    elif events == 'memorySum':
        memory += float(memory)
    elif events == 'memorySub':
        memory -= float(memory)
    elif events == 'zero':
        sentence += '0'
    elif events == 'one':
        sentence += '1'
    elif events == 'two':
        sentence += '2'
    elif events == 'three':
        sentence += '3'
    elif events == 'four':
        sentence += '4'
    elif events == 'five':
        sentence += '5'
    elif events == 'six':
        sentence += '6'
    elif events == 'seven':
        sentence += '7'
    elif events == 'eight':
        sentence += '8'
    elif events == 'nine':
        sentence += '9'
    elif events == 'plus':
        sentence += '+'
    elif events == 'minus':
        sentence += '-'
    elif events == 'mult':
        sentence += '*'
    elif events == 'div':
        sentence += '/'
    elif events == 'potx':
        sentence += '^'
    elif events == 'squareRoot':
        sentence += '√'
    elif events == 'factorial':
        sentence += '!'
    elif events == 'par1':
        sentence += '('
    elif events == 'par2':
        sentence += ')'
    elif events == 'point':
        dotRegex = re.compile(r'\d*\.?\d*$')
        mo = dotRegex.search(sentence)
        if '.' not in mo.group():
            sentence += '.'
    elif events == 'tenPot':
        operationRegex = re.compile(r'[+-/*]\d*')
        operate = operationRegex.findall(sentence)
        if not operate:
            sentence = '10^' + sentence
        else:
            operate = ''.join(operate[-1])
            newOperation = operate
            newOperation = newOperation.replace(newOperation[1:], '10^'+newOperation[1:])
            sentence = sentence.replace(operate, newOperation)
    elif events == 'log':
        if sentence.isnumeric():
            sentence = round(math.log10(float(sentence)), 5)
        sentence = str(sentence)
    elif events == 'sin':
        if sentence.isnumeric():
            sentence = round(math.sin(math.radians(float(sentence))), 3)
            if '.' not in str(sentence):
                int(sentence)
        sentence = str(sentence)
    elif events == 'cos':
        if sentence.isnumeric():
            sentence = round(math.cos(math.radians(float(sentence))), 3)
            if '.' not in str(sentence):
                int(sentence)
        sentence = str(sentence)
    elif events == 'tan':
        if sentence.isnumeric():
            sentence = round(math.tan(math.radians(float(sentence))), 3)
            if '.' not in str(sentence):
                int(sentence)
        sentence = str(sentence)
    elif events == 'potwo':
        sentence += '^2'
    elif events == 'pi':
        sentence += '3.1415926535897932384626433832795'
    elif events == 'inverter':
        sentence = validatesentence(sentence)
        if sentence != 'Syntax Error!':
            sentence = calculator(sentence)
        if sentence != '0' and sentence != 'Syntax Error!' and sentence != '':
            if '-' in sentence:
                sentence = sentence.replace('-', '')
            else:
                sentence = '-' + sentence
    elif events == 'modelX':
        sentence = validatesentence(sentence)
        if sentence != 'Syntax Error!':
            sentence = calculator(sentence)
            if '-' in sentence:
                sentence = sentence.replace('-', '')
    elif events == 'equal':
        sentence = validatesentence(sentence)
        if sentence != 'Syntax Error!':
            sentence = calculator(sentence)
    elif events == sg.WINDOW_CLOSED:
        break

    if sentence == '':
        calculatorGUI['display'].update('0')
        continue

    calculatorGUI['display'].update(sentence)
