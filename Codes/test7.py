import pytesseract
import cv2
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


img = cv2.imread(r'C:\Users\Madona\Desktop\GuilhermeEstudas\OCRPython\Imagens\teste02.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
config_tesseract = '--tessdata-dir tessdata'
resultado = pytesseract.image_to_data(rgb, config=config_tesseract, lang='por', output_type=Output.DICT)
minConf = 40
imgCopia = rgb.copy()
fonte = r'C:\Users\Madona\Desktop\GuilhermeEstudas\OCRPython\Fontes\calibri.ttf'
for i in range(0, len(resultado['text'])):
               confianca = int(resultado['conf'][i])
               if confianca > minConf:
                   x, y, img = caixaTexto(resultado, imgCopia)
                   texto = resultado['text'][i]
                   imgCopia = escrevaTexto(texto, x, y, imgCopia, fonte)
cv2.imshow('imagem', imgCopia)
