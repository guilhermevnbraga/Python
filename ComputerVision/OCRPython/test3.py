import pytesseract
import cv2

img = cv2.imread('/home/solas/PycharmProjects/killerQueen/ComputerVision/OCRPython/Imagens/trecho-livro.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', rgb)
configTesseract = '--tessdata-dir tessdata --psm 6'
text = pytesseract.image_to_string(rgb, lang='por', config=configTesseract)
print(text)
