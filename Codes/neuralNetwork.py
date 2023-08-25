from random import randint
from os import chdir, makedirs
from os.path import exists
from time import sleep

if not exists('./Codes/db'):
    makedirs('./Codes/db')
chdir('./Codes/db')

db = open('db.txt', 'w')
for c in range(9):
    weight = str(randint(-1000, 1000) / 1000)
    db.write(f'{weight}\n')
db.close()

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

finalLayer = []
while waitedResult != finalLayer:
    db = open('db.txt', 'r')

    actualData = []
    out = ''
    for x in db.read():
        if x == '\n':
            actualData.append(float(out))
            out = ''
        else:
            out += x
    db.close()

    euler = 2.718
    firstLayer = []
    out = []
    for x in data:
        for c in range(3):
            summation = int(x[0]) * actualData[c] + int(x[1]) * actualData[c]
            out.append(round(1/(1 + euler**(-summation)), 3))

            if len(out) == 3:
                firstLayer.append(out)
                out = []
                
    finalLayer = []
    for x in firstLayer:
        summation = float(x[0]) * actualData[6] + float(x[1]) * actualData[7] + float(x[2]) * actualData[8]
        finalLayer.append(round(1 / (1 + euler**(-summation)), 3))

    outDelta = []
    for c in range(len(finalLayer)):
        outDelta.append(round((float(waitedResult[c]) - finalLayer[c]) * (finalLayer[c] * (1 - finalLayer[c])), 3))

    firstDelta = []
    for c in range(len(outDelta)):
        delta = []

        for d in range(3):
            delta.append(round(firstLayer[c][d] * actualData[6 + d] * outDelta[c], 3))

        firstDelta.append(delta)

    firstPart = []
    for c in range(3):
        sumPart = 0

        for d in range(4):
            sumPart += firstLayer[d][c] * outDelta[d]
        
        firstPart.append(round(sumPart, 3))

    firstNewWeight = []
    for c in range(3):
        firstNewWeight.append(round(actualData[6 + c] + firstPart[c] * 0.3, 3))

    secondPart = []
    for w in range(2):
        firstPart = []
        for c in range(3):
            sumPart = 0

            for d in range(len(firstDelta)):
                sumPart += int(data[d][w]) * firstDelta[d][c]

            firstPart.append(round(sumPart, 3))
        
        secondPart.append(firstPart)

    secondNewWeight = []
    c = 0
    for d in range(3):
        for w in range(2):
            weight = actualData[c] + secondPart[w][d] * 0.3
            secondNewWeight.append(round(weight, 3))
            c += 1

    for x in firstNewWeight:
        secondNewWeight.append(x)

    db = open('db.txt', 'w')
    for x in secondNewWeight:
        db.write(f'{x}\n')

    print(finalLayer)
    sleep(0.01)
        