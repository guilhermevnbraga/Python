from random import randint
from os import chdir, makedirs
from os.path import exists
from time import sleep


def rewrite():
    db = open('db.txt', 'w')

    for c in range(9):
        weight = str(randint(-1000, 1000) / 1000)
        if c < 8:
            db.write(f'{weight}\n')
        else:
            db.write(weight)

    db.close()
if not exists('./Codes/db'):
    makedirs('./Codes/db')
chdir('./Codes/db')

rewrite()

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
    
    try:
        actualWeight = [float(a) for a in db.read().split('\n')]
    except ValueError:
        rewrite()
        continue

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

    firstLayer = []
    sigmoids = []
    for x in data:
        for c in range(3):
            summation = int(x[0]) * actualWeight[c] + int(x[1]) * actualWeight[c]
            sigmoids.append(round(1/(1 + euler**(-summation)), 3))

            if len(sigmoids) == 3:
                firstLayer.append(sigmoids)
                sigmoids = []
                
    finalLayer = []
    for x in firstLayer:
        summation = float(x[0]) * actualWeight[6] + float(x[1]) * actualWeight[7] + float(x[2]) * actualWeight[8]
        finalLayer.append(round(1 / (1 + euler**(-summation)), 3))

    outDelta = []
    for c in range(len(finalLayer)):
        outDelta.append(round((float(waitedResult[c]) - finalLayer[c]) * (finalLayer[c] * (1 - finalLayer[c])), 3))

    inDelta = []
    for c in range(len(outDelta)):

        delta = []
        for d in range(3):
            delta.append(round(firstLayer[c][d] * actualWeight[6 + d] * outDelta[c], 3))

        inDelta.append(delta)

    firstPart = []
    for c in range(3):
        sumPart = 0

        for d in range(4):
            sumPart += firstLayer[d][c] * outDelta[d]
        
        firstPart.append(round(sumPart, 3))

    newOutWeight = []
    for c in range(3):
        newOutWeight.append(round(actualWeight[6 + c] + firstPart[c] * 0.3, 3))

    secondPart = []
    for w in range(2):
        firstPart = []
        for c in range(3):
            sumPart = 0

            for d in range(len(inDelta)):
                sumPart += int(data[d][w]) * inDelta[d][c]

            firstPart.append(round(sumPart, 3))
        
        secondPart.append(firstPart)

    newInWeight = []
    c = 0
    for d in range(3):
        for w in range(2):
            weight = actualWeight[c] + secondPart[w][d] * 0.3
            newInWeight.append(round(weight, 3))
            c += 1

    for x in newOutWeight:
        newInWeight.append(x)

    db = open('db.txt', 'w')

    for x in newInWeight:
        if not x == newInWeight[-1]:
            db.write(f'{x}\n')
        else:
            db.write(f'{x}')

    db.close()

    print(finalLayer)
    sleep(0.05)
