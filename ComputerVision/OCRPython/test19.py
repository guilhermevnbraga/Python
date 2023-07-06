import cv2
import pytesseract

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\livro02.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\receita01.jpg')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}"'

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
texto = pytesseract.image_to_string(otsu, lang='por', config=configTesseract)
print(texto)

val, thresh = cv2.threshold(gray2, 140, 255, cv2.THRESH_BINARY)
cv2.imshow('imagem', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
texto2 = pytesseract.image_to_string(thresh, lang='por', config=configTesseract)
print(texto2)
