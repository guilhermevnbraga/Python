from random import choice

alunos = ['solas', 'felipeflop', 'mashadow', 'troll', 'samuelito', 'krl', 'milker', 'walter']

c = 0
print('alunos padrão:')
for x in alunos:
	print(c, ' ' * 5, x)
	c += 1
print()

pergunta = input('Adcionar alunos? ').lower().strip()

if pergunta in ['s', 'y', 'sim', 'yes']:
	while True:
		aluno = input('Novo aluno: ')
		
		if not aluno.isalpha():
			break
		
		alunos.append(aluno)
	print()

pergunta = input('Remover alunos? ').lower().strip()

if pergunta in ['s', 'y', 'sim', 'yes']:
	while True:
		aluno = input('Id do aluno: ')
		
		if not aluno.isnumeric():
			break
		
		alunos.pop(int(aluno))
	print()
	

qgrupos = int(input('Quantidade de grupos: '))
qalunos = int(input('Alunos por grupo: '))
print()

for c in range(qgrupos):
	grupo = []
	for d in range(qalunos):
		grupo.append(alunos.pop(alunos.index(choice(alunos))))
	print(f'Grupo {c+1}:')
	for x in grupo:
		print(x, end = ' ')
	print('\n')
