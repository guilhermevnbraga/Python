import pytesseract
import numpy as np
import cv2

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/teste01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
texto = pytesseract.image_to_string(rgb)
print(texto)
