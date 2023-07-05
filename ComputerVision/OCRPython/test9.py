import cv2
import pytesseract
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
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x, y), (x+w, y+h), cor, 2)
    return x, y, img

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\caneca.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}" --psm 11'
resultado = pytesseract.image_to_data(rgb, lang='por', config=configTesseract, output_type=Output.DICT)
fonte = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Fontes\calibri.ttf'
minConf = 70
imgCopia = rgb.copy()
for i in range(0, len(resultado['text'])):
               confianca = int(resultado['conf'][i])
               if confianca > minConf:
                   texto = resultado['text'][i]
                   if not texto.isspace() and len(texto) > 0:
                        x, y, img = caixaTexto(resultado, imgCopia)
                        imgCopia = escrevaTexto(texto, x, y, imgCopia, fonte)
cv2.imshow('imagem', imgCopia)
cv2.waitKey(0)
cv2.destroyAllWindows
print(resultado['conf'])
print(resultado['text'])
 