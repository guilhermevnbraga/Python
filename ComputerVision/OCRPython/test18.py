import cv2
import numpy as np

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\teste_ruido.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

desfoqueMedia = cv2.blur(gray, (5, 5))
cv2.imshow('imagem', desfoqueMedia)
cv2.waitKey(0)
cv2.destroyAllWindows()

desfoqueGauss = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('imagem', desfoqueGauss)
cv2.waitKey(0)
cv2.destroyAllWindows()

desfoqueMediana = cv2.medianBlur(gray, 3)
cv2.imshow('imagem', desfoqueMediana)
cv2.waitKey(0)
cv2.destroyAllWindows()

desfoqueBilateral = cv2.bilateralFilter(gray, 15, 55, 45)
cv2.imshow('imagem', desfoqueBilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
