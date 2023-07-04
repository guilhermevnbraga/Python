import pytesseract
import numpy as np
import cv2

img = cv2.imread('ComputerVision/OCRPython/Imagens/teste01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', img)
texto = pytesseract.image_to_string(rgb)
print(texto)
