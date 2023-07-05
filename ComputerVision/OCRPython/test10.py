import cv2
import numpy as np

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\img-process.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
