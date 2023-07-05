import pytesseract
import cv2
from time import sleep

img = cv2.imread(r'\Imagens\teste02.jpg')
#cv2.imshow('imagem', img)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', rgb)
configTesseract = '--tessdata-dir tessdata'
texto = pytesseract.image_to_string(rgb, lang='por', config=configTesseract)
print(texto)
