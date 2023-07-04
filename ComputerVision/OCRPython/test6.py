import cv2
import pytesseract
from pytesseract import Output


def caixaTexto(resultado, img, cor = [255, 100, 0]):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x, y), (x+w, y+h), cor, 2)
    return x, y, img


img = cv2.imread('./OCRPython/Imagens/teste_manuscrito_01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
configTesseract = '--tessdata-dir tessdata'
resultado = pytesseract.image_to_data(rgb, config=configTesseract, lang='por', output_type=Output.DICT)
minConf = 40
imgCopia = rgb.copy()
for i in range(0, len(resultado['text'])):
               confianca = int(resultado['conf'][i])
               if confianca > minConf:
                   x, y, img = caixaTexto(resultado, imgCopia)
                   texto = resultado['text'][i]
                   cv2.putText(imgCopia, texto, [x, y-10], cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255))
cv2.imshow('imagem', imgCopia)
