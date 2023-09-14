import cv2

img = cv2.imread('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/livro02.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(val)
cv2.imshow('imagem', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

adaptMedia = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('imagem', adaptMedia)
cv2.waitKey(0)
cv2.destroyAllWindows()
