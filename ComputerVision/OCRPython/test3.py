import pytesseract
import cv2

img = cv2.imread(r'/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/trecho-livro.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
tessdataDir = '/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}" --psm 6'
text = pytesseract.image_to_string(rgb, lang='por', config=configTesseract)
print(text)
