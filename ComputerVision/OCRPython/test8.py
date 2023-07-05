import cv2
import pytesseract
import re
import numpy as np
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image


def escrevaTexto(texto, x, y, img, fonte, tamanhoText=32):
    font = ImageFont.truetype(fonte, tamanhoText)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y - tamanhoText), texto, font = font)
    img = np.array(imgPil)
    return img


def caixaTexto(resultado, img, cor = [255, 100, 0]):
    x = resultado['left'][c]
    y = resultado['top'][c]
    w = resultado['width'][c]
    h = resultado['height'][c]

    cv2.rectangle(img, (x, y), (x+w, y+h), cor, 2)
    return x, y, img

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\tabela_teste.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}"'
resultado = pytesseract.image_to_data(rgb, config=configTesseract, lang='por', output_type=Output.DICT)
dateRegex = r'^(0[1-9]/|[12][0-9]/|3[01]/)?(0[1-9]|1[012])/(19|20)\d\d$'
dates = []
fonte = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Fontes\calibri.ttf'
imgCopia = rgb.copy()
confianca = 40
for c in range(len(resultado['conf'])):
    x = int(resultado['conf'][c])
    if x > confianca:
        texto = resultado['text'][c]
        if re.match(dateRegex, texto):
            x, y, img = caixaTexto(resultado, imgCopia, (0,0,255))
            imgCopia = escrevaTexto(texto, x, y, imgCopia, fonte, 12)
            dates.append(texto)
        else:
            x, y, imgCopia = caixaTexto(resultado, imgCopia)

print('Datas Encontradas na imagem: ', end='| ')
for x in dates:
    print(x, end=' | ')

cv2.imshow('imagem', imgCopia)
cv2.waitKey(0)
cv2.destroyAllWindows()
