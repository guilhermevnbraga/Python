import cv2
import numpy as np
from easyocr import Reader
from PIL import ImageFont, ImageDraw, Image


def escreveTexto(texto, x, y, img, fonte, cor=(50,50,255), tamanho = 22):
    fonte = ImageFont.truetype(fonte, tamanho)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y - tamanho), texto, font = fonte, fill = cor)
    img = np.array(imgPil)
    return img


def coordenadaCaixa(caixa):
    (te, td, bd, be) = caixa
    te = (int(te[0]), int(te[1]))
    td = (int(td[0]), int(td[1]))
    bd = (int(bd[0]), int(bd[1]))
    be = (int(be[0]), int(be[1]))
    return te, td, bd, be


def desenhaCaixa(img, te, bd, corCaixa=(200,255,0), espessura=2):
    cv2.rectangle(img, te, bd, corCaixa, espessura)
    return img


idiomas = ['en', 'pt']
gpu = False
fonte = '/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Fontes/calibri.ttf'

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/caneca.jpg')
cv2.imshow('imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
reader = Reader(idiomas, gpu)
resultados = reader.readtext(img)

for (caixa, texto, probabilidade) in resultados:
    print(caixa, texto, probabilidade)
    te, td, bd, be = coordenadaCaixa(caixa)
    img = desenhaCaixa(img, te, bd)
    img = escreveTexto(texto, te[0], te[1], img, fonte)
cv2.imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
