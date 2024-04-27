from re import findall
from random import randint
from os import chdir, makedirs, system
from os.path import exists
from time import sleep


def rewrite():
    db = open('db.txt', 'w')

    for c in range(9):
        weight = str(randint(-1000000000, 1000000000) / 1000000000)
        db.write(f'{weight}\n')

    db.close()
    
    
if not exists('./Codes/db'):
    makedirs('./Codes/db')
chdir('./Codes/db')

# rewrite() uncomment this if you want to restart database

data = [
    '00',
    '01',
    '10',
    '11'
]

waitedResult = [
    '0',
    '0',
    '0',
    '1'
]

euler = 2.718
madeInHeaven = 0
finalLayer = []
lastResult = []
while waitedResult != finalLayer:
    db = open('db.txt', 'r')
    actualWeight = [float(a) for a in findall(r'-?\d*\.\d*', db.read())]
    db.close()

    if lastResult == finalLayer:
        madeInHeaven += 1
        print(madeInHeaven)
    else:
        madeInHeaven = 0

    lastResult = finalLayer[:]
    
    if madeInHeaven == 1000:
        rewrite()
        madeInHeaven = 0
        continue

    firstLayer = []
    sigmoids = []
    for x in data:
        for c in range(3):
            summation = int(x[0]) * actualWeight[c] + int(x[1]) * actualWeight[c]
            sigmoids.append(round(1 / (1 + euler**(-summation)), 34))

            if len(sigmoids) == 3:
                firstLayer.append(sigmoids)
                sigmoids = []
                
    finalLayer = []
    for x in firstLayer:
        summation = float(x[0]) * actualWeight[6] + float(x[1]) * actualWeight[7] + float(x[2]) * actualWeight[8]
        finalLayer.append(round(1 / (1 + euler**(-summation)), 34))
	
    outDelta = []
    for c in range(len(finalLayer)):
        outDelta.append(round((float(waitedResult[c]) - finalLayer[c]) * (finalLayer[c] * (1 - finalLayer[c])), 34))

    inDelta = []
    for c in range(len(outDelta)):

        delta = []
        for d in range(3):
            delta.append(round(firstLayer[c][d] * actualWeight[6 + d] * outDelta[c], 34))

        inDelta.append(delta)

    firstPart = []
    for c in range(3):
        sumPart = 0

        for d in range(4):
            sumPart += firstLayer[d][c] * outDelta[d]
        
        firstPart.append(round(sumPart, 34))

    newOutWeight = []
    for c in range(3):
        newOutWeight.append(round(actualWeight[6 + c] + firstPart[c] * 0.3, 34))

    secondPart = []
    for w in range(2):
        firstPart = []
        for c in range(3):
            sumPart = 0

            for d in range(len(inDelta)):
                sumPart += int(data[d][w]) * inDelta[d][c]

            firstPart.append(round(sumPart, 34))
        
        secondPart.append(firstPart)

    newInWeight = []
    c = 0
    for d in range(3):
        for w in range(2):
            weight = actualWeight[c] + secondPart[w][d] * 0.3
            newInWeight.append(round(weight, 34))
            c += 1

    for x in newOutWeight:
        newInWeight.append(x)

    db = open('db.txt', 'w')

    for x in newInWeight:
        db.write(f'{x}\n')

    db.close()

    print('Resultado:')
    for c in range(len(finalLayer)):
    	print(f'S{c}: {round(finalLayer[c], 3)}')
    
    meanError = 0
    for c in range(len(waitedResult)):
    	meanError += abs(int(waitedResult[c]) - finalLayer[c])
    meanError /= 4
    
    print(f'Precisão: {(1 - meanError) * 100}%\n')
    if  meanError * 100 < 0.1:
        system('cls') or None
        
        print('Solução Encontrada!')
        for c in range(len(actualWeight)):
    	    print(f'Peso{c + 1}: {actualWeight[c]}')
        
        print('\nResultado Final:')
        for c in range(len(finalLayer)):
    	    print(f'S{c}: {round(finalLayer[c], 3)}')
    	    
        print(f'Precisão: {(1 - meanError) * 100}%\n')
        break
    
    system('cls') or None
