'''
1. Cada tipo de pneu tem uma durabilidade (duro = 90, médio = 70, macio = 50 e chuva = 50).

2. Se um pneu de chuva for usado em clima de sol, independentemente da dificuldade,
o programa deve multiplicar o número de voltas por 15 e subtrair da durabilidade
(o mesmo se aplica a pneus que não são de chuva usados em clima de chuva).

3. Se o clima for de sol, a dificuldade for baixa ou média e o tipo de pneu for macio ou medio,
deve-se multiplicar o número de voltas por 2 e subtrair da durabilidade.

4. Se o clima for de sol, a dificuldade for alta e os pneus forem macios,
deve-se multiplicar o número de voltas por 3 e subtrair da durabilidade.

5. Se o clima for de sol, a dificuldade for alta e os pneus forem duros,
deve-se apenas subtrair o número de voltas da durabilidade.

6. Se o clima for de chuva, a dificuldade for baixa e os pneus apropriados para o clima,
deve-se apenas subtrair o número de voltas da durabilidade. No caso da dificuldade ser media,
multiplica-se por 2 e subtrai e finalmente, se for alta multiplica-se por 3 e subtrai.
'''

voltas = int(input())
clima = input()
dificuldade = input()
tipoPneu = input()

if tipoPneu == 'duro':
    durabilidade = 90
elif tipoPneu == 'médio':
    durabilidade = 70
elif tipoPneu == 'macio':
    durabilidade = 50
elif tipoPneu == 'chuva':
    durabilidade = 50

if clima == 'sol':
    if tipoPneu == 'chuva':
        durabilidade -= voltas * 15

    if not dificuldade == 'alta':
        if tipoPneu == 'macio' or tipoPneu == 'médio':
            durabilidade -= voltas * 2
    elif tipoPneu =='macio':
        durabilidade -= voltas * 3
    elif tipoPneu == 'duro':
        durabilidade -= voltas
elif tipoPneu == 'chuva':
    if dificuldade == 'média':
        durabilidade -= voltas * 2
    elif dificuldade == 'alta':
        durabilidade -= voltas * 3
    else:
        durabilidade -= voltas

else:
    durabilidade -= voltas * 15

print(durabilidade)

if durabilidade >= 20:
    print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.')
else:
    print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')
