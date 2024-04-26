condicoesMetereologicas = input()
if condicoesMetereologicas == 'chuvoso':
    pistaMolhada = eval(input())

temperaturaPista = input()
desempenhoTreinos = input()
posicaoLargada = int(input())

print("Estratégia de prova de Max Verstappen!")

if condicoesMetereologicas == 'ensolarado':
    if temperaturaPista == 'alta':
        print('Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!')
    else:
        print('Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.')
elif condicoesMetereologicas == 'nublado':
    if temperaturaPista == 'alta':
        print('Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!')
    else:
        print('Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!')
elif condicoesMetereologicas == 'chuvoso':
    if pistaMolhada == True:
        print('Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.')
    else:
        print('Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!')

if posicaoLargada == 1:
    if desempenhoTreinos == 'bom':
        print('Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.')
    else:
        print('Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.')
elif posicaoLargada > 1 and posicaoLargada <= 12:
    print('Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
else:
    print('Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
