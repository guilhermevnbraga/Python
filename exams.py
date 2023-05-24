import os
from random import shuffle

if not os.path.exists('./exams'):
    os.makedirs('./exams')
if not os.path.exists('./answers'):
    os.makedirs('./answers')
jokerDir = os.getcwd()

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = list(capitals.items())
cap = list(capitals.values())
for c in range(1, 36):
    os.chdir(f'{jokerDir}/exams')
    exam = open(f'exam{c}', 'w')
    os.chdir(f'{jokerDir}/answers')
    answer = open(f'answerExam{c}', 'w')
    shuffle(states)
    for co in range(1, 51):
        os.chdir(f'{jokerDir}/exams')
        con = 0
        shuffle(cap)
        for x in cap:
            if x == states[co - 1][1]:
                safe = cap[con]
                del cap[con]
            con += 1
        answers = [states[co - 1][1], cap[0], cap[1], cap[2], cap[3]]
        shuffle(answers)
        exam.write(f'''Question {co}
What is the capital of {states[co - 1][0]}?

A - {answers[0]}
B - {answers[1]}
C - {answers[2]}
D - {answers[3]}
E - {answers[4]}

''')
        cap.append(safe)
        os.chdir(f'{jokerDir}/answers')
        con = 0
        for x in answers:
            if x == states[co - 1][1]:
                if con == 0:
                    letter = 'A'
                elif con == 1:
                    letter = 'B'
                elif con == 2:
                    letter = 'C'
                elif con == 3:
                    letter = 'D'
                else:
                    letter = 'E'
                answer.write(f'''Question {co}
{letter}

''')
            con += 1
