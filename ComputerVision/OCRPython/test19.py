import cv2
import pytesseract
import numpy as np

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/livro02.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/receita01.jpg')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.imshow('imagem', gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
tessdataDir = '/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}" --psm 6'

otsu = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
erode = cv2.erode(otsu, np.ones((2, 2), np.uint8))
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.imshow('imagem', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
texto = pytesseract.image_to_string(otsu, lang='por', config=configTesseract)
print(texto)

thresh = cv2.adaptiveThreshold(gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('imagem', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
texto2 = pytesseract.image_to_string(thresh, lang='por', config=configTesseract)
print(texto2)
