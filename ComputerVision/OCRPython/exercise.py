import cv2
import pytesseract

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/frase.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(val)
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

tessdataDir = '/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}" --psm 6'
texto = pytesseract.image_to_string(otsu, lang='por', config=configTesseract)
print(texto)
