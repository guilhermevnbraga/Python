import cv2

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/trecho-livro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(val)

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/receita01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(val)
