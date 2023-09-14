import cv2
import numpy as np

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/texto-opencv.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/texto-opencv2.jpg')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

erode = cv2.erode(gray, np.ones((5, 5), np.uint8))
cv2.imshow('imagem', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilate = cv2.dilate(gray2, np.ones((5, 5), np.uint8))
cv2.imshow('imagem', dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

open = cv2.dilate(erode, np.ones((5, 5), np.uint8))
cv2.imshow('imagem', open)
cv2.waitKey(0)
cv2.destroyAllWindows()

close =  cv2.erode(dilate, np.ones((5, 5), np.uint8))
cv2.imshow('imagem', close)
cv2.waitKey(0)
cv2.destroyAllWindows()
