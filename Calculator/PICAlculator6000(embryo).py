import PySimpleGUI as sg

sg.theme('DarkGreen3')
layout = [
    [sg.Text('PICAlculator 3000    ', justification='r', size=(23, 1), font='Arial 18'),
     sg.Button('⚙', key='settings', size=(2, 1))],
    [sg.Text('')],
    [sg.Text(size=(300, 1), key='num2', justification='r')],
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

calculatorGUI = sg.Window('PICAlculator 3000', layout, size=(390, 500))
calculatorGUI.read()
